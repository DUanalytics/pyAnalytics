# -*- coding: utf-8 -*-
#Pivota table
#-----------------------------
#%

import pandas as pd
import numpy as np

df1 = pd.read_excel('data/pythondata.xlsx',2)
df1.head()

df1.columns
df1.dtypes
catcolumns1=['gender', 'cat', 'class12', 'batch','course','branch','city', 'finalgrade', 'btechfinal']

df1[catcolumns1] = df1[catcolumns1].astype('category')
df1.columns
#groupby
df1.groupby('gender')['branch'].size()
df1.groupby('gender')['java'].mean()
df1.columns

#using pivot table : index, left columns , top columns
df1.columns
df1.pivot_table('java','gender', columns='branch')
df1.pivot_table(['java','dbms'],'gender', columns='batch')
df1.pivot_table(values= ['java','dbms'], index=['gender'], columns=['batch','branch'])
#df.pt (values, index, columns)
df1.pivot_table(index=['branch'], columns=['gender','admyr'],  aggfunc ={'java':np.mean,'vlsi':min})

#more practise
#http://www.datasciencemadesimple.com/create-pivot-table-pandas-python/
