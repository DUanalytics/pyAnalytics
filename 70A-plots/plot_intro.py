#Plot introduction
#-----------------------------
#%
#https://realpython.com/python-matplotlib-guide/#a-burst-of-color-imshow-and-matshow

import matplotlib.pyplot as plt
[attr for attr in dir(plt) if attr.startswith('rc')]

#plt.rcdefaults() restores the rc parameters from matplotlib’s internal defaults, which are listed at plt.rcParamsDefault. This will revert (overwrite) whatever you’ve already customized in a matplotlibrc file.
#plt.rc() is used for setting parameters interactively.
#plt.rcParams is a (mutable) dictionary-like object that lets you manipulate settings directly. If you have customized settings in a matplotlibrc file, these will be reflected in this dictionary.

#With plt.rc() and plt.rcParams, these two syntaxes are equivalent for adjusting settings:

plt.rc('lines', linewidth=2, color='r')  # Syntax 1

plt.rcParams['lines.linewidth'] = 2  # Syntax 2
plt.rcParams['lines.color'] = 'r'

plt.style.available

plt.style.use('fivethirtyeight')


#subplots
fig, ax = plt.subplots()

# run these lines together
fig, ax = plt.subplots(nrows=1,ncols=1,figsize=(5, 3))
ax.bar(height=[10,20,15],x=['A','B','C'])
ax.set_title('Title')
ax.legend(loc='upper left')
ax.set_ylabel('Y Label')
ax.set_xlabel('X Label')
ax.set_ylim(ymin=0, ymax=30)
ax.annotate(10, (0,10))
ax.annotate(20, (1,20))
ax.annotate(15, (2,15))
plt.gca().set_title('Main title')
fig.tight_layout()
plt.show();

#multiple plots - add realtime
fig, ax = plt.subplots(figsize=(8, 4))
plt.subplot(1,2,1)
plt.bar(height=[10,20,15],x=['A','B','C'])
plt.title('Title-1')
plt.subplot(1,2,2)
plt.title('Title2')
plt.bar(height=[10,20,15],x=['A','B','C'])
plt.show();
#
x=[1,2,3]; y=[4,5,6]
fig = plt.figure()
plt.subplot(2, 2, 1)
plt.plot(x, y)
plt.subplot(2, 2, 2)
plt.plot(x, y)
plt.subplot(2, 2, 3)
plt.plot(x, y)
plt.subplot(2, 2, 4)
plt.plot(x, y)
plt.show();

#%%%
import matplotlib.pyplot as plt
x = range(10)
y = range(10)
dir(fig); dir(ax)
#
fig, ax = plt.subplots(nrows=2, ncols=2)
for row in ax:
    for col in row:       col.plot(x, y)
plt.show();

#plan before
fig, ax = plt.subplots(nrows=2,ncols=2,figsize=(8, 4))
ax[0, 0].plot(range(10), 'r') #row=0, col=0
ax[0, 0].title.set_text('1 Plot')
ax[1, 0].plot(range(10), 'b') #row=1, col=0
ax[1, 0].title.set_text('2 Plot')

ax[0, 1].plot(range(10), 'g') #row=0, col=1
ax[0, 1].title.set_text('3 Plot')

ax[1, 1].plot(range(10), 'k') #row=1, col=1
ax[1, 1].title.set_text('4 Plot')

plt.show()
#ax.title.set_text('My Plot Title')

#-------
import matplotlib.pyplot as plt
fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, sharex=True, sharey=True)
fig.suptitle('Main title') # or plt.suptitle('Main title')
ax1.plot(range(10), 'r')
ax2.plot(range(10), 'b')
ax3.plot(range(10), 'g')
ax4.plot(range(10), 'k')
plt.show()

#
data = [1, 2, 3, 4, 5]
fig = plt.figure()
fig.suptitle(".........Title for whole figure", fontsize=16)
ax = plt.subplot("211")
ax.set_title("1 Plot")
ax.plot(data)
ax = plt.subplot("212")
ax.set_title("2 Plot")
ax.plot(data)
plt.show()
    
#------------    
#import matplotlib.pyplot as plt
for i in range(4):
    plt.subplot(2,2,i+1).set_title('Subplot n°{}' .format(i+1))
plt.show()

#
import matplotlib.pyplot as plt
import numpy as np

fig=plt.figure()
data=np.arange(900).reshape((30,30))
for i in range(1,5):
    ax=fig.add_subplot(2,2,i)        
    ax.imshow(data)

fig.suptitle('Main title') # or plt.suptitle('Main title')
plt.show()

#When using fig.tight_layout() the title must be shifted with fig.subplots_adjust(top=0.88)


#%%
import numpy as np

# Simple data to display in various forms
x = np.linspace(0, 2 * np.pi, 400)
y = np.sin(x ** 2)

