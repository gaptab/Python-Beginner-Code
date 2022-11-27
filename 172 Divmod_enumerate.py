print(divmod(8,3))
print(divmod(3,8))
print(divmod(5,5))

print(divmod(2.6,0.5))

#enumerate()

grocery=['bread','milk','butter']
enumerateGrocery=enumerate(grocery)
print(type(enumerateGrocery))

print(list(enumerateGrocery))

enumerateGrocery=enumerate(grocery,10)
print(list(enumerateGrocery))

#loop

for item in enumerate(grocery):
    print(item)
    
print('\n')
for count,item in enumerate(grocery):
    print(count,item)

for count,item in enumerate(grocery,100):
    print(count,item)













