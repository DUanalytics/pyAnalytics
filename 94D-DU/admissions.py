#EDM - test
#-----------------------------
#%
https://pandas.pydata.org/pandas-docs/stable/user_guide/advanced.html

import pandas as pd
import numpy as np

#--------------
df = pd.read_csv('E:/rWork/rProjects/edm2/data/admStatus.csv', skiprows=1)
df
pd.read_csv?
colNames = df.columns
colNames, len(colNames)
colNames1 = colNames.to_list()
print(colNames1, end =' ,')
colLevel0 = colNames1[0:5] + colNames1[14:15]  + colNames1[20:24] + colNames1[15:21] + colNames1[5:14] 
print(colLevel0, end =' ,')
colLevel1 = ['Admission'] * 9 +  ['Personal'] * 4 + ['Others'] * 2 + ['Dates'] * 9
# [i for i in range(1,10)  ]
print(colLevel1, end =' ,')

#----------
df.head()
df.set_index('gender')
df1 = df[colLevel0]
df1
#
dfcol = pd.DataFrame({'Level1': colLevel1, 'Level0':colLevel0})
dfcol
data = df1.values
data

data1 = pd.DataFrame(df1.values, columns= pd.MultiIndex.from_frame( dfcol))
data1.head(2)
data1.columns

#del df.columns.name
del data1.columns.gender
data1.rename_axis(axis=1).head(1)
data1.set_index('gender')
data1.head(2)
data1.loc[: , [slice('Dates'),slice('sopDate')]].head(1)
(slice(None),slice(2012,2012)

data1.query("Admission > 1")
data1.loc[: , (slice(None), 'gender')]
data1.loc[: , ('Dates', slice(None))]
data1.loc[: , ('Admission', ['applMode','formNo'])]
data1.loc(axis=1)[:, ['applMode', 'formNo']]

data1.xs('formNo', level='Admission', axis=1)
data1.loc[:, (slice(None), 'formNo')]
https://pandas.pydata.org/pandas-docs/stable/user_guide/advanced.html

['Admission'] * 9 +  ['Personal'] * 4 + ['Others'] * 2 + ['Dates'] * 9