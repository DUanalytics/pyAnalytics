#Pandas DF Properties
#-----------------------------
#%

#mtcars
from pydataset import data
mtcars = data('mtcars')
mtcars.head()

df = mtcars
type(df)

#properties of DF

#df.get_dtype_counts()
df.select_dtypes(include='float64')
df.select_dtypes(include='int64')
df.select_dtypes(include='category')

#column names
df.filter(like='gear').head()

df.rename(columns={'am':'Car_Tx', 'vs':'Car_EngineType'}, inplace=True)
df.columns
df.filter(regex='\d')
#columns that have number



#set index
df.shape
df.head()

#rows
df.iloc[2:4]
df.iloc[2]
df.iloc[1.8]  #error
df.iloc[[1,2,4]]
#
df.loc[1]


#rows and columns
df.iloc[ : , [1,3,5]]
df.iloc[ 1:10:2 , [1,3,5]]
df.iloc[ 1:10:2 , 1:5:1]
df.columns
df.loc[ : , ['hp','gear']]
df.loc['Mazda RX4' , ['hp','gear']]  #use names
df.iloc[[1,5], [3,5]]
df.iloc[8:2:-2, 2]
df.iloc[8:2:-2, 2:5]
df.loc[1:5:2, 'gear'] #not working
df.iloc[ :3]  #first 3 rows
df.iloc[ :4, :3]  #first 4 rows, first 3 columns
df.iloc[ :4, :]  #first 4 rows, all columns
df.index

#get postion of columns and then filter
df.columns
colStart = df.columns.get_loc('cyl')
colEnd = df.columns.get_loc('wt')
df.iloc[ :4, colStart:colEnd]

#index of rows
df.index
df.index[3]
rowStart = df.index[3]
rowEnd = df.index[7]
df.loc[ rowStart:rowEnd, ]
df.columns
df.loc[ rowStart:rowEnd, 'cyl':'wt']


#.iat and .at, are much more faster than .iloc and .loc for selecting a single element from a DataFrame.
df.at['Mazda RX4', 'cyl']
#cylinder of this car

#get locations
df.index
df.index.get_loc('Mazda RX4')
rownum = df.index.get_loc('Honda Civic')
colnum = df.columns.get_loc('gear')
rownum, colnum
df.iloc[ rownum, colnum]
df.iat[ rownum, colnum]


#column start with
df.columns
df['carnames'] = df.index
df.columns
df.carnames
df.carnames.str.contains('^M')
df[df.carnames.str.contains('^M')]
#carnames starting with M
df[df.carnames.str[0]=='C']
df.columns
df.loc[df.iloc[:,11].str.contains(r'(Maz|Hon)')]
#11th column, names Maz or Hon

df.filter(["mpg", "gear", "hp"]) 
df.filter(regex ='[aA]') #columns with a or A
#show columns using RegEx filter (a|A) - a or A 
df.filter(regex ='[g]').head()

df.filter(like ='g').head()
#show columns containing letter 'g'
#DataFrame.filter(items=None, like=None, regex=None, axis=None)
#items : List of info axis to restrict to (must not all be present)
#like : Keep info axis where “arg in col == True”
#regex : Keep info axis with re.search(regex, col) == True
#axis : The axis to filter on. By default this is the info axis, ‘index’ for Series, ‘columns’ for DataFrame# Returns : same type as input object

df.ix[:, ~df.columns.str.contains('^m|g|c')]
#show all columns except those beginning with m/g/c (in other word remove / drop all columns satisfying given RegEx)


#dual condition
df.columns
df.loc[(df["mpg"] > 25 ) & (df["gear"]== 4)]

import numpy as np
def meanValue(x): return np.mean(x)
def sumValue(x): return np.sum(x)

df[['mpg','hp']].apply(meanValue, axis=0)
#mean of columns ; mean of each subject marks
df.index
df[['mpg','hp','wt']].apply(sumValue, axis=1)
#rowwise sum : studentwise sum of marks

from scipy.stats import mode
df.gear.value_counts()
print(mode(df['gear']))
mode(df['gear']).mode[0]


#Sorting
df_sorted = df.sort_values(['gear','mpg'], ascending=False)
df_sorted
df_sorted[['gear','mpg']]

df_sorted2 = df.sort_values(['gear','mpg'], ascending=[False,True])
df_sorted2[['gear','mpg']]


#
import matplotlib.pyplot as plt
df.boxplot(column="mpg",by="gear")
df.boxplot(column="mpg",by=["gear","cyl"])
df.hist(column="mpg",by="gear",bins=30)


#
import pandas as pd
data = pd.read_csv('data/mtcars.csv')
colTypes = pd.DataFrame({'feature':['mpg','disp','hp','drat', 'wt','qsec', 'cyl','vs', 'am', 'gear','carb','carname'], 'atype':['float64','float64', 'float64', 'float64', 'float64', 'float64', 'category', 'category', 'category', 'category','category','object']})
colTypes
data.columns
colTypes
list(colTypes.feature)
def valueType(name):
    return colTypes.loc[colTypes['feature'] == name, 'atype'].iloc[0]
valueType('gear')

for i in data.columns:
    if i in list(colTypes.feature):
        print(i, 'Yes')
        print(i, valueType(i))
        data[i] = data[i].astype(valueType(i))
    else:
        print(i, 'No')

data.dtypes
colTypes.dtypes
colTypes.assigntype
#https://www.analyticsvidhya.com/blog/2016/01/12-pandas-techniques-python-data-manipulation/
#conver by columnames to differnt types