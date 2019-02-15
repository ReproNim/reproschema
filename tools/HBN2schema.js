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
};
const uiInputTypes = {
    'single choice': 'radio',
    'text entry': 'text',
    'text entry.': 'text',
    'numeric': 'number'
};
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
let respVal;
// get all field names and instrument name
csv
    .fromStream(readStream, options)
    .on('data', function (data) {

        let Questionnaire = (data['Questionnaire Name']).replace(/[&\/\\#,+()$~%.'":*?<>{}, +]/g, '');
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
        if (!preambleObj[Questionnaire]) {
            if (data['Instructions'] !== '') {
                preambleObj[Questionnaire] = {'Instructions': data['Instructions']};
            }
            else preambleObj[Questionnaire] = {};
        }

        // check new sections and act accordingly
        if (data['Question Group Instruction'] !== '') {
            let section = (data['Question Group Instruction']).trim();
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
            let sectionList = [];
            let sectionNumber = 1;
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
                    row['Question Group Instruction'] = (row['Question Group Instruction']).trim();
                    // collect preamble for the section too
                    if (sectionList.indexOf(row['Question Group Instruction']) === -1) {
                        sectionList.push(row['Question Group Instruction']);
                        let sectionName = `Section${sectionNumber}`;
                        preambleObj[form][sectionName] = row['Question Group Instruction'];
                        // create section schema
                        createFormSchema(sectionName, formContextUrl, 0);
                        contextOBj[sectionName] = { "@id": `${form}/${sectionName}.jsonld` , "@type": "@id" };
                        if (order.indexOf(sectionName) === -1) {
                            order.push(sectionName);
                        }
                        sectionNumber++;
                    }
                }
                else {
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

        if (schemaMap.hasOwnProperty(current_key) && current_key !== 'Question ID') {

            // check all ui elements to be nested under 'ui' key
            if (uiList.indexOf(schemaMap[current_key]) > -1) {
                let uiValue = (row[current_key]).toLowerCase();
                if (uiValue === 'single choice' || uiValue === 'multiple choice') {
                    if (uiValue === 'single choice')
                        respVal = false;
                    else if (uiValue === 'multiple choice')
                        respVal = true;
                    if (rowData.hasOwnProperty('responseOptions')) {
                        rowData.responseOptions['multipleChoice'] = respVal;
                    }
                    else {
                        rspObj['multipleChoice'] = respVal;
                        rowData['responseOptions'] = rspObj;
                    }
                }
                if (uiValue === 'multiple choice') {
                    if (rowData.hasOwnProperty('responseOptions')) {
                        rowData.responseOptions['multipleChoice'] = true;
                    }
                    else {
                        rspObj['multipleChoice'] = true;
                        rowData['responseOptions'] = rspObj;
                    }
                }
                if (uiInputTypes.hasOwnProperty(uiValue))
                    uiValue = uiInputTypes[uiValue];
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
        "preamble": "",
        "ui": {
            "shuffle": false
        }
    };
    if (blList.length) {
        console.log(301, blList);
        jsonLD.branchLogic = {
            "javascript": blList
        };
    }
    if (slList.length) {
        jsonLD.scoringLogic = {
            "javascript": slList
        };
    }
    if (formFlag) { // form schema
        if (preambleObj.hasOwnProperty(activity))
            jsonLD.preamble = preambleObj[activity]['Instructions'];
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
        if (preambleObj[currentForm].hasOwnProperty([activity]))
            jsonLD.preamble = preambleObj[currentForm][activity];
        let sectionorder = preambleObj[currentForm][activity];
        jsonLD.ui['order'] = sectionOrderObj[sectionorder]; // section order
        const op = JSON.stringify(jsonLD, null, 4);
        fs.writeFile(`activities/${currentForm}/${activity}_schema.jsonld`, op, function (err) {
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
