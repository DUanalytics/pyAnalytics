#Missing Data
#-----------------------------
#%Imputation

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sleep1 = pd.read_csv('sleep.csv')
sleep1.head()
sleep2 = pd.read_csv('https://raw.githubusercontent.com/dupadhyaya/sipPython/master/data/sleep.csv')
sleep2
sleep = sleep2.copy()

#select to drop the rows only if all of the values in the row are missing.
sleep.dropna(how='all',inplace=False).shape
sleep.isna().sum(axis=1)
sleep.isna().sum(axis=0)

#just want to drop a column (variable) that has some missing values.
sleep.head()
sleep.dropna(axis=1,inplace=False).head()                
sleep.dropna(axis=0,inplace=False).head()                
sleep.shape
#keep only the rows with at least 4 non-na values:
sleep.dropna(thresh=9, axis=0, inplace=False).shape
sleep.dropna(thresh=55, axis=1, inplace=False).shape
s1= np.int(.6 * len(sleep)) ; s1
#t1=55
len(sleep)
sleep.shape #using dynamically : not working
sleep.dropna(thresh= t1 , axis=1, inplace=False ).shape
#https://towardsdatascience.com/the-tale-of-missing-values-in-python-c96beb0e8a9d

#negative values
sleep.fillna(value=-99999,inplace=False).head()

list1 = sleep['NonD'].dropna()
list1
import numpy.random
#numpy.random.choice(a, size=None, replace=True, p=None)
#https://docs.scipy.org/doc/numpy/reference/generated/numpy.random.choice.html
np.random.choice(list1, 3, replace=False)
np.asscalar(np.random.choice(list1, 1, replace=False))

sleep['NonD'].fillna(value=np.asscalar(np.random.choice(list1, 1, replace=False)), inplace=False)

random_replace = np.vectorize(lambda x: np.random.randint(2) if np.isnan(x) else x)

sleep.head(10)
sleep5 = random_replace(sleep)
sleep5[1:5, 1:5]

nan_mask = np.isnan(sleep)
nan_mask
sleep.loc[[True, False,True],]
sleep[nan_mask] = np.random.randint(0, 2, size=np.count_nonzero(nan_mask) )
np.count_nonzero( np.isnan(sleep))
np.count_nonzero(np.isnan(sleep))
size=np.count_nonzero(nan_mask)
size
#%%% not working
from sklearn.preprocessing import Imputer
imp = Imputer(missing_values='NaN', strategy='mean', axis=0)
imp.fit(train)
train= imp.transform(train)
