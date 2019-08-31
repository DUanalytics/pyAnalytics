#% mtcars - pivot Table
#Group By / Pivot Table
#%

import pandas as pd
import numpy as np

#import data
df3 = pd.read_csv('data\mtcars.csv')
df3.head()
df3.columns

#groupby

df3.groupby('cyl')
df.groupby('cyl')['mpg'].mean()
df1.groupby('cyl')[['mpg','hp','wt']].mean()
df1.groupby('cyl').describe()
df1.groupby('cyl').describe().unstack()

#multiple groups
df1.groupby(['cyl','gear'])
df1.groupby(['cyl','gear']).aggregate(['mean'])
df1.groupby(['cyl','gear']).size().unstack(fill_value=0)
#value counts works on series
df1.cyl.value_counts()

df2.pivot_table(index=['cyl'], columns='gear', aggfunc='size', fill_value=0)