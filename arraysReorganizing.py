#asarray
import numpy as np
a=np.matrix(np.ones((4,4)))
np.array(a)[2]=3
print(a)

np.asarray(a)[2]=3
print(a)

b=np.arange(0,11,2)
print(b)

#reshape data

e=np.array([(1,2,3),(4,5,6)])
print(e)
print(e.reshape(3,2))

print(e.flatten())
#hstack

f=np.array([1,2,3])
g=np.array([4,5,6])
print("Horizontal Append:",np.hstack((f,g)))

#vstack
print("Vertical Append", np.vstack((f,g)))

normal_array=np.random.normal(5,0.5,10)
print(normal_array)

#Linspace
x=np.linspace(0,10,6)
print(x)
#logspace
y=np.logspace(3.0,4.0,num=4)
print(y)