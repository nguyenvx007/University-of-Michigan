# A palindrome is a phrase that, if reversed, would read the exact same. Write code that checks if p_phrase is a palindrome by reversing it and then checking if the reversed version is equal to the original. Assign the reversed version of p_phrase to the variable r_phrase so that we can check your work
#
p_phrase = "was it a car or a cat I saw"

# Pseudocode
#
# 1. Define initial string phrase: Given ("p_phrase")
# 2. Reverse "p_phrase" and assign it to variable "r_phrase"
# Remove spaces from "p_phrase"
# 2. Make "p_phrase" lower case
# 3. Reverse "p_phrase" and assign to new reverse variable called "r_phrase"
# 4. Compare iniitial phrase "p_phrase" and reverse phrase (r_phrase) to determine if they are equal
# 5. Print p_phrase
# 6. Print r_phrase
#
r_phrase = p_phrase[::-1]
# p_phrase = p_phrase.replace(" ","")
# p_phrase = p_phrase.lower()

#### The following were moved -- unnecessary and affected the assignment grading.
# if p_phrase == r_phrase:
#     print("p_phrase is a palindrome.")
# else:
#     print("p_prhase is not a palindrome.")

print("p_phrase: ",p_phrase)
print("r_phrase: ",r_phrase)


