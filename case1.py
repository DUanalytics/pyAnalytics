#python : Topic :.......
#import data into python
url = 'https://raw.githubusercontent.com/DUanalytics/datasets/master/csv/denco.csv'

import pandas as pd
df = pd.read_csv(url)
df
df.shape #dim of data
df.columns
df.head(n=3)

df.custname.value_counts().sort_values(ascending=False).head(5)
df.custname.value_counts().sort_values(ascending=False).tail(5)
df.custname.value_counts().sort_values(ascending=True).head(5)

#revenue total per customer
df.groupby('custname').revenue.mean()
df.groupby('custname').revenue.sum().sort_values(ascending=False).head(5)
df.groupby('custname')['revenue'].aggregate([np.sum,max,min, 'size'])
df.groupby('custname')['revenue'].aggregate([np.sum,max,min, 'size']).sort_values(by='sum')


#top revenue items

df.groupby('partnum')['revenue'].aggregate([np.sum]).sort_values(by='sum', ascending=False).head(5)
df.groupby('partnum')['revenue'].aggregate([np.sum]).sort_values(by='sum', ascending=False).tail(5)

#top profit making items
df.groupby('partnum')['margin'].aggregate([np.sum]).sort_values(by='sum', ascending=False).head(5)
