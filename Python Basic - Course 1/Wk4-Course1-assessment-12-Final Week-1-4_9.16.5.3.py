# Write code that uses the string stored in "sent" and creates an acronym which is assigned to the variable "acro". The first two letters of each word should be used, each letter in the acronym should be a capital letter, and each element of the acronym should be separated by a “. ” (dot and space). Words that should not be included in the acronym are stored in the list "stopwords". For example, if "sent" was assigned the string “height and ewok wonder” then the resulting acronym should be “HE. EW. WO”.
#
# Pseudocode
# 1. Define list variable called stopwords - given.
# 2. Define string variable called sent - given.
# 3. Convert (split) the "sent" string variable to a list type
# 3. Define acronym string variable called "acro" with blank value.
# 4. Determine an iterating variable ("wrd") to iterate through the "Sent" list
# 5. Iterate through the "sent" list using iterating variable
# 6. If the "wrd" is not listed in the "stopwords" list, then 
# 6.a. Add/accumulate to the "acro" string variable the first two letters of the "wrd" followed by a ".".
# 7. Iteration is completed 
# 8. Capitalized the "acro" string variable.
# 9. Remove the white spaces at end/beginning of "acro" string variable.
# 10. Remove the last character -- the "." from the "acro" variable
#
stopwords = ['to', 'a', 'for', 'by', 'an', 'am', 'the', 'so', 'it', 'and', 'The']
sent = "The water earth and air are vital"
sent = sent.split() 
acro = "" 
for wrd in sent:
    if wrd not in stopwords:
        acro = acro + wrd[:2] + ". "
acro = acro.upper()
acro = acro.strip()
acro = acro.rstrip(acro[-1])
print (acro)
