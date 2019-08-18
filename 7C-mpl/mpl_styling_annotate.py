# -*- coding: utf-8 -*-
#Matplot Styling
#-----------------------------
#Python - Chart Styling
#The charts created in python can have further styling by using some appropriate methods from the libraries used for charting. In this lesson we will see the implementation of Annotation, legends and chart background. 
#Adding Annotations - Many times, we need to annotate the chart by highlighting the specific locations of the chart. In the below example we indicate the sharp change in values in the chart by adding annotations at those points.

#libraries
import numpy as np 
#from matplotlib import pyplot as plt 
import matploylib.pyplot as plt

#generate data
x = np.arange(0,10) 
y = x ^ 2 
z = x ^ 3
t = x ^ 4 

#check 
x,y,z,t

# Labeling the Axes and Title : run next 4 lines together
plt.title("Graph Drawing") 
plt.xlabel("Time") 
plt.ylabel("Distance") 
plt.plot(x,y)

#Annotate - next 3 lines together
plt.annotate(xy=[2,1], s='Second Entry') 
plt.annotate(xy=[4,6], s='Third Entry') 
plt.plot(x,y)


#Adding Legends
#We sometimes need a chart with multiple lines being plotted. Use of legend represents the meaning associated with each line. In the below chart we have 3 lines with appropriate legends.

import numpy as np 
from matplotlib import pyplot as plt 

x = np.arange(0,10) 
y = x ^ 2 
z = x ^ 3
t = x ^ 4 

# Labeling the Axes and Title : run all these lines together
plt.title("Graph Drawing") 
plt.xlabel("Time") 
plt.ylabel("Distance") 
plt.annotate(xy=[2,1], s='Second Entry') 
plt.annotate(xy=[4,6], s='Third Entry') 
plt.plot(x,y)
plt.plot(x,z)
plt.plot(x,t)
plt.legend(['Race1', 'Race2','Race3'], loc=4) # Adding Legends


#Chart presentation Style
#We can modify the presentation style of the chart by using different methods from the style package.
plt.style.available  #available styles
#Style the background
plt.style.use('fast')
plt.plot(x,z)
#other styles
plt.style.use('classic')
plt.plot(x,z)
#
plt.style.use('bmh')
plt.plot(x,z)

#https://matplotlib.org/3.1.0/gallery/style_sheets/style_sheets_reference.html
plt.style.use('ggplot')
plt.plot(x,z)
#https://matplotlib.org/3.1.0/gallery/style_sheets/ggplot.html#sphx-glr-gallery-style-sheets-ggplot-py
plt.style.use('dark_background')
plt.plot(x,z)

#
plt.style.use('seaborn')
plt.plot(x,z)

#Presentation

plt.style.use('presentation')
plt.plot(x,z)

#you can define your style
#https://matplotlib.org/users/style_sheets.html#defining-your-own-style
