#Panda - TS - Financial Data
#-----------------------------
#%
#Pandas 9 : Financial Data 
from pandas_datareader import data
goog = data.DataReader('GOOG', start='2016',end='2017', data_source='yahoo')
type(goog)
goog.iloc[1:5,1:4]
goog2 = goog['Close']
goog2.head()
%matplot inline
import matplotlib.pyplot as plt
import seaborn; seaborn.set()
goog2.plot()
goog2.plot(alpha=0.5, style='-')
goog2.resample('BA').mean().plot(style=':')
goog2.asfreq('BA').plot(style='--');
plt.legend(['input','resample','asfreq'], loc='upper left');

fig, ax = plt.subplots(2, sharex=True)
data=goog2.iloc[:10]
data
#Graph not showing ??
data.asfreq('D').plot(ax=ax[0])
data.asfreq('D', method='bfill').plot(ax=ax[1], style='-o')
data.asfreq('D', method='ffill').plot(ax=ax[1], style='--o')
ax[1].legend(['back-fill', 'forward-fill']);

#Time Shifts
fig. ax = plt. subplots(3, sharey=True)
goog2 = goog2.asfreq('D', method='pad')
goog2.plot(ax=ax[0])

goog2.shift(900).plot(ax=ax[1])
goog2.tshift(900).plot(ax=ax[2])
local_max = pd.to_datetime('2017-10-05')
local_max
offset=pd.Timedelta(900,'D')
offset
ax[0].legend(['input'],loc=2)
ax[0].get_xticklabels()[4].set(weight='heavy', color='red') 
ax[0].axvline(local_max, alpha=0.3, color='red')