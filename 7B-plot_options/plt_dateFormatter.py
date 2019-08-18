# Date Formatter
#-----------------------------
#%
# import required python packages
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter
import os
plt.ion()
import earthpy as et

# matplotlibdate format modules
from matplotlib.dates import DateFormatter
import matplotlib.dates as mdates


myFmt = DateFormatter("%m/%d/%a")
ax.xaxis.set_major_formatter(myFmt); 

#sample data
import pandas_datareader as web
import datetime
start = datetime.datetime(2017, 6, 1)
end = datetime.datetime(2019, 6, 30)
sbi = web.DataReader("sbin.ns", 'yahoo', start, end)
sbi.head() 

data=sbi.copy()
data.reset_index(inplace=True)
data.head()
#fast/ quick
fig, ax = plt.subplots()
ax.plot('Date', 'Adj Close', data=data)
#configure
years = mdates.YearLocator()   # every year
months = mdates.MonthLocator()  # every month
years_fmt = mdates.DateFormatter('%Y')




#%%

import matplotlib.dates as mdates
data[['Date','High']].head()

years = mdates.YearLocator()   # every year
months = mdates.MonthLocator()  # every month
fig = plt.figure(figsize=(10,4))
ax = fig.add_subplot(111)
plt.xticks(rotation=70)
ax.plot('Date','High', data=data)
plt.show()

#%%

fig = plt.figure(figsize=(10,4))
ax = fig.add_subplot(111)
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
ax.plot('Date','High', data=data)
fig.autofmt_xdate()
plt.show()

#%%%
fig = plt.figure(figsize=(10,4))
ax = fig.add_subplot(111)
ax.xaxis.set_major_formatter(mdates.DateFormatter('%b/%y'))
ax.plot('Date','High', data=data)
#fig.autofmt_xdate()#this does auto adjustment
ax.xaxis.set_tick_params(rotation=20) #this works on non dates also
plt.show()

#%%
fig = plt.figure(figsize=(10,4))
ax = fig.add_subplot(111)
ax.xaxis.set_major_formatter(mdates.DateFormatter('%b/%y'))
ax.plot('Date','High', data=data)
fig.autofmt_xdate(bottom=0.1, rotation=30, ha='left')
plt.show()
#https://stackoverflow.com/questions/11264521/date-ticks-and-rotation-in-matplotlib

#%%
#ax.xaxis.set_major_formatter(mdates.DateFormatter('%m-%Y'))
#ax.xaxis.set_major_locator(years)
#ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
#plt.xticks(rotation=90)
#ax.xaxis.set_minor_locator(months)
#ax.xaxis.set_minor_formatter(mdates.DateFormatter('%m-%Y'))
#
# date.autoformatter.year     : %Y
# date.autoformatter.month    : %Y-%m
# date.autoformatter.day      : %Y-%m-%d
# date.autoformatter.hour     : %m-%d %H
# date.autoformatter.minute   : %d %H:%M
# date.autoformatter.second   : %H:%M:%S
# date.autoformatter.microsecond   : %M:%S.%f
#plt.rcParams["date.autoformatter.minute"] = "%Y-%m-%d %H:%M:%S"
