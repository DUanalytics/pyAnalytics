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
X = [[0], [1]] #is it raining #0-no, 1-yes
Y = [1,0]  #class labels -  0- play no, 1- play yes
X
Y

clf = tree.DecisionTreeClassifier()
clf.fit(X,Y)

#visualise
tree.plot_tree(decision_tree= clf)
tree.plot_tree(decision_tree= clf, feature_names =['raining'], class_names=['Dont Play','Play'])  #1-Play, 0=dontplay

#predict for unknown instance
clf.predict([[0.7]])


#saving graph in file
dotfile = open('dtree2.dot','w')
tree.export_graphviz(clf, out_file = dotfile, feature_names= features, filled=True, rounded=True, impurity=False, class_names=['Play','No Play'])
dotfile.close()
#paste the code here : http://www.webgraphviz.com/
#this will create tree 

#predict for unknown instance
clf.predict([[0]])


#now create case of Cretig rating and DV
#https://docs.google.com/spreadsheets/d/1TIKi-K6qGU5RlLgqsQOp9bVkgGELtKDF6YtnnHFJMmo/edit#gid=1380162551

