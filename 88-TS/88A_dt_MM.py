#Time Series - Date Time - MM
#-----------------------------
#datetime
from datetime import datetime
d1= datetime(year=2019, month=9, day=1)
d1
# Parser
from dateutil import parser
d2=parser.parse('1st September 2019 0730 pm')
d2
#Numpy
import numpy as np
d3 = np.array('2019-09-01', dtype=np.datetime64)
#note 07 and 01
d3 + 1
d3 + [1,2,3]
d3 + np.array([5,10,11])
d3 + np.arange(12)
#another way
np.datetime64('2019-09-01')
np.datetime64('2019-09-01 13:00')

#%%% #Pandas Date Time
import pandas as pd
d4 = pd.to_datetime('1st Sep 2019')
d4
#vectorised ops
d4 + 1  #will not work , not numpy format
d4 + np.arange(12) #this will also not work
d4 + pd.to_timedelta(np.arange(12))  #not correct
d4 + pd.to_timedelta(np.arange(12), 'D') # daily interval
d4 + pd.to_timedelta(np.arange(12), 'M') # month interval
#%%%
##index by time
np.random.seed(1234)
attendance = np.random.randint(25,50, size=180)
np.mean(attendance) #37.63
startDate = pd.to_datetime('01 Aug 2019')
startDate
indexvalues = startDate + pd.to_timedelta(np.arange(180), 'D')
indexvalues
data1 = pd.Series(attendance, index=indexvalues)
data1
data1.head()
data1.head(2).append(data1.tail(3))  #heads-2, tails-3
#
data1['2020']  #filter
data1['2019-10'] 
data1['2019-10-01':'2019-12-25']  #between certain dates
data1[data1.index.dayofweek == 2] #2nd day of week


#----------
#Parsing a series of Dates with different dates 
dates3 = pd.to_datetime([ datetime(2019,7,10), '11th July 2019','2019-7-15', '2019-07-20', '18-07-2019']) 
dates3

#convert to periods index : not much use here
dates3.to_period('D')
dates3.to_period('M')
dates3.to_period('Y')

#difference in dates
datetime.today() - dates3[0]
datetime.today() - dates3[3]


#pandas sequence
pd.date_range('2019-07-01', '2019-10-30')

pd.date_range('2019-07-01', periods=45)
pd.date_range('2019-07-01', periods=3, freq='M')
pd.date_range('2019-07-01', periods=5, freq='H')

#%%%
#

#%%%
pd.timedelta_range(0, periods=9, freq='2H20T')

#business day offser
from pandas.tseries.offsets import BDay
pd.date_range('2019-07-01', periods=9, freq=BDay())
#see the gap in days - Sat & SUn

#%%%
#using Frequencies and Offsets




#%%%
#Reading Stock Data
#conda install pandas-datareader
from pandas_datareader import data
#https://pandas-datareader.readthedocs.io/en/latest/
#https://pandas-datareader.readthedocs.io/en/latest/remote_data.html#remote-data-google


goog = data.DataReader('GOOG', start='2004', end='2005', data_source='yahoo')
goog.head()

sbi = data.DataReader('SBIN.NS', start='2018', end='2019', data_source='yahoo')
sbi #https://in.finance.yahoo.com/quote/SBIN.NS?ltr=1
sbi.head(3).append(sbi.tail(2))
#https://github.com/swapniljariwala/nsepy
#https://medium.com/@rohanjoseph_91119/stock-analysis-in-python-4e7b7884517a
from datetime import datetime
start1 = datetime(2017, 1, 1)
end1 = datetime(2019, 7, 10)
icici = data.DataReader('ICICIBANK.NS', start=start1, end=end1, data_source='yahoo')
icici #https://in.finance.yahoo.com/quote/SBIN.NS?ltr=1
icici.head(3).append(icici.tail(2))
#https://in.finance.yahoo.com/quote/ICICIBANK.NS/
#https://in.finance.yahoo.com/quote/ICICIBANK.NS/history?p=ICICIBANK.NS

#--------
stockData = icici['Close']
#visualise
import matplotlib.pyplot as plt
import seaborn
seaborn.set()
#---
stockData
stockData.plot()
#just Close has been plotted with TS
#how to plot all ?

#Resampling- aggregation, asfreq - data selection
stockData.plot(alpha=0.5, style='-')
stockData.resample('BA').mean().plot(style=':')
#pd.options.display.float_format = '{:.2f}'.format
plt.figure(figsize=(7,5))
stockData.plot(alpha=0.5, style='-')
stockData.resample('BA').mean().plot(style=':')
stockData.asfreq('BA').plot(style='--');
plt.legend(['CLOSE','RESAMPLE','ASFREQ'], loc='upper left')

#resample - avg of year, asfreq - value at end of year

#asfreq options of ffill, bfill 
#transactions only on business days
stockData[0:31]  #7, 8 th Jan 2001 missing: how to fill these values
data1 = stockData[0:31]
data1.asfreq('D').plot(figsize=(10,5))
#see the breaks
data1.asfreq('D', method='ffill')
data1.asfreq('D', method='ffill').plot(figsize=(10,5))
#others bfill : plot together
fig, ax = plt.subplots(2, sharex=True, figsize=(10,5))
data1.asfreq('D').plot(ax=ax[0], marker='x')
data1.asfreq('D', method='ffill').plot(ax=ax[1], marker='D')
#https://matplotlib.org/api/markers_api.html
data1.asfreq('D', method='bfill').plot(ax=ax[1], marker='d')
ax[1].legend(['FORWARD fill','BACKWARD fill']);


#drawing line - single and multiple
data1
data1.asfreq('D').plot(figsize=(10,5))
plt.axvline(pd.to_datetime('2017-01-17'), color='r', linestyle='--', lw=2)
#
data1
xcoords = [pd.to_datetime('2017-01-17'), pd.to_datetime('2017-01-20')]
data1.asfreq('D').plot(figsize=(10,5))
for xc in xcoords:   plt.axvline(x=xc, color='r')

#
# x coordinates for the lines with legend
xcoords = [pd.to_datetime('2017-01-17'), pd.to_datetime('2017-01-20')]
# colors for the lines
colors = ['r','k']
data1.asfreq('D').plot(figsize=(10,5))
for xc,c in zip(xcoords,colors):
    plt.axvline(x=xc, label='line at x = {}'.format(xc), c=c)
plt.legend();
