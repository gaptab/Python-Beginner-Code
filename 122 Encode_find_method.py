string='pythön!'
print(string)
string_utf=string.encode()
print(string_utf)

print('Encoded version(with ignore) is:',string.encode('ascii','ignore'))
print('Encoded version(with replace) is:',string.encode('ascii','replace'))

#find()
quote='Let it be, let it be, let it be'
result=quote.find('let it')
print(result)
result=quote.find('small')
print(result)

#how to use find()
if (quote.find('be,')!=-1):
    print("Contains substring 'be,")
else:
    print("doesn't contain substring")
    
quote='Do small things with great love'
print(quote.find('small things',10))
print(quote.find('small things',2))
print(quote.find('o small',10,-1)) 
print(quote.find('things',6,20)) 


s='I love python tutorials' 
print(s.find('I'))
print(s.find('I',2)) 
print(s.find('love'))
print(s.find('t',2,10))    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    