numList=['1','2','3','4']
separator=', '
print(separator.join(numList))

numTuple=('1','2','3','4')
print(separator.join(numTuple))

s1='abc'
s2='123'
print(s2.join(s1))
print(s1.join(s2))
#sets
test={'2','1','3'}
s=', '
print(s.join(test))
test={'Python','Java','Ruby'}
print(s.join(test))

#dictionary
test={'mat':1,'that':2}
s='->'
print(s.join(test))

test={1:'mat',2:'that'}
print(s.join(test))

#ljust

string='PythoN'
width=10
print(string.ljust(width))
fillchar='*'
print(string.ljust(width,fillchar))































