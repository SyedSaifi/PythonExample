import functools

C = [22,45,78,32,98]

fn = lambda x,y: x if x>y else y
z= functools.reduce(fn,C)
print(z)