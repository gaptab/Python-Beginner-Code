number=5
print(bin(number))

class Quantity:
    apple=1
    orange=2
    grapes=2
    
    def __index__(self):
        return self.apple+self.orange+self.grapes
print(bin(Quantity()))

#all()

l=[1,3,4,5]
print(all(l))

l=[0,False]
print(all(l))

l=[1,3,4,0]
print(all(l))

l=[0,False,1]
print(all(l))


l=[]
print(all(l))

s="This is good"

print(all(s))

s='000'

print(all(s))

s=''

print(all(s))
s={0:'False',1:'False'}
print(all(s))
s={1:'True',2:'False'}
print(all(s))

s={1:'True',False:0}

print(all(s))
s={}
print(all(s))

s={'0':'True'}
print(all(s))

























