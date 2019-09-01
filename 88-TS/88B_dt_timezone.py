#Date - Time Zone
#-----------------------------
#%
#Time Zones
#Within datetime, time zones are represented by subclasses of tzinfo. Since tzinfo is an abstract base class, you need to define a subclass and provide appropriate implementations for a few methods to make it useful. Unfortunately, datetime does not include any actual implementations ready to be used, although the documentation does provide a few sample implementations. Refer to the standard library documentation page for examples using fixed offsets as well as a DST-aware class and more details about creating your own class. pytz is also a good source for time zone implementation details.

import datetime
import pytz
#http://pytz.sourceforge.net/

my_date = datetime.datetime.now(pytz.timezone('US/Pacific'))
my_date

TIME_ZONE =  'Asia/Kolkata'
indian_date = datetime.datetime.now(pytz.timezone('Asia/Kolkata'))
indian_date

#%%%

import pytz
from datetime import datetime

intz = pytz.timezone('Asia/Kolkata')

nowdt = datetime.now(intz)
nowdt
todaydt = datetime(2012,6,15,tzinfo=intz)
todaydt


#copy
from datetime import datetime
from pytz import timezone
format = "%Y-%m-%d %H:%M:%S %Z%z"
# Current time in UTC
now_utc = datetime.now(timezone('UTC'))
print(now_utc.strftime(format))
# Convert to Asia/Kolkata time zone
now_asia = now_utc.astimezone(timezone('Asia/Kolkata'))
print(now_asia.strftime(format))
