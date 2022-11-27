number=[2,5,7,8,3,5,3]
print(min(number))

languages=['Python','C Programming','Java']
print(min(languages))

square={2:4,-3:9,-1:1,-2:4}
key1=min(square)
print(key1)

key2=min(square, key=lambda k:square[k])
print(key2)

print(square[key2])
#map()
def calculateSquare(n):
    return n*n
numbers=(1,2,3,4)
result=map(calculateSquare,numbers)
print(result)


numbersSquare=set(result)
print(numbersSquare)

numbers=(1,2,3,4)
result=map(lambda x:x*x,numbers)
print(result)

numbersSquare=set(result)
print(numbersSquare)

num1=[4,5,6]
num2=[5,6,7]

result=map(lambda n1,n2:n1+n2,num1,num2)
print(list(result))
















