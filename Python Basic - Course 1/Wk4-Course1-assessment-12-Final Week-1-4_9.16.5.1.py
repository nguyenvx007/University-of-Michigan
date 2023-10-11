# Below are a set of scores that students 
# have received in the past semester. 
# Write code to determine how many are 
# 90 or above and assign that result to 
# the value a_scores.
# 
# Pseudo Code
# 1. Retrieve past scores: Given in string
# 2. Cast score as Integer and Convert past score 
#     string into 'List of Past Scores'.
# 3. Define: Accumulating Sum Variable for 'Total
#    Score above 90' as variable a_scores and set it 0.
# 4. Define interating variable and iterate
#    through the 'List of Past Scores'.
# 5. For each iteration in 'List of Past Scores',
#    determine if the score is 90 or above?
# 6. If the score is 90 or above, add 1 to the 
#    'Total Score above 90' varuable a_scores
# 7. Print the 'Total Score Above 90' a_scores variable
#
scores = "67 80 90 78 93 20 79 89 96 97 92 88 79 68 58 90 98 100 79 74 83 88 80 86 85 70 90 100"
scores = [int(score) for score in scores.split()]
a_scores = 0
for score in scores:
     if score >= 90:
         a_scores+=1
print(a_scores)
