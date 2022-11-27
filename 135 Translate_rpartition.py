firstString='abc'
secondString='ghi'
thirdString='ab'
string='abcdef'
print(string)
translation=string.maketrans(firstString,secondString,thirdString)
print(string.translate(translation))

translation={97:None,98:None,99:105}
string='abcdef'
print(string.translate(translation))
#rpartition

string='Python is fun'
print(string.rpartition('is '))

print(string.rpartition('not '))

string="Python is fun, isn't it"
print(string.rpartition('is'))















