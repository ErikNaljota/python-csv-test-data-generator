# Python CSV test data generator
This is a small script I made during my graduation internship with the purpose of conveniently generating test data in the form of CSV files.

## Basic Usage

0. If you don't have pipreqs installed:
```sh
$ pip3 install pipreqs
```

1. Install the dependencies
```sh
$ pipreqs .
```

2. Run the script. By default it will generate 10 rows and 3 columns and name the file test-data.csv
```sh
$ python3 python-csv-test-data-generator.py
```

## Available commands

| Argument                      | Functionality                                                         |
| ------------------------------| ----------------------------------------------------------------------|
|`--name` OR `-n`               | Give a custom name to the output file. The script does not check for file extension, so it's up to you to add it or not.|
|`--columns` OR `-c`            | Set a number of columns to generate.                                  |
|`--rows` OR `-r`               | Set a number of rows to generate.                                     |
|`--customColumns` OR `-cc`     | Set custom names for the columns.                                     |
|`--customWords` OR `-cw`       | Use a set of custom words (it will choose words at random, when filling the cell).|
|`--idColumn` OR `-i`           | If set, will add an `ID` column to the output file as first column.   |
|`--useDictionary` OR `-d`      | If set, will generate words from a dictionary (this takes longer to run than to use automatic/custom words). **Note:** if custom words were provided as one of the arguments, this flag will be ignored. |
|`--customDelimiter` OR `-cd`   | Set a custom delimiter that is not a comma.                           |

## Example

This command will generate a file called `my-test-data.csv` with 3 custom columns, an ID column, and 5 rows filled with words from a dictionary (please note that the dictionary functionality takes a little longer to generate the file).
```sh
$ python3 python-csv-test-data-generator.py -n my-test-data.csv -i -r 5 --cw apple orange banana cherry raspberry
```
OR a more verbose version
```sh
$ python3 python-csv-test-data-generator.py --name my-test-data.csv --idColumn --rows 5 --customWords apple orange banana cherry raspberry
```

**NOTE:**
When trying to add a custom delimiter, make sure to use the following syntax in the command line:
```sh
$ python3 python-csv-test-data-generator.py -cd="|"
```

**The output will look something like this:**
| ID | Col 0        | Col 1         | Col 2         | 
|----|--------------|---------------|---------------|
| 1  | orange       | raspberry     | cherry        |
| 2  | cherry       | banana        | raspberry     |
| 3  | apple        | raspberry     | cherry        |
| 4  | apple        | banana        | cherry        |

## License
Built with ♥ by Erik Naljota under [MIT License](https://erik-naljota.mit-license.org/)

## Acknowledgements
To make this script, I used RandomWord package by [vaibhavsingh97](https://github.com/vaibhavsingh97) on Github and an [answer](https://stackoverflow.com/a/34325723) by Greenstick on StackOverflow on a simple progress bar in Python.