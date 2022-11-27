list_1=[1,3,1,6,9]
print(list(set(list_1)))

#remove items that are duplicated
list_2=[1,2,3,4,5,6,7,8,9]

print(list(set(list_1) ^ set(list_2)))