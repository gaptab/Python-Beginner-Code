string='PYTHON IS AWESOME'
print("Lowercase string:",string.casefold())

firstString='der fluß'
secondString='der fluss'
#ß=ss

if firstString.casefold()==secondString.casefold():
    print("the strings are equal")
else:
    print("strings are not equal")
    
#count

string="Python is awesome,isn't it?"
substring='is'
count=string.count(substring)
print("The count is:",count)

substring='i'
count=string.count(substring,8,25)
print("The count is:",count)