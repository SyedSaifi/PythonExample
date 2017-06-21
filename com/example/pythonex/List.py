#List Example
mylist1=[0,1,2,3,4,5,6,7,8,9]
mylist2=['raj', 'priya', 'rohan']

print("List1")
print(mylist1)

print("List2")
print(mylist2)

print("Append, Insert, remove, pop")
mylist1.append(10)
mylist1.insert(3,33)
mylist1.remove(8)
mylist1.pop(0)
mylist1.sort()
mylist1.reverse()
del mylist1[1]
print(mylist1)

print("Concat list")
print(mylist2+mylist1)


print("List size")
print(len(mylist1))

print("List Sclicing")
print(mylist1[3:8])

x = range(1,20,2)
a = list(x)
print(a)

print("Index")
print(a.index(5))

print("count")
print(a.count(4))

sq = [x**2 for x in range(10)]
print(sq)
