testList=[]
print(len(testList))

testList=[1,2,3,54]
print(len(testList))

testTuple=(1,2,3,4,5,6,7)
print(len(testTuple))

testRange=range(1,10)
print(len(testRange))


testString=''
print(len(testString))
testString='Python'
print(len(testString))

testByte=b'Python'
print(len(testByte))
testList=[1,2,3]
testByte=bytes(testList)
print(len(testByte))

testSet={1,2,3}
print(len(testSet))

testSet=set()
print(len(testSet))

testDict={1:'One',2:'Two'}
print(len(testDict))

testSet={1,2}
frozenTestSet=frozenset(testSet)

print(len(frozenTestSet))

class Session:
    def __init__(self,number=0):
        self.number=number
    def __len__(self):
        return self.number
    
s1=Session()
print(len(s1))

s2=Session(6)
print(len(s2))

#max()

number=[3,2,8,5,10,6]
print(max(number))

languages=['Python','C programming','Java','JavaScript']

largest_string=max(languages)
print(largest_string)

square={2:4,-3:9,-1:1,-2:4}

key1=max(square)
print(key1)

key2=max(square,key=lambda k:square[k])

print(key2)

print(square[key2])


result=max(4,-5,23,5)
print(result)































