class Data(object):
    def getData(self):
        print("In data!")
        
class Time(Data): #inheriting from Data class
    def getTime(self):
        print("In time!")
        
if __name__=='__main__':
    data=Data()
    time=Time()
    
    data.getData()
    time.getTime()
    time.getData() #inherited Data method