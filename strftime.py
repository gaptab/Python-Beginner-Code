from datetime import datetime
now=datetime.now()
print(now)

year=now.strftime("%Y")
print("Year:",year)

month=now.strftime("%m")
print("Month:",month)
day=now.strftime("%d")
print("Day:",day)

time=now.strftime("%H:%M:%S")
print("Time:",time)

date_time1=now.strftime("%d%m%Y, %H:%M:%S")
print("date and time:",date_time1)

timestamp=1668797322
date_time=datetime.fromtimestamp(timestamp)

print("Date time object",date_time)

d=date_time.strftime("%m%d%Y, %H:%M:%S")
print("Output 2:",d)

d=date_time.strftime("%d %B,%Y")
print("Output 3:",d)

d=date_time.strftime("%I%p")
print("Output 4",d)