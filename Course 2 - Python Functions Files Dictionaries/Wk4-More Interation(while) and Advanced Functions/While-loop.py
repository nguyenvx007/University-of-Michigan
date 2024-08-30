
count = 0
eve_nums = []
while count <= 15:
    if count % 2 == 0:
        eve_nums.append(count)
    count = count + 1
print(eve_nums)

list1 = [8,3,4,5,6,7,9]
accum = 0
idx = 0
while idx < len(list1):
    accum = accum + list1[idx]
    idx = idx+1
print(accum)

def stop_at_four(x):
    lst = []
    i=0
    while (x[i] != 4) and (i < len(x)):
        lst.append(x[i])
        i = i+1
    return lst
x=[2,2]
print(stop_at_four(x))
