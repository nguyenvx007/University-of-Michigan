infile = open("test.txt","r")
outfile = open("test.csv","w")
incontent = infile.readlines()
header = "Name, Age, Score"
outfile.write(header)
outfile.write("\n")
for lin in incontent:
    lin = lin.replace("\n","")
    lin = lin.split(",")
    row = "{},{},{}".format(lin[0],lin[1],lin[2])
    outfile.write(row)
    outfile.write("\n")


outfile.close()
infile.close()