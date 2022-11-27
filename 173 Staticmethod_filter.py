class Mathematics:
    def addNumbers(x,y):
        return x+y

Mathematics.addNumbers=staticmethod(Mathematics.addNumbers)
print("The sum is: ",Mathematics.addNumbers(5,10))

class Dates:
    def __init__(self,date):
        self.date=date
    def getDate(self):
        return self.date
    def toDashDate(date):
        return date.replace('/','-')
    
date=Dates('20-10-2022')
dateFromDB="20/10/2022"
dateWithDash=Dates.toDashDate(dateFromDB)

if(date.getDate()==dateWithDash):
    print("Equal")
else:
    print("unequal")
#filter() 

letters=['a','b','d','e','i','j','o']
def filterVowels(letter): 
    vowels=['a','e','i','o','u']
    
    if (letter in vowels):
        return True
    else:
        return False

filteredVowels=filter(filterVowels,letters) 
print("The filtered vowels are: ")

for vowel in filteredVowels:
    print(vowel)
    
#without filter function

randomList=[1,'a',0,False,True,'0']

filteredList=filter(None,randomList)

print('The filtered elements are: ' )
for element in filteredList:
    print(element)


















    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    