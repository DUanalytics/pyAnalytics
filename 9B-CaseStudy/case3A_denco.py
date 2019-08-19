#case study - Denco _ Brief (Main)
#others - max_rows, width, precision, height, date_dayfirst, date_yearfirst
import pandas as pd
import numpy as np
pd.set_option('display.max_columns',15) #see all columns
#read data
df = pd.read_csv('data/denco.csv')
#see properties of data
df.head()
df['region'] = df['region'].astype('category')
df.dtypes

#which region sold max parts
df.region.value_counts()
df.region.value_counts().plot(kind='bar')

#Who are the most loyal Customers - Improve repeated sales, Target customers with low sales Volumes
df.custname.value_counts().sort_values(ascending=False)[0:5]
df.groupby('custname').size().sort_values(ascending=False).head(5)
#these are most loyal customers
#Which customers contribute the most to their revenue - How do I retain these customers & target incentives#find total revenue of each customer, sort in descending.
df.groupby('custname').aggregate({'revenue':np.sum}).sort_values(by='revenue', ascending=False).head(5)
#these are top 5 customers who gave revnue to Denco

#What part numbers bring in to significant portion of revenue - Maximise revenue from high value parts #grouby partnum, find value of revenue, sell these more
df[['partnum','revenue']].groupby('partnum').sum().sort_values(by='revenue', ascending=False).head()
#these are top parts which give max revenue

#What parts have the highest profit margin - What parts are driving profits & what parts need to build further
#check for margin value, their individual margin and total sales margin like revenue
df[['partnum','margin']].groupby('partnum').sum().sort_values(by='margin', ascending=False).head(5)
#this total revenue value giving items

#Most sold items
df.groupby('partnum').size().sort_values(ascending=False).head(5)

#which regions gave max revenue
df[['revenue', 'region']].groupby( 'region').sum().sort_values(by='revenue', ascending=False)
#East gave max revenue
df[['revenue', 'region']].groupby( 'region').sum().sort_values(by='revenue', ascending=False).plot(kind='barh')

#End of Analysis
