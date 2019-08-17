#Save Figure
#-----------------------------
#%
from matplotlib import pyplot as plt
import seaborn as sns    

from pydataset import data
mtcars = data('mtcars')
mtcars.head()

fig, ax = plt.subplots()
# the size of A4 paper
fig.set_size_inches(5, 4)
sns.violinplot(data=mtcars[['mpg','wt']], inner="points", ax=ax)    
sns.despine()


fig.savefig('example.png')