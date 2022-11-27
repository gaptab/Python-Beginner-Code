sales={'apple':2,'grapes':3,'orange':4}
print(sales.items())

items=sales.items()
del[sales['apple']]
print(items)

#keys()
person={'name':'Dushasan','age':33,'salary':12000}
print(person.keys())
empty_dict={}
print(empty_dict.keys())

person={'name':'Dushasan','age':33,}
keys=person.keys()
print(keys)

person.update({'salary':12000})
print(keys)