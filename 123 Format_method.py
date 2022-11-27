print("Hello {}, your balance is {}.".format('Yayati',12000))
print("Hello {0}, your balance is {1}.".format('Yayati',12000))
print("Hello {name}, your balance is {blc}.".format(name='Yayati',blc=12000))
print("Hello {0}, your balance is {blc}.".format('Yayati',blc=12000))

#simple number formatting

print("The number is:{:d}".format(1000))
print("The number is:{:f}".format(1000.3253))
#octal,binary,hexadecimal
print("bin:{0:b},oct:{0:o},hex:{0:x}".format(12))

# number formatting with padding

print("{:5d}".format(12))
print("{:2d}".format(1234))
print("{:8.3f}".format(12.2345))
print("{:05d}".format(12))
print("{:08.3f}".format(12.3242))

#signed numbers
print("{:+f}{:+f}".format(12.23,-12.23))
print("{:-f}{:-f}".format(12.23,-12.23))
print("{: f}{: f}".format(12.23,-12.23))

# Number formatting with alignment
print("{:5d}".format(12))

print("{:^10.3f}".format(12.234))

print("{:<05d}".format(12))
print("{:=8.3f}".format(-12.345))

print("{:5}".format("Bhu"))
print("{:>5}".format("Bhuv"))
print("{:^5}".format("Bhuv"))
print("{:*^5}".format("Bhu"))

#truncate strings with format()
print("{:.3}".format("Bhuvishrava"))
print("{:5.3}".format("Bhuvishrava"))
print("{:^5.3}".format("Bhuvishrava"))

#formatting class and dictionary members
class Person:
    age=23
    name='Yuyutsu'
print("{p.name}'s age is: {p.age}".format(p=Person()))

person={'age':24,'name':'Shikhandi'}
print("{p[name]}'s age is: {p[age]}".format(p=person))

print("{name}'s age is: {age}".format(**person))

#arguments as format codes

string="{:{fill}{allign}{width}}"
print(string.format('Virat',fill='*',allign='^',width=5))
num="{:{align}{width}.{precision}f}"
print(num.format(123.234,align='<',width=8,precision=2))


#extra formating options
import datetime
date=datetime.datetime.now()
print("it's now: {:%Y/%m/%d %H:%M:%S}".format(date))

complexNumber=1+2j
print("Real part: {0.real} and imaginary part:{0.imag}".format(complexNumber))

#custom format

class Person:
    def __format__(self,format):
        if(format=='age'):
            return '23'
        return 'None'
    
print("Virat's age is: {:age}".format(Person()))















