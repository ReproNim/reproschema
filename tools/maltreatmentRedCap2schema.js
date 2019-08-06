/* ************ Constants **************************************************** */
const csv = require('fast-csv');
const fs = require('fs');
const shell = require('shelljs');
const camelcase = require('camelcase');
const mkdirp = require('mkdirp');
const HTMLParser =  require ('node-html-parser');

const schemaMap = {
    "Identifier?": "@id",
    "Variable / Field Name": "skos:altLabel",
    "Field Note": "schema:description",
    "Section Header": "preamble",
    "Field Label": "question",
    "Field Type": "inputType",
    "Required Field?": "requiredValue",
    "Text Validation Min": "minValue",
    "Text Validation Max": "maxValue",
    "Choices, Calculations, OR Slider Labels": "choices",
    "Branching Logic (Show field only if...)": "branchLogic"
}
const uiList = ['inputType', 'shuffle'];
const responseList = ['type', 'minValue', 'maxValue', 'requiredValue', 'multipleChoice'];
const defaultLanguage = 'en';
const datas = {};
/* **************************************************************************************** */

// Make sure we got a filename on the command line.
if (process.argv.length < 3) {
    console.log('Usage: node ' + process.argv[1] + ' FILENAME');
    process.exit(1);
}
// Read the file.
let csvPath = process.argv[2];
let readStream = fs.createReadStream(csvPath).setEncoding('utf-8');

let schemaContextUrl = 'https://raw.githubusercontent.com/ReproNim/schema-standardization/master/contexts/generic.jsonld';
let order = {};
let blList = [];
let slList = [];
let blObj = [];
let languages = [];

let options = {
    delimiter: ',',
    headers: true,
    objectMode: true,
    quote: '"',
    escape: '"',
    ignoreEmpty: true
};

// get all field names and instrument name
csv
    .fromStream(readStream, options)
    .on('data', function (data) {
        if (!datas[data['Form Name']]) {
            datas[data['Form Name']] = [];
            // For each form, create directory structure - activities/form_name/items
            shell.mkdir('-p', 'activities/' + data['Form Name'] + '/items');
        }
        // console.log(62, data);
        datas[data['Form Name']].push(data);
    })
    .on('end', function () {
        // console.log(66, datas);
        Object.keys(datas).forEach(form => {
            let fieldList = datas[form];
            createFormContextSchema(form, fieldList);
            let formContextUrl = `https://raw.githubusercontent.com/ReproNim/schema-standardization/master/activities/${form}/${form}_context.jsonld`;
            fieldList.forEach( field => {
                if(languages.length === 0){
                    languages = parseLanguageIsoCodes(field['Field Label']);
                }
                processRow(form, field);
            });

            createFormSchema(form, formContextUrl);
        });
    });

function createFormContextSchema(form, fieldList) {
    // define context file for each form
    let itemOBj = { "@version": 1.1 };
    let formContext = {};
    itemOBj[form] = `https://raw.githubusercontent.com/ReproNim/schema-standardization/master/activities/${form}/items/`;
    fieldList.forEach( field => {
        let field_name = field['Variable / Field Name'];
        // define item_x urls to be inserted in context for the corresponding form
        itemOBj[field_name] = { "@id": `${form}:${field_name}.jsonld` , "@type": "@id" };
    });
    formContext['@context'] = itemOBj;
    const fc = JSON.stringify(formContext, null, 4);
    fs.writeFile(`activities/${form}/${form}_context.jsonld`, fc, function(err) {
        if (err)
            console.log(err);
        else console.log(`Context created for form ${form}`);
    });
}

