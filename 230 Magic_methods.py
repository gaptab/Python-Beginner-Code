class Employee(object):
    def __init__(self,firstname,lastname,salary=0):
        self.firstname=firstname
        self.lastname=lastname
        self.salary=salary
        
    def __str__(self):
        return 'Full name: ' +self.firstname + ' ' +self.lastname
    
    def __int__(self):
        return self.salary
    
    def __add__(self,other):
        return self.salary+other.salary
    
    def __mul__(self,other):
        return self.salary*other.salary
    
if __name__=='__main__':
    mahatma=Employee('Mahatma','Gandhi',1000)
    Gandhi=Employee('John','Parker',2000)
    print(mahatma)
    print(Gandhi)
    print(mahatma +Gandhi)
    print(mahatma*Gandhi)
    print(int(mahatma))
    print(int(Gandhi))
    print(mahatma==Gandhi)