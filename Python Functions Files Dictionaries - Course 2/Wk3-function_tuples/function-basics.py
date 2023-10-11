# Function Compare Length
def length(lst):
    if len(lst) >= 5:
        return "Longer than 5"
    return "Less than 5"
lst = ["hello", "vinh", "how", "are", "you"]
print(length(lst))

# Function Return a number
def int_return(x):
    return(x)
print(int_return(2))

# Function Add a number
def add(x):
    return x + 2
print(add(2))

# Function Append to String
def change(str):
    return str +"Nice to meet you!"
print(change("Vinh, "))

# Function Accumulate Numbers in List
def accum(lst):
    tot = 0
    for num in lst:
        tot = tot + num
    return tot
lst = [1,2,3]
print(accum(lst))

# Function calling another function
def divide(x):
    return x/2
def sum(x):
    divide(x)
    return x/2 + 6
print(sum(4))