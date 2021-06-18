#Topic:Pandas DF
#-----------------------------
#libraries
import numpy as np
import pandas as pd
#pandas DF are combination of panda Series..
#one column data is a Series of one datatype, DF can have multiple data types

from pydataset import data
mtcars = data('mtcars')
mtcarsDF = mtcars

mtcarsDF

#%%describing
mtcarsDF.shape
mtcarsDF.head(3)
mtcarsDF.tail(4)
mtcarsDF.describe
mtcarsDF.columns
mtcarsDF.dtypes

mtcarsDF.index  #here index by rownames
type(mtcarsDF)

mtcarsDF.select_dtypes(include=['int64'])
mtcarsDF.select_dtypes(exclude=['int64'])
mtcarsDF.isna()
mtcarsDF.notna()
id(mtcarsDF)
mtcars.empty
mtcars.size
mtcars.ndim
mtcars.axes
mtcars.values

#%%% access DF
#https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html
#Series : s.loc[indexer]
#DataFrame : df.loc[row_indexer,column_indexer]
mtcarsDF[0:5]
mtcarsDF.loc[:,'mpg']
mtcarsDF.loc['Fiat 128','mpg']
mtcarsDF.loc['Fiat 128':,'wt':]

#single value: at
mtcarsDF.at['Mazda RX4', 'mpg']
mtcarsDF.at['Mazda RX4', 'mpg']

#single values : iat : integer
mtcarsDF.iat[0,0]
mtcarsDF.iat[0,0:5]

#set of values : loc : label value
#purely label based indexing. This is a strict inclusion based protocol. Every label asked for must be in the index, or a KeyError will be raised. When slicing, both the start bound AND the stop bound are included, if present in the index. Integers are valid labels, but they refer to the label and not the position.
mtcarsDF.index
mtcarsDF.loc[['Mazda 4X4']]
mtcarsDF.loc['Mazda 4X4', ['mpg']]
mtcarsDF.loc[7:9]

#loc : purely label based indexing
mtcarsDF
mtcarsDF.loc['Mazda RX4']
mtcarsDF.loc['Mazda RX4', 'mpg']
mtcarsDF.loc['Mazda RX4', ['mpg', 'wt']]
mtcarsDF.loc['Merc 280', ['mpg', 'wt']]
mtcarsDF.loc['Mazda RX4':'Datsun 710']  #difficult to implement

#iloc uses index labels, iloc considers position in the index

mtcarsDF.iloc[1:10, 1:5]
mtcarsDF.iloc[1:10:2, 1:5:2]
mtcarsDF.iloc[1::2, 1::2]
mtcarsDF.iloc[0]
mtcarsDF.iloc[1:5]
mtcarsDF.iloc[1,5] #2nd row, 6th column
mtcarsDF.iloc[1:5, 0:2] #2nd to 5th row, 0 to 2nd column
mtcarsDF.iloc[:5, :3]  #0-4 rows, 0-3 columns
mtcarsDF.iloc[::2]  #alternate rows : start, end, step
mtcarsDF.iloc[::-1]  #reverse order
mtcarsDF.iloc[::2].iloc[::2] #first alternate, again alternate
mtcarsDF.iloc[:-2:-2]  #which rows is this
mtcarsDF.iloc[1::5,:]  #5th row start from 1(2nd row)
mtcarsDF.iloc[0:3]


#filter
mtcarsDF.filter(['gear', 'am'])
mtcarsDF.filter(regex = '[gGa]')  #small or big G or a in the column name

mtcarsDF.filter(items=['gear','am'])
mtcarsDF.filter(regex='Toyota', axis=0)  #rownames axis=0
mtcarsDF.filter(regex='am', axis=1)  #colnames axis=1

