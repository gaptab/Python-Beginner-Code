f=open('e:/test.txt')
print(f)
f.close()
try:
    f=open('e:/test.txt',encoding='utf-8')
finally:
    f.close()
    
# write

with open("test.txt",'w',encoding='utf-8') as f:
    f.write("My first file\n")
    f.write("this is a text file\n")
    f.write("it contains 3 lines\n")
    
with open('test.txt','a',encoding='utf-8') as f:
    f.write("This text has to be appended at the end")
    f.close()
    
#read

f=open("test.txt",'r',encoding='utf-8')
txt=f.read()
print(type(txt))
print(txt)
f.close()

f=open('test.txt','r',encoding='utf-8')
print(f.read(8))
print(f.read(5))
print("last line",f.read())
print(f.read())
print(f.tell())
print(f.seek(0))
print(f.read())

f=open('data.txt','r',encoding='utf-8')
for line in f:
    print(line,end='')
f.seek(0)
print(f.readline())
print(f.readline())
print(f.readline())
f.seek(0)
print(f.read().splitlines())

data=open('data.txt','r+')
file_data=data.read(27)
full_data=data.read()
print(file_data)
print(full_data)
f.close()

#file position

data=open('data.txt','r+')
file_data=data.read(27)
print("current psition after reading 27 byte:",data.tell())
data.seek(0)
full_data=data.read()
print(file_data)
print(full_data)
print("position after reading file:",data.tell())
data.close()

import os
os.remove('e:/test.txt')
os.remove('e:/test.txt')