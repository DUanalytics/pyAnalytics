# -*- coding: utf-8 -*-
"""
Wed May  9 19:56:46 2018: Dhiraj
"""
#http://pbpython.com/market-basket-analysis.html
#pip install mlxtend : in anconda prompt as admin

import pandas as pd
from mlxtend.frequent_patterns import apriori
from mlxtend.frequent_patterns import association_rules

df = pd.read_excel('http://archive.ics.uci.edu/ml/machine-learning-databases/00352/Online%20Retail.xlsx')
df.head()
df.describe()
df.shape

#%%
#remove extra spaces from descriptions
#remove rows with empty invoices and containing C
df['Description'] = df['Description'].str.strip()
df['Description'].head()
df.InvoiceNo.head()
df.dropna(axis=0, subset=['InvoiceNo'], inplace=True) #remove NA invoice nos
df['InvoiceNo'] = df['InvoiceNo'].astype('str')
df = df[~df['InvoiceNo'].str.contains('C')]

#%%
#subset for France. reformat it : Invoice No and items
basket = (df[df['Country'] =="France"]
          .groupby(['InvoiceNo', 'Description'])['Quantity']
          .sum().unstack().reset_index().fillna(0)
          .set_index('InvoiceNo'))
basket.head()
#%%
#recode : 0 (nil) or 1 (> 1)
def encode_units(x):
    if x <= 0:
        return 0
    if x >= 1:
        return 1

basket_sets = basket.applymap(encode_units)
basket_sets.head()
print (basket_sets.values)
print(basket_sets.iloc[:, 5:8].values)
basket_sets.columns
basket_sets.drop('POSTAGE', inplace=True, axis=1) #remove POSTAGE column not an item

#%%
frequent_itemsets = apriori(basket_sets, min_support=0.07, use_colnames=True)
frequent_itemsets

rules = association_rules(frequent_itemsets, metric="lift", min_threshold=1)
rules.head()

#%%
rules[ (rules['lift'] >= 6) &  (rules['confidence'] >= 0.8) ]

basket['ALARM CLOCK BAKELIKE GREEN'].sum()

basket['ALARM CLOCK BAKELIKE RED'].sum()

#%%
basket2 = (df[df['Country'] =="Germany"]
          .groupby(['InvoiceNo', 'Description'])['Quantity']
          .sum().unstack().reset_index().fillna(0)
          .set_index('InvoiceNo'))

basket_sets2 = basket2.applymap(encode_units)
basket_sets2.drop('POSTAGE', inplace=True, axis=1)
frequent_itemsets2 = apriori(basket_sets2, min_support=0.05, use_colnames=True)
rules2 = association_rules(frequent_itemsets2, metric="lift", min_threshold=1)

rules2[ (rules2['lift'] >= 4) &   (rules2['confidence'] >= 0.5)]

