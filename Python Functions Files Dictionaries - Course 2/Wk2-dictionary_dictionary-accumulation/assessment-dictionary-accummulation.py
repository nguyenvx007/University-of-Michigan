
# 1. The dictionary Junior shows a schedule for a junior year semester. The key is the course name and the value is the number of credits. Find the total number of credits taken this semester and assign it to the variable credits. Do not hardcode this – use dictionary accumulation!

Junior = {'SI 206':4, 'SI 310':4, 'BL 300':3, 'TO 313':3, 'BCOM 350':1, 'MO 300':3}

# Pseudocode
# a. Initiate an accumulating variable credits and assign it the value 0
# b. Iterate through each key of  dictionary variable Junior
# c. For each key, update/add its value to the credits accumulataing variable

credits = 0
for key in Junior:
  credits = credits + Junior[key]
print(credits)

# 2. Create a dictionary, freq, that displays each character in string str1 as the key and its frequency as the value.

str1 = "peter piper picked a peck of pickled peppers"

# Pseudocode
# a. Initiate an empty accummulating dictionary variable 'freq'
# b. Iterate through the characters assigned to the str1 variable
# c. For each character, add the character as a key in the dictionary with a value of 0, if it doesn't 
# d. Then, add 1 to the key's value -- to track the frequency of each key.

freq = {}
for char in str1:
  if char not in freq:
    freq[char]=0
  freq[char] = freq[char]+1
print(freq)

# 3. Provided is a string saved to the variable name s1. Create a dictionary named counts that contains each letter in s1 and the number of times it occurs.

s1 = "hello"

# Pseudocode
# a. Initiate an empty accummulating dictionary variable 'counts'
# b. Iterate through the characters assigned to the s1 variable
# c. For each character, add the character as a key in the dictionary with a value of 0, if it doesn't 
# d. Then, add 1 to the key's value -- to track the frequency of each key.

counts = {}
for char in s1:
  if char not in counts:
    counts[char]=0
  counts[char] = counts[char] + 1
print(counts)

# 4. Create a dictionary, freq_words, that contains each word in string str1 as the key and its frequency as the value.

str1 = "I wish I wish with all my heart to fly with dragons in a land apart"

# Pseudocode
# a. Split the str1 variable as a variable list of words
# b. Initiate an empty accummulating dictionary variable 'freq_words'
# c. Iterate through the words assigned to the str1 variable list
# d. For each word, add the word as a key in the dictionary with a value of 0, if it doesn't exist in the dictionary.
# e. Then, add 1 to the word key value -- to track the frequency of each word.

str1 = str1.split()
freq_words = {}
for word in str1:
  if word not in freq_words:
    freq_words[word]=0
  freq_words[word] = freq_words[word] + 1
print(freq_words)

# 5. Create a dictionary called wrd_d from the string sent, so that the key is a word and the value is how many times you have seen that word.

sent = "Singing in the rain and playing in the rain are two entirely different situations but both can be good"

# Pseudocode
# a. Split the sent string variable to word list variable.
# b. Initiate an empty dictionary variable called wrd_d
# c. Iterate through the words in the sent dictionary
# d. Add each word to the wrd_d dictionary if it doesn't already exist with a 0 value. Then add 1 to the value of word

sent = sent.split()
wrd_d = {}
for word in sent:
  wrd_d[word]= wrd_d.get(word,0) + 1
print(wrd_d)

# 6. Create the dictionary characters that shows each character from the string sally and its frequency. Then, find the most frequent letter based on the dictionary. Assign this letter to the variable best_char.

sally = "sally sells sea shells by the sea shore"

# Pseudocode
# a. Initiate empty dictionary called 'characters'
# b. Iterate through the characters in the 'sally' string
# b1. For each character, add to the 'characters' dictionary as a key and add the value one to the key to track its frequency.
# c. Create a list of keys from 'characters' dictionary and assigned to 'key' variable
# d. Initialize the variable 'best_char' as the first and best key in the dictionary -- to server as a comparison key
# e. Iterate through the keys 'characters'
# e1. Compare if each key value is greater than the 'best_char' key value
# e1.1 If key is greater, than replace key as the 'best_char' key
characters = {}
for char in sally:
  characters[char] = characters.get(char,0) + 1
print(characters)

keys = list(characters.keys())
best_char = keys[0]
for key in keys:
  if characters[key] > characters[best_char]:
    best_char = key
print("The best key is:",best_char," with a value of:", characters[best_char])


# 7. Find the least frequent letter. Create the dictionary characters that shows each character from string sally and its frequency. Then, find the least frequent letter in the string and assign the letter to the variable worst_char.
sally = "sally sells sea shells by the sea shore and by the road"

# Pseudocode
# a. Initiate empty dictionary called 'characters'
# b. Iterate through the characters in the 'sally' string
# b1. For each character, add to the 'characters' dictionary as a key and add the value one to the key to track its frequency.
# c. Create a list of keys from 'characters' dictionary and assigned to 'key' variable
# d. Initialize the variable 'best_char' as the first and best key in the dictionary -- to server as a comparison key
# e. Iterate through the keys 'characters'
# e1. Compare if each key value is less than the 'word_char' key value
# e1.1 If key is greater, than replace key as the 'word_char' key
characters = {}
for char in sally:
  characters[char] = characters.get(char,0) + 1
print(characters)

keys = list(characters.keys())
worst_char = keys[0]
for key in keys:
  if characters[key] < characters[worst_char]:
    worst_char = key
print("The worst key is:",worst_char," with a value of:", characters[worst_char])



# 8. Create a dictionary named letter_counts that contains each letter and the number of times it occurs in string1. Challenge: Letters should not be counted separately as upper-case and lower-case. Intead, all of them should be counted as lower-case.

string1 = "There is a tide in the affairs of men, Which taken at the flood, leads on to fortune. Omitted, all the voyage of their life is bound in shallows and in miseries. On such a full sea are we now afloat. And we must take the current when it serves, or lose our ventures."

# Pseudocode
# a. Initiate a blank dictionary called 'letter_counts' for accummalating each char & frequency.
# b. Interate through 'string1' string variable as lower-case value.
# b1. Add each character to 'letter_counts' dictionary as a key and add value 1 to track frequency.

letter_counts = {}
for char in string1.lower():
    letter_counts[char] = letter_counts.get(char,0) + 1
print(letter_counts)

# 9. Create a dictionary called low_d that keeps track of all the characters in the string p and notes how many times each character was seen. Make sure that there are no repeats of characters as keys, such that “T” and “t” are both seen as a “t” for example.

p = "Summer is a great time to go outside. You have to be careful of the sun though because of the heat."

# Pseudocode
# a. Initiate a blank dictionary called 'low_d' for accummalating each char & frequency in the string 'p'.
# b. Interate through the 'p' string variable as lower-case values.
# b1. Add each character to the 'low_d' dictionary as a key and add value 1 to track its frequency.

low_d = {}
for char in p.lower():
    low_d[char] = low_d.get(char,0) + 1
print(low_d)