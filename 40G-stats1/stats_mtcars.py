#Topic ----Basic Statistics using mtcars

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pydataset import data
mtcars = data('mtcars')
data=mtcars
data.head()
data.columns
data.dtypes
data.shape
#%%% Set display options
pd.get_option('display.max_columns')
pd.set_option('display.max_columns',12)
pd.set_option('display.width', 1000)
#pd.reset_option("^display")
data.head()

#%%% Mean of column /rows
mean([1,2,3,10]) #mean not defined in base python
np.mean([1,2,3,10])
np.mean(data.mpg)
data.mpg.mean()
data['mpg'].mean()
data[['mpg','hp','wt']].mean()
data.mean()
data.mean(axis=0)
data.mean(axis=1)
data.groupby('cyl').mean()
data.groupby('cyl').mean().apply(lambda x: round(x, 1))
#df.mean(axis = 1, skipna = True) #with missing values
#%%%
data.mpg #single column is series
#data.mpg.sort()  #depreciated 
data.mpg.sort_values()
data['mpg'].sort_values()
data.mpg.sort_values().iloc[15]
data.mpg.sort_values().iloc[[0,7,15,23,31]]
data[['mpg','wt']].median(axis=0)
data.median(axis=0)  #columns mean
#df.median(axis = 1, skipna = True) #with missing values
#%% Mode - Value with max frequency
data.gear.value_counts()
data.groupby('gear').size()  #how many of each gear type
pd.value_counts('cyl')  #3 cylinder types
data.groupby('cyl').size()
data.groupby('cyl').size().sort_values(ascending=False).head(1)
data.mode()
data[['cyl','gear','am','vs','carb']].mode()
data.carb.value_counts()  #2 modes in carb

import statistics  #single column, single mode
statistics.mode(data.cyl)
statistics.mode(data.carb)#error

#%%Links
#https://www.geeksforgeeks.org/finding-mean-median-mode-in-python-without-libraries/

#%% Quantiles
#uantile() function return values at the given quantile over requested axis, a numpy.percentile. 
#data.quantile?
data.quantile(q=.5) #default 50%
data.quantile([0,.25, .50, .75, 1.0]) #quartiles
data.quantile(np.arange(0,1,.1))  #decile
data.quantile(np.arange(0,1,.01))  #percentile
data.quantile([.1,.5, .9], numeric_only=True, axis=0) #selected percentile
data.mpg.quantile([0,.25, .50, .75, 1.0]) #numpy single column 

#for dates ??
#Links
#https://www.geeksforgeeks.org/python-pandas-dataframe-quantile/
#https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.quantile.html
#https://www.geeksforgeeks.org/numpy-quantile-in-python/
#%%% Plot - Class Interval, Histogram & Density
pd.cut(data.mpg, bins=5, right=True, labels=None, include_lowest=False)
pd.cut(data.mpg, bins=5, labels=['L1','L2','L3','L4','L5'])
data['Weight'] = pd.cut(data.wt, bins=3, labels=['Low','Medium','High'])
data.Weight.value_counts().plot.bar()
pd.cut(data.wt, bins=3, labels=['Low','Medium','High']).value_counts().plot.bar()
#Link:http://benalexkeen.com/bucketing-continuous-variables-in-pandas/
#another plot
h1= data.Weight.value_counts()
h1
plt.bar(['Low Wt','Medium Wt','High Wt'], h1, label="Count of Weight Category")
plt.legend(loc='best')
plt.xticks(rotation = 90)
plt.show()

#%% Histogram
data.mpg.plot(kind='hist')
data.wt.plot(kind='hist', bins=3)
data.Weight.value_counts().plot.bar() #same, order of category is changed
plt.hist(data.wt, bins = 5, stacked=True, normed=True, color='green' )
color=['red','green','blue','purple','black']
import seaborn as sns
sns.distplot(data.wt);
sns.distplot(data.wt, kde=False, rug=True);  #no curve, rug lines at bottom
sns.distplot(data.mpg, bins=20, kde=False, rug=True); #more bins, no curve
sns.distplot(data.mpg, hist=False, rug=True); #without density
sns.jointplot(x="wt", y="mpg", data=data);
sns.jointplot(x="wt", y="mpg", data=data, kind="kde");
sns.jointplot(x="x", y="y", data=df, );
#Links:https://seaborn.pydata.org/tutorial/distributions.html
f, ax = plt.subplots(figsize=(6, 6))
sns.kdeplot(data.wt, data.mpg, ax=ax)
sns.rugplot(data.wt, color="g", ax=ax)
sns.rugplot(data.mpg, vertical=True, ax=ax);
#%% Pair Plot
sns.pairplot(data[['wt','mpg', 'hp', 'qsec']]);
#%%% 


