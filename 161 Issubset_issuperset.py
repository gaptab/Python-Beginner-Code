A={1,2,3}
B={1,2,3,4,5}
C={1,2,4,5}
print(A.issubset(B))
print(B.issubset(A))
print(A.issubset(C))
print(C.issubset(B))

#issuperset

A={1,2,3,4,5}
B={1,2,3}
C={1,2,3}
print(A.issuperset(B))
print(B.issuperset(A))
print(C.issuperset(B))