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
const sectionOrderObj = {};
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
let currentForm = '';
let QInstructionList = [];
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

        let Questionnaire = (data['Questionnaire Name']).replace(/ +/g, "");
        if (!datas[Questionnaire]) {

            field_counter = 0;
            datas[Questionnaire] = [];
            // For each form, create directory structure - activities/form_name/items
            shell.mkdir('-p', 'activities/' + Questionnaire + '/items');
        }
        // create new Questionnaire ID when it is null
        if (data['Questionnaire ID'] === '') {
            data['Questionnaire ID'] = abbreviate(data['Questionnaire Name']);
        }
        field_counter = field_counter + 1;
        // create new Question ID when it is null
        if (data['Question ID'] === '') {
            data['Question ID'] = data['Questionnaire ID'] + '_' + field_counter;
        }

        datas[Questionnaire].push(data);

        // collect preamble for every form
        if (!preambleObj[data['Questionnaire Name']] && data['Instructions'] !== '')
            preambleObj[data['Questionnaire Name']] = data['Instructions'];

        // check new sections and act accordingly
        if (data['Question Group Instruction'] !== '') {
            let section = (data['Question Group Instruction']).replace(/ +/g, "");
            if (QInstructionList.indexOf(section) === -1) {
                QInstructionList.push(section);
                // create directory structure for sections
                shell.mkdir('-p', 'activities/' + Questionnaire + '/' + section);
            }
            // set order of fields in section
            if (!sectionOrderObj[section])
                sectionOrderObj[section] = [];
            sectionOrderObj[section].push(data['Question ID']);
        }
    })
    .on('end', function () {
        Object.keys(datas).forEach(form => {
            order = [];
            currentForm = form;
            let rowList = datas[form];
            let formContextUrl = `https://raw.githubusercontent.com/ReproNim/schema-standardization/master/activities/${form}/${form}_context.jsonld`;
            // define context schema object for each form
            let contextOBj = { "@version": 1.1 };
            contextOBj[form] = `https://raw.githubusercontent.com/ReproNim/schema-standardization/master/activities/${form}/items/`;
            rowList.forEach( row => {
                if(languages.length === 0){
                    languages = parseLanguageIsoCodes(row['Question (number optionally included)']);
                }
                let field_name = row['Question ID'];
                // check if Question Group Instruction exist
                if (row['Question Group Instruction'] !== '') {
                    let sectionID = abbreviate(row['Question Group Instruction']);
                    let sectionName = row['Question Group Instruction'].replace(/ +/g, "");
                    // collect preamble for the section too
                    if (!preambleObj[sectionID])
                        preambleObj[sectionID] = row['Question Group Instruction'];

                    // create section schema
                    createFormSchema(sectionName, formContextUrl, 0);
                    // let field_name = sectionID; // to be used in the form context schema
                    contextOBj[sectionID] = { "@id": `${form}/${sectionName}/${sectionName}.jsonld` , "@type": "@id" };
                    if (order.indexOf(sectionID) === -1) {
                        order.push(sectionID);
                    }
                }
                else {
                    // console.log(126,row['Question ID']);
                    order.push(field_name);
                }
                // define item_x urls to be inserted in context for the corresponding form
                contextOBj[field_name] = { "@id": `${form}:${field_name}.jsonld` , "@type": "@id" };

                processRow(form, row);
            });
            // write context schema to file
            let formContext = {'@context': contextOBj};
            const fc = JSON.stringify(formContext, null, 4);
            fs.writeFile(`activities/${form}/${form}_context.jsonld`, fc, function(err) {
                if (err)
                    console.log(err);
                else console.log(`Context created for form ${form}`);
            });
            // generate each form schema
            createFormSchema(form, formContextUrl, 1);
        });
    });

function createFormContextSchema(form, row, contextOBj) {

}

function processRow(form, row){
    let rowData = {};
    let ui = {};
    let rspObj = {};
    let choiceList = [];
    rowData['@context'] = [schemaContextUrl];
    rowData['@type'] = 'https://raw.githubusercontent.com/ReproNim/schema-standardization/master/schemas/Field.jsonld';
    let field_name = row['Question ID'];
    rowData[schemaMap['Question ID']] = field_name;
    Object.keys(row).forEach(current_key => {

        // get schema key from mapping.json corresponding to current_key
        if (schemaMap.hasOwnProperty(current_key) && current_key !== 'Question ID') {

            // check all ui elements to be nested under 'ui' key
            if (uiList.indexOf(schemaMap[current_key]) > -1) {
                let uiValue = row[current_key];

                if (rowData.hasOwnProperty('ui')) {
                    rowData.ui[schemaMap[current_key]] = uiValue;
                }
                else {
                    ui[schemaMap[current_key]] = uiValue;
                    rowData['ui'] = ui;
                }
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
    // write to item_x file
    fs.writeFile('activities/' + form + '/items/' + field_name + '.jsonld', JSON.stringify(rowData, null, 4), function (err) {
        if (err) {
            console.log("error in writing item schema", err);
        }
    });
}

function createFormSchema(activity, formContextUrl, formFlag) {
    let jsonLD = {
        "@context": [schemaContextUrl, formContextUrl],
        "@type": "https://raw.githubusercontent.com/ReproNim/schema-standardization/master/schemas/Activity.jsonld",
        "@id": `${activity}_schema`,
        "skos:prefLabel": `${activity }_schema`,
        "skos:altLabel": `${activity}_schema`,
        "schema:description": `${activity} schema`,
        "schema:schemaVersion": "0.0.1",
        "schema:version": "0.0.1",
        "preamble": preambleObj[activity],
        "branchLogic": {
            "javascript": blList
        },
        "scoringLogic": {
            "javascript": slList
        },
        "ui": {
            "shuffle": false
        }
    };

    if (formFlag) { // form schema
        jsonLD.ui['order'] = order;
        const op = JSON.stringify(jsonLD, null, 4);
        fs.writeFile(`activities/${activity}/${activity}_schema.jsonld`, op, function (err) {
            if (err) {
                console.log("error in writing form schema", err)
            }
            else console.log("Instrument schema created");
        });
    }
    else { // section schema
        jsonLD.ui['order'] = sectionOrderObj[activity]; // section order
        const op = JSON.stringify(jsonLD, null, 4);
        fs.writeFile(`activities/${currentForm}/${activity}/${activity}_schema.jsonld`, op, function (err) {
            if (err) {
                console.log("error in writing section schema", err)
            }
            else console.log("Section schema created");
        });
    }
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

function abbreviate(QName) {
    var result = QName.replace(/(\w)\w*\W*/g, function (_, i) {
            return i.toUpperCase();
        }
    )
    return result;
}
