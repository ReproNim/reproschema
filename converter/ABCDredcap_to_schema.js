//specify the path to your input CSV
let csvPath = 'redcap_data/demographics.csv';
const csv = require('fast-csv');
const fs = require('fs');
const mkdirp = require('mkdirp');

const schemaMap = {
    "Variable / Field Name": "altLabel",
    "Section Header": "preamble",
    "Field Type": "inputType",
    "Field Label": "question",
    "Choices, Calculations, OR Slider Labels": "choices",
    "Field Note": "description",
    "Text Validation Type OR Show Slider Number": "xy",
    "Identifier?": "@id",
    "Branching Logic (Show field only if...)": "branchLogic",
    "Required Field?": "requiredValue"
}

// let graphArr = [];
let stream = fs.createReadStream(csvPath).setEncoding('utf-8');
// create directory structure - activities/form_name/items
mkdirp('/activities1/demographics/items', 0o777, function (err) {
    if (err) { throw err; }
    console.log("done creation of directories");
});
let ins_name = '';
let csvData = [];
let options = {
    delimiter: ',',
    headers: true,
    objectMode: true,
    quote: '"',
    escape: '"',
    ignoreEmpty: true
};
let csvStream = csv(options)
    .on("data", function(data){
        let rowData = {};
        Object.keys(data).forEach(current_key => {
            // get schema key from mapping.json corresponding to current_key
            if (schemaMap.hasOwnProperty(current_key)) {
                rowData[schemaMap[current_key]] = data[current_key];
            }
            // create new key in schema for non-existing mapping
            else rowData[current_key] = data[current_key];
        });
        ins_name = data['Form Name'];
        const item_name = data['Variable / Field Name'];
        // write to item_x file
        fs.writeFileSync('output/' + item_name + '.jsonld', JSON.stringify(rowData));
        csvData.push(rowData);
    })
    .on("end", function(){
        const op = JSON.stringify(csvData);
        fs.writeFile('output/demographics' + '.jsonld', op, function(err) {
            console.log("File created");
        });
        console.log('csvData', csvData);
        console.log('total rows of table', csvData.length);
    });
stream.pipe(csvStream);
