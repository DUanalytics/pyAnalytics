# -*- coding: utf-8 -*-
#Simple Plots using Pandas library only
#-----------------------------
import pandas as pd
import numpy as np

#numpy
np1 = np.array([1,5,6,5,2,3,4,5,3,4,6,3])
np1
hist = np.histogram(np1)
hist#nothing will happen.

# pandas plot
studentcount = pd.Series([30, 25, 37])
studentcount.plot(kind='barh')
studentcount.plot(kind='bar')

#here plot is method in pandas : no matplotlib used here
#Load Inbuilt Datasets
import statsmodels.api as sm
#https://vincentarelbundock.github.io/Rdatasets/datasets.html
mtcars = sm.datasets.get_rdataset(dataname='mtcars', package='datasets')
mtcars.data.head()
df = mtcars.data
df.head()
df
pd.set_option('display.max_rows',32)
df
df.head()
pd.set_option('display.max_columns',15)
df.head()

df.columns
#convert relevant columns to categories
df.dtypes
catCols = ['cyl','gear', 'am','vs','carb']
df[catCols] = df[catCols].astype('category')
df.dtypes
df.describe()   #describes all numeric cols
df.describe(include='category')  #descibe cat coln
df.describe(include='all')  #describe all
#print(list(df.dtypes), end=' ')
#use plot in pandas

#access column
df.mpg #one col
df['mpg']  #one col
df[['mpg','wt']]   #multiple col
df[catCols]
# row
df.iloc[1]  #first row
df.head(2)
df.loc['Mazda RX4']
#row and col
df.mpg.plot()  #line
df.cyl.plot()  #line
df.cyl.plot(kind='bar')  #line #error because no total
df.cyl.value_counts()
df.cyl.value_counts().plot(kind='bar')
df.mpg.plot(kind='hist')
#other plots
#‘line’ : line plot (default)
#‘bar’ : vertical bar plot
#‘barh’ : horizontal bar plot
#‘hist’ : histogram
#‘box’ : boxplot
#‘kde’ : Kernel Density Estimation plot
#‘density’ : same as ‘kde’
#‘area’ : area plot
#‘pie’ : pie plot
#‘scatter’ : scatter plot
#‘hexbin’ : hexbin plot

#https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.plot.scatter.html

#barplot
df.cyl.value_counts().plot.bar()
df.cyl.value_counts().plot(kind='bar', color='y')
df.gear.value_counts().plot.barh()
df.gear.value_counts().plot(kind='barh', color='green')
df.gear.value_counts()
df.groupby('gear').groups #which car in which group
df.groupby('gear').size()
df.groupby('gear').size().plot.bar()
df.groupby('gear').size().plot.bar(colormap='Paired')
df.groupby('gear').size().plot.bar(color=['r','g','y'])
df.groupby('gear').size().plot.bar(color=['r','g','y'])

df.groupby('gear').size().plot(kind='barh')
df.groupby(['gear','cyl']).size()
df.groupby(['gear','cyl']).count()['am']  #not very simple 
df.groupby(['gear','cyl']).count()['am'].plot.bar() #not very simple
df.groupby(['gear','cyl']).count()['am'].unstack()  #better to see
df.groupby(['gear','cyl','am']).size().plot(kind='barh', color='g')
#gear, cyl, am
df.groupby(['am','vs']).size().plot.bar()
df.groupby(['gear','cyl']).size().plot.barh()

#Histogram
df.mpg.hist()  #call directly
df.mpg.plot(kind='hist')
df.mpg.plot(kind='hist')  #call by method and pass kind
df.mpg.hist(bins=5)
df.mpg.plot(kind='hist',bins=20)
#df[['mpg','cyl']].groupby('cyl').level(0)
df.groupby('cyl')['mpg'].plot(kind='hist' , legend=True)  # correct

#Line Plot
df.mpg.plot.line()  #x axis is row labels
df.mpg.plot(kind='line')
df.plot.line(x='mpg', y='wt' )  #x axis is mpg, y is wt #not correct
#mpg is not sorted
df.sort_values('mpg').plot.line(x='mpg', y='wt')  #method1
df.sort_values('gear').plot.line(x='gear', y='mpg')  #as gear increases, mileage increases
df.sort_values('wt', ascending=False).plot.line(x='wt', y='mpg') 
#as wt increases mileage goes down
df.sort_values('wt', ascending=False).plot(kind='line', x='wt', y='mpg')  #method2


#Scatter Plot
df.plot.scatter(x='wt',y='mpg', figsize=(8,6)) #fig size 
df.plot(kind='scatter', x='wt',y='mpg', c='cyl', figsize=(8,6), legend=True) #fig size 
df[['mpg', 'wt', 'cyl']].plot(kind='scatter', x='mpg', y='wt', c='cyl', legend=True)

#Box Plot 
df.plot.box()  #all numeric columns
df.mpg.plot.box()
df.mpg.plot(kind='box', figsize=(10,8))

#Hexagonal Plot
#hexagons at intersecting data ponts x & y
df.plot.hexbin(x='wt',y='mpg', gridsize=30, figsize=(8,6)) #Method2
df.plot(kind ='hexbin', x='hp',y='mpg', gridsize=30, figsize=(8,6)) #method2


#Kernel Density Plot
#one column at a time
df.mpg.plot.kde()
df.wt.plot(kind='kde')

#area plot
df.sort_values('gear', ascending=False).plot.area(x='gear', y='mpg')  #method1
df.sort_values('wt', ascending=False).plot(kind='area', x='wt', y='mpg')  #method2


#pie plot
df.am.value_counts().plot.pie()
df.cyl.value_counts().plot(kind='pie')



#https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.plot.html

#Extras
df[['mpg','cyl']].groupby('cyl').mean()
df[['mpg','cyl']].groupby('cyl').mean().plot(kind='barh')
df[['mpg','cyl']].groupby('cyl').groups

df.mpg.plot(kind='box')
df.groupby('cyl')['mpg'].plot(kind='box')
df.groupby('cyl').size().plot(kind='area')

