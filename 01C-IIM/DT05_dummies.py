#Topic:Decision Tree with Dummies
#-----------------------------
#libraries

import pandas as pd
from sklearn import tree
data = pd.DataFrame()
data['A'] = ['a','a','b','a']
data['B'] = ['b','b','a','b']
data['C'] = [0, 0, 1, 0]
data['Class'] = ['n','n','y','n']
data

clftree1 = tree.DecisionTreeClassifier()

one_hot_data = pd.get_dummies(data[['A','B','C']],drop_first=True)
one_hot_data

clftree1.fit(one_hot_data, data['Class'])
print(clftree1)
one_hot_data[0:1]
clftree1.predict(one_hot_data[0:1])

tree.plot_tree(clftree1)
tree.plot_tree(clftree1, feature_names=['A','B','C'])
tree.plot_tree(clftree1, feature_names=['A','B','C'], class_names=['y','n'], filled=True, proportion=True)

tree.plot_tree(clftree1, feature_names=['A','B','C'], class_names=['y','n'], filled=True, proportion=True, node_ids=True)
