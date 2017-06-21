'''
Created on Feb 19, 2017

@author: ssaifi
'''
class Person:
    count = 0
    def __init__(self,id):
        self.id=id
        Person.count+=1
        print("Id : ", self.id, " is instantiated")

    def __del__(self):
        print("Id : ", self.id, " is destroyed")

    def setFullName(self,first,last):
        self.first=first
        self.last=last
        
    def printFullName(self):
        print(self.first," ", self.last)

    def getCount(self):
        return Person.count

    def __str__(self):
        return self.first+" -- "+self.last
        
personOne=Person(6)
print(personOne.getCount())
personOne.setFullName("Yasra", "Shakil")
personOne.printFullName()
print(personOne)
print("-------------------------------------")
personOne=Person(5)
print(personOne.getCount())
personOne.setFullName("Syed", "Saifi")
personOne.printFullName()
print(personOne)
