# Facet Plot - configuration
#-----------------------------
#%

import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd

from pydataset import data
mtcars = data('mtcars')
mtcars.head()
x_min = mtcars['mpg'].min()
x_max = mtcars['mpg'].max()
border_pad = (x_max - x_min) * 5 / 100
#xlim=(x_min - border_pad, x_max + border_pad),
g = sns.FacetGrid(  mtcars, row='gear', hue='cyl', legend_out=True,  height=5, palette="Set1", xlim=(x_min - border_pad, x_max + border_pad)    )
g.map(plt.scatter, 'mpg', 'wt', s=5).add_legend()
plt.subplots_adjust(top=.9)
g.fig.suptitle('MTcars Analysis between {start} and  {end}'.format(start=x_min, end=x_max))
#g.savefig(output, format='png')
plt.savefig("mtcars1.png")  
plt.show()