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
mtcarsDF.empty
mtcarsDF.size
mtcarsDF.ndim
mtcarsDF.axes
mtcarsDF.values

#%%% access DF
mtcarsDF[0:5]
mtcarsDF[0:5,0:3]

#single value: at
mtcarsDF.at['Mazda RX4', 'mpg']
mtcarsDF.at['Mazda RX4', 'mpg']

#single values : iat : integer
mtcarsDF.iat[0,0]
mtcarsDF.iat[0,0:5]

#set of values : loc : index values
mtcarsDF.index
mtcarsDF.loc[['Mazda 4X4']]
mtcarsDF.loc['Mazda 4X4', ['mpg']]
mtcarsDF.loc[7:9]

#iloc
mtcarsDF
mtcarsDF.loc['Mazda RX4']
mtcarsDF.loc['Mazda RX4', 'mpg']
mtcarsDF.loc['Mazda RX4', ['mpg', 'wt']]
mtcarsDF.loc['Merc 280', ['mpg', 'wt']]
mtcarsDF.loc['Mazda RX4':'Datsun 710']  #difficult to implement

#loc uses index labels, iloc considers position in the index

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
#%%%
#Add / Remove Columns/ Rows
mtcarsDF.drop(labels=['mpg','hp'], axis=1, inplace=False) #columns
mtcarsDF.drop(labels=['Mazda RX4'], axis=0, inplace=False)  #row


#%%% duplicates
mtcarsDF.duplicated()  #compare each row and find duplicates : Nil here
mtcarsDF['gear'].duplicated()  #there multiple cars can have some duplicates
mtcarsDF.duplicated(subset='gear')  #duplicates by gear
mtcarsDF.duplicated(subset=['gear','cyl'])  #duplicates by gear and cyl

mtcarsDF.drop_duplicates(inplace=False)
mtcarsDF['gear'].drop_duplicates(inplace=False)  #one car of each gear type
mtcarsDF.drop_duplicates(subset='gear', inplace=False)
mtcarsDF.drop_duplicates(subset=['gear', 'cyl'], inplace=False)

#%%% unique values - columns
mtcarsDF.mpg.unique()
mtcarsDF['cyl'].unique()

#%%% search
mtcarsDF['carname'] = mtcarsDF.index
mtcarsDF['carname'].str.contains('Mazda') 
mtcarsDF.columns 
np.where(mtcarsDF.carname.str.contains('Mazda'))
np.where?
#%%%% normalisation
from sklearn import preprocessing
import numpy as np

a = np.random.random((1, 4))
a = a*20
print("Data = ", a)

# normalize the data attributes
normalized = preprocessing.normalize(a)
print("Normalized Data = ", normalized)
mtcarsDF.iloc[0:5,:]
preprocessing.normalize(mtcarsDF.iloc[:,0:5])

#filter
mtcarsDF.filter(['gear', 'am'])
mtcarsDF.filter(regex = '[gGa]')  #small or big G or a in the column name

mtcarsDF.filter(items=['gear','am'])
mtcarsDF.filter(regex='Toyota', axis=0)  #rownames axis=0
mtcarsDF.filter(regex='am', axis=1)  #colnames axis=1

#%%statistics 0- column, 1-row
mtcarsDF.mean(axis=0)
mtcarsDF.mean(axis=1)
mtcarsDF.kurt(axis=0)
mtcarsDF.kurt(axis=1)
mtcarsDF.max(axis=0)
mtcarsDF.max(axis=1)
mtcarsDF.rank(axis=0)
mtcarsDF.skew(axis=0)
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

#%%value_counts
mtcarsDF.cyl.value_counts()  #count group wise
mtcarsDF.cyl.value_counts(normalize=True)  #proportion
mtcarsDF.cyl.value_counts(ascending=True)  #ascending order
mtcarsDF.cyl.value_counts(dropna=False)  #do not drop missing values

#continous data
mtcarsDF.mpg.value_counts()
mtcarsDF.mpg.value_counts(bins=5)  #class intervals

