class Foo:
    a=5
    
fooInstance=Foo()
print(isinstance(fooInstance,Foo))
print(isinstance(fooInstance,(list, tuple)))
print(isinstance(fooInstance,(list,tuple,Foo)))

numbers=[1,2,3]
result=isinstance(numbers,list)
print(result)

result=isinstance(numbers,dict)
print(result)

result=isinstance(numbers,(dict,list))
print(result)

number=5
result=isinstance(number,list)
print(result)

result=isinstance(number,int)
print(result)
#id()

class Foo:
    b=5
dummyFoo=Foo()
print(id(dummyFoo))

print(id(5))

a=5

print(id(a))
b=a
print(id(b))


c=5.0
print(id(c))
















