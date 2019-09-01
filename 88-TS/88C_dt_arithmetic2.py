#Date Arithmetic
#-----------------------------
#%

from datetime import datetime, date
t1 = date(year = 2018, month = 7, day = 12)
t1
t2 = date(year = 2017, month = 12, day = 23)
t2
t3 = t1 - t2
print("t3 =", t3)
t4 = datetime(year = 2018, month = 7, day = 12, hour = 7, minute = 9, second = 33)
t5 = datetime(year = 2019, month = 6, day = 10, hour = 5, minute = 55, second = 13)
t6 = t4 - t5
print("t6 =", t6)
print("type of t3 =", type(t3)) 
print("type of t6 =", type(t6))  


#Difference between two timedelta objects
from datetime import timedelta
t1 = timedelta(weeks = 2, days = 5, hours = 1, seconds = 33)
t2 = timedelta(days = 4, hours = 11, minutes = 4, seconds = 54)
t3 = t1 - t2
print("t3 =", t3)

#Printing negative timedelta object
from datetime import timedelta
t1 = timedelta(seconds = 33)
t2 = timedelta(seconds = 54)
t3 = t1 - t2
print("t3 =", t3)
print("t3 =", abs(t3))


#Time duration in seconds
#You can get the total number of seconds in a timedelta object using total_seconds() method.

from datetime import timedelta
t = timedelta(days = 5, hours = 1, seconds = 33, microseconds = 233423)
print("total seconds =", t.total_seconds())


#
from dateutil.relativedelta import relativedelta
import datetime
myBirthday = datetime.datetime(1994,6,23,16,20,0,0)
type(myBirthday)
now = datetime.datetime.now()
type(now) #datetime.datetime
difference = relativedelta(now, myBirthday)
difference.years

#import df, calculate age
df = pd.read_csv('data/studentdata.csv')
df
df.dob.head()
df.dtypes
#convert date in string to date
from datetime import datetime
dob2 = [datetime.strptime(x, '%Y-%m-%d') for x in df.dob]
type(dob2)
dob2
today = datetime.today()
today
dob2
difference1 = relativedelta(today, dob2)

dob3 = [parse(x) for x in df.dob]
#not working

import pandas as pd
df['dob4'] = pd.to_datetime(df.dob)
df.dtypes
type(df.dob4)

today = datetime.today()
difference1 = relativedelta(today, dob2)

df.dtypes
df['dob5'] = df['dob4'] - pd.DateOffset(years=1)
df.dtypes
df['dob6'] = df['dob5'] - pd.Timedelta(days=365)
df
rom dateutil.relativedelta import  relativedelta

df["dob7"] = df["dob4"].apply(lambda x: x - relativedelta(years=1))
df
from dateutil.relativedelta import relativedelta, MO
delta = relativedelta(hours=25, day=1, weekday=MO(1))
df['dob7'] + delta
relativedelta(df.dob5, df.dob4)
#pd.offsets.DateOffset(years=1)