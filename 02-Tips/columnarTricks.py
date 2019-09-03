#Topic ---- Columnar Tricks
#https://medium.com/@thedatabuddy/pretty-displaying-tricks-for-columnar-data-in-python-2fe3b3ed9b83
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pydataset import data
df = data('mtcars')

df.head()
df.columns
df.dtypes
df.shape

pd.options.display.max_columns = None
pd.options.display.width=1000
#%%%
df
from tabulate import tabulate
print(tabulate(df,headers='firstrow'))

#%%%
from tabulate import tabulate
pdtabulate=lambda df:tabulate(df,headers='keys')
print(pdtabulate(df))
data.head()
print(pdtabulate(df.head()))
#%%%
from tabulate import tabulate
pdtabulate=lambda df:tabulate(df,headers='keys',tablefmt='psql')
print(pdtabulate(df))

#%%%html
from tabulate import tabulate
pdtabulate=lambda df:tabulate(df,headers='keys',tablefmt='html')
print(pdtabulate(df))
