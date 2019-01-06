//specify the path to your input CSV
let csvPath = 'ABCD_csv/family_history.csv';
const csv = require('fast-csv');
const fs = require('fs');
const camelcase = require('camelcase');
const mkdirp = require('mkdirp');
const striptags = require('striptags')

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

// get schema context
let schemaContext = 'https://raw.githubusercontent.com/sanuann/schema-standardization/master/contexts/generic.jsonld';

let readStream = fs.createReadStream(csvPath).setEncoding('utf-8');
let chunks = [];


// Listen for data
readStream.on('data', chunk => {
    // console.log('37', chunk['Form Name']);
    chunks.push(chunk);
});

let ins_name = '';
let order = [];
let blObj = [];
let graphArr = [];
let options = {
    delimiter: ',',
    headers: true,
    objectMode: true,
    quote: '"',
    escape: '"',
    ignoreEmpty: true
};

// create directory structure - activities/form_name/items
mkdirp('activities/family_history_assessment_parent/items', function (err) {
    if (err){
        console.log(err);
    }else{
        console.log('we are good.')
    }
});

let csvStream = csv(options)
    .on("data", function(data){
        let rowData = {};
        let ui = {};
        let rspObj = {};
        let choiceList = [];
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
                    else if (schemaMap[current_key] === 'choices' & data[current_key] !== '') {
                        // parse choice field

                        // split string wrt '|' to get each choice
                        let c = data[current_key].split('|');
                        // split each choice wrt ',' to get schema:name and schema:value
                        c.forEach(ch => {
                            let choiceObj = {};
                            let cs = ch.split(', ');
                            // console.log(94, cs);
                            // create name and value pair for each choice option
                            choiceObj['schema:value'] = cs[0];
                            let cnameList = (cs[1].slice(cs[1].indexOf('<span ')));
                            // console.log(99, unHTML(cnameList));
                            choiceObj['schema:name'] = cnameList;
                            choiceList.push(choiceObj);

                        });
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
                        // console.log(93, data[current_key]);
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
                    else if (schemaMap[current_key] === 'question' & data[current_key] !== '') {
                        // console.log(unHTML(data[current_key]));
                        langList.forEach(lang => {

                            // console.log(lang);
                            if (data[current_key].indexOf(`<span lang="${lang}">`) > -1) {
                                let start = data[current_key].indexOf(`<span`) + '<span lang="en">'.length;
                                // console.log('hi', start);
                                let q = data[current_key].slice(start, data[current_key].indexOf('</span'));
                                // console.log(q);
                            }
                        });

                    }

                    // non-nested schema elements
                    else if (data[current_key] !== '')
                        rowData[schemaMap[current_key]] = data[current_key];
                }
                // insert current_key in schema for non-existing mapping
                else rowData[camelcase(current_key)] = data[current_key];
            }
            else if (current_key === 'Variable / Field Name') order.push(data[current_key]);
        });
        ins_name = data['Form Name'];
        const item_name = data['Variable / Field Name'];
        // write to item_x file
        fs.writeFileSync('activities/' + ins_name + '/items/' + item_name + '.jsonld', JSON.stringify(rowData, null, 4));
        graphArr.push(rowData);
    })
    .on("end", function(){
        let jsonLD = {
            "@context": schemaContext,
            "@type": "https://raw.githubusercontent.com/ReproNim/schema-standardization/master/schemas/Activity.jsonld",
            "@id": ins_name + '_schema',
            "skos:prefLabel": ins_name + '_schema',
            "skos:altLabel": ins_name + '_schema',
            "schema:description": ins_name + ' schema',
            "schema:schemaVersion": "0.0.1",
            "schema:version": "0.0.1",
            "branchLogic": {
                "javascript": blObj},
            "scoringLogic": {
                "javascript": ""},
            "ui": {
                "order": order,
                "shuffle": false
            }
        };
        const op = JSON.stringify(jsonLD, null, 4);
        fs.writeFile('activities/family_history_assessment_parent/' + ins_name + '_schema' + '.jsonld', op, function(err) {
            console.log("File created");
        });
        console.log('total rows of table', graphArr.length);
    });
readStream.pipe(csvStream);

function unHTML( str ) {
    var s = str;
    if (typeof str === 'undefined') {
        return "";
    }
    // we might have no spaces between the spanish and english versions, lets add some first
    str = str.replace(/\<\/span\>/g, "</span> ");
    str = striptags(str);
    str = str.replace(/\&nbsp/g, " ");
    str = str.trim();

    // we could have our own html-ish tags here, try to remove those as well
    var regex = /(##en##)/ig
    str = str.replace(regex,"");
    var regex = /(##es##)/ig
    str = str.replace(regex,"");
    var regex = /(##\/en##)/ig
    str = str.replace(regex," ");
    var regex = /(##\/es##)/ig
    str = str.replace(regex," ");

    // console.log("before: \"" + s + "\" after :\"" + str + "\"")
    return str;
}
