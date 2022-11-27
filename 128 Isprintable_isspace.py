s='Space is printable'
print(s)
print(s.isprintable())

s='\n New line is printable'
print(s)
print(s.isprintable())

s=''
print('\n Empty string is priontable?',s.isprintable())

s=chr(27)+chr(97)
if s.isprintable()==True:
    print('Printable')
else:
    print('not printable')
    
s='2+2=4'
if s.isprintable()==True:
    print("Printable")
else:
    print('not printable')
#issspace() 

s='     \t' 
print(s.isspace()) 
s=' a '
print(s.isspace())
s=''
print(s.isspace()) 

s='\t  \n'
if s.isspace()==True:
    print("All whitespace characters")
else:
    print("contains non-whitespace characters")
    
s='2+2=4'
if s.isspace()== True:
    print("All whitespace characters")
else:
    print("contains non-whitespace characters")

str=' '
print(str.isspace()) 
str='helloworld'
print(str.isspace())   
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    