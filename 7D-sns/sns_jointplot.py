#Joint Plot - sns
#-----------------------------
#%

#mtcars
from pydataset import data
mtcars = data('mtcars')
mtcars.head()

import seaborn as sns

# Joint Distribution Plot
sns.jointplot(x='wt', y='mpg', data=mtcars)
