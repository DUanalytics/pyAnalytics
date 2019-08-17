#KDE - Distribution - Matplotlib
##-----------------------------
#%
#mtcars data
from pydataset import data
mtcars = data('mtcars')
mtcars.head()

mtcars.dtypes
#which are continuous variables
mtcars[['mpg','wt','hp','disp']]. head()

import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

sns.distplot(mtcars.mpg)

#other options
sns.distplot(mtcars.mpg, hist=False)
sns.distplot(mtcars.mpg, hist=True, kde=False)
sns.distplot(mtcars.mpg, hist=True, kde=True,  bins=4, color = 'darkblue',  hist_kws={'edgecolor':'black'},   kde_kws={'linewidth': 4}, rug_kws={'color': 'red'}, rug=True)

plt.hist(mtcars.wt, bins=10))

plt.hist(np.histogram(mtcars.wt, bins=10))
