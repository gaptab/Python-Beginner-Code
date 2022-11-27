list=[{1,2},('a'),['1.1','2.2']]
list.clear()
print(list)

list=[{1,2},('a'),['1.1','2.2']]
del list[:]
print(list)

class MyClass:
    a=10
    def func(self):
        print('Hello')
        
print(MyClass)

del MyClass
#print(MyClass)
my_var=5
my_tuple=('Vibhishan',33)
my_dict={'name':'Vibhishan','age':33}
del my_var
del my_tuple
del my_dict


my_list=[1,2,3,4,5,6,7,8,9]
del my_list[2]
print(my_list)
del my_list[1:4]
print(my_list)
del my_list[:]
print(my_list)

person={'name':'Vibhishan','age':33,'profession':'programmer'}
del person['profession']
print(person)


my_tuple=(1,2,3)

del my_tuple








