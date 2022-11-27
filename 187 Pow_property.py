print(pow(2,2))
print(pow(-2,2))
print(pow(2,-2))
print(pow(-2,-2))

# (x**y) %z
x=7
y=2
z=5
print(pow(x,y,z))

#property()
class Person:
    def __init__(self,name):
        self._name=name
    def get_name(self):
        print('Getting name')
        return self._name
    def set_name(self,value):
        print('Setting name to '+value)
        self._name=value
    def del_name(self):
        print('Deleting name')
        del self._name
    name=property(get_name,set_name,del_name, 'Name property')

p=Person('Sahadev')
print(p.name)
p.name='Nakul'
del p.name
#property decorator

class Person:
    def __init__(self,name):
        self._name=name
        
    @property
    def name(self):
        print('Getting name')
        return self._name
    @name.setter  
    def name(self,value):
        print('Setting name to '+value)
        self._name=value
        
    @name.deleter 
    def name(self):
        print('Deleting name')
        del self._name
        
p=Person('Sahadev')
print('The name is: ',p.name)
p.name='Nakul'
del p.name

















