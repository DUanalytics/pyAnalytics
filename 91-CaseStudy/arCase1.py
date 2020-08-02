#Topic:  Association Rule Analysis
#-----------------------------

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

dataset = [['Apple', 'Beer', 'Rice', 'Chicken'],  ['Apple', 'Beer', 'Rice'], ['Apple', 'Beer'],  ['Apple', 'Bananas'], ['Milk', 'Beer', 'Rice', 'Chicken'], ['Milk', 'Beer', 'Rice'],  ['Milk', 'Beer'], ['Apple', 'Bananas']]

dataset
te = TransactionEncoder()
te_ary = te.fit(dataset).transform(dataset)
te_ary
df = pd.DataFrame(te_ary, columns=te.columns_)
df

#%%% #frequent itemsets - Most Imp Step
support_threshold = 0.25

frequent_itemsets = apriori(df, min_support= support_threshold, use_colnames = True)
frequent_itemsets
print(frequent_itemsets) #dataframe with the itemsets

#%%%%  - Support Rules

#output - DF with antecedents -> consequent
supportRules1 = association_rules(frequent_itemsets, metric="support", min_threshold = .3)
print(supportRules1)

print(supportRules1[['antecedents', 'consequents', 'support','confidence','lift']])


#%%%% Lift  : generally > 1 for strong associations

lift1 = association_rules(frequent_itemsets, metric="lift", min_threshold=1.5)
print(lift1)
lift1
print(lift1[['antecedents', 'consequents', 'support', 'lift','confidence']])

#twin condition : lift> 2;  confidence > .5, support > .2
lift1[(lift1.confidence > .5) & (lift1.support > .2)]

#%%%% Confidence

confidence1 = association_rules(frequent_itemsets, metric="confidence", min_threshold=.6)
print(confidence1)

print(confidence1[['antecedents', 'consequents', 'support','confidence']])

