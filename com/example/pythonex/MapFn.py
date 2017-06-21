C = [1,2,3,4,5,6,7,8,9,10]

fn = lambda x: x+2
print(list(map(fn,C)))

S= "Python is a fun language".split()

fn1= lambda x:x.upper()
print(list(map(fn1, S)))

A1= [1,2,3]
A2= [2,5,8]

fn = lambda x,y: x*y
print(list(map(fn,A1,A2)))