# Accumulating All Results in Dictionary

fileref = open("test.txt","r")
chars = fileref.read()
dict = {}
for char in chars:
    if char not in dict:
        dict[char] = 0
    dict[char] = dict[char] + 1
print(dict.items())

# Accumulating all results in Dicitonary using get ()

dict = {}
for char in chars:
    dict[char] = dict.get(char,0) + 1
print(dict.items())





