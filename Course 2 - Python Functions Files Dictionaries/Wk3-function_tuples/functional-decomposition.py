# Run top level function to identify most common letter in variable string 'history'

# Composition - Top Level Function
def most_common_letter (x):
    letter_freq = frequency_count(x)
    return best_letter(letter_freq)

history = "aabbbccccddddfffff"

# Functional Decomposition

def frequency_count(x):
    accum_list = {}
    for char in x:
        if char not in accum_list:
            accum_list[char] = 0
        accum_list[char] = accum_list[char] + 1
    print(accum_list)
    return accum_list 

def best_letter(dict):
    keys = dict.keys()
    best_key = list(keys)[0]
    for x in keys:
        if dict[x] > dict[best_key]:
            best_key = x
    return best_key

# Invoke Top Level Function
print(most_common_letter(history))


