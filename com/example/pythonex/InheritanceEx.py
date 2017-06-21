'''
Created on Feb 19, 2017

@author: ssaifi
'''
class Parent:
    value1="Value One"

    def __init__(self,name, age):
        self.name=name
        self.age=age

    def changeAge(self,age):
        self.age = age

    def __str__(self):
        return self.name+" -- "+str(self.age)

class Child(Parent):
    def __init__(self,name, age, grade):
        Parent.__init__(self,name,age)
        self.grade=grade

    def __str__(self):
        return Parent.__str__(self)+"--"+str(self.grade)

c1=Child("syed",30,9)
print(c1.value1)
print(c1)

c1.changeAge(29)
print(c1)

