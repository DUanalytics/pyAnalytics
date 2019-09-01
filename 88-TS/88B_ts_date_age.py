#Date - age
#-----------------------------
#%

#Practise Code
import datetime
mdate = "2010-10-05"
rdate = "2010-11-05"
mdate1 = datetime.datetime.strptime(mdate, "%Y-%m-%d").date()
mdate1
rdate1 = datetime.datetime.strptime(rdate, "%Y-%m-%d").date()
rdate1
mdate1 - rdate1
delta =  (mdate1 - rdate1).days
delta
delta2 = (mdate1 - rdate1).ctime
type(delta)
now = datetime.datetime.now()
now2 = datetime.datetime.strptime(now).date()
now
today = datetime.date.today() 
today
mdate1
diff2 = (today - mdate1).days/365.25
round(diff2,0)




dob1 = pd.to_datetime(df.dob)
type(dob1)
year = dob1.dt.year.values[0]
hour

dob2 = [datetime.strptime(x, '%d-%b-%y') for x in df.dob]
type(dob2)
dob3 = [parse(x) for x in df.dob]
type(dob3)
dob2
datetime.datetime(*dob3)
datetime.datetime(*map(int, dob3))


#Age
now = datetime.datetime.now()
now
difference = relativedelta(now, dob1)
str(difference.years))

df['dob'] = dob
df
df['dob'].describe()
df[['rollno','dob']].describe()
today=datetime.date.today()
agedays = today - df.dob
ageyrs = agedays/365
ageyrs
difference_in_years = (agedays.days +
agedays.seconds/86400.0)/365.2425

from dateutil.relativedelta import relativedelta
myBirthday = datetime.datetime(1966,6,23,16,20,0,0)
type(myBirthday)
type(df.dob)
now = datetime.datetime.now()
type(now) #datetime.datetime
difference = relativedelta(now, myBirthday)
difference.years
type(dob1)
difference = relativedelta(today, dob3)


import datetime
from datetime import timedelta
diff = datetime.datetime.now() - datetime.timedelta(days=10)
diff