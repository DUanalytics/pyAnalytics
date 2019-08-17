#Histogram - Matplotlib
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
plt.hist(mtcars.mpg)

#other options
plt.hist(mtcars['mpg'], histtype='stepfilled', alpha=.4)
plt.hist(mtcars.wt, bins=10)
plt.hist(np.histogram(mtcars.wt, bins=10))
