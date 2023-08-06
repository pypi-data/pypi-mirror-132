# log4j-detector-to-csv

This project contains a script to convert and combine all host specific outputs of the [log4j-detector](https://github.com/mergebase/log4j-detector) logs in json format to one single CSV file.

## Getting started  

Prerequisites:
* python

Clone Repository:
```bash
git clone https://github.com/richardbischof/log4j-detector-to-csv.git
```

Change in directory:
```bash
cd log4j-detector-to-csv
```

Run Script:
```bash
python main.py -i $INPUT_DIRECTORY -o $OUTPUT_FILE
```

Example:
```bash 
python main.py -i logs -o report.csv
```
