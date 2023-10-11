# The textfile, travel_plans.txt, contains the summer travel plans for someone with some commentary. Find the total number of characters in the file and save to the variable "num"
fileref = open("travel_plans.txt","r")
content = fileref.read()
num = len(content)

# We have provided a file called emotion_words.txt that contains lines of words that describe emotions. Find the total number of words in the file and assign this value to the variable num_words
fileref = open("emotion_words.txt","r")
content = fileref.readlines()
num_words = 0
for row in content:
    lis = row.split(" ")
    num_words = num_words + len(lis)

#Assign to the variable num_lines the number of lines in the file school_prompt.txt.
fileref = open("school_prompt.txt","r")
rows = fileref.readlines()
num_lines = 0
for row in rows:
    num_lines += 1

# Assign the first 30 characters of school_prompt.txt as a string to the variable beginning_chars.

fileref = open("school_prompt.txt","r")
beginning_chars = ""
content = fileref.read()
for char in content[0:30]:
        beginning_chars = beginning_chars + char

# Challenge: Using the file school_prompt.txt, assign the third word of every line to a list called three.

fileref = open("school_prompt.txt","r")
content = fileref.readlines()
three = []
for lis in content:
    lis = lis.split(" ")
    three.append(lis[2])

# Challenge: Create a list called emotions that contains the first word of every line in emotion_words.txt.
fileref = open("emotion_words.txt","r")
content = fileref.readlines()
emotions = []
for lis in content:
    lis = lis.split(" ")
    emotions.append(lis[0])

# Assign the first 33 characters from the textfile, travel_plans.txt to the variable first_chars.

fileref = open("travel_plans.txt","r")
content = fileref.read()
first_chars = ""
for char in content[:33]:
    first_chars += char
# Challenge: Using the file school_prompt.txt, if the character ‘p’ is in a word, then add the word to a list called p_words.

fileref = open("school_prompt.txt","r")
content = fileref.readlines()
p_words = []
for lis in content:
    lis = lis.split(" ")
    #lis = lis.strip()
    print(lis)
    for word in lis:
        if "p" in word:
            word = word.strip()
            p_words.append(word)

