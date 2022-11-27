class MaxSizeList(object):
    def __init__(self,value):
        self.myList=[]
        self.value=value
        
    def push(self,String):
        try:
            String=str(String)
            self.myList.append(String)
            
        except ValueError:
            print("you can only push strings!")
            
            
    def getList(self):
        print(self.myList[-self.value:])
        
if __name__=='__main__':
    a=MaxSizeList(3)
    b=MaxSizeList(1)
    
    a.push('What')
    a.push('we think')
    a.push('we become')
    
    b.push('What')
    b.push('we think')
    b.push('we become')
    
    a.getList()
    b.getList()
    
    