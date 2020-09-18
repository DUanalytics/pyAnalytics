#Topic Time Series

#%%%
#https://www.analyticsvidhya.com/blog/2018/02/time-series-forecasting-methods/

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import seaborn as sns
sns.set(style='darkgrid', context='talk', palette='Dark2')

my_year_month_fmt = mdates.DateFormatter('%m/%y')

#%%%%
pd.date_range?
dates = pd.date_range('2020-09-01',periods=30, freq='B')
dates   #B Business days (19 & 21 Sep - Sat & Sun)
np.random.randint(1234)
price = np.random.randint(low=50, high=100, size=30)

data = pd.DataFrame({'price':price}, index=dates)
data.head(10)
data.plot(figsize=(10,7))

#%%% Average
#Simple Average
data.price.mean()
#moving Average : shifting period
#1,2,3; 2,3,4 ....

ma3 = data.rolling(window=3, center=True).mean()
ma3
ma3.head()
pd.concat([data, ma3], axis=1)
ma3.plot(figsize=(10,7))
#plot them together
fig, ax = plt.subplots(figsize=(10,7))
ax.plot(data)
ax.plot(ma3)
plt.legend('topright')
plt.show();

#different combinations of windows
#%%%  Exponential Smoothening
#pip install pmdarima  #from anaconda
import pmdarima.datasets as pm
data2= pm.load_airpassengers(True)
data2

from statsmodels.tsa.api import ExponentialSmoothing, SimpleExpSmoothing, Holt
fit2 = SimpleExpSmoothing( np.asarray(data)).fit( smoothing_level=0.6, optimized=False)
data.tail(6)
data
fit2.forecast(5)  #forecast 5 period ahead

#%%%  #some error
fit3 = ExponentialSmoothing(np.asarray(data) ,seasonal_periods=7 , trend='add', seasonal='add',).fit()
fit3.forecast(5)

####
from statsmodels.tsa.api import ExponentialSmoothing
exp = ExponentialSmoothing(data)
exp_model = exp.fit(smoothing_level=0.1)
result = exp_model.fittedvalues
dir(exp_model)
data
exp_model.predict(30)
result
result.plot()


#%%%%
import pmdarima.datasets as pm
wine = pm.load_wineind(True)
wine.head()
wine.tail()
wine.head().append(wine.tail())  #head and tail together
wine.shape
wine
#176 observations
wineTrg = wine[0:108] # Up to December '88
#create model for 108 observations
wineVal = wine[108:] # From January '89 until end
wineTrg
wineVal
#%%%%%
wineTrg.rolling(window=3)
wine_ma3c = wineTrg.rolling(window=3, center=True).mean()
wine_ma3c
wine_ma3 = wineTrg.rolling(window=3, center=False).mean()
wine_ma3


#%%% Exponential Smothening

from statsmodels.tsa.ar_model import AR
model1 = AR(wineTrg)
model1_fit = model1.fit()
# make prediction
yhat1 = model1_fit.predict(len(wineTrg), len(wineTrg))
print(yhat1)


#end 
