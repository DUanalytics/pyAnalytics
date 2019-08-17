#Stock prices using quandl
#-----------------------------
#%
#pip install quandl  #install as admin in anaconda
#register in quandl and create your own keys
#https://help.quandl.com/article/320-where-can-i-find-my-api-key
#quandl.get("TC1/SBIN", start_date="1970-01-01", end_date="1970-01-01")
#https://www.quandl.com/data/TC1/SBIN-State-Bank-of-India-Adjusted-Pricing
import matplotlib.pyplot as plt
import quandl

start1 = datetime.datetime(2017, 1, 1)
end1 = datetime.datetime(2019, 7, 20)
sbi_q = quandl.get("TC1/SBIN", start_date=start1, end_date=end1, api_key="4D8hkYAV4WEkcTmD9LMW")

data = quandl.get("BSE/BOM532174", start_date="2019-06-01", end_date="2019-06-30", api_key="4D8hkYAV4WEkcTmD9LMW")
data.head()
quandl.get("BSE/BOM500112", authtoken="4D8hkYAV4WEkcTmD9LMW",  start_date="2019-06-01", end_date="2019-06-30")
data.head()
data.Close.plot()
plt.show()

data.columns
data[['Open','High','Low','Close']]
data[['Open','High','Low','Close','WAP']].plot()
data.dtypes
data.head()
#--------------------
data[['Open','Close']].plot()
data.columns
data.index
data2 =data.reset_index()
quotes = data2[['Date', 'Open', 'High', 'Low', 'Close']].copy()
quotes.head()
f1, ax = plt.subplots(figsize = (10,5))
from mpl_finance import candlestick_ohlc
#



#pip install mpl_finance
import matplotlib.dates as mdates
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.dates import MONDAY, DateFormatter, DayLocator, WeekdayLocator

from mpl_finance import candlestick_ohlc

date1 = "2019-6-1"
date2 = "2019-6-30"


mondays = WeekdayLocator(MONDAY)        # major ticks on the mondays
alldays = DayLocator()              # minor ticks on the days
weekFormatter = DateFormatter('%b %d')  # e.g., Jan 12
dayFormatter = DateFormatter('%d')      # e.g., 12

quotes = pd.read_csv('stocks/yahoo_stocks.csv',                     index_col=0,  parse_dates=True, infer_datetime_format=True)

# select desired range of dates
quotes = quotes[(quotes.index >= date1) & (quotes.index <= date2)]
quotes
fig, ax = plt.subplots()
fig.subplots_adjust(bottom=0.2)
ax.xaxis.set_major_locator(mondays)
ax.xaxis.set_minor_locator(alldays)
ax.xaxis.set_major_formatter(weekFormatter)
# ax.xaxis.set_minor_formatter(dayFormatter)

# plot_day_summary(ax, quotes, ticksize=3)
candlestick_ohlc(ax, zip( mdates.date2num( quotes.index.to_pydatetime()), quotes[ 'Open'], quotes['High'],quotes['Low'], quotes['Close']), width=0.6)

ax.xaxis_date()
ax.autoscale_view()
plt.setp(plt.gca().get_xticklabels(), rotation=45, horizontalalignment='right')

plt.show()
