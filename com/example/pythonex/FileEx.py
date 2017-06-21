ifile = open("foo.txt", "r+")
ofile = open("foo1.txt", "w")
ifile.write( "Python is a great language.\nYeah its great!!\n");

for line in ifile:
    print(line, end="")
    print(line, file=ofile,end="")

ifile.close()
ofile.close()

print("Done")