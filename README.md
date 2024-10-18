JSON to CSV Converter
Overview
This repository contains two scripts for handling JSON data conversion:

convertAdeJsonToJson.py: Converts ADE-specific JSON files into a format compatible with the second script.
convertJsonToCsv.js: Converts the transformed JSON files to CSV format, extracting specific fields.
Prerequisites
Python
convertAdeJsonToJson.py requires Python 3.x.
Ensure necessary Python packages (if any) are installed.
Node.js
convertJsonToCsv.js requires Node.js to run.
Install the required dependencies by running:
bash
Copy code
npm install json-to-csv
Usage
File Naming Conventions
To use these scripts without modifications, ensure your JSON files are named as follows:

The initial ADE JSON files that need to be transformed by the Python script should follow the naming pattern:
Copy code
data1Ade.json, data2Ade.json, data3Ade.json, etc.
After the Python script processes them, the output JSON files will be named in this format:
Copy code
data1Correct.json, data2Correct.json, data3Correct.json, etc.
The JavaScript script will then use these data#Correct.json files to create corresponding CSV files, named as:
Copy code
data1CsvDescription.csv, data2CsvDescription.csv, etc.
1. JSON to JSON Conversion (Python)
Run the Python script first to process ADE-specific JSON files and generate the corrected JSON files for CSV conversion.

How to run:
Place your ADE JSON files in the appropriate directory.
Run the Python script:
bash
Copy code
python convertAdeJsonToJson.py
This will output the transformed JSON files with names like data1Correct.json, data2Correct.json, etc.
2. JSON to CSV Conversion (JavaScript)
Once the JSON files have been processed by the Python script, you can convert them into CSV format using the JavaScript script.

How to run:
Ensure the transformed JSON files (data1Correct.json, data2Correct.json, etc.) are in the same directory.
Run the JavaScript script:
bash
Copy code
node convertJsonToCsv.js
The CSV files will be generated with names like data1CsvDescription.csv, data2CsvDescription.csv, etc.
Notes
File Naming: Be sure to follow the naming patterns for the JSON files to use the scripts as-is without needing to modify the code.
Make sure to run convertAdeJsonToJson.py first to prepare the JSON files.
Ensure that the JSON files contain description and subject fields, as these will be extracted into the CSV files.
Customize file paths and file names in both scripts if your JSON files do not follow the exact naming patterns mentioned above.
