#Write code that uses the string stored in org and creates an acronym which is assigned to the variable acro. Only the first letter of each word should be used, each letter in the acronym should be a capital letter, and there should be nothing to separate the letters of the acronym. Words that should not be included in the acronym are stored in the list stopwords. For example, if org was assigned the string “hello to world” then the resulting acronym should be “HW”.
##### PseudoCode #####
# 1. Retrieve and define 'org' string - Given.
# 2. Retrieve and define list of 'stopwords' - Given
# 3. Convert 'org' string to lower case
# 4. Convert 'org' string to strip the 'comma'
# 5. Convert element of 'org' type string variable into a list type variable
# 6. Define a blank accumulating pattern string variable called "acro"
# 7. Define a iterating variable ("wrd") and iterate through the 'org' list
# 8. Determine if the interating variable 'wrd' is NOT listed in the 'stopwords' list,
# 9. If it is NOT, append the first letter of iterating variable ('wrd') to the accumulating pattern string variable 'acro'.
# 10. When the iteration of the 'org' list is completed, convert result 'acro' variable to upper.
# 11. Print the 'acro' variable
#
stopwords = ['to', 'a', 'for', 'by', 'an', 'am', 'the', 'so', 'it', 'and', "The"]
org = "The organization for health, safety, and education"
org = org.lower() 
org = org.replace(",","") # strip comma
org = org.split() # split string to list variable
acro = ""
for wrd in org:
    if wrd not in stopwords:
        acro = acro + wrd[0]
acro = acro.upper()
print(acro)
