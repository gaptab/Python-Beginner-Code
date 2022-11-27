
l=[2,34,6,8,3,2,6,3,3]
even_nos=list(filter(lambda x:x%2 ==0,l))
print("Even numbers are:",even_nos)

double=lambda x:x*2
print(double(10))

my_list=[1,6,7,3,45,76,90]
new_list=list(map(lambda x:x*2,my_list))
print("Double values are:",new_list)

list1=[2,5,7,89,90,100,170]
list2=list(map(lambda x:x*x*x,list1))
print("cube values are:",list2)

from functools import reduce 
list1=[20,78,54,67,89,90,102]
add=reduce(lambda x,y:x+y,list1)
print("Addition of all list elements is:",add)