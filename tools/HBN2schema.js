/* ************ Constants **************************************************** */
const csv = require('fast-csv');
const fs = require('fs');
const shell = require('shelljs');
const camelcase = require('camelcase');
const HTMLParser =  require ('node-html-parser');

const schemaMap = {
    'Instructions': 'preamble',
    //'Question Group Instruction': 'preamble',
    'Question (number optionally included)': 'question',
    'Question ID': 'skos:altLabel',
    'Response Type': 'inputType',
    'Response Options': 'choices',
    'Stevens\' level of measurement': 'type',
    // 'Position of \'0\'': 'Center',
    // 'Continuous or Discrete': 'Discrete',
}
const uiList = ['inputType', 'shuffle'];
const responseList = ['type', 'minValue', 'maxValue', 'requiredValue', 'multipleChoice'];
const defaultLanguage = 'en';
const datas = {};
const preambleObj = {};

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
let order = [];
let blList = [];
let slList = [];
let languages = [];
let options = {
    delimiter: ',',
    headers: true,
    objectMode: true,
    quote: '"',
    escape: '"',
    ignoreEmpty: true
};
let field_counter;
// get all field names and instrument name
csv
    .fromStream(readStream, options)
    .on('data', function (data) {


        if (!datas[data['Questionnaire Name']]) {

            field_counter = 0;

            datas[data['Questionnaire Name']] = [];
            // For each form, create directory structure - activities/form_name/items
            shell.mkdir('-p', 'activities/' + data['Questionnaire Name'] + '/items');
        }
        // create new Questionnaire ID when it is null
        if (data['Questionnaire ID'] === '') {
            data['Questionnaire ID'] = abbreviate(data['Questionnaire Name']);
            console.log(60, data['Questionnaire ID']);
        }
        field_counter = field_counter + 1;
        // create new Question ID when it is null
        if (data['Question ID'] === '') {
            data['Question ID'] = data['Questionnaire ID'] + '_' + field_counter;
            console.log(71, data['Question ID']);
        }

        datas[data['Questionnaire Name']].push(data);
        // collect preamble for every form
        if (!preambleObj[data['Questionnaire Name']] && data['Instructions'] !== '')
            preambleObj[data['Questionnaire Name']] = data['Instructions'];

    })
    .on('end', function () {

        Object.keys(datas).forEach(form => {
            let rowList = datas[form];
            createFormContextSchema(form, rowList);
            let formContextUrl = `https://raw.githubusercontent.com/ReproNim/schema-standardization/master/activities/${form}/${form}_context.jsonld`;
            let field_counter = 0;
            rowList.forEach( row => {
                if(languages.length === 0){
                    languages = parseLanguageIsoCodes(row['Question (number optionally included)']);
                }
                field_counter = field_counter + 1;
                processRow(form, row, field_counter);
            });
            createFormSchema(form, formContextUrl);
        });
    });

