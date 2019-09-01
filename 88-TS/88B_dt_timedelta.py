#Date Time - time delta
#-----------------------------

#timedelta - Subtracting dates produces a timedelta, and a timedelta can be added or subtracted from a date to produce another date. The internal values for a timedelta are stored in days, seconds, and microseconds.
#https://docs.python.org/2/library/datetime.html#timedelta-objects

import datetime

print("microseconds:", datetime.timedelta(microseconds=1))
print("milliseconds:", datetime.timedelta(milliseconds=1))
print("seconds     :", datetime.timedelta(seconds=1))
print("minutes     :", datetime.timedelta(minutes=1))
print("hours       :", datetime.timedelta(hours=1))
print("days        :", datetime.timedelta(days=1))
print("weeks       :", datetime.timedelta(weeks=1))
#months, years not avl
#print("months       :", datetime.timedelta(months=1))

#%%%
#Date Arithmetic: Date math uses the standard arithmetic operators. 
import datetime
today = datetime.date.today()
today
#simple arithmetic
today + 1 #will not work
today + datetime.timedelta(days=1)  #this will work

#one Day
one_day = datetime.timedelta(days=1)
one_day
today - datetime.timedelta(days=1)  #another way

yesterday = today - one_day
yesterday

tomorrow = today + one_day
tomorrow
today + datetime.timedelta(days=1)  #another way

diff1 = tomorrow - yesterday
diff1
type(diff1)  #timedelta format

diff2 = yesterday - tomorrow
diff2
type(diff2)


#compare values
d1, d2
d1 < d2
d1 > d2


#combining dates
datetime.datetime.now()
datetime.datetime.today()
datetime.datetime.utcnow()
datetime.datetime.is
#see the output
d = datetime.datetime.now()
print(getattr(d,'hour'))  #put this in loop
#
for attr in [ 'year', 'month', 'day', 'hour', 'minute', 'second', 'microsecond']:     print(attr, ':', getattr(d, attr), end= ' ; ' )
#
    
    
#combining date with time
import datetime
t = datetime.time(6, 30, 40)
t
d = datetime.date.today()
d

dtcombine = datetime.datetime.combine(d, t)
dtcombine   

#Parsing: The default string representation of a datetime object uses the ISO 8601 format (YYYY-MM-DDTHH:MM:SS.mmmmmm). Alternate formats can be generated using strftime(). Similarly, if your input data includes timestamp values parsable with time.strptime(), then datetime.strptime() is a convenient way to convert them to datetime instance

import datetime

format = "%a %b %d %H:%M:%S %Y"

today = datetime.datetime.today()
print('ISO     :', today)

s = today.strftime(format)
print('strftime:', s)

d = datetime.datetime.strptime(s, format)
print('strptime:', d.strftime(format))

#%%% #end
