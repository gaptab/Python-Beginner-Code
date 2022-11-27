rows=6
for i in range(rows):
    for j in range(i+1):
        print('* ',end='')
    print('\n')
    
# half pyramid using numbers

rows=6
for i in range(rows):
    for j in range(i+1):
        print(j+1,end=' ')
    print('\n')

#half pyramid using alphabets

row=6
ascii_value=65
for i in range(rows):
    for j in range(i+1):
        alphabet=chr(ascii_value)
        print(alphabet,end=' ')
    ascii_value+=1
    print('\n')
    
#inverted pyramid using *

rows=6
for i in range(rows,0,-1):
    for j in range(0,i):
        print('*',end=' ')
    print('\n')
    
#inverted pyramid using numbers
rows=6
for i in range(rows,0,-1):
    for j in range(1,i+1):
        print(j,end=' ')
    print('\n')
    
#full pyramid using *

rows=6
k=0
for i in range(1,rows+1):
    for space in range(1,(rows-1)+1):
        print(end='  ')
        
    while k!=(2*i-1):
        print('* ',end='')
        k+=1
    k=0
    print()















