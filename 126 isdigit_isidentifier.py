s='234235'
print(s.isdigit())

s='abc 436547'
print(s.isdigit())

s='\u00BD'
print(s.isdigit())

#isidentifier()
str='Python'
print(str.isidentifier())


str='Pyth on'
print(str.isidentifier())


str='22Python'
print(str.isidentifier())


str=''
print(str.isidentifier())

str='root33'
if str.isidentifier()==True:
    print(str,'is a valid identifier')
    
else:
    print(str,'is not a valid identifier')

str='33root'
if str.isidentifier()==True:
    print(str,'is a valid identifier')
    
else:
    print(str,'is not a valid identifier')


