#%%statistics 0- column, 1-row
mtcarsDF.mean(axis=0)
mtcarsDF.mean(axis=1)
mtcarsDF.kurt(axis=0)  #peakendness
mtcarsDF.kurt(axis=1)
mtcarsDF.max(axis=0)
mtcarsDF.max(axis=1)
mtcarsDF.rank(axis=0)
mtcarsDF.skew(axis=0) #shift
mtcarsDF.skew(axis=1)



#%%filter
#condition
mtcarsDF['gear'] == 3  #T&F
mtcars[mtcarsDF['gear'] == 3]  #rows with T for gear=3
mtcars[mtcarsDF['gear'] != 3, ['gear','am']]

#another way
mtcarsDF[mtcarsDF.gear.eq(3)]  #chaining method

mtcarsDF[mtcarsDF['gear'] == 3 & mtcarsDF['am']== 0]

mtcarsDF.gear.unique()
mtcarsDF.carb.unique()

gears=[4,5]
mtcarsDF[mtcarsDF.gear.isin(gears)]


#rows NOT condition
mtcarsDF[~ mtcarsDF.gear.isin(gears)] #cars of not gear(4,5)

#multiple conditions
carbs = [1,3]
mtcarsDF[mtcarsDF.gear.isin(gears) & mtcarsDF.carb.isin(carbs) ]
mtcarsDF[~ mtcarsDF.gear.isin(gears) & mtcarsDF.carb.isin(carbs) ]

#query function
mtcarsDF.query('gear==4')
#if a string
mtcarsDF.query('gear=="4"')
mtcarsDF.query('gear==4 & am==0')
mtcarsDF.query('gear in [3,7]')



#%% summaries - group, sort
mtcarsDF

#stats
mtcarsDF['gear'].count()
mtcarsDF['wt'].max()
mtcarsDF['wt'][mtcarsDF['gear'] == 4]
mtcarsDF['wt'][mtcarsDF['gear'] == 4].sum()  #sum of wt of 4 gear cars
mtcarsDF['gear'].value_counts()
mtcarsDF[mtcars['hp'] > 150].gear.value_counts()
mtcarsDF['mpg'].unique()
mtcarsDF['mpg'].nunique()# how many non-null unique values
mtcarsDF['mpg'].count()
#other stats functions - count, sum, mean, mad, median, min, max, mode, abs, prod, std, var, sem, skew, kurt, quantile, cumsum, cumprod, cummax, cummin, describe
mtcarsDF.describe()  # default only numeric

#%% sort
mtcarsDF.sort_values(by='gear', axis=0)
mtcarsDF.sort_values(by=['gear', 'mpg']).head(n=10)
mtcarsDF.sort_values(by=['cyl','mpg'], ascending=[True, False]).head(n=20)




#%%% groupby
mtcarsDF.describe()
mtcarsDF.groupby('gear')
mtcarsDF.groupby(['gear'])
mtcarsDF.groupby(['gear']).groups.keys()
mtcarsDF.groupby(['gear']).groups[3] #cars of group with gear 3
mtcarsDF.groupby('carb').first()  #first item of each group
mtcarsDF.groupby('carb').last()
mtcarsDF.groupby('gear')['mpg'].mean()
mtcarsDF.groupby('gear').count()
mtcarsDF.groupby('gear')['mpg'].count()  #not useful
mtcarsDF.groupby('gear')['mpg'].mean()  #useful
mtcarsDF.groupby('cyl')['mpg','wt'].mean()
mtcarsDF.groupby(['cyl','gear'])['mpg','wt'].mean()

#with aggregate
mtcarsDF.groupby('gear').agg('mean')
mtcarsDF.groupby('gear').size()
mtcarsDF.groupby(['gear','cyl']).size()
mtcarsDF.groupby(['gear','cyl']).count() #size better


