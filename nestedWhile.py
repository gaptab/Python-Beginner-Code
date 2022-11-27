i=1
while i<=3:
    j=1
    while j<=10:
        print(j,end='')
        j+=1
    i+=1
    print()
    
# printing pattern

i=1
while i<=6:
    j=0
    while j<i:
        print("*",end=' ')
        j+=1
    print('')
    i+=1
    
# for inside while statement

i=1
while i<=6:
    for j in range(1,i+1):
        print("*",end=' ')
    print()
    i+=1