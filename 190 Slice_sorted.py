result1=slice(3)
print(result1)

result2=slice(1,5,2)
print(result2)

py_string='Python'
slice_object=slice(3)
print(py_string[slice_object])

slice_object=slice(1,6,2)
print(py_string[slice_object])

py_string='Python'
slice_object=slice(-1,-4,-1)
print(py_string[slice_object])

py_list=['P','y','t','h','o','n']
py_tuple=('P','y','t','h','o','n')

slice_object=slice(3)
print(py_list[slice_object])

slice_object=slice(1,5,2)
print(py_tuple[slice_object])

py_string='Python'
print(py_string[0:3])
print(py_string[1:5:2])
#sorted()

py_list=['e','a','u','o','i']
print(sorted(py_list))

py_string='Python'
print(sorted(py_string))

py_tuple=('e','a','u','o','i')
print(sorted(py_tuple))


py_set={'e','a','u','o','i'}
print(sorted(py_set,reverse=True))

py_dict={'e':1,'a':2,'u':3,'o':4,'i':5}
print(sorted(py_dict,reverse=True))

frozen_set=frozenset(('e','a','u','o','i'))
print(sorted(frozen_set,reverse=True))
def take_second(elem):
    return elem[1]

random=[(2,2),(3,4),(4,1),(1,3)]
sorted_list=sorted(random,key=take_second)

print(sorted_list)

participant_list=[
    ('Yudhistir',50,18),
    ('Arjun',75,12),
    ('Bheem',75,20),
    ('Sahadev',90,22),
    ('Nakul',65,12)
]



































