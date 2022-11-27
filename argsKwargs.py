
#Non keyword argument

def adder(*num):
    sum=0
    for n in num:
        sum=sum+n
        
    print("Sum:",sum)
    
adder(2,4,3,6,3)
adder(2,6,8,43,2,5,2,7)

#Keyword argument

def intro(**data):
    print("\nDatatype of argument:",type(data))
    
    for key, value in data.items():
        print("{} is {}".format(key,value))

intro(Firstname="Subhadra", Age=24, Phone=8881212)
intro(Firstname="Draupadi", Age=42, Phone=8884242,Email="panchali@gmail.com")