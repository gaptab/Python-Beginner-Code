vowels=('a','e','i','o','u')
fSet=frozenset(vowels)
print(fSet)
print(frozenset())

#fSet.add('V')

person={'name':'John','age':22,'gender':'male'}

fSet=frozenset(person)
print(fSet)

A=frozenset([1,2,3,4])
B=frozenset([3,4,5,6])
C=A.copy()
print(C)

print(A.union(B))
print(A.intersection(B))
print(A.difference(B))

print(A.symmetric_difference(B))
#format

print(format(12,'b'))
print(format(1234.5323,'f'))
print(format(1243,'d'))

print(format(1234,'*>+7,d'))
print(format(123.5464,'^-093,f'))

class Person:
    def __format__(self,format):
        if (format=='age'):
            return '25'
        return 'None'
    
print(format(Person(),'age'))

















