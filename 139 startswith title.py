text='Python is easy to learn.'
result=text.startswith('is easy')
print(result)

result=text.startswith('Python is')
print(result)

result=text.startswith('Python is easy to learn.')
print(result)

result=text.startswith('is easy',7)
print(result)

result=text.startswith('is easy',7,18)
print(result)

result=text.startswith('easy',7,18)
print(result)
#tuple prefix

text='Programming is easy'
result=text.startswith(('python','Programming'))

print(result)                

result=text.startswith(('is','easy','java'))
print(result)

result=text.startswith(('Programming','easy'),12,19)
print(result)

#title()

text='My favorite number is 77.'
print(text.title())

text=' 963 k312 *63 fun'
print(text.title())

text="he's an engineer, isn't he?"
print(text.title())

import re

def titlecase(s):
    return re.sub(r"[A-Za-z]+('[A-Za-z]+)?",
     lambda mo: mo.group(0)[0].upper() +
     mo.group(0)[1:].lower(),
     s)

text="He's an engineer, isn't he?"

print(titlecase(text))






















