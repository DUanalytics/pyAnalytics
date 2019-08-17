# -*- coding: utf-8 -*-
# Interfaces in the plots
#-----------------------------
#%
#library
import numpy as np
import matplotlib.pyplot as plt


x = np.linspace(0, 10, 100)
fig = plt.figure()  #plot Figure

#MATLAB interface
#create 1st panel
#(row, column, panel)
plt.subplot(2, 1, 1)
plt.plot(x, np.sin(x))
#create 2nd panel
#(row, column, panel)
plt.subplot(2, 1, 2)
plt.plot(x, np.cos(x))

#%%%
#how to add something into the first one, overlap
#first create grid of plots
fig1, ax1 = plt.subplots(2)
#call plot() method on the appropriate object
ax1[0].plot(x, np.sin(x))
ax1[1].plot(x, np.cos(x))

# switching between
plt.plot() and ax.plot() 
#for best visualisation
