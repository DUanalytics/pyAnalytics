#Topic: Association Rule Mining
#-----------------------------
#can you increase sales by selling 1 item at time : NO
#you would like cross sell, up sell
#for this you have to find which items are often bought together by customers ( bread & butter, Suggest them to buy eggs also)
#if you give discount on eggs, they may

#libraries
import pandas as pd
import numpy as np

#pip install mlxtend
from mlxtend.frequent_patterns import apriori
from mlxtend.frequent_patterns import association_rules

#data
df = pd.read_csv('data/ARitemdata.csv')
df
df.dtypes
variable_name = {'True' : 0 , 'False' : 1 }
df[['I1','I2']] = df[['I1','I2']].map(variable_name)
df

#model
frequent_itemsets = apriori(df, min_support=.1, use_colnames=True)
