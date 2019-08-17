# -*- coding: utf-8 -*-
#Matplot -Line Plot
#-----------------------------
#%

#library

import matplotlib.pyplot as plt
import numpy as np

#Line-1
plt.plot([1,2,3,4])
plt.ylabel('Some Numbers')
plt.show()

#Line-2
plt.style.use('seaborn-whitegrid')
x = np.linspace(0, 10, 100)

#create a figure
fig = plt.figure()
#The whole figure is regarded as the figure object. It is necessary to explicitly use plt.figure() when we want to tweak the size of the figure and when we want to add multiple Axes objects in a single figure.

#Method-1
ax = plt.axes()
ax.plot(x, np.sin(x))

#Method-2
plt.plot(x, np.sin(x))

#Method-3 : combined
plt.plot(x, np.sin(x))
plt.plot(x, np.cos(x))


#Adjusting Axes Limits


#Changing Color of lines

#Axis Labels


#Legend
