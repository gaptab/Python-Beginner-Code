import numpy as np
x=np.array([1,2])
print(x.dtype)

xf=np.array([1.4,2.0])
print(xf.dtype)

x64=np.array([1,2],dtype=np.int64)
print(x64.dtype)


y=np.random.randn(4,3)
print(y)

yrandint=np.random.randint(2,100)
print(yrandint)

y=np.random.randint(-4,8,size=(3,3))
print(y)

print(x,y)