import numpy as np
a=np.arange(0,11)
print(a[3:])

slice_a=a[0:5]
print(slice_a)
slice_a[:]=100
print(slice_a)
print(a)

a_copy=a.copy()
print(a_copy)
a_copy[:]=200
print(a_copy)
print(a)

a=np.array([1,2,3])
b=a
b[0]=100
print(a)

mat=np.array(([5,10,20],[20,25,30],[35,40,10]))
print(mat[2,:])

a=np.array([[1,2,3,4,5,6,7],[8,9,10,11,12,13,14]])
print(a[1:5])

a[:,2]=[1,2]
print(a)

#3D array

b=np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
print(b[:,1,:])