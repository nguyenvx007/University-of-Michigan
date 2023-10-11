# Accumulating Multiple Results in Dictionary

fileref = open("test.txt","r")
chars = fileref.read()
dict = {}
dict['a'] = 0
dict['b'] = 0
for char in chars:
    if char == 'a':
        dict['a'] = dict['a'] + 1
    elif char == 'b':
        dict['b'] = dict['b'] + 1
print("a: ", dict['a'])
print("b: ", dict['b'])
print("Dictionary Keys: ", dict.keys())
print("Dictionary Values: ", dict.values())
print("Dictionary Items: ", dict.items())
