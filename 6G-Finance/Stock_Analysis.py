#This part of the program will explain the steps of doing Financial Analysis of Indian Stock
#Common Financial Analysis - Time Series, Returns, Percentage Change, Cumulative Daily Rate of Return
#Moving Windows, OLS Regression;Buidling Trading Strategy, Backtesting the Trading Strategy
#import libraries 
#import external pandas_datareader library with alias of web
import pandas_datareader as web
#import datetime internal datetime module
import datetime
#datetime.datetime is a data type within the datetime module
#import plot lib and also show plots inline within notebook
import matplotlib.pyplot as plt
#get_ipython().run_line_magic('matplotlib', 'inline')
#set the start and end dates
start1 = datetime.datetime(2017, 1, 1)
end1 = datetime.datetime(2019, 7, 20)
#url yahoo finance
sbi_y = web.DataReader("sbin.ns", 'yahoo', start=start1, end=end1)

# In[4]:
sbi_y.head(5)

# In[8]:
sbi_y.Close.plot()
# In[13]:
#import from quandl : create your own key after registration: service is free for limited functions
import quandl
sbi_q = quandl.get("BSE/BOM500112", start_date=start1, end_date=end1, api_key="4D8hkYAV4WEkcTmD9LMW")
#https://www.quandl.com/data/BSE/BOM500112-STATE-BANK-OF-INDIA-EOD-Prices
sbi_q.head(3)


# In[14]:
sbi_q.Close.plot()
# In[33]:
#Lets use Yahoo
sbi_y.head(5).append(sbi_y.tail(3))
# In[15]:
# Describe stock
sbi_y.describe()
# In[40]:
#Save to CSV for loading the data again : check if there is folder data
import pandas as pd
sbi_y.to_csv('data/sbi.csv')
df = pd.read_csv('data/sbi.csv', header=0, index_col='Date', parse_dates=True)
df.head(5)  #reading 
# In[46]:
# Inspect the index 
print(df.index)
# Inspect the columns
print(df.columns)
# Select only the last 10 observations of `Close`: it will be series
ts = df['Close'][-10:]
# Check the type of `ts` 
type(ts)
# In[52]:
# Inspect the few rows of November-December 2018
print(df.loc[pd.Timestamp('2018-11-01'):pd.Timestamp('2018-12-31')].head(3))
# In[53]:
# Inspect the first rows of 2018
print(df.loc['2018'].head())

# In[55]:


# Inspect (row no 10 to 15)
print(df.iloc[10:15])


# In[62]:


# Inspect the 'Open' and 'Close' values at x and y : few rows
print(len(df))
print(df.iloc[[1,25,75,100, 200,300,400,500,600], [0, 3]])


# In[67]:


# Sample 10 rows
sample = df.sample(10)
# Print `sample`
print(sample)


# In[69]:


# Resample to monthly level 
monthly_df = df.resample('M').mean()
# Print `monthly_df`
print(monthly_df)


# In[70]:


#check use of as.freq
df.asfreq("M", method="bfill")


# In[72]:


# Add a column `diff` 
df['diff'] = df.Open - df.Close
df['diff']
# Delete the new `diff` column
#del aapl['diff']


# In[75]:


# Import Matplotlib's `pyplot` module as `plt`
import matplotlib.pyplot as plt
# Plot the closing prices 
df['Close'].plot(grid=True)
df['Open'].plot(grid=True)
# Show the plot
plt.legend()
plt.show()


# In[77]:


#Return -
# Import `numpy` as `np`
import numpy as np
# Assign `Adj Close` to `daily_close`
daily_close = df[['Adj Close']]

# Daily returns
daily_pct_change = daily_close.pct_change()

# Replace NA values with 0
daily_pct_change.fillna(0, inplace=True)


# In[78]:


# Inspect daily returns
print(daily_pct_change)


# In[79]:


# Daily log returns
daily_log_returns = np.log(daily_close.pct_change()+1)
#calculate the log returns to get a better insight into the growth of your returns over time.
# Print daily log returns
print(daily_log_returns)


# In[82]:


# Resample to business months, take last observation as value 
monthly = df.resample('BM').apply(lambda x: x[-1])

# Calculate the monthly percentage change
monthly.pct_change()


