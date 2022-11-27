class Data(object):
    def __init__(self,data):
        self.data=data
        
    def getData(self):
        print('Data:',self.data)
        
class Time(Data):
    def getTime(self):
        print("Time:",self.data)
        
if __name__=='__main__':
    data=Data(20)
    time=Time(10)
    
    time.getTime()
    data.getData()
    time.getData()
    
    print(Time.mro())