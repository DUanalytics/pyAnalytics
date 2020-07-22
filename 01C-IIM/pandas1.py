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
mtcarsDF.index  #here index by rownames
type(mtcarsDF)
#%%% access DF
mtcarsDF[0:5]
mtcarsDF[0:5,0:3]
mtcarsDF.loc[['Mazda']]
mtcarsDF.loc('Mazda', axis=1)
mtcarsDF.loc[7:9]
mtcarsDF.at[4, 'am']
mtcarsDF.filter(['gear', 'am'])
mtcarsDF.filter(regex = '[gGa]')  #small or big G or a in the column name

#loc uses index labels, iloc considers position in the index
#position 
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
mtcarsDF.loc['Mazda RX4':'Datsun 710']  #different to implement



mtcarsDF.filter(items=['gear','am'])
mtcarsDF.filter(regex='Toyota', axis=0)  #rownames axis=0
mtcarsDF.filter(regex='am', axis=1)  #colnames axis=1


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


#groups

mtcarsDF.groupby('gear')
mtcarsDF.groupby(['gear'])
mtcarsDF.groupby(['gear']).groups.keys()
mtcarsDF.groupby(['gear']).groups[3] #cars of group with gear 3
mtcarsDF.groupby('carb').first()  #first item of each group
mtcarsDF.groupby('carb').last()
mtcarsDF.groupby('gear')['mpg'].mean()
mtcarsDF.groupby('gear').count()
mtcarsDF.groupby('gear')['mpg'].count()
mtcarsDF[]

mtcarsDF.groupby('gear').agg(meanMPG = pd.NamedAgg(column='mpg', aggfunc='mean'))
mtcarsDF.groupby(['gear','am']).agg(meanMPG = pd.NamedAgg(column='mpg', aggfunc='max'))
mtcarsDF.groupby('gear').agg(meanMPG = pd.NamedAgg(column='mpg', aggfunc='mean'), maxMPG = pd.NamedAgg(column='wt', aggfunc='max'))
mtcarsDF['gear'].count()
mtcarsDF['gear'].max()


#%% graphs 
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