
#### Splitting/Separating CSV Ignoring Commas in Double Quotes ####
# 1. Import csv module
import csv
# Open csv file with" csv.reader()" funtion
fileref = csv.reader("test2.csv")
# "next()" function reads first row as list of values. Each value is then strip of leading and trailing space using list comprehension and handles commas with double 
row = next(fileref)
for row in lines:
    row=row.split(",")
    print(row)

