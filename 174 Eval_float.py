x=1
print(eval('x+1'))

def calculatePerimeter(l):
    return 4*l

def calculateArea(l):
    return l*l

expression=input("Type a function: ")

   if(expression=='calculatePerimeter(l)'):
        print("If length is",l,", perimeter=",eval(expression))
   elif(expression=='calculateArea(l)'):
        print("If length is",l,", Area= ",eval(expression))
   else:
        print('Wrong function!')
        break
#float()


print(float(10))    
print(float(11.22))
print(float(-13.33))
print(float("       -24.55\n")) 
print(float(4)) 

print(float("nan"))
print(float("NaN")) 
print(float("InF"))
print(float("Infinity")) 
print(float("InFINITY"))
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    