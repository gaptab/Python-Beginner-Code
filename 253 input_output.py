print(1,2,3,4)
print(1,2,3,4,sep="#")
print(1,2,3,4,sep='*',end='#')

x=6;y=9
print('The value of x is {} and y is {}'.format(x,y))

#input()
#num=input('Enter a number:')
#print(num)
print(int('90'))
print(eval('6*9'))

Multiline=[]
print("Tell me about yourself")
while True:
    line=input()
    if line:
        Multiline.append(line)
    else:
        break
finalText='\n'.join(Multiline)
print('\n')
print("Final text input")
print(finalText)

text= input("enter a text")
print('{:<25}.format(text)
