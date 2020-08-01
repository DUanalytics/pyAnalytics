#Topic ---- MB - store
#https://stackabuse.com/association-rule-mining-via-apriori-algorithm-in-python/
#%%%
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
#pip install apyori
from apyori import apriori

store_data = pd.read_csv('data/store_data1.csv')
store_data.head()
store_data = pd.read_csv('data/store_data1.csv', header=None)
store_data.head()
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


