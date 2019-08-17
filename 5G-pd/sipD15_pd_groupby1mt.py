# -*- coding: utf-8 -*-
#-----------------------------
#%
#Group By
#%

import pandas as pd
import numpy as np

#import data
df2 = pd.read_csv('data\mtcars.csv')
df2.head()
df2.columns
df2.am
df2[df2['am']== 0]['mpg'].min()
df2.groupby("am").agg({ "mpg" : "min" })

#groupby

df2.groupby('cyl')
df2.groupby('cyl').size()
df2.groupby('cyl')['mpg'].mean()
df2.groupby('cyl')[['mpg','hp','wt']].mean()
df2.groupby('cyl').describe()
df2.groupby('cyl').describe().unstack()

#multiple groups
df2.groupby(['cyl','gear'])
df2.groupby(['cyl','gear']).aggregate(['mean'])
df2.groupby(['cyl','gear']).size().unstack(fill_value=0)
#value counts works on series
df2.cyl.value_counts()


df2.groupby('cyl').aggregate({'mpg':'mean'})
#see column headings
df2.groupby('cyl', as_index=True).aggregate({'mpg':'mean'})  #index - cyl
df2.groupby('cyl', as_index=False).aggregate({'mpg':'mean'})  #no index

#sort
df2.groupby(['cyl','gear'], sort=False, as_index= True).aggregate({'mpg' :'mean'})
df2.groupby(['cyl','gear'], sort=True, as_index= True).aggregate({'mpg' :'mean'})

#level 
df2.groupby(level=0)['mpg'].mean()  #first level of index (here only 1)
df2.groupby(level=1)['mpg'].mean()  #error as there is no index



#axis
df2.groupby(['cyl','gear'], axis=0, sort=True).aggregate({'mpg':'mean'})
#sort by row index
df2.groupby(['cyl','gear'], axis=1, sort=True).aggregate({'mpg':'mean'})  #error : cannot index cols
df2.groupby(['cyl','gear'], axis=1, sort=True)['mpg'].mean()  #error

#observed
df2['gear'] = df2['gear'].astype('category')
df2.groupby(['cyl','gear'], observed=True).aggregate({'mpg':'mean'})
df2.groupby(['cyl','gear'], observed=False).aggregate({'mpg':'mean'})

#groupkeys - with apply, index pieces


#squeeze - reduce dimn
df2.groupby(['cyl','gear'], squeeze=True)['mpg'].mean()
df2.groupby(['cyl','gear'], squeeze=False)['mpg'].mean()



#df2.pivot_table(index=['cyl'], columns='gear', aggfunc='size', fill_value=0)

#attributes
df2.groupby('gear')
geargp  = df2.groupby('gear')
geargp.groups
len(geargp)  #3 groups


#groupby multiindex
df2b = df2.set_index(['gear','cyl'])
df2b
#columns shifted to first 2 columns as index

group2b = df2b.groupby('carb')

df2b.groupby(level=0).size()
df2b.groupby(level='gear').size()

df2b.groupby(level=1).size()
df2b.groupby(level='cyl').size()

df2b
df2b.groupby(level=[0,1]).size() #gear-level0, cyl-Level1
df2b.groupby(level=['gear','cyl']).size()

df2b.groupby(level=[1,0]).size()
df2b.groupby(level=['cyl','gear']).size()
df2b.groupby(level=['cyl','gear']).sum()


#index and columns

df2b.groupby([pd.Grouper(level=1), 'carb']).size()
df2b.groupby(['gear', 'carb']).size()  #can be specified directly

df2b.groupby([pd.Grouper(level=0), 'carb']).size()
df2b.groupby([pd.Grouper(level=[0,1]), 'carb']).size() #not working 

#find groups

group2 = df2.groupby('gear')
group2.get_group(4)  #4 gear cars
group3 = df2.groupby(['gear','am'])
group3.get_group((4,0))  #4 gear cars


#aggregation

group2.aggregate(np.sum)
group2.agg(np.sum)  #agg same as aggregate
group3.agg(np.sum)
group3.agg(np.sum).reset_index()  #remove index


#if index names not required
group4 = df2.groupby(['gear','am'], as_index=False)
group4.agg(np.sum)
#no index column now
group4.sum()
group4.size()
group4.describe()
group4.count() #size better

#other functions
#mean(), sum(), size(), count(), std(), var(), sem(), describe(), first(), last(), nth(), min(), max()

#aggregating multiple functions
group4.groups 
group4.size()
group4.sum()
group4['mpg'].agg([np.sum, np.mean, np.median])  #one column agg mpg
group4.agg([np.sum, np.mean, np.median])  #all numeric columns

#rename columns as you aggregate
group4['mpg'].agg([np.sum, np.mean, np.median])
group4['mpg'].agg([np.sum, np.mean, np.median]).rename(columns={'sum':'Total', 'mean':"Average", 'median':'Middle_Value'})

#rename columns as you aggregate
group4['mpg'].agg([np.sum, np.mean, np.median])
group4.agg([np.sum, np.mean, np.median]).rename(columns={'sum':'Total', 'mean':"Average", 'median':'Middle_Value'})  #all columns

#different functions different columns
group4.agg({'mpg':np.mean, 'wt':[np.mean, np.median], 'hp':'std'})
group4.agg({'mpg':np.mean, 'wt': lambda x:np.std(x) + 2}) #lambda functions
group4.agg({'mpg':np.mean, 'wt':[np.mean, 'mean'], 'hp':'mean'})  #error
#functions can be strings but must unique function defn
group4.agg({'mpg':np.mean, 'wt':[np.median,'mean'], 'hp':'mean'})  #error


#apply function
group4.apply(lambda x:x.describe())
group4.apply(lambda x:np.multiply(x,2))


#unobserved
pd.Series([1,2,3,4])
pd.Series([1,2,3,4]).groupby(pd.Categorical(['a','b','a','a']))

pd.Series([1,2,3,4]).groupby(pd.Categorical(['a','b','a','a'], categories=['a','b','c']), observed=False).count()
#show only observed values
pd.Series([1,2,3,4]).groupby(pd.Categorical(['a','b','a','a'], categories=['a','b','c']), observed=True).count()
#no c category here


#first/last rows of each group
group4.size()
group4.first()
group4.last()

#nth row
group4.nth(1) #check & compare
group4.nth(-1) #last
group4.nth(-1, dropna='any') #drop any ??
group4.nth(-1, dropna='all') #drop all??

#enumerate
group4.cumcount()
#where each row is 

#listing
list(group4)

#add prefix
group4.mean()
group4.mean().add_prefix('MEAN_')

#function 
def get_status(group):
    return {'min': group.min(), 'max':group.max()}
get_status(group4)

group4.apply(get_stats)



#end----------------------------