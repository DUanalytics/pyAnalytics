#Time Series Data
#-----------------------------
#%

import pandas as pd
import numpy as np
from datetime import datetime as dt

dt(2019,7,1)
dt.strptime('2019-7-1', '%Y-%m-%d')
dates1 = ['01/01/2016 04:50','01/01/2016 05:50','01/01/2016 06:50','01/01/2016 07:50']
DATE1 = [datetime.strptime(x,'%m/%d/%Y %H:%M') for x in dates]
DATE1

#

dates = ['2019-7-1', '2019-7-2', '2019-7-3','2019-7-4', '2019-7-5']
classDays = [datetime.strptime(x,'%Y-%m-%d') for x in dates]
attendance = [49, 35, 40, 50, 38]

attndTS = pd.Series(attendance, index=classDays)
attndTS
plt.plot(attndTS)


#Sort Dates
from datetime import datetime

dates2 = ['2019-7-10', '2019-7-9', '2019-7-3','2019-7-4', '2019-7-5']

dates2.sort(key = lambda x: datetime.strptime(x, '%Y-%m-%d')) 
dates2
type(dates2)


#end here




