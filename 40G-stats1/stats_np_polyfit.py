#
#-----------------------------
#%
#Poly Fit

import numpy as np
import matplotlib.pyplot as plt

x = [i for i in range(11)]
x  #list
np.arange(0,11)  #np array

y = [i for i in range(0,21,2)]
y

x,y
slope, intercept = np.polyfit(x,y,1)
#degree of line 
slope
intercept
intercept.round(0)
plt.plot(x,y)

predY = [ i * slope + intercept for i in range(11)]
predY
plt.plot(x, predY)

#plot them together
plt.scatter(x,y)
plt.plot(x, predY)
plt.show()
