#Panda Data Ranges
#-----------------------------
#%
from datetime import datetime
datetime(year=2021, month=6, day=26)
datetime.today() #todays date
datetime.now() 
datetime.now().strftime('%A %y %B %d :: %c ::: %H-%M:%S')
datetime.today().day , datetime.today().month
datetime.today().year, datetime.today().weekday()
from dateutil import parser
date = parser.parse('25th of January, 2022')
date
date.strftime('%A')
#https://docs.python.org/3/library/datetime.html
#Typed array of times 
import numpy as np
date = np.array('2022-01-01', dtype=np.datetime64)
date
date + np.arange(12)
np.datetime64('2022-01-25')

np.datetime64('2022-01-25 20:00')
np.datetime64('2021-01-25 20:00', 'ns')  #decimals

#Dates & Times in Pandas
import pandas as pd
date = pd.to_datetime('25th of January, 2022')
date
date.strftime('%A')
date + pd.to_timedelta(np.arange(12), 'D')

#date row - sales value in cols
index = pd.DatetimeIndex(['2020-09-11','2020-09-12', '2020-09-13', '2020-09-14'])
data = pd.Series([10,11,22,35], index=index)
data
data['2020']

#pandas Time Series Data Structures
dates = pd.to_datetime([datetime(2022,1,1),'3rd of Jan 2022', '2022-January-27','25-01-2022', '20220126'])
dates
dates.to_period('D')
dates - dates[0]

pd.date_range('1950-01-26','2022-01-26')
pd.date_range('2022-01-01',periods=12)
pd.date_range('2022-01-01',periods=12, freq='W') #12 weeks dates
help(pd.date_range)
pd.date_range('2022-01-25',periods=12, freq='6M')
pd.date_range('2022-01-01',periods=6, freq='M')
pd.date_range('2017-07-16',periods=6, freq='3M', Q='JAN')
pd.date_range('2017-01-01',periods=4, freq='Q-JAN')
pd.date_range('2017-01-01',periods=6, freq='Q-FEB')
pd.date_range('2017-01-01',periods=6, freq='BQ-FEB')
pd.date_range('2017-01-01',periods=3, freq='A-JAN')
pd.date_range('2017-12-12',periods=3, freq='W-SAT')


pd.timedelta_range(0, periods=9, freq='2H30T')
pd.timedelta_range(0, periods=9, freq='150T')


#practise more from internet resources
#https://docs.python.org/3/library/datetime.html
#https://www.programiz.com/python-programming/datetime
#https://www.guru99.com/date-time-and-datetime-classes-in-python.html
