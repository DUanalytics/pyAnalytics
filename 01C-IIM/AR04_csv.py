#python : DUP - Topic :Importing CSV data for AR analysis.......

#standard libaries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pydataset import data
import seaborn as sns
from mlxtend.frequent_patterns import apriori
from mlxtend.frequent_patterns import association_rules

#%%%%
#https://www.analyticsvidhya.com/blog/2021/10/a-comprehensive-guide-on-market-basket-analysis/

# Load transactions from pandas
groceries2=pd.read_csv('data/groceries.csv',header=None)
groceries2
data=groceries2
color = plt.cm.rainbow(np.linspace(0, 1, 40))
data[0].value_counts().head(40).plot.bar(color = color, figsize=(13,5))
plt.title('frequency of most popular items', fontsize = 20)
plt.xticks(rotation = 90 )
plt.grid()
plt.show()

# Split transaction strings into lists
#transactions = groceries['____'].apply(lambda t: t.split(','))
#converting dataframe into list of lists
l=[]
for i in range(1,7501):
    l.append([str(data.values[i,j]) for j in range(0,20)])
l
# Convert DataFrame column into list of strings
# Print the list of transactions

#applying apriori algorithm
help(apriori)
l
association_rules = apriori(l, min_support=0.0045)
association_results = list(association_rules)

# Getting the list of transactions from the dataset
transactions = []
for i in range(0, len(data)):
    transactions.append([str(data.values[i,j]) for j in range(0,len(data.columns))])

transactions[:1]

from itertools import permutations

# Extract unique items.
flattened = [item for transaction in transactions for item in transaction]
items = list(set(flattened))
items

print('# of items:',len(items))
print(list(items))
if 'nan' in items: items.remove('nan')
print(list(items))
# Compute and print rules.
rules = list(permutations(items, 2))
print('# of rules:',len(rules))
print(rules[:5])

frequent_itemsets = apriori(l, min_support=.1, use_colnames=True)
association_rules = apriori(l, min_support=0.0045)
association_results = list(association_rules)


#https://goldinlocks.github.io/Market-Basket-Analysis-in-Python/
#https://www.kaggle.com/l0new0lf/association-rules-mining-market-basket-analysis?scriptVersionId=29787184
