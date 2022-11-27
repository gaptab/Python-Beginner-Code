numbers=dict(x=5,y=0)
print(numbers)
print(type(numbers))

empty=dict()
print(empty)
print(type(empty))

numbers1=dict([('x',5),('y',-5)])
print(numbers1)

numbers2=dict([('x',5),('y',-5)],z=8)
print(numbers2)

numbers3=dict(dict(zip(['x','y','z'],[1,2,3])))
print(numbers3)

#mapping

numbers1=dict({'x':4,'y':5})
print(numbers1)

numbers2={'x':4,'y':5}
print(numbers2)
numbers3=dict({'x':4,'y':5},z=8)
print(numbers3)
#dir()

numbers=[1,2,3]
print(dir(numbers))

print(dir())

class Person:
    def __dir__(self):
        return ['age','name','salary']
    
teacher=Person()
print(dir(teacher))















