text='python is easy to learn.'
result=text.endswith(('to learn.'))
print(result)

text='Python programming is easy to learn.'
result=text.endswith('learn.',7)
print(result)

result=text.endswith('is',7,26)
print(result)
result=text.endswith('easy',7,26)
print(result)

#expandtabs
str='xyz\t12345\tabc'
result=str.expandtabs()
print(result)

print('Original string:',str)
print('Tabsize 2:',str.expandtabs(2))
print('Tabsize 3:',str.expandtabs(3))
print('Tabsize 4:',str.expandtabs(4))
print('Tabsize 5:',str.expandtabs(5))