#%%%
#%%%outliers
#In statistics, an outlier is an observation point that is distant from other observations.
sns.boxplot(x=data['mpg'])
#The Z-score is the signed number of standard deviations by which the value of an observation or data point is above the mean value of what is being observed or measured
#Links: https://towardsdatascience.com/ways-to-detect-and-remove-the-outliers-404d16608dba
from scipy import stats
import numpy as np
z = np.abs(stats.zscore(data.mpg))
print(z)
threshold = 3
print(np.where(z > 3))  #no outliers
#Another way : IQR
Q1 = data.mpg.quantile(0.25)
Q3 = data.mpg.quantile(0.75)
Q1,Q3
IQR = Q3 - Q1
print(IQR)
#The data point where we have False that means these values are valid whereas True indicates presence of an outlier.
np.where((data['mpg'] < (Q1 - 1.5 * IQR)) | (data['mpg'] > (Q3 + 1.5 * IQR)))
data.iloc[15:20,0:5]  #toyota Corolla MPG is outlier
#what to do with outliers - Remove the row 
#Links
#https://www.analyticsvidhya.com/blog/2019/02/outlier-detection-python-pyod/
#http://colingorrie.github.io/outlier-detection.html
#https://www.dasca.org/world-of-big-data/article/identifying-and-removing-outliers-using-python-packages

#%%%Range and interquartile range
#range() is commonly used in for looping hence, knowledge of same is key aspect when dealing with any kind of Python code.
range(1,10,2)  #nothing
for i in range(6) : print(i, end=', ')
min(data.mpg), max(data.mpg)

#IQR
Q1= data.mpg.quantile(.25)
Q2= data.mpg.quantile(.5)  #median
Q3= data.mpg.quantile(.75)
Q1, Q2, Q3
IQR = Q3- Q1
IQR

from scipy.stats import iqr
iqr(data.mpg)  #numpy array
data[['mpg','wt','hp']].values
iqr(data[['mpg','wt','hp']].values, axis=0)  #multiple columns

#%%% Std Deviation, Correlation , Covariance, Variance
np.std(data.mpg)
#Links : https://docs.scipy.org/doc/numpy/reference/generated/numpy.std.html
np.std(data[['mpg','wt','hp']].values, axis=0) 

data.std(axis = 0, skipna = True) #diff with np.std
#Links : https://www.geeksforgeeks.org/python-pandas-dataframe-std/

#%%Missing Values
url1 = 'https://raw.githubusercontent.com/DUanalytics/datasets/master/csv/mtcars3.csv'
data2 = pd.read_csv(url1)
data2a = data2.copy()
#Sources of Missing ValuesBefore we dive into code, it’s important to understand the sources of missing data. Here’s some typical reasons why data is missing:
#User forgot to fill in a field.
#Data was lost while transferring manually from a legacy database.
#There was a programming error.
#Users chose not to fill out a field tied to their beliefs about how the results would be used or interpreted.
data2a.describe()
data2a.isnull() #True for missing locations
data2a.isnull().sum(axis=0)  #columnwise sum
data2a.isnull().sum(axis=1)  #rowwise sum
data2a.qsec.isnull()  #particular column
data2a.isnull().values.any()  #any missing value in dataset
data2a.isnull().sum().sum()  #total missing values
sum(data2a.isnull().values.ravel())
#https://www.geeksforgeeks.org/numpy-ravel-python/
data2a.isnull().values.ravel().sum()
data2a.qsec.mean()
sum(map(any, data2a.isnull())) #Rows with any missing:
data2a.isnull().sum(axis=1)  #rowwise sum
#Replacing
data2a['qsec']
data2a['qsec'].fillna(17, inplace=False)
data2a['qsec']
data2a['qsec'].fillna(17, inplace=True)
data2a['qsec']

data2a['wt'].fillna(data2.median, inplace=True)
data2a.isnull().sum()
sum(data2a.isnull().values.ravel())
#method - bfill, ffill
#fillna( method ='ffill', inplace = True)
#fillna( method ='ffill', limit = 1, inplace = True) 
data2b = data2.copy()
data2b.isnull().sum()
data2b.fillna(method='ffill', inplace=False)
data2b.fillna(method='ffill', limit=1, inplace=False)
data2b.fillna(data2b.mean(), inplace=False)

#%%%Skewness
data.head
#kew(axis=None, skipna=None, level=None, numeric_only=None
data.skew(axis = 0, skipna = True) 
#skewness = 0 : normally distributed.
#skewness > 0 : more weight in the left tail of the distribution.
#skewness < 0 : more weight in the right tail of the distribution.
data.mpg.skew(skipna = True) #right skewed
sns.kdeplot(data['mpg'])
sns.kdeplot(data['cyl']) #not correct as this is category

iris = sns.load_dataset('iris')
iris.skew()
plt.figure(figsize=(10,10))
plt.subplot(2, 2, 1)  #row, col, position
sns.kdeplot(iris['sepal_width'])
plt.subplot(2, 2, 2)
sns.kdeplot(iris['sepal_length'])
plt.subplot(2, 2, 3)
sns.kdeplot(iris['petal_length'])
plt.subplot(2, 2, 4)
sns.kdeplot(iris['petal_width'])
plt.show();




#%%%Kurtosis -  degree of peakedness of a distribution” 
data.kurtosis(axis = 0, skipna = True) 
iris.kurtosis()

#Negative - Flat
#Near 0  - Normal
#Positive - Peak
#Links : https://www.geeksforgeeks.org/scipy-stats-kurtosis-function-python/
#https://www.spcforexcel.com/knowledge/basic-statistics/are-skewness-and-kurtosis-useful-statistics
#https://stackoverflow.com/questions/45483890/how-to-correctly-use-scipys-skew-and-kurtosis-functions