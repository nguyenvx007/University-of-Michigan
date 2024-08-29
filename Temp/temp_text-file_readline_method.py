# We have provided a file called emotion_words.txt that contains lines of words that describe emotions. Find the total number of words in the file and assign this value to the variable num_words
fileref = open("test.json","r")
content = fileref.readlines()
num_words = 0
for row in content:
    lis = row.split(" ")
    print(lis)
    print(type(lis))
    num_words = num_words + len(lis)
    print (num_words)
print(num_words)