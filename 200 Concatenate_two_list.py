# + operator

list_1=[7,'n','m']
list_2=[3,6,9]
list_joined=list_1+list_2
print(list_joined)

# iterable unpacking operator *

list_joined=[*list_1,*list_2]
print(list_joined)

# unique values

list_joined=list(set(list_1+list_2))
print(list_joined)

#extend()
list_2.extend(list_1)
print(list_2)
