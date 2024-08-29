fileref = open("test.json","r")
content = fileref.readlines()
lst= []
for row in content:
        row = row.split()
        lst.append(row[1])
print(lst)