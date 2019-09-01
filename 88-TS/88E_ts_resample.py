#Dates  - Range
#-----------------------------
#https://towardsdatascience.com/playing-with-time-series-data-in-python-959e2485bff8

import pandas as pd
import numpy as np

dtrange1D = pd.date_range('2019-1-1', '2019-7-11', freq='D')
dtrange1D
dtrange1D.min()


#The resulting DatetimeIndex has an attribute freq with a value of 'D', indicating daily frequency.#Available frequencies in pandas include 
#hourly ('H'), 
#calendar daily ('D'),
#business daily ('B'),
#weekly ('W'),
#monthly ('M'),
#quarterly ('Q'),
#annual ('A'), and many others.
#Frequencies can also be specified as multiples of any of the base frequencies, for example '5D' for every five days.

dtrange3D = pd.date_range('2019-1-1', '2019-7-11', freq='3D')
dtrange3D

dtrange1M = pd.date_range('2019-1-1', '2019-7-11', freq='1M')
dtrange1M

#date range at hourly frequency, specifying the start date and number of periods, instead of the start date and end date.

pd.date_range('2019-7-11', periods=8, freq='H')
pd.date_range('2019-7-11 09:00', periods=8, freq='H')

#https://www.dataquest.io/blog/tutorial-time-series-analysis-with-pandas/
#convert to different freq
#create data frame - weekly freq with some data
classStrength = np.random.randint(25,60, size=100)
weekdates = pd.date_range('2019-5-1', periods=100, freq='B')
weekdates
attendance = pd.DataFrame({'classStr':classStrength, 'wdates':weekdates})
attendance.head(10).append(attendance.tail(10))

#
attendance.set_index('wdates', inplace=True)
attendance
#create another column with daily freq
attendance.asfreq('D')  #some missing values Sat/ Sun
attendance.head(10)
#temporarily creates dates for Sat/ Sun, fill with NA

#del dailyAttendance
attendance.asfreq('D', method='ffill')
attendance.head()
daily1 = attendance.asfreq('D', method='bfill')
daily1.head(10)
#replace permanently
daily1.rename(columns= {'classStr':'Dattnd'}, inplace=True)

newAttendance2 = pd.concat([attendance, daily1], axis=1)
newAttendance2.head()

#a.to_frame().join(b)#with same index
#resample
newAttendance2.resample('W').sum()
newAttendance2.resample('M').sum()

newAttendance2.classStr
newAttendance2.Dattnd

#
# Start and end of the date range to extract
start, end = '2019-05', '2019-06'
# Plot daily and weekly resampled time series together
#run together upto plt.show
fig, ax = plt.subplots()
ax.plot(newAttendance2.loc[start:end, 'Dattnd'], marker='.', linestyle='-', linewidth=0.5, label='Daily')
ax.plot(newAttendance2.loc[start:end, 'classStr'], marker='o', markersize=8, linestyle='-', label='Weekly Mean Resample')
ax.set_ylabel('Class Strength')
plt.xticks(rotation=90)
ax.legend()
plt.show();

#------------------------------------

#
newAttendance2['Dattnd'].resample('M').sum()
newAttendance2['Dattnd'].resample('M').sum(min_count=5)
#min rows=5

#----------
fig, ax = plt.subplots()
ax.plot(newAttendance2['Dattnd'], color='black', label='Daily Attendance')
newAttendance2[['classStr','Dattnd']].plot.area(ax=ax, linewidth=0)
ax.xaxis.set_major_locator(mdates.YearLocator())
ax.legend()
ax.set_ylabel('Student Strength');


#https://www.dataquest.io/blog/tutorial-time-series-analysis-with-pandas/
#resample() method, which splits the DatetimeIndex into time bins and groups the data by time bin