# In[83]:


# Resample to quarters, take the mean as value per quarter
quarter = df.resample("4M").mean()

# Calculate the quarterly percentage change
quarter.pct_change()


# In[84]:


# Daily returns : with shift
daily_pct_change = daily_close / daily_close.shift(1) - 1

# Print `daily_pct_change`
print(daily_pct_change)


# In[86]:


daily_log_returns_shift = np.log(daily_close / daily_close.shift(1))
print(daily_log_returns_shift)


# In[87]:


# Import matplotlib
import matplotlib.pyplot as plt

# Plot the distribution of `daily_pct_c`
daily_pct_change.hist(bins=50)

# Show the plot
plt.show()

# Pull up summary statistics
print(daily_pct_change.describe())


# In[88]:


# Calculate the cumulative daily returns
cum_daily_return = (1 + daily_pct_change).cumprod()

# Print `cum_daily_return`
print(cum_daily_return)


# In[89]:


# Import matplotlib
import matplotlib.pyplot as plt 

# Plot the cumulative daily returns
cum_daily_return.plot(figsize=(12,8))

# Show the plot
plt.show()


# In[90]:


# Resample the cumulative daily return to cumulative monthly return 
cum_monthly_return = cum_daily_return.resample("M").mean()

# Print the `cum_monthly_return`
print(cum_monthly_return)


# In[95]:


def get(tickers, startdate, enddate):
  def data(ticker):
    return (web.get_data_yahoo(ticker, start=startdate, end=enddate))
  datas = map (data, tickers)
  return(pd.concat(datas, keys=tickers, names=['Ticker', 'Date']))

tickers = ['AAPL', 'MSFT', 'IBM', 'GOOG']
all_data = get(tickers, datetime.datetime(2017, 10, 1), datetime.datetime(2019, 1, 1))
all_data.head()


# In[94]:


# Import matplotlib
import matplotlib.pyplot as plt 

# Isolate the `Adj Close` values and transform the DataFrame
daily_close_px = all_data[['Adj Close']].reset_index().pivot('Date', 'Ticker', 'Adj Close')

# Calculate the daily percentage change for `daily_close_px`
daily_pct_change = daily_close_px.pct_change()

# Plot the distributions
daily_pct_change.hist(bins=50, sharex=True, figsize=(12,8))

# Show the resulting plot
plt.show()


# In[101]:


# Import matplotlib
import matplotlib.pyplot as plt
#from matplotlib import plotting  
# Plot a scatter matrix with the `daily_pct_change` data 
pd.plotting.scatter_matrix(daily_pct_change, diagonal='kde', alpha=0.1,figsize=(12,12))
# Show the plot
plt.show()


# In[102]:


# Isolate the adjusted closing prices 
adj_close_px = df['Adj Close']

# Calculate the moving average
moving_avg = adj_close_px.rolling(window=40).mean()

# Inspect the result
print(moving_avg[-10:])


# In[106]:


# Import matplotlib 
import matplotlib.pyplot as plt

# Short moving window rolling mean
df['42'] = adj_close_px.rolling(window=40).mean()

# Long moving window rolling mean
df['252'] = adj_close_px.rolling(window=252).mean()

# Plot the adjusted closing price, the short and long windows of rolling means
df[['Adj Close', '42', '252']].plot()

# Show plot
plt.show()


# In[107]:


# Import matplotlib
import matplotlib.pyplot as plt 

# Define the minumum of periods to consider 
min_periods = 75 

# Calculate the volatility
vol = daily_pct_change.rolling(min_periods).std() * np.sqrt(min_periods) 

# Plot the volatility
vol.plot(figsize=(10, 8))

# Show the plot
plt.show()


# In[110]:


# Import the `api` model of `statsmodels` under alias `sm`
import statsmodels.api as sm

# Import the `datetools` module from `pandas`
#from pandas.core import datetools

# Isolate the adjusted closing price
all_adj_close = all_data[['Adj Close']]

# Calculate the returns 
all_returns = np.log(all_adj_close / all_adj_close.shift(1))

# Isolate the AAPL returns 
aapl_returns = all_returns.iloc[all_returns.index.get_level_values('Ticker') == 'AAPL']
aapl_returns.index = aapl_returns.index.droplevel('Ticker')

