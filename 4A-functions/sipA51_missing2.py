#Missing Values
#-----------------------------
#%#handling missing values
#find, row, col, total, #import, #handle, replace (techniques)

# import the pandas library
import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randint(40,100, size=(5, 3)), index=['Rahul', 'Tanisha', 'Vijay', 'Hitesh', 'Priyanka'],columns=['HR', 'MM', 'Stats'])
df
#add blank rows by adding indexes - b, d, g
df = df.reindex(['Saksham','Rahul', 'Pooja','Tanisha','Arunabh', 'Vijay','Rakhi', 'Hitesh', 'Priyanka','Yash'])
df
#Using reindexing, we have created a DataFrame with missing values. In the output, NaN means Not a Number.

#o make detecting missing values easier (and across different array dtypes), Pandas provides the isnull() and notnull() functions, which are also methods on Series and DataFrame objects 
df.isnull()  #cell wise 
df.notnull()
df.isna() 
df.isna() == df.isnull()
df.isna() == df.notnull()

#
df
df.HR.isnull() # missing in HR 
df.MM.isnull().sum()  #how many missing in HR col
df.isnull().sum() # how many missing in data frame
df.MM.sum()
#filling missing values
df.HR.fillna(0, inplace=True)
df.HR.fillna(np.random.randint(10,200))
df  #set column one

df.fillna(99)  #only show not replaced
df.fillna(99).isnull().sum()  #no missing values now

#filling missing values fwd / reverse left / right
#Fill NA Forward and Backward
#pad/fill- Fill methods Forward
#bfill/backfill- Fill methods Backward
df
df.fillna(method='pad') #same column, fill fwd (first row is not filled)
df.fillna(method='backfill')  #yash is left out
df.fillna(method='backfill', axis=1)
#drop missing values
df
df.dropna()
df.dropna(axis=0)  #keep only complete rows
df
df.dropna(axis=1) #col which is complete

df
#replace generic values
df2 = pd.DataFrame({'subject1':[10,20,30,40,50,2000], 'subject2':[1000,0,30,40,50,60]})
df2 #these values of 1000 and 2000 are not correct

df2.replace({1000:10,2000:60})

assert pd.isnull(df2).all().all()

#%%
df
df.describe()
df.info()
#%%
df['MM']
df['MM'].replace(np.nan, 0)  #replace missing values with 0
#or vice versa
df['MM'].replace(np.nan, 0, inplace=True)
df
df['MM'].replace(0, np.nan, inplace=True)  #0 may mean missing
df

#%%%
#arithmetic on missing values
df.HR.mean()
df.MM.mean()  #R does not allow this. na.rm=T required
df
meanMM = df.MM.mean()
meanMM
df
df['MM'].fillna(74.2, inplace=True)
df
df['HR'].fillna(meanMM, inplace=True)
df['Stats'].fillna(80, inplace=True)

df
#%%%
df.mean(axis=0)  #col
df.mean(axis=1)  #col
df.isna()
df

#%%%
#fill missing values with random values
df2=df
df2
import random
df3=df2.fillna(random.random()* 100)
df3
df = df.apply(lambda x: x.fillna(np.random.choice(x.dropna())), axis=1)
df2

df["HR"].fillna(lambda x: random.choice(df[df['HR'] != np.nan]["HR"]), inplace =True)
df

df['HR'].apply(lambda x: np.random.choice([x for x in range(min(df['HR']),max(df['HR'])]) if (np.isnan(x)) else x))
#
import numpy
dataset = read_csv('pima-indians-diabetes.csv', header=None)
# mark zero values as missing or NaN
dataset[[1,2,3,4,5]] = dataset[[1,2,3,4,5]].replace(0, numpy.NaN)
# count the number of NaN values in each column
print(dataset.isnull().sum())










#https://machinelearningmastery.com/handle-missing-data-python/
#https://www.tutorialspoint.com/python_pandas/python_pandas_missing_data.htm


df.apply(lambda x: sum(x.isnull().values), axis=0) # columns
df.apply(lambda x: sum(x.isnull().values), axis=1) # rows
sum(df.apply(lambda x: sum(x.isnull().values), axis=1) >= 1) # rows with NA > 1
sum(df.apply(lambda x: sum(x.isnull().values), axis=1) >= 0) # rows with NA > 1
