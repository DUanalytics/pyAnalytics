#Topic:Decision Tree - Class and Regr
#-----------------------------
#Read the case from this link
#https://stackabuse.com/decision-trees-in-python-with-scikit-learn/


#%% Classification Tree - Predict if not is face or otherwise depending upon features

#libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import os
os.listdir('E:/analytics/projects/pyanalytics/data') #change the folder to see what are the file in folder
#dataset
#data = pd.read_csv('E:/analytics/projects/pyanalytics/data/bill_authentication.csv')
data = pd.read_csv('https://raw.githubusercontent.com/DUanalytics/pyAnalytics/master/data/bill_authentication.csv')
data.head()
data.shape
data.columns
#data preparation : X & Y
X= data.drop('Class', axis=1) #axis=1 -> column
y= data['Class']
X
y
y.value_counts()
#split data
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.20)
X_train.shape
X_test.shape
275/data.shape[0]

#model
from sklearn.tree import DecisionTreeClassifier
clsModel = DecisionTreeClassifier()  #model with parameter
clsModel.fit(X_train, y_train)

#predict
ypred1 = clsModel.predict(X_test)
len(ypred1)

#metrics
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
classification_report(y_true=y_test, y_pred= ypred1)
confusion_matrix(y_true=y_test, y_pred=ypred1)
accuracy_score(y_true=y_test, y_pred=ypred1)

#new data
newData = X.sample(4)
clsModel.predict(newData)

#visualise 
#pip install graphviz
from graphviz import Source
from sklearn import tree
tree.plot_tree(decision_tree=clsModel)
tree.plot_tree(decision_tree=clsModel, feature_names=['Var', 'Skew', ' Kur',  'Ent'], class_names=['Org','Fake'], fontsize=12)
#not a good way to draw graphs.. other methods to be experimented
tree.plot_tree(decision_tree=clsModel, max_depth=2, feature_names=['Var', 'Skew', ' Kur',  'Ent'], class_names=['Org','Fake'], fontsize=12)

Source(tree.export_graphviz(clsModel))

dot_data1 = tree.export_graphviz(clsModel, max_depth=3, out_file=None, filled=True, rounded=True,  special_characters=True, feature_names=['Var', 'Skew', ' Kur',  'Ent'], class_names=['Org','Fake'])  
#check the folder location after installing the graphviz
import os
os.environ["PATH"] += os.pathsep + 'c:/Program Files (x86)/Graphviz2.38/bin/'
import graphviz 
from subprocess import call
call(['dot', '-Tpng', 'tree.dot', '-o', 'tree.png', '-Gdpi=600'])
graph1 = graphviz.Source(dot_data1)  
graph1 





#%% Regression Tree - Predict Petrol Consumption on other parameters
#Predict Numerical value based on IV
#os.listdir('E:/analytics/projects/pyanalytics/data')

#data2 = pd.read_csv('E:/analytics/projects/pyanalytics/data/petrol_consumption.csv')
data2 = pd.read_csv('https://raw.githubusercontent.com/DUanalytics/pyAnalytics/master/data/petrol_consumption.csv')
data2.head()
data2.shape
data2.columns
#data preparation : X & Y
X2= data2.drop('Petrol_Consumption', axis=1) #axis=1 -> column
y2= data2['Petrol_Consumption']
X2
y2
y2.mean()

#split data
from sklearn.model_selection import train_test_split
X2_train, X2_test, y2_train, y2_test = train_test_split(X2, y2, test_size=.20, random_state=123 )
X2_train.shape
X2_test.shape
10/data2.shape[0]

#model
from sklearn.tree import DecisionTreeRegressor #note this
regrModel = DecisionTreeRegressor()  #model with parameter
regrModel.fit(X2_train, y2_train)

#predict
ypred2 = regrModel.predict(X2_test)
ypred2
len(ypred2)
df2 = pd.DataFrame({'Actual':y2_test, 'Predicted': ypred2, 'diff':y2_test-ypred2})
df2
df2.shape[0]
#metrics
from sklearn import metrics
#Mean Abs Error
metrics.mean_absolute_error(y_true=y2_test, y_pred=ypred2)
sum(abs(df2['diff']))/df2.shape[0]

#Mean Squared Error (MSE)
metrics.mean_squared_error(y_true=y2_test, y_pred=ypred2)

#Root Mean Squared Error (RMSE)
np.sqrt(metrics.mean_squared_error(y_true=y2_test, y_pred=ypred2))

#we don't find confusion matrix & accuracy in Regression Tree

#new data
newData2 = X2.sample(4)
regrModel.predict(newData2)

#visualise 
from graphviz import Source
from sklearn import tree
tree.plot_tree(decision_tree=regrModel)
data2.columns
tree.plot_tree(decision_tree=regrModel, feature_names=['Tax', 'AvgInc', 'Highway',  'DvrLic'], class_names=None, fontsize=12)
#not a good way to draw graphs.. other methods to be experimented

dot_data2 = tree.export_graphviz(regrModel, max_depth=3, out_file=None, filled=True, rounded=True,  special_characters=True)  
import os
os.environ["PATH"] += os.pathsep + 'c:/Program Files (x86)/Graphviz2.38/bin/'
import graphviz 
from subprocess import call
call(['dot', '-Tpng', 'tree.dot', '-o', 'tree.png', '-Gdpi=600'])
graph2 = graphviz.Source(dot_data2)  
graph2 



#this is not working
# Source(tree.export_graphviz(regrModel))
# from io import StringIO
# from IPython.display import Image
# import pydotplus
# dot_data = StringIO()
# tree.export_graphviz(decision_tree=regrModel, out_file=dot_data, filled=True, rounded=True, special_characters=True)
# graph= pydotplus.graph_from_dot_data(dot_data.getvalue())
# Image(graph.create_png())