fig, axarr = plt.subplots(2, 2, figsize=(12,4))
fig.suptitle("This Main Title is Nicely Formatted", fontsize=16)
#plt.suptitle("Main Title", size=16)
axarr[0, 0].plot(x, y)
axarr[0, 0].set_title('Axis [0,0] Subtitle')
axarr[0, 1].scatter(x, y)
axarr[0, 1].set_title('Axis [0,1] Subtitle')
axarr[1, 0].plot(x, y ** 2)
axarr[1, 0].set_title('Axis [1,0] Subtitle')
axarr[1, 1].scatter(x, y ** 2)
axarr[1, 1].set_title('Axis [1,1] Subtitle')

# # Fine-tune figure; hide x ticks for top plots and y ticks for right plots
plt.setp([a.get_xticklabels() for a in axarr[0, :]], visible=False)
plt.setp([a.get_yticklabels() for a in axarr[:, 1]], visible=False)

# Tight layout often produces nice results
# but requires the title to be spaced accordingly
fig.tight_layout()
fig.subplots_adjust(top=0.7)

plt.show()

#
# The number of rows in the final figure # The number of columns in the final figure # Which axis (subplot) to use, counting from the one top-left axis
#ax = fig.add_subplot(211)
#
import matplotlib.pyplot as plt
#from mpl_toolkits.basemap import Basemap

fig, ax = plt.subplots(2, 1)
ax[0].set_title("Plot1")
ax[0].plot(range(10), 'r')
ax[1].set_title("Plot2")
ax[1].plot(range(10), 'g')
plt.show()

#
#When the number of subplots is bigger, or the subplots must have different sizes, subplot2grid or gridspec can be used. Here is an example with subplor2grid:
import matplotlib.pyplot as plt
#from mpl_toolkits.basemap import Basemap
import matplotlib.patches as patches

fig = plt.figure()

ax1 = plt.subplot2grid((2,2), (0,0))
ax2 = plt.subplot2grid((2,2), (1,0))
ax3 = plt.subplot2grid((2,2), (0,1), rowspan=2)
ax.plot(range(10), 'r', ax=ax1)


#

fig = plt.figure()
ax1 = fig.add_subplot(211)
ax2 = fig.add_subplot(212)
ax1.plot(range(10), 'r')
ax2.plot(range(10), 'g')
ax1.set_title('ax1 title')
ax2.set_title('ax2 title')
plt.show()




#Example PLot - function
def example_plot(ax, fontsize=12):
     ax.plot([1, 2])
     ax.locator_params(nbins=3)
     ax.set_xlabel('x-label', fontsize=fontsize)
     ax.set_ylabel('y-label', fontsize=fontsize)
     ax.set_title('Title', fontsize=fontsize)
fig, ax = plt.subplots()
example_plot(ax, fontsize=24)

#
fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(nrows=2, ncols=2)
example_plot(ax1)
example_plot(ax2)
example_plot(ax3)
example_plot(ax4)
#plt.tight_layout()
plt.tight_layout(pad=0.4, w_pad=0.5, h_pad=1.0)

#
fig = plt.figure()
ax1 = plt.subplot(221)
ax2 = plt.subplot(223)
ax3 = plt.subplot(122)
example_plot(ax1)
example_plot(ax2)
example_plot(ax3)

plt.tight_layout()

#---
fig = plt.figure()
ax1 = plt.subplot2grid((3, 3), (0, 0))
ax2 = plt.subplot2grid((3, 3), (0, 1), colspan=2)
ax3 = plt.subplot2grid((3, 3), (1, 0), colspan=2, rowspan=2)
ax4 = plt.subplot2grid((3, 3), (1, 2), rowspan=2)

example_plot(ax1)
example_plot(ax2)
example_plot(ax3)
example_plot(ax4)

plt.tight_layout()

#
arr = np.arange(100).reshape((10,10))

plt.close('all')
fig = plt.figure(figsize=(5,4))

ax = plt.subplot(111)
im = ax.imshow(arr, interpolation="none")

plt.tight_layout()
#

plt.close('all')
fig = plt.figure()
import matplotlib.gridspec as gridspec
gs1 = gridspec.GridSpec(2, 1)
ax1 = fig.add_subplot(gs1[0])
ax2 = fig.add_subplot(gs1[1])
example_plot(ax1)
example_plot(ax2)
#gs1.tight_layout(fig)
gs1.tight_layout(fig, rect=[0, 0, 0.5, 1])

#---
fig = plt.figure()
from mpl_toolkits.axes_grid1 import Grid
grid = Grid(fig, rect=111, nrows_ncols=(2,2),  axes_pad=0.25, label_mode='L',)

for ax in grid:
    example_plot(ax)
    ax.title.set_visible(False)

plt.tight_layout()

#https://matplotlib.org/users/tight_layout_guide.html

