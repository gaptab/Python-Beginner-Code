num=1000000
count=0
while num!=0:
    num//=10
    count+=1
    
print("Number of digits: "+str(count))

#len()
num=12434365867
print(len(str(num)))