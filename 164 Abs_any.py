integer=-20
print(abs(integer))
floating=-30.33
print(abs(floating))

complex=(3-4j)
print(abs(complex))

#any()

l=[1,3,4,0]
print(any(l))

l=[0,False,5]
print(any(l))

l=[0,False]
print(any(l))

l=[]
print(any(l))
s='This is good'
print(any(s))

s='000'
print(any(s))

s=''
print(any(s))

d={0:'False'}
print(any(d))

d={0:'False',1:'True'}
print(any(d))

d={0:'False',False:0}
print(any(d))
d={}
print(any(d))

d={'0':'False'}
print(any(d))












