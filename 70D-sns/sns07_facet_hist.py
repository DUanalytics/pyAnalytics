#Facet Histogram
#-----------------------------
#%
import seaborn as sns
import numpy as np
import pandas as pd

np.random.seed(1234)
age  = np.random.randint(18,25, size=100)
np.mean(age)
len(age)

import collections
np.random.seed(1234)
gender = np.random.choice(['M','F'], size=100, replace=True, p=[.6,.4])
collections.Counter(gender)
gender.tolist().count('M')
pd.Series(gender).value_counts()
len(gender)

np.random.seed(1234)
course = np.random.choice(['BBA','MBA','PHD'], size=100, replace=True, p=[.5,.4,.1])
len(course)

data = pd.DataFrame({'age':age, 'gender':gender,'course':course})
data.head()

g = sns.FacetGrid(data, row='gender', col='course', size=4)
g.map(plt.hist, 'age', alpha=0.5, bins=15)
g.add_legend()
plt.show()

