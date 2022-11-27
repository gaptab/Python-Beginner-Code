class Mammal(object):
    def __init__(self,mammalName):
        print(mammalName,'is a warm-blooded animal.')
        
class Dog(Mammal):
    def __init__(self):
        print('Dog has four legs.')
        super().__init__("Dog")
        
d1=Dog()


#zip()

number_list=[1,2,3]
str_list=['one','two','three']

result=zip()
result_list=list(result)
print(result_list)


result=zip(number_list,str_list)
result_set=set(result)
print(result_set)

numbersList=[1,2,3]
str_list=['one','two']
number_tuple=('ONE','TWO','THREE','FOUR')
result=zip(number_list,number_tuple)
resut_set=set(result)
print(result_set)

result=zip(number_list,str_list,number_tuple)

result_set=set(result)
print(result_set)

#unzip

coordinate=['x','y','z']
value=[3,4,5]

result=zip(coordinate,value)
result_list=list(result)
print(result_list)

c,v=zip(*result_list)
print('c=',c)
print('v=',v)










