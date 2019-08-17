#Facet - Histogram, box plot
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
g = sns.FacetGrid(mtcars, col="cyl")
g.map(plt.hist, "mpg");

#-----------
g = sns.FacetGrid(mtcars, row='am', col="cyl")
g.map(plt.hist, "mpg");
#---
g = sns.FacetGrid(mtcars, row='am', col="cyl", hue='vs')
g.map(plt.hist, "mpg");


g = sns.FacetGrid(mtcars)
g.map(sns.violinplot, "mpg");

g = sns.FacetGrid(mtcars, col="cyl")
g.map(sns.violinplot, "mpg");

g = sns.FacetGrid(mtcars, col="am")
g.map(sns.violinplot, "wt");
g.add_legend()

grid = sns.FacetGrid(mtcars[['mpg', 'wt','hp','am','cyl', 'gear']], row='cyl', col='gear', hue='cyl')
grid.map(plt.hist,'wt')
#g.add_legend()
g.add_legend(title='LEGEND')
g.add_legend?
