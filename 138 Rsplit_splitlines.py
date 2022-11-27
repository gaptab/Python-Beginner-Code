text='Tolerance is not a easy quality'
print(text.rsplit())

grocery='Milk, Coffee, Bread, Butter, Rice'
print(grocery.rsplit(', '))

print(grocery.rsplit(':'))

#maxsplit

print(grocery.rsplit(', ',2))
print(grocery.rsplit(', ',5))
print(grocery.rsplit(', ',0))
#splitlines

grocery='Milk\nButter\nCoffee\nRice\nBread'

print(grocery.splitlines())
print(grocery.splitlines(True))

grocery='Milk Butter Coffee Rice Bread'
print(grocery.splitlines())














