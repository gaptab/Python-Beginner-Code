def compute_hcf(x,y):
    if x>y:
        smaller=y
    else:
        smaller=x
        
    for i in range(1,smaller+1):
        if((x%i==0) and(y%i==0)):
            hcf=i
    return hcf

num1=64
num2=24

print("The H.C.F. of",num1,'and',num2,'is:',compute_hcf(num1, num2))

#Euclidean algorithm
def compute_hcf(x,y):
    while(y):
        x,y=y,x%y
    return x

hcf=compute_hcf(600, 900)

print("The H.C.F. is:",hcf)
















