#Matlop - Practise Exercise - Good
#-----------------------------
#%
#https://www.machinelearningplus.com/plots/matplotlib-tutorial-complete-guide-python-plot-examples/
import matplotlib.pyplot as plt
#%matplotlib inline
#%matplotlib inline is a jupyter notebook specific command that let’s you see the plots in the notebook itself.
#ou want to draw a specific type of plot, say a scatterplot, the first thing you want to check out are the methods under plt (type plt and hit tab or type dir(plt) in python prompt).

# Plot
plt.plot([1,2,3,4,10])
#drew a line chart automatically. It assumed the values of the X-axis to start from zero going up to as many items in the data.
#Matplotlib returns the plot object itself besides drawing the plot
#If you only want to see the plot, add plt.show() at the end and execute all the lines in one shot.
#notice instead of the intended scatter plot, plt.plot drew a line plot. That’s because of the default behaviour.
#plt.plot accepts 3 basic arguments in the following order: (x, y, format)
#This format is a short hand combination of {color}{marker}{line}
#example, the format 'go-' has 3 characters standing for: ‘green colored dots with solid line’. By omitting the line part (‘-‘) in the end, you will be left with only green dots (‘go’), which makes it draw a scatterplot.
#Few commonly used short hand format examples are:
#* 'r*--' : ‘red stars with dashed lines’
#* 'ks.' : ‘black squares with dotted line’ (‘k’ stands for black)
#* 'bD-.' : ‘blue diamonds with dash-dot line’.
#For a complete list of colors, markers and linestyles, check out the help(plt.plot) command.

# 'go' stands for green dots
plt.plot([1,2,3,4,5], [1,2,3,4,10], 'go')
plt.show()

#How to draw two sets of scatterplots in same plot
# Draw two sets of points
plt.plot([1,2,3,4,5], [1,2,3,4,10], 'go')  # green dots
plt.plot([1,2,3,4,5], [2,3,4,5,11], 'b*')  # blue stars
plt.show()
#plt object has corresponding methods to add each of this.
plt.plot([1,2,3,4,5], [1,2,3,4,10], 'go', label='GreenDots')
plt.plot([1,2,3,4,5], [2,3,4,5,11], 'b*', label='Bluestars')
plt.title('A Simple Scatterplot')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend(loc='best')  # legend text comes from the plot's label parameter.
plt.show()

#how to increase the size of the plot? (The above plot would actually look small on a jupyter notebook) The easy way to do it is by setting the figsize inside plt.figure() method.

plt.figure(figsize=(10,7)) # 10 is width, 7 is height
plt.plot([1,2,3,4,5], [1,2,3,4,10], 'go', label='GreenDots')  # green dots
plt.plot([1,2,3,4,5], [2,3,4,5,11], 'b*', label='Bluestars')  # blue stars
plt.title('A Simple Scatterplot')  
plt.xlabel('X')
plt.ylabel('Y')
plt.xlim(0, 6)
plt.ylim(0, 12)
plt.legend(loc='best')
plt.show()

#every plot that matplotlib makes is drawn on something called 'figure'. You can think of the figure object as a canvas that holds all the subplots and other plot elements inside it.
#And a figure can have one or more subplots inside it called axes, arranged in rows and columns. Every figure has atleast one axes. (Don’t confuse this axes with X and Y axis, they are different.)

#%%
#How to draw 2 scatterplots in different panels
#understand figure and axes in little more detail.
#Suppose, I want to draw our two sets of points (green rounds and blue stars) in two separate plots side-by-side instead of the same plot. How would you do that?
#You can do that by creating two separate subplots, aka, axes using plt.subplots(1, 2). This creates and returns two objects:
#* the figure
#* the axes (subplots) inside the figure
#https://www.machinelearningplus.com/wp-content/uploads/2019/01/99_matplotlib_structure-1-297x300.png
#Previously, we called plt.plot() to draw the points. Since there was only one axes by default, it drew the points on that axes itself.
#But now, since you want the points drawn on different subplots (axes), you have to call the plot function in the respective axes (ax1 and ax2 in below code) instead of plt.
##Notice in below code, I call ax1.plot() and ax2.plot() instead of calling plt.plot() twice.

# Create Figure and Subplots
fig, (ax1, ax2) = plt.subplots(1,2, figsize=(10,4), sharey=True, dpi=120)
# Plot
ax1.plot([1,2,3,4,5], [1,2,3,4,10], 'go')  # greendots
ax2.plot([1,2,3,4,5], [2,3,4,5,11], 'b*')  # bluestart
# Title, X and Y labels, X and Y Lim
ax1.set_title('Scatterplot Greendots'); ax2.set_title('Scatterplot Bluestars')
ax1.set_xlabel('X');  ax2.set_xlabel('X')  # x label
ax1.set_ylabel('Y');  ax2.set_ylabel('Y')  # y label
ax1.set_xlim(0, 6) ;  ax2.set_xlim(0, 6)   # x axis limits
ax1.set_ylim(0, 12);  ax2.set_ylim(0, 12)  # y axis limits
# ax2.yaxis.set_ticks_position('none') 
plt.tight_layout()
plt.show()

#Setting sharey=True in plt.subplots() shares the Y axis between the two subplots.
#And dpi=120 increased the number of dots per inch of the plot to make it look more sharp and clear. You will notice a distinct improvement in clarity on increasing the dpi especially in jupyter notebooks.
#Thats sounds like a lot of functions to learn. Well it’s quite easy to remember it actually.
#The ax1 and ax2 objects, like plt, has equivalent set_title, set_xlabel and set_ylabel functions. Infact, the plt.title() actually calls the current axes set_title() to do the job.
#plt.xlabel() → ax.set_xlabel()
#plt.ylabel() → ax.set_ylabel()
#plt.xlim() → ax.set_xlim()
#plt.ylim() → ax.set_ylim()
#plt.title() → ax.set_title()
#Alternately, to save keystrokes, you can set multiple things in one go using the ax.set()
ax1.set(title='Scatterplot Greendots', xlabel='X', ylabel='Y', xlim=(0,6), ylim=(0,12))
ax2.set(title='Scatterplot Bluestars', xlabel='X', ylabel='Y', xlim=(0,6), ylim=(0,12))