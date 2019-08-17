# -*- coding: utf-8 -*-
#Created on Mon Jun 24 17:47:13 2019 : dhiraj@sony

#mtcars
from pydataset import data
mtcars = data('mtcars')
mtcars.head()

import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt

mtcars.gear.value_counts().plot(kind='bar')
#only 1 dimen

#Part-1 : nothing to show 
g = sb.FacetGrid(mtcars, col='am')
plt.show()  #2 am types
#2 plots

g = sb.FacetGrid(mtcars, col='gear')
plt.show()  #3 gear types
#that means, Facets are created as per types of gear or am

#Part 2 : 
g = sb.FacetGrid(mtcars, col='am')
g.map(plt.hist, 'mpg')  #histogram of mpg
plt.show()
#histogram of mpg as types of am

g = sb.FacetGrid(mtcars, col='gear')
g.map(plt.hist, 'mpg')  #histogram of mpg
plt.show()
#histogram as per types of gear

g = sb.FacetGrid(mtcars, col='gear')
g.map(plt.hist, 'cyl')  #
plt.show() #not working...
#cyl should be category and plot should be bar
mtcars['cyl'] = mtcars['cyl'].astype('category')
#This does not work - use Factor plots


#now it is working
g = sb.FacetGrid(mtcars, col='gear')
g.map(plt.scatter, 'wt', 'mpg')  #
plt.show() #now working...
#not quite right

#mtcars.groupby(['gear','cyl']).size().unstack()


#
g = sb.FacetGrid(mtcars, col='gear')
g.map(plt.scatter, 'wt', 'mpg')  #scatter
plt.show()
