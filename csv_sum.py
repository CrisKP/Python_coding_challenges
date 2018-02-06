import sys
import csv

file_name = sys.argv[1]
column = int(sys.argv[2])


def col_add(file_name, column):
    '''Give a Comma Separated File (csv) and a column number (zero being the left most column) and return the sum of all the entries in that column.'''
    # Open the file passed as a parameter, and read and save content to a variable.
    file = open(file_name, "r", encoding="utf-8-sig")
    text = csv.reader(file)
    total = 0

    # Loop through the rows to get the content in the specified index (column number) and add to the total variable. Close file.
    for row in text:
        total += (int(row[column]))
    file.close()
    print(total)

col_add(file_name, column)
