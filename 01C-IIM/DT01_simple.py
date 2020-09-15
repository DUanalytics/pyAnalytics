#Topic: Decision Tree
#-----------------------------
#libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pydataset import data
import seaborn as sns

#Decision Tree - one of the most popular ML algo
#obsvervation to conclusion(category); Observations are represented as branches, conclusions as leaves
#classification tree - target variable discrete value
#reression tree - target is continuous value

#Method1
from sklearn import tree
#https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeClassifier.html
from sklearn.model_selection import train_test_split
#https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html

#DT
X = [[0], [1]] #is it raining #0-no, 1-yes
Y = [1,0]  #class labels -  0- play no, 1- play yes
X
Y
np.array(X)  #array form
np.concatenate((np.array(X), np.array(Y)))
np.concatenate((np.array(X), np.array(Y).reshape(-1,1)), axis=1)  #column
#if X=0(not raining), Y=1(Play)

clf = tree.DecisionTreeClassifier()  #blank model
clf.fit(X,Y)  #fit - Build a decision tree classifier from the training set (X, y)
#https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeClassifier.html#sklearn.tree.DecisionTreeClassifier.fit

#visualise
tree.plot_tree(decision_tree= clf)
tree.plot_tree(decision_tree= clf, feature_names =['raining'], class_names= ['Dont Play','Play'])  #1-Play, 0=dontplay

#predict for unknown instance
clf.predict([[0]]) #if X=0, Y=1
clf.predict([[1]]) #if X=1, Y=0

#Later------
#saving graph in file
dotfile = open('dtree2.dot','w')
features=['Rain']
tree.export_graphviz(clf, out_file = dotfile, feature_names= features, filled=True, rounded=True, impurity=False, class_names=['Play','No Play'])
dotfile.close()
#paste the code here : http://www.webgraphviz.com/
#this will create tree 

#predict for unknown instance
clf.predict([[0]])


#now create case of Cretig rating and DV
#https://docs.google.com/spreadsheets/d/1TIKi-K6qGU5RlLgqsQOp9bVkgGELtKDF6YtnnHFJMmo/edit#gid=1380162551

