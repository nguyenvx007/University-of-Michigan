
def yes_or_no(message):
    valid_input = False
    while not valid_input:
        answer = input(message)
        answer = answer.upper()
        if answer == "Y" or answer == "N":
            valid_input = True
        else:
            print("Valid response is 'Y' or 'N': ")
    return answer
response = yes_or_no("Do you like beans? Y or N: ")
if response == "Y":
    print("Beans are good for you")
else:
    print("That's too bad -- beans are good for you")


