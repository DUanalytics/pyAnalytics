# -*- coding: utf-8 -*-
#% Histogram , Class Interval

import pandas as pd
import numpy as np

#with numpy data
pd.cut(np.array([1,7,5,4,6,3,10]),bins=3)
#equal size bins
pd.cut(np.array([1,7,5,4,6,3,10]),bins=3, retbins=True) #retun bins
pd.cut(np.array([1,7,5,4,6,3,10]),bins=3, labels=['low','medium','high'])
pd.cut(np.array([1,7,5,4,6,3,10]),bins=3, labels=False) #only bins

#import data
df5 = pd.read_csv('data\mtcars.csv')
df5.head()
df5.columns

pd.cut(df5.mpg, bins=3)
pd.cut(df5.mpg, bins=3, labels=['low','medium','high'])
df5['mtype'] = pd.cut(df5.mpg, bins=3, labels=['low','medium','high'])
df5.mtype.value_counts()
df5.mtype.value_counts().plot(kind='bar')
df5.mtype.value_counts().plot(kind='barh')
df5.mtype.value_counts().plot(kind='pie')


#Histogram
df5.mpg.plot(kind='hist')
df5.mpg.agg(['min', 'max'])
bins = [0,10,20,30,40]
mtype = ['poor','average','good','excellent']
bins, mtype

#create bins 
df5.mpg.agg(['min', 'max'])
bins = [0,10,20,30,40]
mtype = ['poor','average','good','excellent']
bins, mtype
df5['mcat'] = pd.cut(df5['mpg'], bins, labels=mtype)
df5.mcat

df5.groupby(['mcat'])['hp'].apply(get_status).unstack()


#function 
def get_status(group):
    return {'min': group.min(), 'max':group.max()}

df