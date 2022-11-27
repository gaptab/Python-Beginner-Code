
rows=6
k=0
for i in range(1,rows+1):
    for space in range(1,(rows-i)+1):
        print(end='  ')
        
    while k!=(2*i-1):
        print('* ',end='')
        k+=1
        
    k=0
    print()
    
#full pyramid of numbers
rows=6
k=0
count=0
count1=0
for i in range(1,rows+1):
    for space in range(1,(rows-i)+1):
        print('  ',end='')
        count+=1
    while k!=((2*i)-1):
        if count<=rows-1:
            print(i+k,end=' ')
            count+=1
        else:
            count1+=1
            print(i+k-(2*count1),end=' ')
        k+=1
    count1=count=k=0
    print()
#inverted pyramid using *

rows=6
for i in range(rows,1,-1):
    for space in range(0,rows-i):
        print('  ',end='')
    for j in range(i,2*i-1):
        print('* ',end='')
    for j in range(1,i-1):
        print('* ',end='')
    print()
# Pascal's Triangle

rows=6
coef=1
for i in range(1,rows+1):
    for space in range(1,rows-1+1):
        print(' ',end='')
    for j in range(0,i):
        if j==0 or i==0:
            coef=1
        else:
            coef=coef * (i-j)//j
        print(coef,end=' ')
    print()

#floyds triangle

rows=6
number =1
for i in range(1,rows+1):
    for j in range(1,i+1):
        print(number,end=' ')
        number +=1
    print()

















    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    