#Annotations
#-----------------------------
#%
#https://matplotlib.org/2.0.2/users/annotations.html

import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.add_subplot(111)
t = np.arange(0.0, 5.0, 0.01)
s = np.cos(2*np.pi*t)
line, = ax.plot(t, s, lw=2)

ax.annotate('local max', xy=(2, 1), xytext=(3, 1.5),   arrowprops= dict(facecolor ='black', shrink=0.05), )
#place the text coordinates in fractional axes coordinates, o
ax.annotate('local max 2', xy=(4, 1),  xycoords='data', xytext=(0.8, 0.95), textcoords='axes fraction',  arrowprops= dict(facecolor= 'black', shrink=0.05), horizontalalignment='left', verticalalignment='top', )

ax.set_ylim(-2,2)
plt.show()