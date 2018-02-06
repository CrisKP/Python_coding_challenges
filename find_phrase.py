import sys

file_name = sys.argv[1]
phrase = sys.argv[2]


def checker(file_name, phrase):
    '''Give a text file and a string and return True if the phrase is found in the document or False otherwise.'''
    # Open the file passed as a parameter, and read and save the content to a variable.
    file = open(file_name, "r")
    text = file.read()

    # Search if the phrase passed as a parameter exists in the content variable and close the file.
    if phrase in text:
        print("True")
    else:
        print("False")
    file.close()

checker(file_name, phrase)
