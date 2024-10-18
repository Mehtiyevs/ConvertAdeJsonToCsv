const jsonToCSV = require('json-to-csv');
const fs = require('fs');
let index  = 1

function loadJSON(filePath) {
    
    try {
        const data = fs.readFileSync(filePath, 'utf8'); 
        
        return JSON.parse(data);
        
    } catch (err) {
        console.error("Error reading or parsing JSON file:", err);
        return null;
    }
}

while (index < 46 /* Last file of data"SpecificNumber"Correct.json provide here */) {

    const o = loadJSON(`data${index}Correct.json`)
    const oCopy = o.map(item => ({
        description: item.description,
        subject: item.subject
    }) )
    
    const fileName = `data${index}CsvDescription.csv`;



    jsonToCSV(oCopy, fileName)
    .then(() => {
    
    })
    .catch(error => {
    
    })

    index++
}






 
    





