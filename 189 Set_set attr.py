print(set())
print(set('Python'))
print(set(('a','e','i','o','u')))
print(set(['a','e','i','o','u']))
print(set(range(5)))

print(set({'a','e','i','o','u'}))
print(set({'a':1,'e':2,'i':3,'o':4,'u':5}))
frozen_set=frozenset(('a','e','i','o','u'))
print(set(frozen_set))

class PrintNumber:
    def __init__(self,max):
        self.max=max
    def __iter__(self):
        self.num=0
        return self
    def __next__(self):
        if(self.num>=self.max):
            raise StopIteration
        self.num+=1
        return self.num
    
print_num=PrintNumber(5)
print(set(print_num))
#setattr
class Person:
    name='Anant'
    
p=Person()
print(p.name)
setattr(p, 'name', 'Akash')
print(p.name)

class Person:
    name='Anant'
p=Person()
setattr(p,'name','Akash')
print(p.name)

setattr(p,'age',22)
print(p.age)














