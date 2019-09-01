#Panda Data Ranges
#-----------------------------
#%

from datetime import datetime
datetime(year=2017, month=12, day=23)

from dateutil import parser
date = parser.parse('23rd of December, 2017')
date
date.strftime('%A')

#Typed array of times 
import numpy as np
date = np.array('2017-12-23', dtype=np.datetime64)
date
date + np.arange(12)
np.datetime64('2017-12-23')

np.datetime64('2017-12-23 12:00')
np.datetime64('2017-12-23 12:00', 'ns')


#Dates & Times in Pandas
import pandas as pd
date = pd.to_datetime('23rd of December, 2017')
date
date.strftime('%A')
date + pd.to_timedelta(np.arange(12), 'D')

index = pd.DatetimeIndex(['2016-07-21','2016-08-23', '2017-07-21', '2017-08-22'])
data = pd.Series([0,1,2,3], index=index)
data
data['2017']

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