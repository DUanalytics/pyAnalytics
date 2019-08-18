# -*- coding: utf-8 -*-
#Matplot - Scatter Plot
#-----------------------------
#%
import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(0, 10, 100)
y = np.sin(x)
x
y

#plot

plt.scatter(x, y)
plt.plot(x,y)  #this is faster is customisation is not required
plt.scatter(x, y, color='r')
plt.scatter(x, y, c='r' , marker='o')
plt.scatter?
size = (30 * np.random.rand(100))**2
plt.scatter(x, y, c='r' , marker='o', s=size)

#matplotlib.pyplot.scatter(x, y, s=None, c=None, marker=None, cmap=None, norm=None, vmin=None, vmax=None, alpha=None, linewidths=None, verts=None, edgecolors=None, *, plotnonfinite=False, data=None, **kwargs)

#https://matplotlib.org/3.1.0/api/_as_gen/matplotlib.pyplot.scatter.html



#eg2
import matplotlib.pyplot
import pylab

x = [1,2,3,4]
y = [3,4,8,6]
size = (30 * np.random.rand(4))**2
matplotlib.pyplot.scatter(x,y, s=size)
matplotlib.pyplot.show()