#Topic ---- MB - store
#https://stackabuse.com/association-rule-mining-via-apriori-algorithm-in-python/
#%%%
#libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori
from mlxtend.frequent_patterns import association_rules
import time
import logging
pd.set_option('display.max_columns',None)

url='https://raw.githubusercontent.com/DUanalytics/pyAnalytics/master/data/store_data.csv'
store_data = pd.read_csv(url)
store_data.head()

#----
te = TransactionEncoder()
te_ary = te.fit(store_data).transform(store_data)
te_ary
te.columns_
df = pd.DataFrame(te_ary, columns=te.columns_)

df = store_data
#this matrix of transactions : T/ F indicate their presence in each Trans ID
df.shape

#%%% #frequent itemsets - Most Imp Step
support_threshold = 0.01
#https://github.com/rasbt/mlxtend/blob/master/mlxtend/frequent_patterns/apriori.py
frequent_itemsets = apriori(df, min_support= support_threshold, use_colnames = True)
frequent_itemsets
print(frequent_itemsets) #dataframe with the itemsets

#%%%%  - Support Rules
association_rules?
#output - DF with antecedents -> consequent
supportRules3 = association_rules(frequent_itemsets, metric="support", min_threshold = .1)
print(supportRules3)
supportRules3.head()

print(supportRules3[['antecedents', 'consequents', 'support','confidence','lift']])
#---
supportRules2 = association_rules(frequent_itemsets, metric="support", min_threshold = .2)
print(supportRules2[['antecedents', 'consequents', 'support','confidence','lift']])






#%%%
records = []
for i in range(0, 7501):    records.append([str(store_data.values[i,j]) for j in range(0, 20)])

association_rules = apriori(records, min_support=0.0045, min_confidence=0.2, min_lift=3, min_length=2)
association_results = list(association_rules)
association_results

#%%%
association_rules = apriori(records, min_support=0.0045, min_confidence=0.2, min_lift=3, min_length=2)
association_results = list(association_rules)
association_results
print(association_rules[0])


