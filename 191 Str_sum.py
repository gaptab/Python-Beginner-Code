result=str(10)
print(result)

print(str('Adam'))
print(str(b'Python!'))

#bytes
b=bytes('python',encoding='utf-8')
print(str(b,encoding='ascii',errors='ignore'))

#sum()

numbers=[2.5,3,4,-5]
numbers_sum=sum(numbers)
print(numbers_sum)

numbers_sum=sum(numbers,10)
print(numbers_sum)