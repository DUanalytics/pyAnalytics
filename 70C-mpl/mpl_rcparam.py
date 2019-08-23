#MPL parameters
#-----------------------------
#%

import matplotlib.pyplot as plt
import numpy as np

dir(plt)
[attr for attr in dir(plt) if attr.startswith('rc')]

#
plt.rcdefaults()
#restores the rc parameters from matplotlib’s internal defaults, which are listed at plt.rcParamsDefault. This will revert (overwrite) whatever you’ve already customized in a matplotlibrc file.

plt.rc()
#is used for setting parameters interactively.

plt.rcParams
#is a (mutable) dictionary-like object that lets you manipulate settings directly. If you have customized settings in a matplotlibrc file, these will be reflected in this dictionary.

#
plt.rc('lines', linewidth=2, color='r')  # Syntax 1
plt.rcParams['lines.linewidth'] = 2  # Syntax 2
plt.rcParams['lines.color'] = 'r'

#With plt.rc() and plt.rcParams, these two syntaxes are equivalent for adjusting settings

#plt.style.available
plt.style.available

plt.style.use('fivethirtyeight')

#Interactive -interactive mode is off by default, you can check its status with 
plt.rcParams['interactive'] #or
plt.isinteractive() 
#,and toggle it on and off with plt.ion() and plt.ioff(), respectively:

plt.rcParams['interactive']  # or: plt.isinteractive()
plt.ioff()
plt.rcParams['interactive']

#https://realpython.com/python-matplotlib-guide/#why-can-matplotlib-be-confusing



#Interactive mode Off
plt.ioff()
#run together
x=np.arange(-4, 5)
y1 = x ** 2
y2 = 10 / (x ** 2 + 1)
fig, ax = plt.subplots()
ax.plot(x, y1, 'rx', x, y2, 'b+', linestyle='solid')
ax.fill_between(x, y1, y2, where=y2>y1, interpolate=True, color='green', alpha=0.3)
lgnd = ax.legend(['y1', 'y2'], loc='upper center', shadow=True)
lgnd.get_frame().set_facecolor('#ffb19a')
plt.show()

#
#Interactive mode On
plt.ion()
#run together
x=np.arange(-4, 5)
y1 = x ** 2
y2 = 10 / (x ** 2 + 1)
fig, ax = plt.subplots()
ax.plot(x, y1, 'rx', x, y2, 'b+', linestyle='solid')
ax.fill_between(x, y1, y2, where=y2>y1, interpolate=True, color='green', alpha=0.3)
lgnd = ax.legend(['y1', 'y2'], loc='upper center', shadow=True)
lgnd.get_frame().set_facecolor('#ffb19a')
#plt.show()  #commented

#Notably, interactive mode has nothing to do with what IDE you’re using, or whether you’ve enable inline plotting with something like jupyter notebook --matplotlib inline or %matplotlib.