# 5. Create a dictionary called lett_d that keeps track of all of the characters in the string product and notes how many times each character was seen. Then, find the key with the highest value in this dictionary and assign that key to max_value.

product = "iphone and android phones"

# Accumulate to dictionary chars keys and number of chars
lett_d = {}
for char in product:
    lett_d[char] = lett_d.get(char,0) + 1
print(lett_d)

# Accumulate best (max) value from lett_d dictionary

keys = list(lett_d.keys())
max_value = keys[0]
for key in keys:
    if lett_d[key] > lett_d[max_value]:
        max_value = key
print(max_value)