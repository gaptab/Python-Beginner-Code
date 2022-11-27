print(help(list))
print(help(dict))
print(help(print))
print(help('def'))

#hasattr()

class Person:
    age='22'
    name='Virat'
    
person=Person()
print(hasattr(person,'age'))
print(hasattr(person,'salary'))