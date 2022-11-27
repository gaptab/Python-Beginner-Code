dict={'a':'123','b':'456','c':'789'}
string='abc'
print(string.maketrans(dict))

dict={97:'123',98:'456',99:'789'}
string='abc'
print(string.maketrans(dict))

#Translational table using two string

firstString='abc'
secondString='def'
string='abc'
print(string.maketrans(firstString,secondString))

#Translational table using removable string

firstString='abc'
secondString='def'
thirdString='abd'
string='abc'
print(string.maketrans(firstString,secondString,thirdString))

#partition

string='Python is fun'
print(string.partition('is '))

print(string.partition('not '))

string="Python is fun, isn't it"

print(string.partition('is'))



























