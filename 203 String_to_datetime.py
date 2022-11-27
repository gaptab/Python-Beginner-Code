from datetime import datetime
my_date_string='Nov 1 2022 11:11AM'
datetime_object=datetime.strptime(my_date_string,'%b %d %Y %I:%M%p')
print(type(datetime_object))
print(datetime_object)

# dateutil module
from dateutil import parser
date_time=parser.parse('Nov 1 2022 11:11AM')
print(type(date_time))
print(date_time)