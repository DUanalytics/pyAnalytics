# -*- coding: utf-8 -*-
#dfply library functions for data manipulation

from dfply import *
#install from conda as admin #: pip install dfply
import pandas as pd
import numpy as np


#data 
df = pd.read_csv('data/mtcars.csv')
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
df1 = df.set_index('carname')
df1

df1[catcolumns1] = df1[catcolumns1].astype('category')
df1.dtypes

df1.describe()
df1[catcolumns1].describe()
df1.columns
#now summarise

#%%
#piping in the code : >> 
#final_result = orginal_data --> dfplyfunction1() --> dfplyfunction12()
#multiple chaiing with >>
#each step of chain represented by X.

#%%
df1 >> select(X.mpg)
df1 >> select(X.mpg, X.cyl)
df1 >> select(X.mpg, X.cyl) >> arrange(X.mpg) >> drop(X.cyl)
#drop is inverse of select (selecting a column)
df1 >> select(~ X.mpg)  #drop column by ~ tilde
df1 >> select(~ X.mpg, ~ X.cyl)

#%%
#arrange
df1 >> select( X.mpg, X.cyl, X.am) >> arrange(X.cyl, X.am, X.mpg, ascending=False)
#mixed sorting ---


#%%
#Filter Data with mask
df1 >> mask( X.mpg > 25)
df1 >> mask( X.mpg > 25, X.cyl==4)
df1 >> mask( X.am==0, X.car == 'Honda')

#%%
#mutate - add new columns
df1 >> mutate(newMPG = X.mpg * 1.2, newHP = X.hp + 10) >> select(X.newMPG, X.newHP, X.wt)
df1 >> mutate(newMPG = X.mpg * 1.2, newHP = X.hp + 10) >> select(X.newMPG, X.newHP, X.wt) >> mutate(MPGperWt = X.newMPG/ X.wt)


#%%
#group and ungroup
df1 >> group_by(X.cyl)  #nothing
df1 >> group_by(X.cyl, X.am)  #nothing
df1 >> group_by(X.cyl) >> summarise(meanMPG = X.mpg.mean())
df1 >> group_by(X.cyl,X.am) >> summarise(meanMPG = X.mpg.mean())


#%%
#combined multiple operations

result1 = df1 >> group_by(X.cyl,X.am) >> summarise(meanMPG = X.mpg.mean())
result1
result1.sort_values('meanMPG', ascending=False)

#%%
