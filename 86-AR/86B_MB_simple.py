#Topic ----

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori
from mlxtend.frequent_patterns import association_rules
import time
import logging
#%%%
transactions = [['milk', 'bread', 'water'],['coffe', 'sugar' ],['burgers', 'eggs']]
transactions
#%%%
support_threshold = 0.004
te = TransactionEncoder()
te_ary = te.fit(transactions).transform(transactions)
te_ary
df = pd.DataFrame(te_ary, columns=te.columns_)
df
logging.debug("Calculating itemset according to support...")
# time 
start_time = time.clock()
# apriori
frequent_itemsets = apriori(df, min_support=support_threshold, use_colnames=True)
frequent_itemsets
# end time to calculation
end_time = time.clock()
time_apriori = (end_time-start_time)/60
apriori_decimals = "%.2f" % round(time_apriori,2)
print("\n\nCompleted in %s minutes\n" % apriori_decimals)

print(frequent_itemsets) #dataframe with the itemsets
pd.set_option('display.max_columns',None)
lift = association_rules(frequent_itemsets, metric="lift", min_threshold=1)
print(lift) #dataframe with confidence, lift, conviction and leverage metrics calculated

confidence = association_rules(frequent_itemsets, metric="confidence", min_threshold=1)
print(confidence) #dataframe with confidence, lift, conviction and leverage metrics calculated
print(confidence[['antecedents', 'consequents', 'support','confidence']])

support = association_rules(frequent_itemsets, metric="support", min_threshold=.3)
print(support)
print(support[['antecedents', 'consequents', 'support','confidence']])

#%%%

