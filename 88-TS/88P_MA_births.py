#Topic: Time Series - Moving Average
#-----------------------------
#libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

url='https://raw.githubusercontent.com/jbrownlee/Datasets/master/daily-total-female-births.csv'

series = pd.read_csv(url, header=0, index_col=0)
print(series.head())
series.plot(figsize=(10,7))
plt.show();


#Moving Avg : obs(t) = 1/3 * (t-2 + t-1 + t)
series.head()
t=series.to_numpy()
t[0]
ma1 = 1/3 * (t[0]+t[1]+t[2])
ma1
#obs(t) = 1/3 * (35 + 32 + 30)
#obs(t) = 32.333
i=0
ma1 = 1/3 * (t[i]+t[i+1]+t[i+2])
ma1
i=0+1
ma2 = 1/3 * (t[i]+t[i+1]+t[i+2])
ma2
#%%%
movavg = series.rolling(window=3).mean()
movavg
movavg.head()
# plot original and transformed dataset
fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(series[:10], color='blue')
ax.plot(movavg[:10],color='red')
plt.show();

#%% Shifting of series data 
#series needs to be shifted forward by one, minus the window size. This is to ensure that the moving average summarizes the last few values and does not include the value to be predicted in the average, which would be an invalid framing of the problem as the input would contain knowledge of the future being predicted. For example, with a window size of 3, we must shift the series forward by 2 time steps. This is because we want to include the previous two observations as well as the current observation in the moving average in order to predict the next value. We can then calculate the moving average from this shifted series.
width = 3
lag1 = series.shift(1)
lag3 = series.shift(width - 1)
mashift = lag3.rolling(window=width).mean()
dataframe = pd.concat([mashift, lag1, series], axis=1)
dataframe.columns = ['mashift', 't-1', 't+1']
print(dataframe.head(10))



#https://machinelearningmastery.com/moving-average-smoothing-for-time-series-forecasting-python/
