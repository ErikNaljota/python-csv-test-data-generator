import csv
import random
import argparse
from random_word import RandomWords

# Setting up custom command line arguments
parser = argparse.ArgumentParser()
parser.add_argument("-n", "--name", type=str, dest="name", help="Sets the name of the output file.", default="test-data.csv")
parser.add_argument("-c", "--columns", type=int, dest="numCols", help="Sets a number of columns to generate.", default=3)
parser.add_argument("-r", "--rows", type=int, dest="numRows", help="Sets a number of rows to generate.", default=10)
parser.add_argument("-cc", "--customColumns", nargs="+", type=str, dest="custCols", help="Generates columns from a provided list.")
parser.add_argument("-cw", "--customWords", nargs="+", type=str, dest="custWords", help="Populates fields with provided list of words.")
parser.add_argument("-i", "--idColumn", type=bool, const="t", nargs="?", dest="hasIdColumn", help="Adds an ID column.", default=False)
parser.add_argument("-d", "--useDictionary", type=bool, const="t", nargs="?", dest="useDictionary", help="Loads words from dictionary.", default=False)
parser.add_argument("-cd", "--customDelimiter", type=str, dest="delimiter", help="Set custom delimiter in the output file.", default=",")
args = parser.parse_args()

randomWords = RandomWords()

def main():
    with open(args.name, "w", newline="") as file:
        writer = csv.writer(file, delimiter=args.delimiter)

        writer.writerow(generateColumns())

        printProgressBar(0, args.numRows, prefix = "Progress:", suffix = "Complete", length = args.numRows)

        for rowNum in range(args.numRows):
            writer.writerow(generateRow(rowNum))
            printProgressBar(rowNum + 1, args.numRows, prefix = "Progress:", suffix = "Complete", length = args.numRows)

def generateColumns():
    columns = []

    if args.hasIdColumn:
        columns.append("ID")

    if args.custCols:
        for col in args.custCols:
            columns.append(col)
    elif args.useDictionary:
        word = randomWords.get_random_word()
        columns.append(word if word != "None" else "Col" + str(args.numCols))
    else:
        for colNum in range(args.numCols):
            columns.append("Col "+ str(colNum))

    return columns

def generateRow(rowNum):
    row = []

    if args.hasIdColumn:
        row.append(rowNum)

    numOfCols = len(args.custCols) if args.custCols else args.numCols

    for col in range(numOfCols):
        if args.custWords:
            row.append(random.sample(args.custWords, 1))
        elif args.useDictionary:
            word = randomWords.get_random_word()
            row.append(word if word != "None" else "-")
        else:
            row.append("Word " + str(rowNum) + str(col))

    return row

# Progress bar by Greenstick https://stackoverflow.com/a/34325723
def printProgressBar (iteration, total, prefix = '', suffix = '', decimals = 1, length = 100, fill = '█', printEnd = "\r"):
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print(f'\r{prefix} |{bar}| {percent}% {suffix}', end = printEnd)
    # Print New Line on Complete
    if iteration == total: 
        print()

main()