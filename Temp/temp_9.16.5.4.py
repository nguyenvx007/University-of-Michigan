# A palindrome is a phrase that, if reversed, would read the exact same. Write code that checks if p_phrase is a palindrome by reversing it and then checking if the reversed version is equal to the original. Assign the reversed version of p_phrase to the variable r_phrase so that we can check your work
# Default/Given
p_phrase = "was it a car or a cat I saw"
# make lowercase
p_phrase = p_phrase.lower()
# remove spaces
p_phrase=p_phrase.replace(" ","")
print(p_phrase)
# Remove Spaces
r_phrase = p_phrase.replace(" ","")
# Switch order
r_phrase = r_phrase[::-1]
if p_phrase == r_phrase:
    print("great")
else:
    print("Not Great")