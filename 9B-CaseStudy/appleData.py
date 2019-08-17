#Topic: Apple Data
#-----------------------------
#libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


%matplotlib inline


url = 'https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/09_Time_Series/Apple_Stock/appl_1980_2014.csv'
apple = pd.read_csv(url)

apple.head()
apple.dtypes
apple.Date = pd.to_datetime(apple.Date)

apple['Date'].head()
apple = apple.set_index('Date')
apple.head()

# NO! All are unique
apple.index.is_unique


apple.sort_index(ascending = True).head()

apple_month = apple.resample('BM').mean()
apple_month.head()

#diff btw first and last dt
(apple.index.max() - apple.index.min()).days

#data of months
apple_months = apple.resample('BM').mean()
len(apple_months.index)

#plot
# makes the plot and assign it to a variable
appl_open = apple['Adj Close'].plot(title = "Apple Stock")
# changes the size of the graph
fig = appl_open.get_figure()
fig.set_size_inches(13.5, 9)