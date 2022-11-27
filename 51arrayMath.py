import numpy as np
a=np.array([0,1,2,3,4,5])
print(a**3)
print("square root:",np.sqrt(a))
print("Exponential:", np.exp(a))
print("Sin:",np.sin(a))
print("Cos:",np.cos(a))

f=np.array([1,2])
g=np.array([4,5])
print("Dot product is:",np.dot(f,g))

a=np.ones((2,3))
b=np.full((3,2),2)
print("Matrix multiplication is:",np.matmul(a,b))