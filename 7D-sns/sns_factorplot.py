#Factor Plot - sns
#-----------------------------
#%
#factorplot` function has been renamed to `catplot`. The original name will be removed in a future release. Please update your code. Note that the default `kind` in `factorplot` (`'point'`) has changed `'strip'` in `catplot`.
#mtcars
from pydataset import data
mtcars = data('mtcars')
mtcars.head()

import seaborn as sns
sns.set(rc={'figure.figsize':(3,2)})
# Factor Plot -separate plots by categorical classes
g=sns.factorplot(x='gear',  y='carb',  data=mtcars, hue='cyl', col='am',  kind ='swarm') 
# Color by am, # Separate by cyl # Swarmplot
# Rotate x-axis labels
g.set_xticklabels(rotation=-45)
 
# Doesn't work because only rotates last plot
# plt.xticks(rotation=-45)


g=sns.factorplot(x='gear',  y='carb',  data=mtcars, hue='cyl', col='am',  kind ='swarm', aspect=1/1, legend=True)
