# log4j-detector-to-csv

This project contains a script to convert and combine all host specific outputs of the [log4j-detector](https://github.com/mergebase/log4j-detector) logs in json format to one single CSV file.

## Getting started  

### With Python and pip installed

Install log4j-detector-to-csv with pip:
```bash
pip install log4j-detector-to-csv
```

Run log4j-detector-to-csv:
```bash
log4j-detector-to-csv -h
```

Output:
```bash
usage: log4j-detector-to-csv [-h] -i INPUT -o OUTPUT

Convert log4j-detector json file into one csv

optional arguments:
  -h, --help            show this help message and exit
  -i INPUT, --input INPUT
                        Input directory
  -o OUTPUT, --output OUTPUT
                        Output directory

```

### From Sourcecode
Prerequisites:
* python
* poetry

Clone Repository:
```bash
git clone https://github.com/richardbischof/log4j-detector-to-csv.git
```

Change in directory:
```bash
cd log4j-detector-to-csv/log4j_detector_to_csv
```

Run Script:
```bash
python main.py -i $INPUT_DIRECTORY -o $OUTPUT_FILE
```

Example:
```bash 
python main.py -i logs -o report.csv
```
