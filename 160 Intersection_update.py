A={2,3,5,4}
B={2,5,100}
C={2,3,8,9,10}

print(B.intersection(A))
print(B.intersection(C))
print(A.intersection(C))
print(C.intersection(A,B))


A={100,7,8}
B={200,4,5}
C={300,2,3}
D={100,200,300}

print(A.intersection(D))
print(B.intersection(D))
print(C.intersection(D))
print(A.intersection(B,C,D))
#& operator

print(A&C)
print(A&D)
print(A&C&D)
print(A&B&C&D)
print(B&D)

#intersection_update

A={1,2,3,4}
B={2,3,4,5}
result=A.intersection_update(B)
print(result)

print(A)
print(B)

#2 parameters

A={1,2,3,4}
B={2,3,4,5,6}
C={4,5,6,9,10}

result=C.intersection_update(B,A)
print(result)
print(C)
print(B)
print(A)


























