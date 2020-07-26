#Topic: Decision Tree
#-----------------------------
#libraries

#Decision Tree - one of the most popular ML algo
#obsvervation to conclusion(category); Observations are represented as branches, conclusions as leaves
#classification tree - target variable discrete value
#reression tree - target is continuous value

#Method1
from sklearn import tree
from sklearn.model_selection import train_test_split
import numpy as np

#DT
features = ['raining']
X = [[0], [1]]
Y = [0,1]

clf = tree.DecisionTreeClassifier()
clf.fit(X,Y)

#visualise
dotfile = open('dtree2.dot','w')
tree.export_graphviz(clf, out_file = dotfile, feature_names= features, filled=True, rounded=True, impurity=False, class_names=['No Umbrella','Umbrella'])
dotfile.close()
#paste the code here : http://www.webgraphviz.com/
#this will create tree 

#predict for unknown instance
clf.predict([[0]])
