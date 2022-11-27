
from datetime import datetime
timestamp=1665730073
dt_object=datetime.fromtimestamp(timestamp)
print("dt_object=",dt_object)
print("type(dt_object",type(dt_object))

now=datetime.now()
timestamp=datetime.timestamp(now)
print("Timestamp=",timestamp)