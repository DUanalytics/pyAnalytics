#Topic:RFM
#-----------------------------
#dataset: http://archive.ics.uci.edu/ml/machine-learning-databases/00352/Online%20Retail.xlsx
#https://towardsdatascience.com/find-your-best-customers-with-customer-segmentation-in-python-61d602f9eee6
#libraries

import pandas as pd
pd.set_option("display.max_columns",10)
import numpy as np
import matplotlib.pyplot as plt
url='https://raw.githubusercontent.com/dupadhyaya/datasets/master/OnlineRetail1.csv'
from datetime import datetime
df = pd.read_csv(url, parse_dates=['InvoiceDate'])
df.head()
df.shape
df.info()
#01-12-2010  08:26:00

#----
df1 = df.copy()
df1.Country.nunique()
df1.Country.value_counts()
df1.Country.unique()
#---
customer_country=df1[['Country','CustomerID']].drop_duplicates()
customer_country
customer_country.shape
customer_country.columns
customer_country.groupby(['Country'])[ 'CustomerID'].aggregate( 'count').reset_index().sort_values( 'CustomerID', ascending=False)

#which country has max customers ???
#%%%% : lets do it for UK only
df1 = df1.loc[df1['Country'] == 'United Kingdom']
df1
df1.isnull().sum(axis=0)  #missing values

#if any missing values in customerID, remove those rows
df1 = df1[pd.notnull(df1['CustomerID'])]

df1.Quantity.min()
#remove negative values
df1 = df1[(df1['Quantity']>0)]
df1.shape
df1.info()
df1.Quantity.min()

#%%%%Check unique value for each column.
def unique_counts(df1):
   for i in df1.columns:
       count = df1[i].nunique()
       print(i, ": ", count)

unique_counts(df1)
df1.shape

#Add a column for total price.
df1['TotalPrice'] = df1['Quantity'] * df1['UnitPrice']
df1.head()

import datetime as dt
NOW = dt.datetime(2011,12,10)
df1['InvoiceDate'] = pd.to_datetime(df1['InvoiceDate'])
#Find out the first and last order dates in the data.
df1['InvoiceDate'].min()
df1['InvoiceDate'].max()

#%%%: RFM Customer Segmentation : RFM segmentation starts from here.

#RFM table
rfmTable = df1.groupby('CustomerID').agg({'InvoiceDate': lambda x: (NOW - x.max()).days, 'InvoiceNo': lambda x: len(x), 'TotalPrice': lambda x: x.sum()})
rfmTable.head()
df1.head()
df1.columns
df1.CustomerID.value_counts()
df1.loc[df1['CustomerID'] == 13047 ]

#few changes
rfmTable['InvoiceDate'] = rfmTable['InvoiceDate'].astype(int)
rfmTable.rename(columns={'InvoiceDate': 'recency',            'InvoiceNo': 'frequency','TotalPrice': 'monetary_value'}, inplace=True)
rfmTable.head()

first_customer = df1[df1['CustomerID'] == 13047]
first_customer


#%%% : Split the metrics
#The easiest way to split metrics into segments is by using quartiles.
#This gives us a starting point for the detailed analysis.
#4 segments are easy to understand and explain.
rfmTable.columns
rfmTable.head()
quantiles = rfmTable.quantile(q=[0.25,0.5,0.75])
quantiles
quantiles = quantiles.to_dict()
quantiles

#Create a segmented RFM table
segmented_rfm = rfmTable

#The lowest recency, highest frequency and monetary amounts are our best customers.
def RScore(x,p,d):
    if x <= d[p][0.25]:
        return 1
    elif x <= d[p][0.50]:
        return 2
    elif x <= d[p][0.75]: 
        return 3
    else:
        return 4
    
def FMScore(x,p,d):
    if x <= d[p][0.25]:
        return 4
    elif x <= d[p][0.50]:
        return 3
    elif x <= d[p][0.75]: 
        return 2
    else:
        return 1

#%%%
#Add segment numbers to the newly created segmented RFM table
segmented_rfm['r_quartile'] = segmented_rfm['recency'].apply(RScore, args=('recency',quantiles,))
segmented_rfm
segmented_rfm['f_quartile'] = segmented_rfm['frequency'].apply(FMScore, args=('frequency',quantiles,))
segmented_rfm['m_quartile'] = segmented_rfm['monetary_value'].apply(FMScore, args=('monetary_value',quantiles,))
segmented_rfm.head()


#%%%
#RFM segments split the customer base into an imaginary 3D cube which is hard to visualize. However, we can sort it out.
#Add a new column to combine RFM score: 111 is the highest score as we determined earlier.
segmented_rfm['RFMScore'] = segmented_rfm.r_quartile.map(str)                             + segmented_rfm.f_quartile.map(str) + segmented_rfm.m_quartile.map(str)
segmented_rfm.head()

#Who are the top 10 of our best customers!
segmented_rfm[segmented_rfm['RFMScore']=='111'].sort_values('monetary_value', ascending=False).head(10)

#%%%
#https://github.com/susanli2016/Machine-Learning-with-Python/blob/master/Customer_Segmentation_Online_Retail.ipynb
#https://guillaume-martin.github.io/rfm-segmentation-with-python.html
#https://www.kaggle.com/regivm/rfm-analysis-tutorial
#https://codereview.stackexchange.com/questions/212955/customer-segmentation-using-rfm-analysis
#https://joaocorreia.io/blog/rfm-analysis-increase-sales-by-segmenting-your-customers.html

