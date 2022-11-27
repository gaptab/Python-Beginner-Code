A={'a','c','d'}
B={'c','d',3}
C={1,2,3}
print(A.union(B))
print(B.union(C))
print(A.union(B,C))
print(A.union())

# | operator

print(A|B)
print(B|C)
print(A|B|C)

#update()

A={'a','b'}
B={1,2,3}
result=A.update(B)
print(A)
print(result)

string_alphabet='abc'
numbers_set={1,2}

numbers_set.update(string_alphabet)
print(numbers_set)

info_dictionary={'key':1,'lock':2}
numbers_set={'a','b'}
numbers_set.update(info_dictionary)
print(numbers_set)

set1=set()
set1.update({20,30.45,'Learn with','Python'})
print(set1)

set2={"Welcome","to","Python","course"}
set2.update({20,30.45,"hi"})
print(set2)













