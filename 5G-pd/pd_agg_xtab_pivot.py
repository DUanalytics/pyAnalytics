#Topic: Pandas - group-aggregate, pivot, crosstab together 
#-----------------------------
#libraries
import pandas as pd
pd.set_option('display.max_columns',11)
import numpy as np
import matplotlib.pyplot as plt
from pydataset import data
mtcars = data('mtcars')
mtcars.head()
df = mtcars
df.head()
df.columns
df.describe()

#%% Groupby

df.groupby("am").agg({ "mpg" : "min" }) #min mileage of each am 
df.groupby('cyl')[['mpg','hp','wt']].mean()
df.groupby('cyl').sum()
df.groupby(['cyl','gear']).aggregate(['mean'])
#agg and aggregate are same
df.groupby('cyl', as_index=True).aggregate({'mpg':'mean'}) 

#%%
group1 = df.groupby(['gear','am'])
group1
group1.sum()
group1.size()
group1.describe()
group1.count() #size better

##mean(), sum(), size(), count(), std(), var(), sem(), describe(), first(), last(), nth(), min(), max()
group1['mpg'].agg([np.sum, np.mean, np.median])  #one column agg mpg
group1.agg([np.sum, np.mean, np.median])  #all numeric columns

#rename columns as you aggregate
group1['mpg'].agg([np.sum, np.mean, np.median])
group1['mpg'].agg([np.sum, np.mean, np.median]).rename(columns={'sum':'Total', 'mean':"Average", 'median':'Middle_Value'})

#different functions different columns
group1.agg({'mpg':np.mean, 'wt':[np.mean, np.median], 'hp':'std'})
group1.agg({'mpg':np.mean, 'wt': lambda x:np.std(x) + 2}) #lambda

#first/last rows of each group
group1.size()
group1.first()
group1.last()

#nth row
group1.nth(1) #check & compare
group1.nth(-1) #last

#add prefix
group1.mean()
group1.mean().add_prefix('MEAN_')


#%% Cross Tab
df1 = mtcars
#cross tab - two cols
pd.crosstab(df1.cyl, df1.gear)

#df1.pivot_table(index='cyl', columns='gear')
#with margin total
pd.crosstab(df1.cyl, df1.gear, margins=True, margins_name="Total")
pd.crosstab(df1.cyl, [df1.gear, df1.am])
#multiple cols - left and top: with col names
pd.crosstab([df1.cyl, df1.vs], [df1.gear, df1.am], rownames=['Cylinder', "Engine Type"], colnames=['Gear', "Transmission Type"],  dropna=False)

xtab1 = pd.crosstab([df1.cyl, df1.vs], [df1.gear, df1.am], rownames=['Cylinder', "Engine Type"], colnames=['Gear', "Transmission Type"],  dropna=False)
xtab1


#%%%
#Pivot Table
df3 = mtcars
df3.columns
df3.pivot_table('cyl','am', columns='gear')  #default function - mean
df3.pivot_table(values= ['mpg','hp'], index=['gear'], columns=['am','vs'])
#df.pt (values, index, columns)
df1.pivot_table(index=['gear'], columns=['cyl'],  aggfunc ={'mpg':np.mean,'wt':min})
