#Panda Data Ranges
#-----------------------------
#%
from datetime import datetime
datetime(year=2020, month=09, day=18)

from dateutil import parser
date = parser.parse('18th of September, 2020')
date
date.strftime('%A')
#https://docs.python.org/3/library/datetime.html
#Typed array of times 
import numpy as np
date = np.array('2020-09-18', dtype=np.datetime64)
date
date + np.arange(12)
np.datetime64('2020-09-18')

np.datetime64('2020-09-18 20:00')
np.datetime64('2020-09-18 20:00', 'ns')  #decimals

#Dates & Times in Pandas
import pandas as pd
date = pd.to_datetime('18th of September, 2020')
date
date.strftime('%A')
date + pd.to_timedelta(np.arange(12), 'D')

index = pd.DatetimeIndex(['2020-09-11','2020-09-12', '2020-09-13', '2020-09-14'])
data = pd.Series([10,11,22,35], index=index)
data
data['2020']

#pandas Time Series Data Structures
dates = pd.to_datetime([datetime(2017,12,23),'24rd of Dec 2017', '2017-December-27','26-12-2017', '20171231'])
dates
dates.to_period('D')
dates - dates[0]

pd.date_range('2017-08-16','2017-12-23')
pd.date_range('2017-08-16',periods=12)
pd.date_range('2017-08-16',periods=12, freq='W')

pd.date_range('2017-12-23',periods=12, freq='H')
pd.date_range('2017-07-16',periods=6, freq='M')
pd.date_range('2017-07-16',periods=6, freq='Q', Q='JAN')
pd.date_range('2017-01-01',periods=4, freq='Q-JAN')
pd.date_range('2017-01-01',periods=6, freq='Q-FEB')
pd.date_range('2017-01-01',periods=6, freq='BQ-FEB')
pd.date_range('2017-01-01',periods=3, freq='A-JAN')
pd.date_range('2017-12-12',periods=3, freq='W-SAT')


pd.timedelta_range(0, periods=9, freq='2H30T')
pd.timedelta_range(0, periods=9, freq='150T')


#practise more from internet resources