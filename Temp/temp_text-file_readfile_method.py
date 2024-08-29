# The textfile, test.json. Find the total number of characters in the file and save to the variable "num"
fileref = open("test.json","r")
content = fileref.read()
num = len(content)
print(num)