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
dates = ['2019-7-01', '2019-7-2', '2019-7-3','2019-7-4', '2019-7-5']
classDays = [datetime.strptime(x,'%Y-%m-%d') for x in dates]
attendance = [49, 35, 40, 50, 38]

attndTS = pd.Series(attendance, index=classDays)
attndTS
plt.plot(attndTS)


#Air Passengers
#https://machinelearningmastery.com/power-transform-time-series-forecast-data-python/

url= "https://raw.githubusercontent.com/jbrownlee/Datasets/master/airline-passengers.csv"

from matplotlib import pyplot
series = pd.Series.from_csv(url, header=0)

pyplot.figure(1)
# line plot
pyplot.subplot(211)
pyplot.plot(series)
# histogram
pyplot.subplot(212)
pyplot.hist(series)
pyplot.show()