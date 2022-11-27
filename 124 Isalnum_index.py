name='Rambha122343apsara'
print(name.isalnum())
name='Rambha122343 apsara'
print(name.isalnum())
name='31244536'
print(name.isalnum())

name='Menaka 123'
if name.isalnum()==True:
    print("All characters of string are alphanumeric.")
else:
    print("All characters are not alphanumeric")
#index()
sentence='Python programming is fun.' 
result=sentence.index('is fun')  
print(result) 

#result=sentence.index('Java')
#print(result)

print(sentence.index('ing',10))
print(sentence.index('g is',10,-4)) 
print(sentence.index('fun',7,18))

















