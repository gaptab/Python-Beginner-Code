s='this is good'
print(s.islower())

s='th!s is also g00d'
print(s.islower())

s='this is Not good'
print(s.islower())

s='this is good'
if s.islower()== True:
    print("Does not contain any uppercase letter.")
else:
    print("Contains uppercase letter.")

s='this is Good'
if s.islower()== True:
    print("Does not contain any uppercase letter.")
else:
    print("Contains uppercase letter.")
#isnumeric()

s='1234324'
print(s.isnumeric())
s='\u00b23455'
print(s.isnumeric())
s='\u00BD'
print(s.isnumeric())
s='python0909'
print(s.isnumeric())

s='\u00BD'
if s.isnumeric()==True:
    print("All characters are numeric.")
else:
    ("All characters are not numeric")

str='hello009'
print(str.isnumeric())
str='10123435'
print(str.isnumeric())













    
    