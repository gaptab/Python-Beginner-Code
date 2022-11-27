class BankAccount:
    def __init__(self,name,balance):
        self.name=name
        self.balance=balance
        self.total=self.name+ ' has '+ self.balance+' dollars in the account'
        
user1=BankAccount('Damayanti', '10000')
user1.name='Hidimbi'
print(user1.name)
print(user1.total)

# with property decorator

class BankAccount:
    def __init__(self,name,balance):
        self.name=name
        self.balance=balance
        
    @property 
    def total(self):
        return self.name+' has '+self.balance+' dollars in the account' 
user1=BankAccount('Damayanti', '10000')
user1.name='Hidimbi'

print(user1.name)
print(user1.total)