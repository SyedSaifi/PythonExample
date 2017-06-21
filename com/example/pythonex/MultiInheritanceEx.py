class Parent:
    value1="Value One"

    def __init__(self,name, age):
        self.name=name
        self.age=age

    def changeAge(self,age):
        self.age = age

    def __str__(self):
        return self.name+" -- "+str(self.age)

class Address:
    def __init__(self,city, state):
        self.city=city
        self.state=state

    def changeCity(self,city):
        self.city = city

    def __str__(self):
        return self.city+" -- "+self.state

class Child(Parent, Address):
    def __init__(self,name, age, city, state, grade):
        Parent.__init__(self,name,age)
        Address.__init__(self, city,state)
        self.grade=grade

    def changeAge(self,age):
        self.age = age + 10

    def __str__(self):
        return Address.__str__(self)+"--"+Parent.__str__(self)+"--"+str(self.grade)

c1=Child("syed",30,"boston", "MA", 9)
print(c1)

c1.changeAge(29)
c1.changeCity("New York")
print(c1)

