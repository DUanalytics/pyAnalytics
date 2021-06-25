#Multiple Columns
#-----------------------------
#%#Converting multiple columns to Categories
#multiple columns to categories
import pandas as pd
from pydataset import data
data =data('iris')
data.columns
data.describe()
data.dtypes
def rstr(df): return df.shape, df.apply(lambda x: [x.unique()])
print(rstr(data))
df.info(null_counts=True, verbose=True)
#which columns are categories
df=data.copy()  #not link
df
df.describe()
df.dtypes
df['Species'] = df['Species'].astype('category')
df.dtypes
df.describe(include='category')
df.dtypes
df = df.astype({"Species":'category', "Sepal.Length":'int64'})
df.dtypes
df.describe()
df.describe(include=all)
include =['object', 'float', 'int', 'category']
# percentile list
perc =[.20, .40, .60, .80]
desc = df.describe(percentiles = perc, include = include)
desc
df.Species.value_counts() #numbers now
data.Species.value_counts()

df.Weight = df.Weight.astype('int64')
#run these together
for col_name in df.columns:
    if(df[col_name].dtype == 'object'):
        df[col_name]= df[col_name].astype('category')
        df[col_name] = df[col_name].cat.codes
df.dtypes
help(df.describe())
df.describe(include='category')
help(df.describe)

#cols are categories
#run these together
for col_name in df.columns:
    if(df[col_name].dtype == 'object'):
        df[col_name]= df[col_name].astype('category')
        df[col_name] = df[col_name].cat.codes

#plots
#https://realpython.com/python-matplotlib-guide/