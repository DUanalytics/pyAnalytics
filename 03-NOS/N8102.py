#python : DUP - Topic :N8102 Missing data

#standard libaries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#!pip install pydataset
from pydataset import data
import seaborn as sns

#import data set
from pydataset import data
mtcars = data('mtcars')
mtcars
type(mtcars)
#%%%PC1: define the format and structure for the dataset
mtcars.describe()   #describe
mtcars.shape  #rows and columns
mtcars.count()
mtcars.dtypes
mtcars.head()
mtcars.size
mtcars.axes
mtcars.values


#groupby 
mtcars.groupby(['gear']).count()
mtcars['gear'].value_counts()


#identify data types for each variable of the dataset
mtcars.dtypes
#convert to a dtype ----
mtcars['am'] = mtcars['am'].astype('category')
mtcars.dtypes


#encoding data
mtcars2 = mtcars.copy()
from sklearn.preprocessing import LabelEncoder
L1 = LabelEncoder()
L1.fit(mtcars2['gear'])
mtcars2.gear = L1.transform(mtcars2.gear)
print(mtcars2)
mtcars2.describe()
mtcars2.dtypes
mtcars2.groupby('gear').size()
mtcars2.groupby('gear').count()
mtcars2.isna().sum()
mtcars2.dropna()

#%%%

#define indexes and organize variables as per the defined forma
mtcars.index   #row values
mtcars.sort_index()  #sort DF by rownames
mtcars.sort_index(ascending=False)  #sort by desc rownames
mtcars.iloc[1] # first row with index integer
mtcars.iloc[1:4]  #1st to 4th row
mtcars.iloc[1:4, 3:6]  #1-4 row, 3-6cols
index1 = mtcars.index  #get index values
index1 
mtcars['Mazda RX4':'Merc 450SL']  #from particular row index to other

mtcars3 = mtcars.copy()
mtcars3.set_index('am', append=True)  #add another index
mtcars3.set_index('am', append=False)  #replace index

#%%% define index and organise variables as per the defined format
import pandas as pd
dataForIndex = pd.DataFrame({'city':['Delhi','Delhi','Chandigarh', 'Chandigarh','Chandigarh'], 'institute':['AIIT', 'ABS', 'AIIT', 'ABS', 'ALS']})
dataForIndex
indexFromDF = pd.MultiIndex(levels=dataForIndex, codes=[[0,0,1,1,1], [0, 1, 0, 1, 2]])
midx = pd.MultiIndex(levels=[['Delhi', 'Chandigarh'], ['AIIT', 'ABS', 'ALS']],codes=[[0,0,1,1,1], [0, 1, 0, 1, 2]])
midx
d = [[100,120],[75,70],[120,105],[90,65],[80,55]]
d
df = pd.DataFrame(index=midx, columns=['Male', 'Female'], data=d)
df
df.index
df.drop(index='ABS')
df.drop(columns=['Male'], axis=1)
df.drop(index=['Delhi'], axis=0)
df.drop(index='ABS',level=1,axis=0)
df.drop(index='Delhi',level=0,axis=0)
df.drop(index=['Delhi','Chandigarh'],level=1,axis=0)  #no effect
df.drop(index=['Delhi','Chandigarh'],level=0,axis=0)  #no data
df.drop(index=['AIIT'],level=1,axis=0)  #no data

#%%%
#Discrepancies, outliers, skew, deviations from baselines, variance, missing values, bias, inconsistencies

#mean/median/mode----
mtcars.describe()
mtcars.mean()
mtcars.median()
mtcars.gear.mode()
mtcars.gear.value_counts()
import statistics 
statistics.mode(mtcars.mpg)
statistics.mode(mtcars.gear)

#sd and variance ----
mtcars.std()
mtcars.var()
statistics.stdev(mtcars.mpg)
statistics.variance(mtcars.mpg)

#skewness :shape of the distribution
mtcars.columns
mtcars.mpg.skew()  #if 0, it ND
mtcars.mpg.plot(kind='hist')
mtcars.mpg.plot(kind='density')
mtcars.skew()

#kurtosis :peakedness
mtcars.kurtosis()
mtcars.mpg.kurtosis()

#outliers-----
mtcars.boxplot()
mtcars.mpg.plot(kind='box')
import seaborn as smtcars
sns.boxplot(mtcars.mpg)

np.where(mtcars['mpg'] > 30)  #position of value

import matplotlib.plot as plt
plt.scatter(mtcars.mpg, mtcars.wt)
np.where((mtcars['mpg'] < 12, mtcars['wt'] > 5))
mtcars.iloc[[14,15,16],['mpg','wt']]

#using IQR
import numpy as np
Q1=np.percentile(mtcars.mpg, 25)
Q3=np.percentile(mtcars.mpg, 75)
IQR = Q3- Q1
IQR
from scipy import stats
IQR2 = stats.iqr(mtcars.mpg)
IQR2
upper_bound = Q3 + (1.5 * IQR)
lower_bound = Q1 - (1.5 * IQR)
print(upper_bound, lower_bound)
arr1 = mtcars.mpg
arr1
outliers = [(arr1 <= lower_bound) | (arr1 >= upper_bound)]
outliers
arr1.values[outliers]
mtcars[mtcars.mpg >= 33]

#PC4 : identify and fix missing values in each variable of the dataset

