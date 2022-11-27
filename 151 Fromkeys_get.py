keys={'a','e','i','o','u'}
vowels=dict.fromkeys(keys)
print(vowels)

values='vowel'
vowels=dict.fromkeys(keys,values)
print(vowels)

#mutable object list
value=[1]
vowels=dict.fromkeys(keys,value)
print(vowels)

value.append(2)
print(vowels)

value=[1]
vowels={key:list(value) for key in keys}
print(vowels)
value.append(2)
print(vowels)
#get()

person={'name':'Nakul','age':22}
print('Name: ',person.get('name'))
print('Age: ',person.get('age'))
print('Salary: ',person.get('salary'))

print('Salary: ',person.get('salary', 0.0))

person={}
print('Salary: ',person.get('salary'))
print(person['salary'])
















