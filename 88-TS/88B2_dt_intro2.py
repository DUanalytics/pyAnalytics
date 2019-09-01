#Date Time - Operations & Arithmetic
#-----------------------------
#%
from datetime import datetime as dt

#to date from integer values
new_date = dt(2019,7,4)
new_date

equinoxDate = dt(2019,6,23)
equinoxDate

#%%

d1 = dt(2010,6,10)
d2 = dt(2019,7,28)
d2 + d1 #error
diff=d2 - d1  #number of days
diff
diff/365  #this yrs
#%%
d3 = dt(2019, 7, 4, 15, 30, 59, 10)
d3

d3.hour   #hour
d3.minute #minute
d3.second  #second
d3.microsecond #microsecond
d3.tzinfo  #no info store in environment


#time instance
datetime.time.min
datetime.time.max
datetime.time.resolution

#Date parts
today = datetime.date.today()
today
today.ctime()
today.timetuple()
today.toordinal()
today.year
today.month
today.day


#time
import time
time.time()
time.localtime()


#time
from datetime import time
# time(hour = 0, minute = 0, second = 0)
a = time()
print("a =", a)
# time(hour, minute and second)
b = time(11, 34, 56)
print("b =", b)
# time(hour, minute and second)
c = time(hour = 11, minute = 34, second = 56)
print("c =", c)
# time(hour, minute, second, microsecond)
d = time(11, 34, 56, 234566)
print("d =", d)


#Replace a portion of date
d = dt(2019, 7, 4,15,30)
d
d1=d.replace(day=28, year=2011)
d1
#tuple : date time value

d.timetuple()
d.weekday()
d.isoweekday()
d.isocalendar()
d.ctime()
d.isoformat()
#From 0 date
d3 = dt.fromordinal(730920) # 730920th day after 1. 1. 0001
d3

#https://www.programiz.com/python-programming/datetime
