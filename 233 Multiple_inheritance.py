class A(object):
    def doThis(self):
        print('doing this in A')
        
class B(A):
    pass

# if class C was also being derived from A then the lookup order would be D,B,C,A
class C(object):
    def doThis(self):
        print("doing this in C")
        
class D(B,A):
    pass

if __name__=='__main__':
    dObj=D()
    dObj.doThis()
# A method gets called because the order for lookup is D,B,A,C  
# this is shown in function mro  
    print(D.mro())