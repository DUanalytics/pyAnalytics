#Topic ---- Case Study - Denco - Manufacturing Firm
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#see all columns
pd.set_option('display.max_columns',15)
#others - max_rows, width, precision, height, date_dayfirst, date_yearfirst
pd.set_option('display.width', 1000)
pd.options.display.float_format = '{:.2f}'.format
#read data
url='https://raw.githubusercontent.com/DUanalytics/datasets/master/csv/denco.csv'
df = pd.read_csv(url)
#see properties of data
df.head()
df.columns
len(df)
df.describe()
df.shape
df.dtypes
df['region'] = df['region'].astype('category')

df.region.value_counts()
df.region.value_counts().plot(kind='bar')
df.sort_values(['custname']) 
#%%%% : Summary1
#Who are the most loyal Customers - Improve repeated sales, Target customers with low sales Volumes
#count by customers, sort, pick top 5 
#Series
df.custname.value_counts()
df.custname.value_counts().sort_values(ascending=False)[0:8]
df.custname.value_counts().sort_values(ascending=False).head(5)
#pandas
df.groupby('custname').size().sort_values(ascending=False)
df.groupby('custname').size().sort_values(ascending=False).head(5)
#these are most loyal customers
#%%% - Summary2
#Which customers contribute the most to their revenue - How do I retain these customers & target incentives
#find total revenue of each customer, sort in descending.
df.groupby('custname').aggregate({'revenue':np.sum})
df.groupby('custname').aggregate({'revenue':np.sum}).sort_values(by='revenue', ascending=False)
df.groupby('custname').aggregate({'revenue':np.sum}).sort_values(by='revenue', ascending=False).head(5)
#these are top 5 customers who gave revnue to Denco
#Number of times customer bought and total revenue
#this is ordered by revenue
df.groupby('custname')['revenue'].aggregate([np.sum, 'size'] ).sort_values(by='sum', ascending=False).head(5)
#this is ordered by count
df.groupby('custname')['revenue'].aggregate([np.sum, 'size'] ).sort_values(by='size', ascending=False).head(5)

#%%% Summary3
#What part numbers bring in to significant portion of revenue - Maximise revenue from high value parts
#grouby partnum, find value of revenue, sell these more
df[['partnum','revenue']].sort_values(by='revenue', ascending=False)
df[['partnum','revenue']].sort_values(by='revenue', ascending=False).head(5)
#these are top parts which give max revenue per part
#which partnum gave how much revenue total
df[['partnum','revenue']].groupby('partnum').sum()
df[['partnum','revenue']].groupby('partnum').sum().sort_values(by='revenue', ascending=False).head(5)
#this total revenue value giving items

#%%% Summary4
#What parts have the highest profit margin - What parts are driving profits & what parts need to build further
#check for margin value, their individual margin and total sales margin like revenue
df[['partnum','margin']].sort_values(by='margin', ascending=False)
df[['partnum','margin']].sort_values(by='margin', ascending=False).head(5)
#these are top parts which give max margins

#if total sales has to be considered
df[['partnum','margin']].groupby('partnum').sum()
df[['partnum','margin']].groupby('partnum').sum().sort_values(by='margin', ascending=False).head(5)
#this total revenue value giving items

#%%% Extras
#Most sold items
df.groupby('partnum').size().sort_values(ascending=False).head(5)

#which regions gave max revenue
df[['revenue', 'region']].groupby( 'region').sum().sort_values(by='revenue', ascending=False)
#East gave max revenue
df[['revenue', 'region']].groupby( 'region' ).sum().sort_values( by='revenue', ascending=False).plot(kind='barh')

#end here

#%%% Extras - Plan more
df.groupby(['custname'])['margin'].nlargest(3)
df.sort_values(['revenue'], ascending= True).groupby( 'region' ).mean()
df.groupby(['custname'])['margin'].nlargest(3)
df.sort_values(['revenue'], ascending= True).groupby( 'region' ).mean()
df[['revenue','custname']].groupby('custname').size().sort_values(ascending=False).head(5) 


#Ne