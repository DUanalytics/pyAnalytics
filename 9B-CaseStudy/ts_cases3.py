#Time Series - Multiple Columns
#-----------------------------
#%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#attendance of multiple classes
random.seed(1234)
attend2 = np.random.randint(low=25,high=40, size=(100,3))
attend2
dates2 = pd.date_range('2019-06-15', periods=100, freq='B')
random.seed(1234)
import random
classType = random.choices(['Theory','Tutorial', 'Practical'], k=100)
classType
workshop2 = pd.DataFrame(attend2, index=dates2)
#not able to add another column classType
workshop2
workshop2['classType'] = classType
workshop2.columns=(["BBA", "MBA", "BTECH",'classType'])
workshop2.head()
#categories no order
workshop2.classType = workshop2.classType.astype('category')
workshop2.describe(include='all')
workshop2.dtypes

#%%%

#plot
workshop2.plot(figsize=(10,5))
workshop2[['BBA','MBA','BTECH']].plot(figsize=(10,5))
workshop2.plot.scatter(x='MBA', y='BBA', c='DarkBlue')

workshop2['BBA'].plot()
workshop2['MBA'].plot()

#different plots from different columns
cols_plot = ['BBA', 'MBA', 'BTECH']
axes = workshop2[cols_plot].plot(marker='.', alpha=0.8, linestyle='None', figsize=(11, 9), subplots=True)
for ax in axes:    ax.set_ylabel('Daily Attendance')
# Line
axes = workshop2[cols_plot].plot(marker='.', alpha=0.8, figsize=(11, 9), subplots=True, linestyle='-')
for ax in axes:    ax.set_ylabel('Daily Attendance')
ax.text('2019-09-1', 30, "Attendance in Sep")

#different method

fig, ax = plt.subplots(3,1,figsize=(10,4), sharex=True)
ax[0].plot(workshop2['BBA'])
ax[1].plot(workshop2['MBA'])
ax[2].plot(workshop2['BTECH'])
plt.xticks(rotation='vertical')
fig.text(.3,.9,"Attendance of Classes")
#plt.suptitle will also work
ax[0].plot.title("Attendance of BBA Classes")
plt.xlabel('Dates')
plt.ylabel('Count of Students')
plt.axvline(pd.to_datetime('2019-07-10'), color='r', linestyle='--', lw=2)
ax[0].vlines(pd.to_datetime('2019-07-15'), ymin=30, ymax=40, colors='red', linestyles='solid')
fig.tight_layout()
#https://matplotlib.org/3.1.0/api/_as_gen/matplotlib.axes.Axes.vlines.html
#https://matplotlib.org/api/_as_gen/matplotlib.axes.Axes.axvline.html
plt.savefig('workshop2.png', bbox_inches='tight')
plt.show();