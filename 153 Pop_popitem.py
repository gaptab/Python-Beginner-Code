sales={'apple':2,'orange':3,'grapes':4}
element=sales.pop('apple')
print(element)
print(sales)

element=sales.pop('papaya','mango')
print(element)
print(sales)

#pop()

person={'name':'Virat','age':27,'salary':10000}
result=person.popitem()
print(result)
print(person)

person['profession']='Plumber'
result=person.popitem()
print(result)
print(person)