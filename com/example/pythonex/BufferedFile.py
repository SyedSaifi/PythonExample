
BUFFSIZE = 2500
ifilename = "applet.txt"
ofilename = "appletOut.txt"
ifile = open(ifilename, "r")
ofile = open(ofilename, "w")

buffer = ifile.read(BUFFSIZE)

while(len(buffer)):
    ofile.write(buffer)
    print("{} bytes written to {}".format(len(buffer),ifilename) )
    buffer = ifile.read(BUFFSIZE)


ifile.close()
ofile.close()

print("Done")