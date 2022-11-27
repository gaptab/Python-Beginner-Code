
import time
seconds=time.time()
print("Seconds since epoch",seconds)

seconds=1660177774.9951324
local_time=time.ctime(seconds)
print("Local time:",local_time)

print("This is printed immediately")
time.sleep(1.6)
print("This is printed after 1.6 seconds")

result=time.gmtime(1660177774.9951324)
print("result:",result)
print("Year:",result.tm_year)
print("tm_hour",result.tm_hour)

#strftime()
named_tuple=time.localtime()
time_string=time.strftime("%m%d%Y, %H:%M:%S",named_tuple)
print(time_string)

#strptime()

time_string="10 August, 2022"
result=time.strptime(time_string, "%d %B, %Y")
print(result)