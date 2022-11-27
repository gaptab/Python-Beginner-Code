index=[1,2,3]
languages=['python','java','c']
dictionary=dict(zip(index,languages))
print(dictionary)

#list comprehension

dictionary={k:v for k,v in zip(index,languages)}
print(dictionary)