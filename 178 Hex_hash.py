number=435
print(hex(number))
number=0
print(hex(number))

number=-34
print(hex(number))
returnType=type(hex(number))
print(returnType)


number=2.5
print(float.hex(number))
number=0.0
print(float.hex(number))
number=10.5
print(float.hex(number))

#hash()
print(hash(181))
print(hash(181.23))

print(hash('Python'))


vowels=('a','e','i','o','u')
print(hash(vowels))


class Person:
    def __init__(self,age,name):
        self.age=age
        self.name=name
    def __eq__(self,other):
        return self.age==other.age and self.name==other.name
    def __hash__(self):
        print("The hash is: ")
        return hash((self.age,self.name))

person=Person(33,'Yuyutsu')

print(hash(person))













