#Filling Missing Values
#-----------------------------
#%

import pandas as pd
import numpy as np
#
sleep1= pd.read_csv('data/sleep.csv')
sleep= sleep1.copy()
sleep.head()

sleep.isnull().sum(axis=0)
sleep.isnull().sum(axis=1)
sleep.iloc[:,0:5].isnull().sum(axis=1) #specific columns

#random replace values
sleep.isna().sum()
sleep.isna().sum().sum()
#38 missing in total

sleep.head()

#complete cases - rows
sleep.dropna(axis=0)

#complete columns
sleep.dropna(axis=1)

#random filling
import random
sleep.columns
sleep = sleep1.copy()
sleep.isna().sum()
colNA = 'NonD'
sleep[colNA].isna().sum()
#full columns filled with random value
sleep[colNA] = sleep[colNA].apply(lambda v: random.random() * 1000)
sleep[colNA].isna().sum()
sleep.head(10)
sleep1.head(10)

#
import random
sleep.head(10)
sleep1.head(10)
sleep.fillna(random.random()).head(10)
#all filled with 1 random value

sleep = sleep1.copy()


#fill with mean or median value of DF
sleep.fillna(sleep.median(), inplace=False).head(10)
sleep.fillna(sleep.mean(), inplace=False).head(10)
#column specific
sleep['NonD'].fillna(sleep['NonD'].mean(), inplace=False)

#each column with its own mean of column
sleep.apply(lambda x: x.fillna(x.mean(), inplace=False),axis=0).head(10)
#NonD - 8.67, Dream-1.97

sleep.groupby(sleep.columns, axis = 1).transform(lambda x: x.fillna(x.mean(), inplace=False)).head(10)
#NonD - 8.67, Dream-1.97

#forward
sleep.fillna(method='ffill', inplace=False).head(10)
sleep.fillna(method='bfill', inplace=False).head(10)
sleep.fillna(method='bfill', inplace=False).tail(10) #backfill =bfill
sleep.fillna(method='pad', inplace=False).head(10) #pad and ffill are same
sleep.fillna(method='ffill', axis=1, inplace=False).head(10)
sleep.fillna(method='ffill', axis=0, inplace=False).head(10)
sleep.fillna(method='bfill', axis=0, inplace=False).head(10)
sleep.fillna(method='bfill', axis=1, inplace=False).head(10)
#limit ??



#------------
#Taking care of missing data
from sklearn.preprocessing import Imputer
imputer = Imputer(missing_values = 'NaN', strategy = 'mean', axis = 0)
imputer = imputer.fit(sleep[:, ])
X[:, 1:3] = imputer.transform(X[:, 1:3])
