//specify the path to your input CSV
let csvPath = 'ABCD_csv/family_history.csv';
const csv = require('fast-csv');
const fs = require('fs');
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
const langList = ['en', 'es'];

let readStream = fs.createReadStream(csvPath).setEncoding('utf-8');

let schemaContextUrl = 'https://raw.githubusercontent.com/ReproNim/schema-standardization/master/contexts/generic.jsonld';
let formContextUrl = '';
let ins_name = '';
let order = [];
let blObj = [];
let graphArr = [];
let formContext = {};
let itemOBj = { "@version": 1.1 };
let languages = [];
const defaultLanguage = 'en';

// create directory structure - activities/form_name/items
mkdirp('activities/family_history_assessment_parent/items', function (err) {
    if (err){
        console.log(err);
    }else{
        console.log('directory created in activities')
    }
});

let options = {
    delimiter: ',',
    headers: true,
    objectMode: true,
    quote: '"',
    escape: '"',
    ignoreEmpty: true
};

let dataArr = [];
let readFileStream = fs.createReadStream(csvPath).setEncoding('utf-8');
readStream.pipe(csv(options))
    .on('data', function(data){
        dataArr.push(data); // Add a row
        ins_name = data['Form Name'];
        let field_name = data['Variable / Field Name'];
        // define item_x urls to be inserted in context
        itemOBj[field_name] = { "@id": `${ins_name}:${field_name}.jsonld` , "@type": "@id" };
        itemOBj[ins_name] = `https://raw.githubusercontent.com/ReproNim/schema-standardization/master/activities/${ins_name}/items/`;
        readFileStream.destroy();
    })
    .on('end', function(){
        formContext['@context'] = itemOBj;
        const fc = JSON.stringify(formContext, null, 4);
        fs.writeFile('activities/family_history_assessment_parent/' + ins_name + '_context' + '.jsonld', fc, function(err) {
            console.log("Context created");
        });
        formContextUrl = `https://raw.githubusercontent.com/ReproNim/schema-standardization/master/activities/${ins_name}/${ins_name}_context.jsonld`;
        for (let i = 0, len = dataArr.length; i < len; i++) {
            if (i === 0) { // take instrument name from first row - 'Form Name' column
                if (ins_name === '') {
                    ins_name = dataArr[i]['Form Name'];
                }
            }
            if(languages.length === 0){
                languages = parseLanguageIsoCodes(dataArr[i]['Field Label']);
            }

            processRow(dataArr[i]);
        }
        finishSchemaCreation();
    });

function processRow(data){
    let rowData = {};
    let ui = {};
    let rspObj = {};
    let choiceList = [];
    rowData['@context'] = [schemaContextUrl, formContextUrl];
    rowData['@type'] = 'https://raw.githubusercontent.com/ReproNim/schema-standardization/master/schemas/Field.jsonld';
    Object.keys(data).forEach(current_key => {
        if (current_key !== 'Form Name') {
            // get schema key from mapping.json corresponding to current_key
            if (schemaMap.hasOwnProperty(current_key)) {
                // check all ui elements to be nested under 'ui' key
                if (uiList.indexOf(schemaMap[current_key]) > -1) {

                    if (rowData.hasOwnProperty('ui')) {
                        rowData.ui[schemaMap[current_key]] = data[current_key];
                    }
                    else {
                        ui[schemaMap[current_key]] = data[current_key];
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
                // check all response elements to be nested under 'responseOptions' key
                else if (responseList.indexOf(schemaMap[current_key]) > -1) {
                    if (rowData.hasOwnProperty('responseOptions')) {
                        rowData.responseOptions[schemaMap[current_key]] = data[current_key];
                    }
                    else {
                        rspObj[schemaMap[current_key]] = data[current_key];
                        rowData['responseOptions'] = rspObj;
                    }
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
                    blObj.push(bl);
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
            // insert current_key in schema for non-existing mapping
            else rowData[camelcase(current_key)] = data[current_key];
        }
    });
    ins_name = data['Form Name'];
    const field_name = data['Variable / Field Name'];
    order.push(field_name);
    // write to item_x file
    fs.writeFileSync('activities/' + ins_name + '/items/' + field_name + '.jsonld', JSON.stringify(rowData, null, 4));
    graphArr.push(rowData);
}

function finishSchemaCreation() {
    let jsonLD = {
        "@context": [schemaContextUrl, formContextUrl],
        "@type": "https://raw.githubusercontent.com/ReproNim/schema-standardization/master/schemas/Activity.jsonld",
        "@id": ins_name + '_schema',
        "skos:prefLabel": ins_name + '_schema',
        "skos:altLabel": ins_name + '_schema',
        "schema:description": ins_name + ' schema',
        "schema:schemaVersion": "0.0.1",
        "schema:version": "0.0.1",
        "branchLogic": {
            "javascript": blObj
        },
        "scoringLogic": {
            "javascript": ""
        },
        "ui": {
            "order": order,
            "shuffle": false
        }
    };
    const op = JSON.stringify(jsonLD, null, 4);
    fs.writeFile('activities/family_history_assessment_parent/' + ins_name + '_schema' + '.jsonld', op, function (err) {
        console.log("Instrument schema created");
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


