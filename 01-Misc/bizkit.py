#Topic ----
https://pypi.org/project/bizkit/
#bizkit is a Python package to help streamlining business analytics data mining tasks. This package provides methods for market basket analysis, anomaly detection, customer survival analysis, customer clustering, and uplifting analysis. Implemented algorithms include mlxtend.apriori, sklearn.IsolationForest, lifelines.KaplanMeierFitter, [], and []. bizkit focuses on ease of use by providing a well-documented and consistent interface. The results are visualized via bokeh library, d3fgraph library, and [].
#https://pbpython.com/market-basket-analysis.html

import bizkit
dir(bizkit)
dir(bizkit.name)

import pandas as pd
from mlxtend.frequent_patterns import apriori
from mlxtend.frequent_patterns import association_rules

df = pd.read_excel('http://archive.ics.uci.edu/ml/machine-learning-databases/00352/Online%20Retail.xlsx')
df.head()
#%%%



#%%%



#%%%

