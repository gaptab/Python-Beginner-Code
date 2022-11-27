test=object()
print(type(test))
print(dir(test))

#oct()

print(oct(10))
print(oct(0b101))
print(oct(0XA))

class Person():
    age=22
    
    def __index__(self):
        return self.age
    
    def __int__(self):
        return self.age
    
person=Person()
print(oct(person))