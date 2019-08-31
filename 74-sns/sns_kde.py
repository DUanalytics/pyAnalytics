#Joint Plot - sns
#-----------------------------
#%

#mtcars
from pydataset import data
mtcars = data('mtcars')
mtcars.head()

import seaborn as sns

# Joint Distribution Plot
sns.kdeplot(x='wt', y='mpg', data=mtcars)  #error, 
#needs actual series

# Density Plot
sns.kdeplot(mtcars.wt, mtcars.mpg)
