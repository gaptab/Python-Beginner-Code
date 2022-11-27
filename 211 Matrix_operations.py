#Addition

import numpy as np
A=np.array([[3,6],[7,-9]])
B=np.array([[9,-3],[3,6]])
C=A+B
print(C)

#Multiplication

A=np.array([[3,6,5],[7,-3,0]])
B=np.array([[1,1],[2,1],[3,-3]])
C=A.dot(B)
print(C)

#Transpose

A=np.array([[1,1],[2,1],[3,-3]])
print(A.transpose())