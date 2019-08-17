# -*- coding: utf-8 -*-
##%
#Boxplots
# Boxplots are a measure of how well distributed the data in a data set is. It divides the data set into three quartiles. This graph represents the minimum, maximum, median, first quartile and third quartile in the data set. It is also useful in comparing the distribution of data across data sets by drawing boxplots for each of them.
# # Drawing a Box Plot
# Boxplot can be drawn calling Series.box.plot() and DataFrame.box.plot(), or DataFrame.boxplot() to visualize the distribution of values within each column.
# # For instance, here is a boxplot representing five trials of 10 observations of a uniform random variable on [0,1).
#

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.DataFrame(np.random.rand(10, 5), columns=['A', 'B', 'C', 'D', 'E'])
df.head()
#10 rows, 5 columns; continuous values
#this through pandas plot
df.plot.box(grid='True')

#matplot way
#https://matplotlib.org/3.1.0/api/_as_gen/matplotlib.pyplot.boxplot.html
matplotlib.pyplot.boxplot(x, notch=None, sym=None, vert=None, whis=None, positions=None, widths=None, patch_artist=None, bootstrap=None, usermedians=None, conf_intervals=None, meanline=None, showmeans=None, showcaps=None, showbox=None, showfliers=None, boxprops=None, labels=None, flierprops=None, medianprops=None, meanprops=None, capprops=None, whiskerprops=None, manage_ticks=True, autorange=False, zorder=None, *, data=None)
plt.boxplot(df.A)
# Run next 4 lines together
fig1, ax1 = plt.subplots()
ax1.set_title('Basic Plot')
df.columns
ax1.boxplot(df.A)

#with notch
plt.boxplot(df.A, notch=True)
#
fig2, ax2 = plt.subplots()
ax2.set_title('Box Plot with Notch')
df.columns
ax2.boxplot(df['B'], notch=True)

#with outliers color
green_diamond = dict(markerfacecolor='g', marker='D')
fig3, ax3 = plt.subplots()
ax3.set_title('Outlier Symbols')
ax3.boxplot(df['C'], flierprops=green_diamond)
#no outliers here.. we will take another eg
#outliers are above or below : Q1/Q3 -/+ IQR


#Hide outliers
fig4, ax4 = plt.subplots()
ax4.set_title('Hide Outlier Points')
ax4.boxplot(df['D'], showfliers=False)


#Horizontal Box Plot
red_square = dict(markerfacecolor='r', marker='s')
fig5, ax5 = plt.subplots()
ax5.set_title('Horizontal Boxes')
ax5.boxplot(df.B, vert=False, flierprops=red_square)

#changing the length of whiskers : comment and see
fig6, ax6 = plt.subplots()
ax6.set_title('Shorter Whisker Length')
ax6.boxplot(df.C, flierprops=red_square, vert=False, whis=0.15)
#ax6.boxplot(df.C, flierprops=red_square, vert=False, whis=1.25)

#multiple data columns
fig7, ax7 = plt.subplots()
ax7.set_title('Multiple Columns')
ax7.boxplot(df)
plt.show()



#more practise
#https://python-graph-gallery.com/boxplot/