mtcarsDF.groupby('gear').mpg.agg('mean')
mtcarsDF.groupby('gear')['mpg'].agg('mean')
mtcarsDF.groupby('gear')['mpg','wt'].agg('mean')
mtcarsDF.groupby('gear')['mpg','wt'].agg(['mean','max'])
mtcarsDF.groupby('gear').agg([np.mean, np.sum])  #all columns, np is faster, numeric values
mtcarsDF.groupby('gear')['mpg','wt'].agg([np.mean, np.sum, 'count'])
mtcarsDF.groupby('gear')['mpg'].agg([np.mean, np.sum, 'count'])
#.rename(columns={'meanMPG','sumMPG','countMPG'})


mtcarsDF.groupby('gear').agg(meanMPG = pd.NamedAgg(column='mpg', aggfunc='mean'))
mtcarsDF.groupby(['gear','am']).agg(meanMPG = pd.NamedAgg(column='mpg', aggfunc='max'))
mtcarsDF.groupby('gear').agg(meanMPG = pd.NamedAgg(column='mpg', aggfunc='mean'), maxMPG = pd.NamedAgg(column='wt', aggfunc='max'))
mtcarsDF['gear'].count()
mtcarsDF['gear'].max()

mtcarsDF.groupby('gear').mean()
mtcarsDF.groupby('gear').mean().add_prefix('MEAN_')

gearGp = mtcarsDF.groupby('gear')
gearGp.mean()
gearGp.nth(1)  #nth row in each gp
gearGp.nth([1,3])  # 1st and 3rd row in each gp
gearGp.first() #1st row in each gp
gearGp.last() #last row in each gp
gearGp.max()  #max value for each gp : max mpg for 3,4,5 gears is.. 
gearGp.min()
gearGp.size()   #size or count per gp
gearGp.count()
gearGp.mean()
gearGp.describe()  #standard summary for each gp and variable

#crosstab
import pandas as pd
pd.crosstab(mtcarsDF.cyl, mtcarsDF.gear)

#pivot
pd.crosstab(mtcarsDF.cyl, mtcarsDF.gear, margins=True, margins_name='Total')
pd.crosstab(mtcarsDF.cyl, [mtcarsDF.gear, mtcarsDF.am])
pd.crosstab([mtcarsDF.cyl, mtcarsDF.vs], [mtcarsDF.gear, mtcarsDF.am], rownames=['Cylinder','EngineShape'], colnames=['Gear', 'TxType'], dropna=False)

#pivottable
mtcarsDF.pivot_table('cyl','am', columns='gear')  #mean by default
mtcarsDF.pivot_table(values=['mpg','hp'], index=['gear'], columns=['am','vs'])
#index on left, values on columns, columns on left top

#dfply
#pip install dfply  #install this library first from anaconda
from dfply import *
mtcarsDF2 = mtcarsDF.copy()
id(mtcarsDF)
id(mtcarsDF2)
mtcarsDF2['carname'] = mtcarsDF2.index
mtcarsDF2.head()  #column with carnames

catcol = ['cyl', 'vs', 'am', 'gear' , 'carb']
mtcarsDF2[catcol] = mtcarsDF2[catcol].astype('category')
mtcarsDF2.dtypes
#chaining with >>
mtcarsDF2 >> head(10) >> tail(3)
mtcarsDF2 >> select(X.mpg)   #X is current DF
mtcarsDF2 >> select(~X.mpg, ~X.wt).   # exclude
mtcarsDF2 >> select(X.mpg, X.wt, X.am) >> head()
mtcarsDF2 >> select(X.mpg, X.wt)  >> arrange(X.mpg, ascending = False)
mtcarsDF2 >> select(X.mpg, X.gear, X.wt)  >> arrange(-X.gear, X.mpg) 
mtcarsDF2 >> mutate(newMPG = 1.2 * X.mpg)  >> select(X.mpg, X.newMPG)

mtcarsDF2 >> group_by(X.cyl) #nothing
mtcarsDF2 >> group_by(X.cyl, X.am) >> summarise(meanMPG = X.mpg.mean())

mtcarsDF2 >> group_by(X.cyl, X.am) >> summarise(meanMPG = X.mpg.mean()) >> arrange(X.cyl, X.meanMPG)