function createFormContextSchema(form, rowList) {
    // define context file for each form
    let itemOBj = { "@version": 1.1 };
    let formContext = {};
    itemOBj[form] = `https://raw.githubusercontent.com/ReproNim/schema-standardization/master/activities/${form}/items/`;
    let field_counter = 0;
    rowList.forEach( row => {
        // check Question ID and correct if needed
        //field_counter = field_counter + 1;
        let field_name = row['Question ID'];
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

function processRow(form, row, field_counter){
    let rowData = {};
    let ui = {};
    let rspObj = {};
    let choiceList = [];
    rowData['@context'] = [schemaContextUrl];
    rowData['@type'] = 'https://raw.githubusercontent.com/ReproNim/schema-standardization/master/schemas/Field.jsonld';

    // check Question ID and correct if needed
    // let field_name = parseQuestionID(row['Question ID'], row, field_counter);
    let field_name = row['Question ID'];
    rowData[schemaMap['Question ID']] = field_name;
    Object.keys(row).forEach(current_key => {

        // get schema key from mapping.json corresponding to current_key
        if (schemaMap.hasOwnProperty(current_key) && current_key !== 'Question ID') {
            // if (schemaMap[current_key] === 'scoringLogic' && data[current_key] !== '')

            // check all ui elements to be nested under 'ui' key
            if (uiList.indexOf(schemaMap[current_key]) > -1) {
                let uiValue = row[current_key];
                /*if (current_key === 'Field Type' && row[current_key] === 'calc')
                    uiValue = 'number';*/

                if (rowData.hasOwnProperty('ui')) {
                    rowData.ui[schemaMap[current_key]] = uiValue;
                }
                else {
                    ui[schemaMap[current_key]] = uiValue;
                    rowData['ui'] = ui;
                }
            }
            // when Question ID is null
            else if ((schemaMap[current_key] === 'skos:altLabel' && row[current_key] === '')) {
                field_name = row['Questionnaire ID'] + '_' + field_counter;
            }
            // parse choice field
            else if (schemaMap[current_key] === 'choices' & row[current_key] !== '') {

                // split string wrt '|' to get each choice
                let c = row[current_key].split(',');
                // split each choice wrt ',' to get schema:name and schema:value
                c.forEach(ch => {
                    let choiceObj = {};
                    let cs = ch.split('=');
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
                    rowData.responseOptions[schemaMap[current_key]] = row[current_key];
                }
                else {
                    rspObj[schemaMap[current_key]] = row[current_key];
                    rowData['responseOptions'] = rspObj;
                }
            }
            // scoring logic
            else if (schemaMap[current_key] === 'scoringLogic' && row[current_key] !== '') {
                // set ui.hidden for the item to true by default
                if (rowData.hasOwnProperty('ui')) {
                    rowData.ui['hidden'] = true;
                }
                else {
                    ui['hidden'] = true;
                    rowData['ui'] = ui;
                }
                let condition = row[current_key];
                let s = condition;
                // normalize the condition field to resemble javascript
                let re = RegExp(/\(([0-9]*)\)/g);
                condition = condition.replace(re, "___$1");
                condition = condition.replace(/([^>|<])=/g, "$1 ==");
                condition = condition.replace(/\ and\ /g, " && ");
                condition = condition.replace(/\ or\ /g, " || ");
                re = RegExp(/\[([^\]]*)\]/g);
                condition = condition.replace(re, " $1 ");
                let sl = `${row['Question ID']} = ${condition}`;
                slList.push(sl);
            }
            // branching logic
            else if (schemaMap[current_key] === 'branchLogic' & row[current_key] !== '') {
                // set ui.hidden for the item to true by default
                if (rowData.hasOwnProperty('ui')) {
                    rowData.ui['hidden'] = true;
                }
                else {
                    ui['hidden'] = true;
                    rowData['ui'] = ui;
                }
                let condition = row[current_key];
                let s = condition;
                // normalize the condition field to resemble javascript
                let re = RegExp(/\(([0-9]*)\)/g);
                condition = condition.replace(re, "___$1");
                condition = condition.replace(/([^>|<])=/g, "$1 ==");
                condition = condition.replace(/\ and\ /g, " && ");
                condition = condition.replace(/\ or\ /g, " || ");
                re = RegExp(/\[([^\]]*)\]/g);
                condition = condition.replace(re, " $1 ");
                let bl = (`if ( ${condition} ) { ${row['Question ID']}.ui.hidden = false }`);
                blList.push(bl);
            }
            // decode html fields
            else if ((schemaMap[current_key] === 'question' || schemaMap[current_key] ==='schema:description') & row[current_key] !== '') {
                let questions = parseHtml(row[current_key]);
                rowData[schemaMap[current_key]] = questions;
            }
            // non-nested schema elements
            else if (row[current_key] !== '')
                rowData[schemaMap[current_key]] = row[current_key];
        }
        // insert non-existing mapping as is
        // else rowData[camelcase(current_key)] = row[current_key];
    });
    order.push(field_name);
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
        "preamble": preambleObj[form],
        "branchLogic": {
            "javascript": blList
        },
        "scoringLogic": {
            "javascript": slList
        },
        "ui": {
            "order": order,
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

function parseQuestionID(QId, row, field_counter) {
    // console.log(312, QId, field_counter);
    if (QId !== '')
        return QId;
    // when Question ID is null, assign it to QuestionnaireID_x
    else {
        // console.log(317, row['Questionnaire ID'] + '_' + field_counter);
        // check if Questionnaire ID exists. If not abbreviate Questionnaire Name and get one.
        if (row['Questionnaire ID'] !== '')
            return row['Questionnaire ID'] + '_' + field_counter;
        else {
            abbreviate(row['Questionnaire Name'], field_counter);
        }
    }

}

/*function abbreviate(QName, field_counter) {
    // var toMatch = "The Columbia Impairment Scale-Self Report Version";
    var result = QName.replace(/(\w)\w*\W*!/g, function (_, i) {
            return i.toUpperCase();
        }
    )
    console.log(66, result + '_' + field_counter);
}*/

function abbreviate(QName) {
    // var toMatch = "The Columbia Impairment Scale-Self Report Version";
    var result = QName.replace(/(\w)\w*\W*/g, function (_, i) {
            return i.toUpperCase();
        }
    )
    return result;
    //console.log(66, QName, result);
}
