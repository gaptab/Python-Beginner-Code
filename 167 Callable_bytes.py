x=5
print(callable(x))

def testFunction():
    print('test')

y=testFunction 
print(callable(y))

class Foo:
    def __call__(self):
        print("test foo")
        
print(callable(Foo))

InstanceOfFoo=Foo()
InstanceOfFoo()
#bytes()

string='python is interesting.'

arr=bytes(string,'utf-8')
print(arr)

size=5
arr=bytes(size)
print(arr)

rList={1,2,3,4,5}
arr=bytes(rList)
print(arr)