url = 'https://raw.githubusercontent.com/DUanalytics/pyAnalytics/master/data/missingdata1.csv'
MD = pd.read_csv(url)
MD
MD.info
MD.describe(include='all')
MD.isnull()
MD.isnull().sum(axis=0) #col
MD.isnull().sum(axis=1) #row
MD.isnull().sum().sum()  #all
sleep = data('sleep')
sleep.describe
sleep.isna()

#specifying missing values---
missing_values = ['n/a', 'na', '--']
MD2 = pd.read_csv(url, na_values= missing_values)
MD2.isnull().sum().sum()
MD2['ST_NUM'].fillna(125, inplace=True)
MD2
MD2.isnull().sum().sum()

medianRooms = MD2['NUM_BEDROOMS'].median()
medianRooms
MD2['NUM_BEDROOMS'].fillna(medianRooms, inplace=True)
MD2

MD2.dropna(axis=0, thresh=1, subset=None, inplace=False)

#PC5- Identify and fix incorrect data types in each variable of dataset
mtcars.dtypes
#cyl, gear, am, - Category
#carb, vs - integer (INT32)
#dtypes - str
mtcars['cyl'] = mtcars['cyl'].astype('category')
mtcars['carb'] = mtcars['carb'].astype('int')
mtcars.dtypes
mtcars['name'] = mtcars.index
mtcars.dtypes  #str is object type

#PC6 - Sort the data and create subsets of data

mtcars.head()
mtcars.columns
mtcars.sort_values(by='mpg')
mtcars.sort_index(ascending=False, axis=0)
mtcars.sort_index(ascending=False, axis=1)
mtcars.sort_values(by = ['gear','hp'])[['gear','hp']]
mtcars.sort_values(by = ['gear','hp'], ascending=[False,True])[['gear','hp']] 
mtcars.sort_values(by='mpg', inplace=True)
mtcars
#with missing data---
urlsleep ='https://raw.githubusercontent.com/DUanalytics/datasets/master/csv/sleep1.csv'
sleep = pd.read_csv(urlsleep)
sleep.head()
sleep.isna().sum().sum()  #missing values
sleep.isna().sum()
sleep.sort_values(by='NonD')
sleep.sort_values(by='NonD', na_position='first')


#subset data
mtcars.head()
mtcars.mpg
mtcars['mpg']

type(mtcars.mpg)
mtcars.mpg[mtcars.mpg > 25]

mtcars[mtcars.mpg > 25]

mtcars[mtcars['gear'].isin([3,5])]
mtcars[(mtcars['gear']==2) | (mtcars['gear']==5)]

#specific rows/ cols
mtcars.loc[mtcars.gear ==3, ['gear','mpg']]  #label loc
mtcars.iloc[1:4, 2:5] #integer loc

#filter 
mtcars.columns
mtcars.index
mtcars.filter(items=['mpg','gear'])  #col names
mtcars.filter(regex='c$', axis=0) #end with c in rows
mtcars.filter(like='Merc', axis=0) #contains xx in rows 

#PC7 : Perform operations to transform data types of variables as required
mtcarsT = data('mtcars')
df = pd.DataFrame({'A': range(3), 'B': range(1, 4)})
df
df.transform(lambda x: x + 1)  #add 1 to all values
s = pd.Series(range(3))
s
s.transform([np.sqrt, np.exp])

df = pd.DataFrame({"Date": ["2015-05-08", "2015-05-07", "2015-05-06", "2015-05-05", "2015-05-08", "2015-05-07", "2015-05-06", "2015-05-05"], "Data": [5, 8, 6, 1, 50, 100, 60, 120],})
df
df.groupby('Date')['Data'].transform('sum')  #datewise sum

#square DF
d1 = {'col1': [1, 2], 'col2': [3, 4]}
df1 = pd.DataFrame(data=d1)
df1.transpose()

#non-square
d2 = {'name': ['Alice', 'Bob'],    'score': [9.5, 8],  'employed': [False, True],   'kids': [0, 0]}
df2 = pd.DataFrame(data=d2)
df2.T

#scale
iris = data('iris')
iris
df = iris.drop('Species', axis=1)
df.head()
df_norm = (df-df.min())/(df.max()-df.min())
df_norm.head()

from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()
df_scaled = scaler.fit_transform(df.to_numpy())
df_scaled = pd.DataFrame(df_scaled, columns=['sepal_length', 'sepal_width', 'petal_length', 'petal_width'])
df_scaled.head()

from sklearn.preprocessing import StandardScaler
std_scaler = StandardScaler()
df_scaled = std_scaler.fit_transform(df.to_numpy())
df_scaled = pd.DataFrame(df_scaled, columns= ['sepal_length', 'sepal_width','petal_length','petal_width'])
df_scaled.head()
#PC8 : identify and deal with data redundancy by normalising the dataset

data = { "A": ["TeamA", "TeamB", "TeamB", "TeamC", "TeamA"], "B": [50, 40, 40, 30, 50],  "C": [True, False, False, False, True]}
data  
df = pd.DataFrame(data)
df
df.drop_duplicates()
df1 = df.copy()
df1.drop_duplicates(inplace=True)
df1

#remove duplicates from specific col
df.head()
df[df.duplicated()]
df.sort_values(by='A')
df.drop_duplicates(subset='A')
df.drop_duplicates(subset='C')

#PC9 Validate pre-processed data using appropriate tools and processes
mtcars.describe()
mtcars.isna().sum().sum()
mtcars[mtcars.duplicated()]
mtcars.shape



#%%%end here