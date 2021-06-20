#Topic: Missing Values in Python
#-----------------------------
#libraries

import numpy as np
import pandas as pd

#url = 'data/missingdata1.csv'
url = 'https://raw.githubusercontent.com/DUanalytics/pyAnalytics/master/data/missingdata1.csv'
df = pd.read_csv(url)
df

#missing data - NaN
#na is not missing, it is a text
df.head()
df.describe(include='all')
#
#ST_NUM: Street number
#ST_NAME: Street name
#OWN_OCCUPIED: Is the residence owner occupied
#NUM_BEDROOMS: Number of bedrooms


#better values could be
#ST_NUM: float or int… some sort of numeric type
#ST_NAME: string
#OWN_OCCUPIED: string… Y (“Yes”) or N (“No”)
#NUM_BEDROOMS: float or int, a numeric type

#missing values
# Looking at the ST_NUM column
df['ST_NUM']   #display all values of column
df['ST_NUM'].isnull()  # T / F : T - missing data
df['ST_NUM'].isnull().sum()  #how many missing

#In this column, there’s four missing values.n/a, NA, —, na
df
df.isnull().sum()  #how many missing in each column
df['NUM_BEDROOMS'].isnull()
df['NUM_BEDROOMS']   #2. 5. 8 are missing, but 8 is not showing
df.NUM_BEDROOMS.value_counts()
np.mean(df.NUM_BEDROOMS)

#we can specify at the time of import as which type of values to mark missing
# Making a list of missing value types
missing_values = ["n/a", "na", "--"]
df2 = pd.read_csv(url, na_values = missing_values)
df2
df
df['NUM_BEDROOMS'].isnull().sum()
df2['NUM_BEDROOMS'].isnull().sum()

#any missing values
df2
df2.isnull().values.any()

#Total number of missing values
df2.isnull().sum().sum()
df2.isnull().sum(axis=0)  #column
df2.isnull().sum(axis=1)  #row

#%%%replacing Missing values
# Replace missing values with a number
df2['ST_NUM']
df2['ST_NUM'].fillna(125, inplace=True)
df2

# Location based replacement
df2.loc[2,'ST_NUM'] = 300
df2

# Replace using median 
df2['NUM_BEDROOMS']
df2['NUM_BEDROOMS'].median()
median = df2['NUM_BEDROOMS'].median()
median
df2['NUM_BEDROOMS'].fillna(median, inplace=True)
df2
df2
df2.dropna(axis=1) #remove col having missing values
df2.dropna(axis=0) #remove rows having missing values
df2
df2.dropna(axis=0,thresh=1, subset=None, inplace=False) #threshold

#https://towardsdatascience.com/data-cleaning-with-python-and-pandas-detecting-missing-values-3e9c6ebcf78b
#https://thispointer.com/pandas-drop-rows-from-a-dataframe-with-missing-values-or-nan-in-columns/
#https://stackoverflow.com/questions/45515031/how-to-remove-columns-with-too-many-missing-values-in-python
