#Topic: Dummies in DT
#-----------------------------
#libraries
import pandas as pd
import numpy as np
from sklearn import tree

data = pd.DataFrame()
data['A'] = ['a','a','b','a']
data['B'] = ['b','b','a','b']
data['C'] = [0, 0, 1, 0]
data['Class'] = ['n','n','y','n']
data
data.dtypes
tree = DecisionTreeClassifier()

one_hot_data = pd.get_dummies(data[['A','B','C']],drop_first=True)
one_hot_data
tree.fit(one_hot_data, data['Class'])
