def myRange(start, stop, step):
    i = start
    while(i<stop):
        yield i
        i = i+step

r = myRange(1,10,1)
for x in r:
    print(x,end=' ')