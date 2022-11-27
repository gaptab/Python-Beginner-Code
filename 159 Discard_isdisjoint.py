numbers={2,3,4,5}
numbers.discard(3)
print(numbers)

numbers.discard(10)
print(numbers)

numbers={2,3,4,5}
print(numbers.discard(3))
print(numbers)

set1={'Welcome','to','Python','course'}
set1.discard(20)
print(set1)
#isdisjoint

A={1,2,3,4}
B={5,6,7}
C={4,5,6}

print(A.isdisjoint(B))
print(A.isdisjoint(C))

A={'a','b','c','d'}
B={'b','e','f'}
C='5de4'
D={1:'a',2:'b'}
E={'a':1,'b':2}

print(A.isdisjoint(B))
print(A.isdisjoint(C))
print(A.isdisjoint(D))
print(A.isdisjoint(E))
# & operator

A={100,7,6}
B={200,4,5}
C={300,2,3,7}
D={100,200,300}
print(A&C)
print(A&D)

print(A&C&D)
print(A&B&C&D)



































