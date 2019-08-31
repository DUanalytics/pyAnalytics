# -*- coding: utf-8 -*-
#
#-----------------------------
#%
# -*- coding: utf-8 -*-

#Python has excellent libraries for data visualization. A combination of Pandas, numpy and matplotlib can help in creating in nearly all types of visualizations charts. In this chapter we will get started with looking at some simple chart and the various properties of the chart.
##Creating a Chart
#We use numpy library to create the required numbers to be mapped for creating the chart and the pyplot method in matplotlib to draws the actual chart.
#import libraries
import numpy as np 
import matplotlib.pyplot as plt 
#create sample data
x = np.arange(0,10) 
x
y = x ^ 2 
y
#Simple Plot
plt.plot(x,y)
#line plot by default for numerical values

#Labling the Axes: we can apply labels to the axes as well as a title for the chart using appropriate methods from the library as shown below.

import numpy as np 
import matplotlib.pyplot as plt 
#%%%
x = np.arange(0,10) 
y = x ^ 2 
x,y
#Labeling the Axes and Title
#run these 4 lines together
plt.title("Graph Drawing") 
plt.xlabel("Time") 
plt.ylabel("Distance") 
plt.plot(x,y)
#see label values: title, x&y label

