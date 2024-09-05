# 1. Open Source file
# 2. Open Destination File to be written
# 3. Read lines in source file
# 4. Print Header to destination file and hard return
# 5. Iterate through Lines in source file, 
# 5a. Convert String to List
# 5b. Write 2nd item of the list
# 6. Close source and destination file
infile = open("test.json","r")
outfile = open("test.csv","w")
incontent = infile.readlines()
header = "Disabled, ID, Kind"
outfile.write(header)
outfile.write("\n")
for lin in incontent:
    lin = lin.split()
    outfile.write(lin[1])
outfile.close()
infile.close()