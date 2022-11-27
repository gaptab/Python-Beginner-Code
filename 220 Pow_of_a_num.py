#while_statement
base=2
exponent=3
power=exponent

result=1
while exponent!=0:
    result*=base
    exponent-=1
    
print('value of',base,'power',power,'is:',str(result))

#for_statement

for exponent in range(exponent,0,-1):
    result*=base
print('value of',base,'power',power,'is:',str(result))

#pow()
base=2
exponent=3
result=pow(base,exponent)
print('value of',base,'power',power,'is:',str(result))














