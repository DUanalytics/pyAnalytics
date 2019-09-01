#Time Series Plot
#-----------------------------
#%
#https://machinelearningmastery.com/time-series-data-visualization-with-python/
Line Plots.
Histograms and Density Plots.
Box and Whisker Plots.
Heat Maps.
Lag Plots or Scatter Plots.
Autocorrelation Plots.

#data
import pandas as pd
import numpy as np
import matplotlib.pyplot as pyplot

url ="https://raw.githubusercontent.com/jbrownlee/Datasets/master/daily-min-temperatures.csv"
series = pd.read_csv(url, header=0)
print(series.head())
series.columns
series.dtypes
pd.to_datetime('2018-01-15 3:45pm')
pd.to_datetime('7/8/1952')
pd.to_datetime('7/8/1952', dayfirst=True)
pd.to_datetime(['2018-01-05', '7/8/1952', 'Oct 10, 1995'])
pd.to_datetime(['2/25/10', '8/6/17', '12/15/12'], format='%m/%d/%y')
series['Date'] = pd.to_datetime(series['Date'])
series.dtypes
series.head()
#conver to dates


#TS
series.set_index('Date', inplace=True)

series.plot(linewidth=0.1)
pyplot.show()

#with multiple cols
cols_plot = ['C1', 'C2', 'C3']
axes = df[cols_plot].plot(marker='.', alpha=0.5, linestyle='None', figsize=(11, 9), subplots=True)
for ax in axes:
    ax.set_ylabel('Y Label')
    
#customising Dates
import matplotlib.dates as mdates    
fig, ax = plt.subplots()
ax.plot(......)
ax.set_ylabel('Y Labels')
ax.set_title('Main Title')
# Set x-axis major ticks to weekly interval, on Mondays
ax.xaxis.set_major_locator(mdates.WeekdayLocator(byweekday=mdates.MONDAY))
# Format x-tick labels as 3-letter month name and day number
ax.xaxis.set_major_formatter(mdates.DateFormatter('%b %d'));
#https://www.dataquest.io/blog/tutorial-time-series-analysis-with-pandas/
