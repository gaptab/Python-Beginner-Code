person={'name':'Bahushrava','age':25}
age=person.setdefault('age')
print(person)
print(age)

person={'name':'Vikarna'}
salary=person.setdefault('salary')
print(person)
print(salary)

age=person.setdefault('age',22)
print(person)
print(age)
#update()

d={1:'one',2:'two'}
d1={2:'two'}
d.update(d1)
print(d)


d1={3:'three'}
d.update(d1)
print(d)

d={'x':2}
d.update(y=3,z=0)
print(d)















