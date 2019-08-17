#Plot Data with Missing Values
#-----------------------------
#%

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

day = ([ 1 , 2 , 3, 4, 5 , 6 , 7 , 8 , 9])
rain = ([0.6 , 0.8 , np.nan, np.nan, 1 , 6 , 6.5 ,7 , 4])
snow = ([ 1 , 2 , np.nan, np.nan, 0.5 , 7 , 8 , 9 , 10])

df = pd.DataFrame({'rain': rain, 'snow': snow}, index = day)
df.index.name = 'day'
df

fig, ax = plt.subplots()
line, = ax.plot(df['rain'].fillna(method='ffill'), ls = '--', lw = 1, label='_nolegend_')
ax.plot(df['rain'], color=line.get_color(), lw=1.5, marker = 'o')
line, = ax.plot(df['snow'].fillna(method='ffill'), ls = '--', lw = 1, label='_nolegend_')
ax.plot(df['snow'], color=line.get_color(), lw=1.5, marker = 'o')
plt.legend()
plt.xlabel('day')
plt.ylabel('mm')
plt.show()

#https://stackoverflow.com/questions/50821484/python-plotting-missing-data
