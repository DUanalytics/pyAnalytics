#Iter over rows
#-----------------------------
from pydataset import data
mtcars = data('mtcars')
mtcars.head()
import pandas as pd
import numpy as np
df5 = mtcars

z = []
for index, row in df5.iterrows():
    z.append(row.mpg + row.hp)
z

z2 = [ row.mpg + row.hp for index, row in df5.iterrows() ]
z2
df5.apply(lambda row: row.mpg + row.hp, axis=1)


#vectorised ops
df5.mpg * 2
df5.mpg + df5.hp


df5.groupby(['gear','carb'])['cyl'].value_counts().unstack().fillna(0)

#https://towardsdatascience.com/pandas-tips-and-tricks-33bcc8a40bb9
df = df.sort_values(by=['name','timestamp'])
df['time_diff'] = df.groupby('name')['timestamp'].diff()