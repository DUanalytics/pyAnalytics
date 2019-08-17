#Topic: Group - Sort - Index
#-----------------------------
#libraries

import pandas as pd
pd.set_option('display.max_columns',10)
import numpy as np
import matplotlib.pyplot as plt
#df = pd.read_csv('data/mtcars.csv')
from pydataset import data
mtcars = data('mtcars')
mtcars.head()
df = mtcars
#create simple index like car1, car2 
carNo = ['Car' + str(i) for i in range(1,33)]
carNo
#carNo2 = pd.Series(["car" + str(i) for i in range(1,33)])
#carNo2

df.index = carNo  #give name to index
df.head()
df.index.name = 'carNo'

mDate = pd.date_range('2017-02-24', periods=32, freq='Q')
mDate
df['mDate'] = mDate
df.head()
dfcopy = df.copy()
#
df.columns
df.groupby('gear').size()
df.groupby(['gear','cyl']).size()
df.groupby(['gear','cyl']).size().reset_index('gear')
df.groupby(['gear','cyl']).size().reset_index(['gear','cyl'])

df.groupby(['gear']).get_group(3)
#cars of group 3
gA1 = df.groupby('gear', as_index=False)
gA1
gA1.get_group(3)


gB1=df.groupby('gear').apply(lambda x: x.reset_index(drop=True))
gB1  #this is groupwise
gB1.drop('gear',axis=1).reset_index()
#this is without group: gear columns is first

gC1 =df.groupby('gear', as_index=True).get_group(3).index
gC1
#names of 3 gear cars

gD1 = df.groupby(['gear','cyl'], as_index=False)
gD1
gD1.apply(lambda x: x.reset_index())
#shows as levels not as values : gear3-0level, cyl4-0level and so on
gD2 = gD1.apply(lambda x: x.reset_index(drop = True)).reset_index()
gD2 #levels shown now

#Sorting
sA1 = df.sort_values(['gear', 'cyl'], ascending=[1, 0])
sA1



#%%% Filtering
df.iloc[:5]
df.head(5)
df.iloc[:5, :4]
df[['mpg','cyl','disp','hp']].iloc[:5]
df[df['cyl'] == 6]
df[(df['cyl'] == 6) & (df['gear']==4)]
df.loc['Car1']
df.loc['Car1':'Car5']  #index should be sorted
df.loc['Car1':'Car5', 'mpg'] 
df.loc['Car1':'Car5', 'mpg':'wt'] 
df.loc[['Car1','Car5'], ['mpg','wt','mDate']] 

#DF.loc[ ] : This function is used for labels.
#DF.iloc[ ] : This function is used for positions or integer based
#DF.ix[] : This function is used for both label and integer based

df.iloc[2] # 2nd row
df.loc[:, 'mpg']
df.loc[::2, ['mpg','cyl']]  #rowno also works
df.loc[::3, ::3]
df.iloc[::3, ::3] 
df.iloc[::3, ['mpg','cyl']]  #error
df.iloc[-1:, -1:]   #last row & last col
df.iloc[-1:, ]  #last row
df.iloc[:,-1: ]  #last col
df.iloc[[3, 4], [1, 2]] #access by integer pos
# retrieving all rows and some columns by iloc method  
df.iloc [:, [1, 2]] 
df.ix["Car1"] 
df.ix[["Car1",'Car5']] 
df.ix[["Car1",'Car5'], ['mpg','cyl']] 


#%%
#index
df2= df.set_index(pd.DatetimeIndex(df['mDate']), drop=False, inplace=False)

#between certain dates
df2['2018-1-1':'2020-1-1']

df.columns
df.index
df3 = df.set_index(['mDate'], append=True, inplace=False)
df3.head()


#%%%
df.isin()
filter1 = df["gear"].isin([4]) 
filter2 = df["cyl"].isin([4,6]) #4,6,8 
df[filter1]
df[filter1 & filter2]
df[filter1 | filter2]

#----df.where()
# making boolean series for a team name 
filter3 = df["cyl"]==4
# filtering data 
df.where(filter3, inplace = False) 
#-----
df.query()
df.query('gear ==4 and cyl ==6', inplace = False)

#
df.insert()

#%%df.xs()



#%% df.at - not working
position = 2
label = 2
label2 = 'mpg'
# calling .iat[] method 
df.iat[position, label] 



#%%%
df.mask([True,False,True],)
df.mask(df['mpg'] > 27, 99, inplace=False) #replace all values > 27 with with 99
df
df.mask(df.isna(), 1000, inplace=False) 
df5= df.copy()
df5.mask(df5['mpg'] > 27, None, inplace=False)
df5
df5['mpg'].mask(df5['mpg'] > 27, None, inplace=True)
df5
df5.isna().sum()
df5.mask(df5.isna(), 1000, inplace=False)
df5['mpg'].mask(df5['mpg'].isna(), 1000, inplace=True)
df5
