#% Histogram , Class Interval
#egs from mtcars

import pandas as pd
import numpy as np

#with numpy data
pd.cut(np.array([1,7,5,4,6,3,10]),bins=3)
#equal size bins
pd.cut(np.array([1,7,5,4,6,3,10]),bins=3, retbins=True) #return bins
pd.cut(np.array([1,7,5,4,6,3,10]),bins=3, labels=['low','medium','high'])
pd.cut(np.array([1,7,5,4,6,3,10]),bins=3, labels=False) #only bins

#import data
url='https://raw.githubusercontent.com/DUanalytics/datasets/master/csv/mtcars1.csv'
df = pd.read_csv(url)
df.head()
df.columns

pd.cut(df.mpg, bins=3)
pd.cut(df.mpg, bins=3, labels=['low','medium','high'])
df['mtype'] = pd.cut(df.mpg, bins=3, labels=['low','medium','high'])
df.mtype.value_counts()
df.mtype.value_counts().plot(kind='bar')
df.mtype.value_counts().plot(kind='barh')
df.mtype.value_counts().plot(kind='pie')


#Histogram
df.mpg.plot(kind='hist')
df.mpg.agg(['min', 'max'])  #find range
bins = [0,10,20,30,40]
mtype = ['poor','average','good','excellent']
bins, mtype

#create bins 
df.mpg.agg(['min', 'max'])
bins = [0,10,20,30,40]
mtype = ['poor','average','good','excellent']
bins, mtype
df['mcat'] = pd.cut(df['mpg'], bins, labels=mtype)
df.mcat
#function 
def get_status(group):   return {'min': group.min(), 'max':group.max()}

df.groupby(['mcat'])['hp'].apply(get_status).unstack()

df