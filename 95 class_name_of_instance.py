# __class__.__name__

class Car:
    def name(self,name):
        return name
    
c=Car()
print(c.__class__.__name__)

# using type() and __name__ attribute

class Car:
    def name(self,name):
        return name
c=Car()
print(type(c).__name__)