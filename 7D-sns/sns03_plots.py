#Seaborn Plots
#-----------------------------
#%

import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd

#
from pydataset import data
mtcars = data('mtcars')
mtcars.head()
mtcars.columns
mtcars.dtypes
mtcars[['am','vs','gear','cyl']] = mtcars[['am','vs','gear','cyl']].astype('category')
mtcars.dtypes
mtcars.describe(include='all')

#Histogram using matplotlib plt
plt.hist(mtcars['mpg'])
plt.hist(mtcars[['mpg','wt']])  #error

for col in ['mpg','wt']:
    plt.hist(mtcars[col])

for col in ['mpg','wt']:
    plt.hist(mtcars[col], normed=True, alpha=0.5)

#Kernel Density - sns
for col in ['mpg','wt']:
    sns.kdeplot(mtcars[col], shade=True)

for col in ['mpg','wt']:
    sns.kdeplot(mtcars[col], cumulative=True, shade=True)

#Combining Histogram and KDE
sns.distplot(mtcars['mpg'])
sns.distplot(mtcars['wt'])
#one by one and together to se both plots
#sns.distplot(mtcars[['mpg','wt','hp','disp']], color =['r','g','b','y'])


#Joint Plot
sns.axes_style('white')
sns.jointplot('mpg','wt', mtcars, kind='kde')

#Hex
sns.jointplot('mpg','wt', mtcars, kind='hex')

#Pair 
sns.pairplot(mtcars[['mpg','wt']])
sns.pairplot(mtcars)


#Facet
grid = sns.FacetGrid(mtcars, row='gear', col='cyl', margin_titles=True)
grid.map(plt.hist, 'mpg', bins=np.linspace(0,35,5))

#Factor Plot
g= sns.factorplot('cyl', 'wt', hue='am', data=mtcars, kind='box')
g.set_axis_labels('Mileage', 'Weight')


#Joint Distributions
sns.jointplot('wt', 'mpg', data=mtcars)
sns.jointplot('wt', 'mpg', data=mtcars, kind='reg')


#Bar Plots
g = sns.factorplot(x='mpg', y=None, data=mtcars, aspect=1, kind='count', color='blue')
g.set_xticklabels(step=5)
#with cat colomn
g = sns.factorplot(x='cyl', y=None, data=mtcars, aspect=1, kind='count', color='blue')
#g.set_xticklabels(step=1)# not reqd here