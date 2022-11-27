class Person:
    age=25
    def printAge(cls):
        print("The age is: ",cls.age)
        
Person.printAge=classmethod(Person.printAge)
Person.printAge()

#Factory method

from datetime import date

class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        
    def display(self):
        print(self.name+"'s age is: "+str(self.age))
        
person=Person('Vikarna',25)
person.display()















