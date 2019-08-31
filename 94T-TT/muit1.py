#Topic:
#-----------------------------
#libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime as dt
#df = pd.read_csv('data/mtcars.csv')
df.head()



#

df1 = pd.read_csv('data/daily-min-temperatures.csv', header=0, parse_dates=['Date'])
df1.head()
#df1['Date'] = pd.to_datetime(df1['Date'])
df1.info()
pd.to_datetime(data.index, unit='s')
df1.groupby(pd.TimeGrouper(%A))
groups1 = df1.groupby(pd.Grouper(key='Date', freq='A'))
groups1 = df1.groupby(pd.TimeGrouper('A'))
groups1.agg({'Temp':sum})

years = DataFrame()
for name, group in groups1:	years[name.year] = group.values
years = years.T
pyplot.matshow(years, interpolation=None, aspect='auto')
pyplot.show()

