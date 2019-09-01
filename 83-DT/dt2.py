# -*- coding: utf-8 -*-
"""
Wed May  9 14:38:47 2018: Dhiraj
"""

from sklearn import tree

X = [[0,0],[1,1]]
type(X)
X
Y = [0,1]
Y

#DT classifier
clf = tree.DecisionTreeClassifier()
clf
clf = clf.fit(X,Y)
clf

clf.predict([[2., 2.]])
clf.predict_proba([[2.,2.]])


#Iris dataset
from sklearn.datasets import load_iris
from sklearn import tree
iris = load_iris()
clf = tree.DecisionTreeClassifier()
clf = clf.fit(iris.data, iris.target)
clf

#graphics
import graphviz
dot_data = tree.export_graphviz(clf, out_file=None)
graph = graphviz.Source(dot_data)
graph.render('iris')
