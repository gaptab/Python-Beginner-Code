vowels=['e','a','u','o','i']
vowels.sort()
print(vowels)

vowels.sort(reverse=True)
print(vowels)

def takeSecond(elem):
    return elem[1]

random=[(2,2),(3,3),(4,1),(1,3)]
random.sort(key=takeSecond)
print(random)

#Copy()
old_list=[1,2,3]
new_list=old_list

print(new_list)

new_list.append('a')
print(old_list)
print(new_list)


my_list=['monkey',0,6.7]
new_list=my_list.copy()
print(new_list)


list=['monkey',0,6.7]
new_list=list[:]
new_list.append('lion')
print('Old list',list)
print('New list',new_list)











