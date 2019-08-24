#Topic: MPL - grid
#-----------------------------
#libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pydataset import data
mtcars = data('mtcars')
mtcars.head()
df = mtcars
#%%
fig, ax = plt.subplots()
df.plot(kind='scatter', x='wt', y='mpg', ax=ax)
ax.grid() # Turn on the grid
plt.show()

#%%
#Cutomising Grid
fig, ax = plt.subplots()
df.plot(kind='scatter', x='wt', y='mpg', ax=ax)
# Don't allow the axis to be on top of your data
ax.set_axisbelow(True)
# Customize the grid
ax.grid(linestyle='-', linewidth='0.5', color='red')


#%%%Render with a larger grid (major grid) and a smaller grid (minor grid)
fig, ax = plt.subplots()
df.plot(kind='scatter', x='wt', y='mpg', ax=ax)
# Don't allow the axis to be on top of your data
ax.set_axisbelow(True)
# Turn on the minor TICKS, which are required for the minor GRID
ax.minorticks_on()
#custom labels
plt.tick_params(labelsize = 10)
plt.xticks((0,1,2,3,4), ("0kg", "0.5", "1", '3', '4'))
plt.yticks((0,10,20,30), ("0MPG", "10", "20",'30'))
# Customize the major grid
ax.grid(which='major', linestyle='-', linewidth='0.5', color='red')
# Customize the minor grid
ax.grid(which='minor', linestyle=':', linewidth='0.5', color='black')
plt.tick_params(axis='x', which='both',bottom=False, top=True, labelbottom=False)
plt.show();


#%%%Turn on the grid but turn off ticks

fig, ax = plt.subplots()
df.plot(kind='scatter', x='wt', y='mpg', ax=ax)
ax.set_axisbelow(True)
ax.minorticks_on()
ax.grid(which='major', linestyle='-', linewidth='0.5', color='red')
ax.grid(which='minor', linestyle=':', linewidth='0.5', color='black')
# Turn off the display of all ticks.
#ax.tick_params(which='both',top=True, left=True, right=True, bottom=True)
plt.tick_params(axis='x', which='both',
bottom=True, top=False, labelbottom=True)
plt.savefig('graphs/fig1.png', bbox_inches='tight')
plt.show();

plt.savefig('graphs/fig1.png', bbox_inches='tight')