import sys

x = int(sys.argv[1])
y = int(sys.argv[2])


def calc(x, y):
    '''Give two integers and return a list of numbers between them that are divisible by 5 but not by 7.'''
    numbers = []
    # Arrange arguments so the lowest number is first in order to determine the range.
    if x < y:
        nbetween = range(x, (y+1))
    else:
        nbetween = range(y, (x+1))

    # Loop through the range of numbers and add to list if they are divisible by 5 but not by 7.
    for i in nbetween:
        if (i % 5 == 0) and (i % 7 != 0):
            numbers.append(i)
    print(numbers)

calc(x, y)
