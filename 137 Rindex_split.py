quote='Let  it be, let it be, let it be'
result=quote.rindex('let it')
print(result)

#result=quote.rindex('small')
print(result)

quote='Do small things with great love.'
print(quote.rindex('t',2))

print(quote.rindex('th',6,20))

#print(quote.rindex('o small',10,-1))
#split()

text='Love thy neighbor'
print(text.split())

grocery='Milk, Bread, Rice'
print(grocery.split(', '))

print(grocery.split(':'))

grocery='Rice, Wheat, Bread, Milk'

print(grocery.split(', ',2))


print(grocery.split(', ',1))

print(grocery.split(', ',5))
print(grocery.split(', ',0))























