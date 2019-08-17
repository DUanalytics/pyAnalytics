#index ing python pandas

#single index
import pandas as pd
import numpy as np

#df = pd.read_csv('data/mtcars.csv')
from pydataset import data
mtcars = data('mtcars')
mtcars.head()
df = mtcars
df.head()
df.columns
df.describe
df.dtypes
#convert selected columns to category
df.columns
catcolumns1 = ['cyl', 'vs', 'am', 'gear', 'carb']
catcolumns1

#%%
#create index with carname ; first keep a column with names also
df['car'] = df.carname
df = df.set_index('carname')
df

df[catcolumns1] = df[catcolumns1].astype('category')
df.dtypes

df.describe()
df[catcolumns1].describe()
df.columns

df.describe(include='all')


df.index

#multiple index
from pydataset import data
mtcars = data('mtcars')
df2 = mtcars.reset_index(drop=False)
#carnames move as columns, integer indexing
df2.head()
df2.columns
df2.rename({'index':'carnames'}, inplace=True)
df2.dtypes
df2.index # 0 to 32 with gap of 1 : 0 to 31

#access with index number
df2.loc[1]
df2.loc[0:2]
#first level of index, cyl
df3a = df2.set_index('cyl')
df3a
df3a.index

#two levels of index
df3b = df2.set_index(['cyl','gear'])
df3b.head()
df3b.index

#Three levels of index
df3c = df2.set_index(['cyl','gear','am'])
df3c.head()
df3c.index
#we can keep increasing the index levels

#%%%
#grouping using Index
df2.head()
df2.groupby(['cyl','am'])['wt'].mean()

df3a.groupby(['cyl','am'])['wt'].mean()
df3b.groupby(['cyl','am'])['wt'].mean()
df3c.groupby(['cyl','am'])['wt'].mean()

#unstack it : grouping based in on index columns
df3a.head()
df3a.groupby(['carb'])['wt'].mean().unstack()
#error - remove unused levels - single 
df3b.head()
df3b.groupby(['cyl','gear'])['wt'].mean().unstack()
df3c.head()
df3c.groupby(['cyl','gear','am'])['wt'].mean().unstack()

df3c.index

#understand what is index
#it is like rollno, 
#it can be multiple level: rollno, gender,

df
df.reset_index()
df.drop(columns='mpg')
df2.drop(axis=1, index=1)


#aggr wrt index 
df2.head()
df2.rename({'index':'cars'}, axis='columns', inplace=True)
df2.head()

df2index1 = df2.set_index(['gear','cyl'])
df2index1
df2index1.mpg.mean(level='gear')
df2index1.mpg.mean(level=[0,1])
df2index1.mpg.mean(level=[1,0])
df2.head()
df2[['mpg','disp']].mean(axis=1)
#32 rows, row means of mpg and disp
df2[['mpg','disp']].mean(axis=0)
#2 columns, their means