# Isolate the MSFT returns
msft_returns = all_returns.iloc[all_returns.index.get_level_values('Ticker') == 'MSFT']
msft_returns.index = msft_returns.index.droplevel('Ticker')

# Build up a new DataFrame with AAPL and MSFT returns
return_data = pd.concat([aapl_returns, msft_returns], axis=1)[1:]
return_data.columns = ['AAPL', 'MSFT']

# Add a constant 
X = sm.add_constant(return_data['AAPL'])

# Construct the model
model = sm.OLS(return_data['MSFT'],X).fit()

# Print the summary
print(model.summary())


# In[111]:


# Import matplotlib
import matplotlib.pyplot as plt

# Plot returns of AAPL and MSFT
plt.plot(return_data['AAPL'], return_data['MSFT'], 'r.')

# Add an axis to the plot
ax = plt.axis()

# Initialize `x`
x = np.linspace(ax[0], ax[1] + 0.01)

# Plot the regression line
plt.plot(x, model.params[0] + model.params[1] * x, 'b', lw=2)

# Customize the plot
plt.grid(True)
plt.axis('tight')
plt.xlabel('Apple Returns')
plt.ylabel('Microsoft returns')

# Show the plot
plt.show()


# In[112]:


# Import matplotlib 
import matplotlib.pyplot as plt

# Plot the rolling correlation
return_data['MSFT'].rolling(window=252).corr(return_data['AAPL']).plot()

# Show the plot
plt.show()


# In[114]:


# Initialize the short and long windows
short_window = 40
long_window = 100

# Initialize the `signals` DataFrame with the `signal` column
signals = pd.DataFrame(index=df.index)
signals['signal'] = 0.0

# Create short simple moving average over the short window
signals['short_mavg'] = df['Close'].rolling(window=short_window, min_periods=1, center=False).mean()

# Create long simple moving average over the long window
signals['long_mavg'] = df['Close'].rolling(window=long_window, min_periods=1, center=False).mean()

# Create signals
signals['signal'][short_window:] = np.where(signals['short_mavg'][short_window:] 
                                            > signals['long_mavg'][short_window:], 1.0, 0.0)   

# Generate trading orders
signals['positions'] = signals['signal'].diff()

# Print `signals`
print(signals)


# In[116]:


# Import `pyplot` module as `plt`
import matplotlib.pyplot as plt

# Initialize the plot figure
fig = plt.figure()

# Add a subplot and label for y-axis
ax1 = fig.add_subplot(111,  ylabel='Price in $')

# Plot the closing price
df['Close'].plot(ax=ax1, color='r', lw=2.)

# Plot the short and long moving averages
signals[['short_mavg', 'long_mavg']].plot(ax=ax1, lw=2.)

# Plot the buy signals
ax1.plot(signals.loc[signals.positions == 1.0].index, signals.short_mavg[signals.positions == 1.0],
         '^', markersize=10, color='m')
         
# Plot the sell signals
ax1.plot(signals.loc[signals.positions == -1.0].index,   signals.short_mavg[signals.positions == -1.0],
         'v', markersize=10, color='k')
         
# Show the plot
plt.show()


# In[120]:


# Set the initial capital
initial_capital= float(100000.0)

# Create a DataFrame `positions`
positions = pd.DataFrame(index=signals.index).fillna(0.0)

# Buy a 100 shares
positions['AAPL'] = 100*signals['signal']   
  
# Initialize the portfolio with value owned   
portfolio = positions.multiply(df['Adj Close'], axis=0)

# Store the difference in shares owned 
pos_diff = positions.diff()

# Add `holdings` to portfolio
portfolio['holdings'] = (positions.multiply(df['Adj Close'], axis=0)).sum(axis=1)

# Add `cash` to portfolio
portfolio['cash'] = initial_capital - (pos_diff.multiply(df['Adj Close'], axis=0)).sum(axis=1).cumsum()   

# Add `total` to portfolio
portfolio['total'] = portfolio['cash'] + portfolio['holdings']

# Add `returns` to portfolio
portfolio['returns'] = portfolio['total'].pct_change()

# Print the first lines of `portfolio`
print(portfolio.head())