#%% graphs 

#from pandas: some graphs may not come correct. This is just syntax demo
mtcarsDF.plot(x='wt', y='mpg')
mtcarsDF.plot.area(x='wt', y='mpg')
mtcarsDF.plot.bar(x='gear', y='am')
mtcarsDF.plot.barh(x='gear', y='am')

mtcarsDF.plot.density()
mtcarsDF.mpg.plot.density()
mtcarsDF.plot.hist()
mtcarsDF.mpg.plot.hist()
mtcarsDF.plot.line()
mtcarsDF.mpg.plot.line()
mtcarsDF.plot.pie(y='gear')
mtcarsDF.gear.plot.pie() #not correct
mtcarsDF.boxplot()
mtcarsDF.plot.scatter(x='mpg',y='hp')



#seaborn
import seaborn as sns
xt1 = pd.crosstab(mtcarsDF.cyl, mtcarsDF.gear)
xt1
sns.heatmap(xt1, cmap='YlGnBu', annot=True, cbar=False)
xt2 = pd.crosstab(index=mtcarsDF.gear, columns=[mtcarsDF.am, mtcarsDF.vs], rownames=['Gear'] , colnames =['AM','VS'])
xt2
sns.heatmap(xt2)
sns.heatmap(xt2, cmap='YlGnBu', annot=True, cbar=False)


#ggplot #https://pypi.org/project/ggplot/
#$ pip install -U ggplot
from pandas import Timestamp
import datetime
import pandas as pd
date_types = ( pd.Timestamp,    pd.DatetimeIndex,    pd.Period,    pd.PeriodIndex,   datetime.datetime,    datetime.time)
#error module 'pandas' has no attribute 'tslib'
from ggplot import *
help(ggplot)
p = ggplot(aes(x='carat', y='price'), data=diamonds)
print(p + geom_point())
ggplot(aesthetics= aes(x='wt', y='mpg'), data=mtcarsDF) + geom_point(color='red')
help(ggplot(aesthetics, data))

ggplot(aesthetics=aes(x='gear'), data=mtcarsDF2) + geom_bar(stat='count', fill='green') 

#error tslib https://github.com/yhat/ggpy/issues/662
#C:\ProgramData\Anaconda3\Lib\site-packages\ggplot
#C:\ProgramData\Anaconda3\Lib\site-packages\ggplot\stats
#pip list -v  #c:\programdata\anaconda3\lib\site-packages

#%%plotnine
pip install plotnine 
from plotnine.data import economics
from plotnine import ggplot, aes, geom_line
(  ggplot(economics)  # What data to use
    + aes(x="date", y="pop")  # What variable to use
    + geom_line()  # Geometric object to use for drawing
)

#%% save to/from excel
mtcarsDF.to_csv('mtcars.csv') #check the folder in working dir tab
mtcarsDF.to_excel('mtcars.xlsx', sheet_name='mtcars1')
mtcarsDF.to_clipboard() #clipboard, paste it anywhere



import matplotlib.pyplot as plt
#scatter plot
plt.scatter(x=mtcarsDF.wt, y=mtcarsDF.mpg)
plt.scatter(x='wt', y='mpg', data=mtcarsDF)
plt.scatter(x='wt', y='mpg', data=mtcarsDF, label='MTCars : wt vs mpg')

#run these lines together
plt.scatter(x='wt', y='mpg', c='am' , cmap='bwr', marker ='s',data=mtcarsDF)
plt.scatter(x='wt', y='hp', c='am' , cmap='bwr', marker ='+', data=mtcarsDF)
plt.legend()
plt.show();

#barplot

mtcarsDF.groupby(['gear']).count()
df = mtcarsDF.groupby(['cyl'])['mpg'].mean()
df.plot.bar()


#using matplotlib






#%%  other pandas function
#merge, missing values, outliers, join, reshape


