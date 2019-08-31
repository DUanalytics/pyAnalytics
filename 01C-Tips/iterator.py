#Topic: iterator
#-----------------------------
#libraries
#https://medium.com/@formigone/stop-using-df-iterrows-2fbc2931b60e
#df.iterrows() yields a Pandas Series, and df.itertuples() yields a named tuple. The API is still the same to access elements in the object yielded at each iteration.Also, wrapping enumerate doesn’t affect the performance of df.itertuples() ,
#One of the claims was that df.itertuples() should be used instead of df.iterrows()

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#df = pd.read_csv('data/mtcars.csv')
from pydataset import data
mtcars = data('mtcars')
mtcars.head()
df = mtcars


#Iterate over rows
#http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.iterrows.html
#terate over DataFrame rows as (index, Series) pairs.
for index, row in df.iterrows():    print(index, row['mpg'], row['wt'])

#itertuples : Iterate over DataFrame rows as namedtuples.
for row in df.itertuples():     print(row)
#By setting the index parameter to False we can remove the index as the first element of the tuple:
for row in df.itertuples(index=False):    print(row)    
#With the name parameter set we set a custom name for the yielded namedtuples:
for row in df.itertuples(name='MTCARSdata'):     print(row)   
#no space in MTCARsdata, any name 
#The column names will be renamed to positional names if they are invalid Python identifiers, repeated, or start with an underscore. 
