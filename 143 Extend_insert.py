language=['French','English']
language1=['Spanish','Portuguese']
language.extend(language1)
print(language)

language=['French']
language_tuple=('Spanish','Portuguese')
language_set={'Chinese','Japanese'}
language.extend(language_tuple)
language.extend(language_set)
print(language)

a=[1,2]
b=[3,4]

a+=b
print(a)

#slicing syntax

a[len(a):]=b
print(a)
#extend() vs append()

a1=[1,2]
a2=[1,2]
b=(3,4)

a1.extend(b)
print(a1)

a2.append(b)
print(a2)
#insert()

vowel=['a','e','i','u']
vowel.insert(3,'o')
print(vowel)

mixed_list=[{1,2},[5,6,7]]
number_tuple=(3,4)
mixed_list.insert(1,number_tuple)
print(mixed_list)

































