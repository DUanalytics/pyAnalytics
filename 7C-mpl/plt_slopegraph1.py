#
#-----------------------------
#%
# Slopegraphs in matplotlib
# Trey Causey (@treycausey)
# Problems arise when equal values occur
# within the same time unit

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

units = ['A', 'B', 'C', 'D']
times = ['time1', 'time2', 'time3']
df = pd.DataFrame(index=units, columns=times)

df.time1 = [4, 5, 6, 7]
df.time2 = [5, 4, 7, 6]
df.time3 = [5, 4, 6, 7]

ymin = min(df.min())
ymax = max(df.max())

num_times = df.shape[1]
num_units = df.shape[0]

plt.xlim(0, num_units)
plt.ylim(ymin - 1, ymax + 1)
plt.axis('off')

for time in range(num_times):
    for unit in range(num_units):
        plt.text(time + 1, 
                df.values[unit][time] - .05,
                '{} : {}'.format(df.index[unit], df.values[unit][time]),
                horizontalalignment='center',
                verticalalignment='baseline')

num_lines = range(1, num_times)

for l in num_lines:
    for row in df.values:
        plt.plot([l + .25, l + .75], [row[l - 1], row[l]])

plt.show()