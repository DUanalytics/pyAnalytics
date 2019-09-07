#
#-----------------------------
#%
#The Airline Passengers dataset describes the total number of airline passengers over a period of time.

The units are a count of the number of airline passengers in thousands. There are 144 monthly observations from 1949 to 1960.

from matplotlib import pyplot
import pandas as pd
series = pd.read_csv('https://raw.githubusercontent.com/jbrownlee/Datasets/master/airline-passengers.csv', header=0)
series.plot()
pyplot.show()

#
from matplotlib import pyplot
from statsmodels.tsa.seasonal import seasonal_decompose
series = pd.read_csv('https://raw.githubusercontent.com/jbrownlee/Datasets/master/airline-passengers.csv', header=0)
series.head()
series.index
series.shape
series.index = pd.DatetimeIndex(freq='m', start='1949-01', periods=144)
result = seasonal_decompose(series, model='multiplicative')
result.plot()
pyplot.show()