#Seaborn
#-----------------------------
#%

import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd

from pydataset import data
mtcars = data('mtcars')
mtcars.head()

#histogram
for col in ['mpg','wt']:
    plt.hist(mtcars[col], normed = True, alpha=0.5)

for col in ['mpg','wt']:
    sns.distplot(mtcars[col])
    
#kde
for col in ['mpg','wt']:   sns.kdeplot(mtcars[col])

#combined
plt.scatter(mtcars.wt, mtcars.mpg)
with sns.axes_style('white'):
    sns.jointplot('mpg', 'wt', mtcars, kind='kde')

with sns.axes_style('white'):
    sns.jointplot('mpg', 'wt', mtcars, kind='hex')

#pair plot
sns.pairplot(mtcars[['mpg', 'wt','hp','cyl']], hue='cyl', size=2.5)

#facet 
grid = sns.FacetGrid(mtcars[['mpg', 'wt','hp','am','cyl', 'gear']], row='cyl', col='gear')
grid.map(plt.bar, 'am')
#not working; needs height


#facet - 
#factor plot
