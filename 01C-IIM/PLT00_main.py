#python : Topic :Graphs on mtcars

#standard libaries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pydataset import data
import seaborn as sns

df = data('mtcars')
df.describe()
df.head()
df.columns
df.dtypes

#scatter
plt.scatter(x=df.wt, y=df.mpg, color='red', marker='o')
plt.show();
help(plt.scatter)
#plot2
df['wt']; df['mpg']
size1 = df['hp'].to_numpy() 
plt.scatter(x='wt', y='mpg', data=df, s=size1)
plt.xlabel('Weight')
plt.ylabel('Mileage')
plt.show();

#color, transparency, shape
plt.scatter(x='wt', y='mpg', s='hp', alpha=.5, c='carb', data=df)
plt.show();

#histogram
plt.hist(x=df.mpg, bins=5)
plt.show();

plt.hist(x=df.mpg, bins=[0,15,20,24,27,35,50])
plt.show();

plt.hist(x=df.mpg, bins=[0,15,20,22,25,30,35,40,50])
plt.show();

#barplot
gearSum = df.groupby('gear').size()
gearSum
plt.bar(x=['G3','G4','G5'], height = gearSum)
plt.show();

plt.barh(y=['G3','G4','G5'], width = gearSum)
plt.show();


#pie
plt.pie(x=gearSum, labels=['G3','G4','G5'])

#pair
sns.pairplot(df[['wt', 'mpg','hp']])
plt.show();


#boxplot
sns.boxplot(x=None, y=df['mpg'])
sns.boxplot(x=df['gear'], y=df['mpg'])
sns.boxplot(x=df['carb'], y=df['mpg'], color='g')

#heatmap
df.corr()
sns.heatmap(df.corr(), annot=True)

plt.figure(figsize=(15,10))
sns.heatmap(df.corr(), annot=True)


#line plot
plt.plot([1,2,4,5], [10,3,2,4])
plt.plot(df.wt, df.mpg)
#first sort wt, and then plot
plt.plot([2010, 2011,2012, 2013], [10,13,12,14])

df.sort_values(by='wt')  #temporary
df.sort_values(by='wt', inplace=True, ascending=True)  #permanent
df.head(10)
plt.plot(df.wt, df.mpg)


#cat plot
#for discreete values
sns.countplot(x="gear", data=df)
sns.countplot(y="gear", data=df, hue="carb")  #horis
sns.countplot(x="am", data=df, hue="carb")  #vertical
sns.countplot(x="carb", data=df, palette="Set3")
sns.catplot(x="gear", data=df, hue="gear", col='am', kind='count', height=4)  #vertical + matrix

#barplot
plt.bar?
gearSum = df.groupby('gear').size()
plt.bar(x=['G3','G4','G5'], height=gearSum)
plt.show();

plt.barh(y=['G3','G4','G5'], width=gearSum)
plt.show();
#pie
plt.pie?
plt.pie(labels=['G3','G4','G5'], x=gearSum)
plt.show();

#pair
sns.pairplot(df[['mpg','wt','hp']])
plt.show();

#heatmap
fig = plt.figure(size=(30,20))
sns.heatmap(df.corr(), annot=True)
plt.show();

gearCarb = df[['gear','carb']].pivot('gear','carb')
gearCarb
gearCarb2 = gearCarb.reset_index()
sns.heatmap(gearCarb2, center=0)

#box plot
sns.boxplot(y='mpg', data=df)
sns.boxplot(x='am', y='mpg', data=df)
sns.swarmplot(x='carb', y='mpg', data=df)
sns.violinplot(x='gear', y='mpg', data=df)


#end.. practise with other datasets