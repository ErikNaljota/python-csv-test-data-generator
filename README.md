# python-csv-test-data-generator
This is a small script I made during my graduation internship with the purpose of conveniently generating test data in the form of CSV files.

## Basic Usage

If you don't have pipreqs installed:
```sh
$ pip3 install pipreqs
```

Install the dependencies
```sh
$ pipreqs .
```

Run the script. By default it will generate 10 rows and 3 columns and name the file test-data.csv
```sh
$ python3 python-csv-test-data-generator.py
```

## Available commands

All of the commands are optional.
- `-n` OR `--name` - Give a custom name to the output file. The script does not check for file extension, so it's up to you to add it or not
- `-c` OR `--columns` - Set a number of columns to generate
- `-r` OR `--rows` - Set a number of rows to generate
- `-cc` OR `--customColumns` - Set custom names for the columns
- `-cw` OR `--customWords` - Use a set of custom words (it will choose words at random, when filling the cell)
- `-i` OR `--idColumn` - If set, will add an `ID` column to the output file as first column
- `-d` OR `--useDictionary` - If set, will generate words from a dictionary. Note: if custom words were provided as one of the arguments, this flag will be ignored
- `-cd` OR `--customDelimiter` - Set a custom delimiter that is not a comma


## Example

This command will generate a file called `my-test-data.csv` with 3 custom columns, an ID column, and 5 rows filled with words from a dictionary (please note that the dictionary functionality takes a little longer to generate the file).
```sh
$ python3 python-csv-test-data-generator.py -n my-test-data.csv -cc apple orange banana -i -r 5 -d
```
OR a more verbose version
```sh
$ python3 python-csv-test-data-generator.py --name my-test-data.csv --customColumns apple orange banana --idColumn --rows 5 --useDictionary
```

## Acknowledgements
To make this script, I used RandomWord package by [vaibhavsingh97](https://github.com/vaibhavsingh97) on Github and an [answer](https://stackoverflow.com/a/34325723) by Greenstick on StackOverflow on a simple progress bar in Python.