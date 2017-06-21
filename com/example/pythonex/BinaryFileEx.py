
BUFFSIZE = 2500
ifilename = "liveserver.PNG"
ofilename = "liveservertOut.jpg"
ifile = open(ifilename, "rb")
ofile = open(ofilename, "wb")

buffer = ifile.read(BUFFSIZE)

while(len(buffer)):
    ofile.write(buffer)
    print("{} bytes written to {}".format(len(buffer),ifilename) )
    buffer = ifile.read(BUFFSIZE)


ifile.close()
ofile.close()

print("Done")