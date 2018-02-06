# Python exercises

### Math - divisible by: 
Write a function that takes two integers (x and y) and returns a list of numbers between x and y that are divisible by 5 but not by 7.

#### To Run:
```py
python3 math_divisible.py x y
```

#### Arguments:
+ x = first integer  
+ y = second integer  

#### Example:
```py
python3 math_divisible.py 1 100
```  
--------------------

### Find a phrase in file: 
Write a function that takes a phrase and a text file as inputs. The function returns True if the phrase is found in the document and returns False otherwise. Note: Newline characters will not be included in the phrase.

#### To Run:
```py
python3 find_phrase.py file_name phrase
```

#### Arguments:
+ file_name = text file to be used as input. Use the file name if it is in the same directory as this script or the folder path if it is in another directory. A test file is provided: testfile.txt    
+ phrase = phrase to check (string)

#### Example:
```py
python3 find_phrase.py testfile.txt "This is a test"
``` 
--------------------

### Add column in csv: 
Give a Comma Separated File (csv) and a column number (zero being the left most column) return the sum of all the entries in that column. Assume that all the entries in the CSV are numbers. Assume also that there are no column headers.

#### To Run:
```py
python3 csv_sum.py file_name column
```

#### Arguments:
+ file_name = CSV file to be used as input. Use the file name if it is in the same directory as this script or the folder path if it is in another directory. A test file is provided: sample.csv   
+ column = column number

#### Example:
```py
python3 csv_sum.py sample.csv 2
```