function processRow(form, data){
    let rowData = {};
    let ui = {};
    let rspObj = {};
    let choiceList = [];
    rowData['@context'] = [schemaContextUrl];
    rowData['@type'] = 'https://raw.githubusercontent.com/ReproNim/schema-standardization/master/schemas/Field.jsonld';

    // map Choices, Calculations, OR Slider Labels column to choices or scoringLogic key
    if (data['Field Type'] === 'calc')
        schemaMap['Choices, Calculations, OR Slider Labels'] = 'scoringLogic';
    else schemaMap['Choices, Calculations, OR Slider Labels'] = 'choices';

    //console.log(110, schemaMap);
    Object.keys(data).forEach(current_key => {

        // get schema key from mapping.json corresponding to current_key
        if (schemaMap.hasOwnProperty(current_key)) {
            // if (schemaMap[current_key] === 'scoringLogic' && data[current_key] !== '')

            // check all ui elements to be nested under 'ui' key
            if (uiList.indexOf(schemaMap[current_key]) > -1) {
                let uiValue = data[current_key];
                if (current_key === 'Field Type' && data[current_key] === 'calc')
                    uiValue = 'number';

                if (rowData.hasOwnProperty('ui')) {
                    rowData.ui[schemaMap[current_key]] = uiValue;
                }
                else {
                    ui[schemaMap[current_key]] = uiValue;
                    rowData['ui'] = ui;
                }
            }
            // parse choice field
            else if (schemaMap[current_key] === 'choices' & data[current_key] !== '') {

                // split string wrt '|' to get each choice
                let c = data[current_key].split('|');
                // split each choice wrt ',' to get schema:name and schema:value
                c.forEach(ch => {
                    let choiceObj = {};
                    let cs = ch.split(', ');
                    // create name and value pair for each choice option
                    choiceObj['schema:value'] = parseInt(cs[0]);
                    let cnameList = parseHtml(cs[1]);
                    choiceObj['schema:name'] = cnameList;
                    choiceList.push(choiceObj);

                });
                // insert 'choices' key inside responseOptions
                if (rowData.hasOwnProperty('responseOptions')) {
                    rowData.responseOptions[schemaMap[current_key]] = choiceList;
                }
                else {
                    rspObj[schemaMap[current_key]] = choiceList;
                    rowData['responseOptions'] = rspObj;
                }
            }
            // check all other response elements to be nested under 'responseOptions' key
            else if (responseList.indexOf(schemaMap[current_key]) > -1) {
                if (rowData.hasOwnProperty('responseOptions')) {
                    rowData.responseOptions[schemaMap[current_key]] = data[current_key];
                }
                else {
                    rspObj[schemaMap[current_key]] = data[current_key];
                    rowData['responseOptions'] = rspObj;
                }
            }
            // scoring logic
            else if (schemaMap[current_key] === 'scoringLogic' && data[current_key] !== '') {
                // set ui.hidden for the item to true by default
                if (rowData.hasOwnProperty('ui')) {
                    rowData.ui['hidden'] = true;
                }
                else {
                    ui['hidden'] = true;
                    rowData['ui'] = ui;
                }
                let condition = data[current_key];
                let s = condition;
                // normalize the condition field to resemble javascript
                let re = RegExp(/\(([0-9]*)\)/g);
                condition = condition.replace(re, "___$1");
                condition = condition.replace(/([^>|<])=/g, "$1 ==");
                condition = condition.replace(/\ and\ /g, " && ");
                condition = condition.replace(/\ or\ /g, " || ");
                re = RegExp(/\[([^\]]*)\]/g);
                condition = condition.replace(re, " $1 ");
                let sl = `${data['Variable / Field Name']} = ${condition}`;
                slList.push(sl);
            }
            // branching logic
            else if (schemaMap[current_key] === 'branchLogic' & data[current_key] !== '') {
                // set ui.hidden for the item to true by default
                if (rowData.hasOwnProperty('ui')) {
                    rowData.ui['hidden'] = true;
                }
                else {
                    ui['hidden'] = true;
                    rowData['ui'] = ui;
                }
                let condition = data[current_key];
                let s = condition;
                // normalize the condition field to resemble javascript
                let re = RegExp(/\(([0-9]*)\)/g);
                condition = condition.replace(re, "___$1");
                condition = condition.replace(/([^>|<])=/g, "$1 ==");
                condition = condition.replace(/\ and\ /g, " && ");
                condition = condition.replace(/\ or\ /g, " || ");
                re = RegExp(/\[([^\]]*)\]/g);
                condition = condition.replace(re, " $1 ");
                let bl = (`if ( ${condition} ) { ${data['Variable / Field Name']}.ui.hidden = false }`);
                blList.push(bl);
            }
            // decode html fields
            else if ((schemaMap[current_key] === 'question' || schemaMap[current_key] ==='schema:description') & data[current_key] !== '') {
                let questions = parseHtml(data[current_key]);
                rowData[schemaMap[current_key]] = questions;
            }
            // non-nested schema elements
            else if (data[current_key] !== '')
                rowData[schemaMap[current_key]] = data[current_key];
        }
        // insert non-existing mapping as is
        else rowData[camelcase(current_key)] = data[current_key];
    });
    const field_name = data['Variable / Field Name'];
    if (!order[form]) {
        order[form] = [];
        order[form].push(field_name);
    }
    else order[form].push(field_name);
    // write to item_x file
    fs.writeFile('activities/' + form + '/items/' + field_name + '.jsonld', JSON.stringify(rowData, null, 4), function (err) {
        if (err) {
            console.log("error in writing item schema", err);
        }
    });
}

function createFormSchema(form, formContextUrl) {
    let jsonLD = {
        "@context": [schemaContextUrl, formContextUrl],
        "@type": "https://raw.githubusercontent.com/ReproNim/schema-standardization/master/schemas/Activity.jsonld",
        "@id": `${form}_schema`,
        "skos:prefLabel": `${form }_schema`,
        "skos:altLabel": `${form}_schema`,
        "schema:description": `${form} schema`,
        "schema:schemaVersion": "0.0.1",
        "schema:version": "0.0.1",
        "branchLogic": {
            "javascript": blList
        },
        "scoringLogic": {
            "javascript": slList
        },
        "ui": {
            "order": order[form],
            "shuffle": false
        }
    };
    const op = JSON.stringify(jsonLD, null, 4);
    // console.log(269, jsonLD);
    fs.writeFile(`activities/${form}/${form}_schema.jsonld`, op, function (err) {
        if (err) {
            console.log("error in writing form schema", err)
        }
        else console.log("Instrument schema created");
    });
}

function parseLanguageIsoCodes(inputString){
    let languages = [];
    const root = HTMLParser.parse(inputString);
    if(root.childNodes.length > 0 && inputString.indexOf('lang') !== -1){
        if(root.childNodes){
            root.childNodes.forEach(htmlElement => {
                if (htmlElement.rawAttributes && htmlElement.rawAttributes.hasOwnProperty('lang')) {
                    languages.push(htmlElement.rawAttributes.lang)
                }
            });
        }
    }
    return languages;
}

function parseHtml(inputString) {
    let result = {};
    const root = HTMLParser.parse(inputString);
    if(root.childNodes.length > 0 ){
        if (root.childNodes) {
            root.childNodes.forEach(htmlElement => {
                if(htmlElement.text) {
                    if (htmlElement.rawAttributes && htmlElement.rawAttributes.hasOwnProperty('lang')) {
                        result[htmlElement.rawAttributes.lang] = htmlElement.text;
                    } else {
                        result[defaultLanguage] = htmlElement.text;
                    }
                }
            });
        }
    }
    else {
        result[defaultLanguage] = inputString;
    }
    return result;
}

