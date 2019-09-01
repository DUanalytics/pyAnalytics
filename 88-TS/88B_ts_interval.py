#Date Time Interval
#-----------------------------
#%

from datetime import date

today = date.today()
today
today.day
today.month
today.year
today.weekday()

#Time
from datetime import datetime
datetime.now()
datetime.time(datetime.now())
#only time

#Weekday
#weekday returns 0 (monday) through 6 (sunday)
wd=date.weekday(today)
wd
#Days start at 0 for monday
days= ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
print("Today is day number %d" % wd)
print("which is a " + days[wd])



#format date time
from datetime import datetime
now = datetime.now()
now
now.strftime("%Y")  #Year
now.strftime("%d %B")  #date and Month
now.strftime("%a, %d-%b-%Y")
now.strftime("%A, %d-%b-%Y")
#
%C- indicates the local date and time
%x- indicates the local date
%X- indicates the local time
now.strftime("%C, %x, %X")

#Time
#2 hours time is declared [print now.strftime("%I:%M:%S %P) ]
now.strftime("%I, %M, %S : ")
#24 hours time is declared [print now.strftime("%H:%M")]
now.strftime("%H, %M")


#time conversion
# printing out the time or date, but something to CALCULATE about the future or past. 
from datetime import timedelta
timedelta(days=365, hours=8, minutes=15)

datetime.now()
str(datetime.now())
newdate = datetime.now() + timedelta(days=365)
newdate
str(newdate)
newdate.strftime("%d, %b, %Y")

newdate2 = datetime.now() + timedelta(weeks=5)
newdate2.strftime("%d, %b, %Y")

#get newyear
today = date.today()
today
nyd = date(today.year, 1, 1)
nyd
#how many days past NY
(today - nyd).days

#https://www.guru99.com/date-time-and-datetime-classes-in-python.html
#%%
#https://www.guru99.com/calendar-in-python.html
import calendar

# Create a plain text calendar
c = calendar.TextCalendar(calendar.THURSDAY)
str = c.formatmonth(2025, 1, 0, 0)
print(str)

# Create an HTML formatted calendar
hc = calendar.HTMLCalendar(calendar.THURSDAY)
str = hc.formatmonth(2019, 6)
print(str)
#will see better in notebook


#
import calendar
for name in calendar.month_name:    print(name, end =' :: ', sep=' ,')
print?

for name in calendar.day_name : print(name , end =' ')


#day when you were born

#1994,08,14
from datetime import datetime 
bday = datetime.strptime('14081994', "%d%m%Y").date()
bday.day
bday.strftime("%A, %d-%b-%Y")
#Sunday


#days between
from datetime import date
a = date(2019,6,15)  #no 06, but 6
b = date(2019,7,28)
b-a
datetime.timedelta(7)
(b-a).days
#library datetime
from datetime import datetime
a2 = datetime(2019,6,15)  #no 06, but 6
b2 = datetime(2019,7,28)
a2, b2
b2-a2
(b2-a2).days


#range of dates
from datetime import datetime
base = datetime.today()
numdays=15  #how many
  #diff
date_list = [base + timedelta(days=x) for x in range(0, numdays)]
date_list

import pandas as pd
datelist = pd.date_range(pd.datetime.today(), periods=100).tolist()
datelist

#fwd
datelist2 = pd.date_range(start = pd.datetime.today(), periods = 100).to_pydatetime().tolist()
datelist2

#rev order
datelist3 = pd.date_range(end = pd.datetime.today(), periods = 100).to_pydatetime().tolist()
datelist3


#between ranges
import datetime

start = datetime.strptime("16-06-2019", "%d-%m-%Y")
end = datetime.strptime("07-10-2019", "%d-%m-%Y")
date_generated = [start + timedelta(days=x) for x in range(0, (end-start).days)]

for date in date_generated:    print(date.strftime("%d-%m-%Y"), end=' ')

#
import itertools
date_generator = (datetime.today() - timedelta(days=i) for i in itertools.count())
dates = itertools.islice(date_generator, 10)
list(dates)

#
dates_2 = [ start + timedelta(n) for n in range(int ((end - start).days))]
dates_2


#pandas
pd.date_range(start='1/1/2018', end='1/08/2018')
pd.date_range(start='1/1/2018', periods=8)
pd.date_range(end='1/1/2018', periods=8)
pd.date_range(start='2018-04-24', end='2018-04-27', periods=3)
pd.date_range(start='1/1/2018', periods=5, freq='M')
pd.date_range(start='1/1/2018', periods=5, freq='3M')
pd.date_range(start='1/1/2018', periods=5, freq=pd.offsets.MonthEnd(3))
pd.date_range(start='1/1/2018', periods=5, tz='Asia/Tokyo')
pd.date_range(start='1/1/2018', periods=5, tz='Asia/Kolkata')
pd.date_range(start='2017-01-01', end='2017-01-04', closed=None)
pd.date_range(start='2017-01-01', end='2017-01-04', closed='left')
pd.date_range(start='2017-01-01', end='2017-01-04', closed='right')
#https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.date_range.html
