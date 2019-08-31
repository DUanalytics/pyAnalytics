#Topic: Financial data
#-----------------------------
#libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# package to extract data from various Internet sources into a DataFrame
# make sure you have it installed
from pandas_datareader import data, wb

# package for dates
import datetime as dt
start = dt.datetime(2018, 1, 1)
end = dt.datetime.today()
start

stocks = ['AAPL', 'TSLA', 'IBM', 'LNKD']
df = wb.DataReader(stocks, 'google', start, end)
df

df.items
vol = df['Volume']
vol.head()

vol['week'] = vol.index.week
vol['year'] = vol.index.year

week = vol.groupby(['week','year']).sum()
week.head()


del vol['week']
vol['year'] = vol.index.year

year = vol.groupby(['year']).sum()
year


#------------
#%%%
url = 'https://raw.githubusercontent.com/datasets/investor-flow-of-funds-us/master/data/weekly.csv'
df = pd.read_csv(url)
df.head()
df = df.set_index('Date')
df.head()
df.index
# it is a 'object' type
df.index = pd.to_datetime(df.index)
type(df.index)

monthly = df.resample('M').sum()
monthly

year = monthly.resample('AS-JAN').sum()
year
