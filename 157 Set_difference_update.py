A={'a','b','c','d'}
B={'c','f','g'}
print(A.difference(B))
print(B.difference(A))

# - operator
A={'a','b','c','d'}
B={'c','f','g'}

print(A-B)
print(B-A)
#difference update

A={'a','b','c','d'}
B={'c','f','g'}

result=A.difference_update(B)
print(A)
print(B)
print(result)



















