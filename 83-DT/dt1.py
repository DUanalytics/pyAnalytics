# -*- coding: utf-8 -*-
"""
Tue May  8 21:54:03 2018: Dhiraj
"""
# Decision Tree
import numpy as np
from sklearn.externals.six import StringIO
from sklearn.tree import DecisionTreeClassifier, export_graphviz
from sklearn.tree import export_graphviz
import pydotplus  #install it
from IPython.display import Image  
import sklearn.datasets as datasets
import pandas as pd
#import DecisionTreeRegressor from sklearn.tree if you want to use a decision tree to predict a numerical target variable

iris=datasets.load_iris()
df=pd.DataFrame(iris.data, columns=iris.feature_names)
y=iris.target


dtree=DecisionTreeClassifier()
dtree.fit(df,y)
dtree.splitter

export_graphviz(dtree)

dot_data = StringIO()
export_graphviz(dtree, out_file=dot_data, filled=True, rounded=True, special_characters= True)
graph = pydotplus.graph_from_dot_data(dot_data.getvalue())  
graph
Image(graph.create_png())
graph[0].write_pdf("iris.pdf")



#%%
from sklearn import tree
clf = tree.DecisionTreeClassifier()
iris = load_iris()
clf = clf.fit(iris.data, iris.target)
tree.export_graphviz(clf, out_file='tree.dot')    

from sklearn.externals.six import StringIO  
import pydot 
dot_data = StringIO() 
tree.export_graphviz(clf, out_file=dot_data) 
graph = pydot.graph_from_dot_data(dot_data.getvalue()) 
graph.write_pdf("iris.pdf") 
graph[0].write_pdf("iris.pdf")


#%% install graphviz and set path
#C:\Program Files (x86)\Graphviz2.38\bin\dot.exe
#https://graphviz.gitlab.io/_pages/Download/Download_windows.html