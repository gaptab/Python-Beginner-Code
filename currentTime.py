
from datetime import datetime

now=datetime.now()
current_time=now.strftime("%H:%M:%S")
print("Current time:",current_time)

#time object containing current time
now=datetime.now().time() #time object
print("Now:",now)
print("Type of now is",type(now))

import pytz

tz_NY=pytz.timezone("America/New_York")
datetime_NY=datetime.now(tz_NY)
print("NY time:",datetime_NY.strftime("%H:%M:%S"))

tz_London=pytz.timezone("Europe/London")
datetime_London=datetime.now(tz_London)
print("London time:",datetime_London.strftime("%H:%M:%S"))