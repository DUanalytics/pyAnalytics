#Bubble Chart - Such a chart is a scatter plot with an extra dimension, which makes it apparently 3-dimensional. This means larger bubbles denotes higher values. 
#-----------------------------
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd

x=np.random.rand(30)
y=np.random.rand(30)
z=np.random.rand(50)
z

plt.scatter(x,y,s=z*777) #s is for global size
plt.show();

#Setting bubble color
plt.scatter(x,y,s=z*777,c='Chartreuse') ; plt.show()

#assign random colors to different bubbles chart in Python.
colors=np.random.rand(30)
colors
plt.scatter(x,y,s=z*777,c=colors,alpha=0.5) ; plt.show();
#alpha for transparency

#%%%
#Setting bubble shape
plt.scatter(x,y,s=z*3001,marker='D') ; plt.show();

plt.scatter(x,y,s=z*3001,marker='<',color='brown') ; plt.show();

plt.scatter(x,y,s=z*3001,marker='*',color='pink'); plt.show();

plt.scatter(x,y,s=z*3001,marker='8',color='lavender') ; plt.show();

#Setting the edges for your Python bubbles charts
plt.scatter(x,y,s=z*4000,c='beige', alpha=0.4,linewidth=7) ; plt.show();

plt.scatter(x,y,s=z*4000, c='beige', linewidth=7,edgecolors='brown') ; plt.show();

#Mapping a color to a plot

plt.scatter(x,y,s=z*2000,c=x,cmap='Greys',alpha=0.4,edgecolors='green',linewidth=2) ;  plt.show()

#https://medium.com/@rinu.gour123/python-charts-bubble-3d-charts-with-properties-of-chart-574baae59080
#Python 3D Charts
