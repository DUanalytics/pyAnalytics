#Mtcars - Muli Index
#-----------------------------
#% Multindex in Pandas DF
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pydataset import data
data('iris')
data('titanic')
#https://github.com/iamaziz/PyDataset/blob/master/examples/sample-datasets.ipynb
mtcars = data('mtcars')
mtcars.head()
#mtcars.to_csv('data/mcarsdataset.csv')
data1 = mtcars
#describe data
data1.columns  #col names
data1.values# values of DF
data1.index
data1.dtypes
data1[['am','vs','cyl','gear','carb']] = data1[['am','vs', 'cyl','gear', 'carb']].astype('category')
#data1[['am','vs', 'cyl','gear', 'carb']].astype('category', inplace=False)
data1.dtypes
data1.iloc[0:3,0:4]
#reset the index : index to column
data2 = data1.reset_index()
data2.iloc[0:3,0:4]

data2.columns
data2.rename({'index':'carname'},inplace=True, axis='columns')
#rename index column to carname : old to new
data2.head()
data2.columns
 #create a new index
#DataFrame.set_index(keys, drop=True, append=False, inplace=False, verify_integrity=False)
data2.columns
#to_clipboard(excel=True, sep=None, **kwargs)[source]
#cyl vs	am gear	carb
data3cyl = data2.set_index('cyl')
data3cyl.head() 
data2.cyl.value_counts()
data3cyl.loc[6,]
data3cyl.loc[4,]
data3cyl.loc[[4,6],]

data3cyl.iloc[4,]

#data3cyl.head().to_clipboard()
data3cyl.head()
data3cyl.columns
pd.set_option('display.max_columns',13)
data2.head()
data3 = data2.set_index('gear', drop=True).head()
data3.head()
data3.reset_index().set_index('cyl').head()
data3cyl.set_index('gear', append=True).set_index('am', append=True)


data3cyl.set_index('gear', drop=False).head().to_clipboard()
data3cyl.set_index('vs', drop=False).head()
data3cyl.set_index('vs', drop=False).head().to_clipboard()
data3cyl.set_index('am', drop=False).head()
data3cyl.set_index('am', drop=False).head().to_clipboard()
#keys: Column name or list of a column name.
#drop: It’s a Boolean value which drops the column used for the index if True.
#append: It appends the column to the existing index column if True.
#inplace: It makes the changes in the DataFrame if True.
#verify_integrity: It checks the new index column for duplicates if True.
#%%%
#query on index columns
data2.columns
data2.head()

#groupby : Mean mpg by gear
dataGg = data2.groupby(['gear']).mpg.mean()
#dataGg.to_clipboard()
dataGg
dataGg.index
type(dataGg)
dataGg[3]
#groupby 2 columns
dataGga = data2.groupby(['gear','am']).mpg.mean()
dataGga.index
#dataGga.to_clipboard()
dataGga

#groupby 3 columns
dataGgcc = data2.groupby(['gear','cyl','carb']).mpg.mean()
dataGgcc
dataGgcc.index
#dataGgcc.to_clipboard()


#Unstack after Group
dataGg
dataGg.unstack()  #will not work as it is Series not multi Index

dataGga
dataGga.unstack()

dataGgcc
dataGgcc.unstack()
dataGgcc.unstack().unstack()

#search with Groupby output
dataGgcc
dataGgcc.loc[3]  #gear3
dataGgcc.head() 
dataGgcc.loc[4]  #gear4
dataGgcc.loc[4,6]  #gear4, cyl6
dataGgcc.loc[4,4,1]  #gear4, cyl4, carb1


#sort index
dataGgcc
#dataGgcc.to_clipboard()
dataGgcc.sort_index()
#dataGgcc.sort_index().to_clipboard()
dataGgcc.sort_index(level=1)   #cyl
#dataGgcc.sort_index(level=1).to_clipboard()
dataGgcc.sort_index(level=2)  #carb
dataGgcc.sort_index(level=[2,1])  #carb then gear
#dataGgcc.sort_index(level=[2,0]).to_clipboard()
#https://www.geeksforgeeks.org/python-pandas-dataframe-sort_index/

#DataFrame.sort_index(axis=0, level=None, ascending=True, inplace=False, kind=’quicksort’, na_position=’last’, sort_remaining=True, by=None)

#Mutiple Aggregations
#group on different columns
data2.head()
data2.groupby(['gear', 'carb']).agg({'hp':np.sum, 'mpg':np.mean})
data2Ggchm = data2.groupby(['gear', 'carb']).agg({'hp':np.sum, 'mpg':np.mean})
data2Ggchm.head()
data2Ggchm.loc[3]  #1st index is Gear; 3rd Gear
data2Ggchm.loc[3,2]  #gear3, Carb2 : hp and mileage
data2Ggchm.loc[(3,2)]
data2Ggchm.loc[(3,2), :]
data2Ggchm.loc[(3,2), 'hp']
data2Ggchm.loc[(3,2), :'hp']

data2Ggchm
data2Ggchm.loc[([3,4], 2), ['hp','mpg']]  #Gear 3 and gear 4 with cyl2
data2Ggchm.loc[(5,[2,8]), ['hp','mpg']]  #Gear5, Carb2, carb8
#note round and square bracket


#Pivot Table
data1
data2  #use this
data2.columns
data2.pivot_table(index='gear', values='mpg', columns='cyl')
#default aggregation is mean
pd.pivot_table?
#table = pivot_table(df, values=['D', 'E'], index=['A', 'C'], aggfunc = {'D': np.mean,'E': [min, max, np.mean]})
data2.pivot_table(index)
#s orting DF
mtcars.sort_values(['mpg','hp']).head(10)
mtcars.sort_values(['mpg','hp','wt'], ascending=True).head(10)
mtcars[['gear','cyl','wt']].sort_values(['gear','cyl','wt'], ascending=[True, False, True])
mtcars.loc[mtcars['mpg'] > 25, ]
mtcars.loc[(mtcars['mpg'] > 25) & (mtcars['hp'] > 35 ) , ['mpg', 'hp']]
mtcars.loc[(mtcars['vs'] == 1) | (mtcars['am'] == 1 ) , ['mpg', 'hp','vs','am']].head(10)
mtcars.pivot_table(index='gear', values='mpg', columns='am')
mtcars.pivot_table(index=['gear','vs'], values='mpg', columns='am')
mtcars.pivot_table(index=['gear','vs'], values='mpg', columns=['am','cyl'], fill_value=0)
mtcars.pivot_table(index=['gear'], columns=['vs','am'],  aggfunc ={'mpg':np.mean,'wt':min})
