my_list=[[7],[6,5],[4,3,2,1]]
flat_list=[num for sublist in my_list for num in sublist]
print(flat_list)

# using nested for loops

flat_list=[]
for sublist in my_list:
    for num in sublist:
        flat_list.append(num)
        
print(flat_list)

# itertools package

import itertools
flat_list=list(itertools.chain(*my_list))
print(flat_list)
#sum()
flat_list=sum(my_list,[])
print(flat_list)

# lambda and reduce()

from functools import reduce
print(reduce(lambda x,y:x+y,my_list))

