#%% sort
mtcarsDF.sort_values(by='gear', axis=0)
mtcarsDF.sort_values(by=['gear', 'mpg'])


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
mtcarsDF.groupby('gear')['mpg'].count()
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
mtcarsDF.groupby('gear')['mpg'].agg([np.mean, np.sum, 'count']).rename(columns={'meanMPG')



mtcarsDF.groupby('gear').agg(meanMPG = pd.NamedAgg(column='mpg', aggfunc='mean'))
mtcarsDF.groupby(['gear','am']).agg(meanMPG = pd.NamedAgg(column='mpg', aggfunc='max'))
mtcarsDF.groupby('gear').agg(meanMPG = pd.NamedAgg(column='mpg', aggfunc='mean'), maxMPG = pd.NamedAgg(column='wt', aggfunc='max'))
mtcarsDF['gear'].count()
mtcarsDF['gear'].max()

mtcarsDF.groupby('gear').mean()
mtcarsDF.groupby('gear').mean().add_prefix('MEAN_')

gearGp = mtcarsDF.groupby('gear')
gearGp.mean()
gearGp.nth(1)
gearGp.nth([1,3])


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
#pip install dfply  #install this library first
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
mtcarsDF2 >> select(X.mpg)   #X is current DF
mtcarsDF2 >> select(~X.mpg, ~X.wt).tail()   # exclude
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


#ggplot
#pip install ggplot
from ggplot import *
ggplot(data=mtcarsDF, mapping= aes(x='wt', y='mpg')) + geom_point(colour='r')
#error tslib https://github.com/yhat/ggpy/issues/662

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
df = df.groupby(['home_team'])['arrests'].mean()

df.plot.bar()


#using matplotlib



#%%%random numbers
#https://docs.scipy.org/doc/numpy-1.13.0/reference/routines.random.html


#%%  other pandas function
#merge, missing values, outliers, join, reshape

mtcarsDF
mtcarsDF.shape
mtcarsDF.isnull().sum().sum()  #no missing values
mtcarsMDF = mtcarsDF.copy()
mtcarsMDF.columns 
#hp=3, wt=5, vs=7
#choose selected column and introduce missing values by NaN
loc1 = np.random.randint(low=1, high=32, size=3)
mtcarsMDF.iloc[loc1, 3]  #location by integer values
mtcarsMDF.iloc[loc1, 3] = None
mtcarsMDF.isnull().sum()

loc1 = np.random.randint(low=1, high=32, size=5)
mtcarsMDF.iloc[loc1, 5]  #location by integer values
mtcarsMDF.iloc[loc1, 5] = None
mtcarsMDF.isnull().sum()

loc1 = np.random.randint(low=1, high=32, size=7)
mtcarsMDF.iloc[loc1, 7]  #location by integer values
mtcarsMDF.iloc[loc1, 7] = None
mtcarsMDF.isnull().sum()

mtcarsMDF.isnull().sum(axis=0)
mtcarsMDF.isnull().sum(axis=1)

#drop rows/columns with any missing values
mtcarsMDF.dropna(inplace=False,axis=1) #columns
mtcarsMDF.dropna(inplace=False,axis=0) #rows
mtcarsMDF.dropna(subset=['hp'],inplace=False)  #drop rows with missing values in hp column


#replace missing values
mtcarsMDF.fillna(0)  #all missing values with 0
mtcarsMDF
mtcarsMDF[mtcarsMDF.isnull().any(axis=1)]
mtcarsMDF.fillna(method='bfill')  #fill with previous row value of the column
mtcarsMDF.fillna(method='ffill')  #fill with next row value of the column


df.dropna(inplace=True,axis=1)



#%%%
import pandas as pd
import numpy as np

from pydataset import data
mtcars = data('mtcars')
mtcars.head()

mtcars.values
mtcars.index
mtcars.columns
mtcars.dtypes
mtcars[['cyl','vs', 'am', 'gear','carb']] = mtcars[['cyl','vs', 'am', 'gear','carb']].astype('category')
data = mtcars.values
data
mtindexDF1 = pd.DataFrame({'TYPE':['NUMERIC','CATEGORY','NUMERIC', 'NUMERIC','NUMERIC', 'NUMERIC', 'NUMERIC', 'CATEGORY','CATEGORY', 'CATEGORY', 'CATEGORY' ], 'COLNAME': ['mpg', 'cyl','disp', 'hp', 'drat', 'wt', 'qsec', 'vs', 'am', 'gear','carb']}) 
mtindexDF1
mtindex1 = pd.MultiIndex.from_frame(mtindexDF1)
mtindex1
pdMTCARS1 = pd.DataFrame(data, columns=mtindex1)
pdMTCARS1.head(2)

pdMTCARS1(['TYPE', 'COLNAME']).sort_index.sort_values(['TYPE', 'COLNAME'], ascending=True, inplace=True)
pdMTCARS1.sort_index()
df = pdMTCARS1.sample(5)
#----
#DataFrame.sort_index(axis=0, level=None, ascending=True, inplace=False, kind=’quicksort’, na_position=’last’, sort_remaining=True, by=None)
#
df
df.sort_index(axis = 0)  #rownames
df.sort_index(axis = 1)   #columnames - level0 : CAT, NUM
# sorting based on column labels 
df.sort_index(axis = 1, level=1)  # Level 1 of column names- am, carb
df.sort_index(axis = 1, level=[1,0]).columns
df.query('mpg > 25')
df.swaplevel(0, 1, axis=1)  #levels in columns changed
df.reorder_levels([1,0], axis=1)
df

#https://pandas.pydata.org/pandas-docs/version/0.15/advanced.html
df.mean
df.mean(level=0)
df.mean(level=0, axis=1)
df.mean(level=1, axis=1)
df2 = pd.concat([df,df])
df2
df2.mean(level=1, axis=1)
df2.mean(level=0, axis=1)
df2.align(df, level=0)  #join
df.align(df, level=0) #show them together
df.align(df, level=1)
df.align(df, level=1, axis=0)
df.align(df, level=1, axis=1)
df
df.xs('disp', level='COLNAME', axis=1)
df.xs('NUMERIC', level='TYPE', axis=1)
df.xs('CATEGORY', level='TYPE', axis=1)
df.sort_index(axis=1)
df.sort_index(level=[1],axis=1)
df.sort_index(level=[0],axis=1)
df.sort_index(level=[0,1],axis=1)
df.sort_index(level=[1,0],axis=1)
df.loc[:,(slice(None),'am')]
df.loc[:,(slice(None),['vs','am'])]
df.loc[:,(slice('CATEGORY'),['vs','am'])]  #needs to be sorted
df.sort_index(level=[0,1],axis=1).loc[:,(slice('CATEGORY'),['vs','am'])]
#
df
df.xs(('NUMERIC', 'mpg'), level=('TYPE', 'COLNAME'), axis=1)
df.xs(('NUMERIC', 'hp'), level=('TYPE', 'COLNAME'), axis=1)
df.xs(('NUMERIC', 'am'), level=('TYPE', 'COLNAME'), axis=1)  #error

df.loc[(slice(None)),:]


#------
#can we create index in random order
type2 = ['CATEGORY'] * 5 + ['NUMERIC']*6
type2
colname2 = ['cyl','vs', 'am', 'gear','carb'] + ['mpg','disp', 'hp', 'drat', 'wt', 'qsec']
colname2
mtindexDF2 = pd.DataFrame({'TYPE':type2,'COLNAME': colname2}) 
mtindexDF2
mtindex2 = pd.MultiIndex.from_frame(mtindexDF2)
mtindex2
data2 = mtcars[colname2].values
pdMTCARS2 = pd.DataFrame(data2, columns=mtindex2)
pdMTCARS2.head(2)

DF = pdMTCARS2.sample(5)
DF.xs(('NUMERIC', 'hp'), level=('TYPE', 'COLNAME'), axis=1)
DF.loc[:,(slice(None),['vs','am'])]
DF.xs('NUMERIC', level='TYPE', axis=1)
DF.xs('CATEGORY', level='TYPE', axis=1)

DF2 = DF.set_index('gear')
DF.loc[(slice(1,7), ['mpg','hp']),:]
#DataFrame.set_index(self, keys, drop=True, append=False, inplace=False, verify_integrity=False)[source]