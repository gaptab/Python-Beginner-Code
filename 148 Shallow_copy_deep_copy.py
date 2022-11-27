old_list=[[1,2,3],[4,5,6],[7,8,'a']]
new_list=old_list
new_list[2][2]=9

print(old_list)
print(id(old_list))
print(new_list)
print(id(new_list))


import copy
x=9
copy.copy(x)
copy.deepcopy(x)

#shallow_copy

old_list=[[1,2,3],[4,5,6],[7,8,9]]
new_list=copy.copy(old_list)
print(old_list)
print(new_list)
old_list=[[1,1,1],[2,2,2],[3,3,3]]
new_list=copy.copy(old_list)
old_list.append([4,4,4])
print(old_list)
print(new_list)

old_list=[[1,1,1],[2,2,2],[3,3,3]]
new_list=copy.copy(old_list)
old_list[1][1]='AA'
print(old_list)
print(new_list)

#Deep_copy
old_list=[[1,1,1],[2,2,2],[3,3,3]]
new_list=copy.deepcopy(old_list)
print(old_list)
print(new_list)

old_list[1][0]='BB'
print(old_list)
print(new_list)















