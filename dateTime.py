
import datetime 
datetime_object=datetime.datetime.now()
print(datetime_object)

date_object=datetime.date.today()
print(date_object)

print(dir(datetime))

d=datetime.date(2022,9,18)
print(d)

from datetime import date

today=date.today()
print("Current date:",today)

today=date.today()
print("Current year=",today.year)
print("Current month=",today.month)
print("Current day=",today.day)

from datetime import time
a=time()
print("a=",a)
b=time(11,34,56)
print("b=",b)
