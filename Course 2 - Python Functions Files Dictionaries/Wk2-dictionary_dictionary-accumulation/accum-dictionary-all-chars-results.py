# Accumulating All Results in Dictionary

# Counts all characters in the file
# For Loop enumerates all char and add to empty dictionary with value of 0; adds 1 to 
# dictionary value each time the same char repeat

fileref = open("test.txt","r")
chars = fileref.read()
dict = {}
for char in chars:
    if char not in dict:
        dict[char] = 0
    dict[char] = dict[char] + 1
print(dict.items())

# Accumulating all results in Dicitonary using get ()
# Same as above except use get() to check value of key. If not, set value of key to 0 and add 1


dict = {}
for char in chars:
    dict[char] = dict.get(char,0) + 1
print(dict.items())





