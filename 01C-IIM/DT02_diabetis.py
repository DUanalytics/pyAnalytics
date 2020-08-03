#Topic: DT - Diabetis Data Set
#-----------------------------
#pip install graphviz  #install whichever library is not present
#pip install pydotplus

# Load libraries
import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeClassifier, export_graphviz
from sklearn.model_selection import train_test_split
from sklearn import metrics, tree
from graphviz import Source
from IPython.display import Image, SVG
import pydotplus

#%%%% : Load Data
col_names = ['pregnant', 'glucose', 'bp', 'skin', 'insulin', 'bmi', 'pedigree', 'age', 'label']
url='https://raw.githubusercontent.com/DUanalytics/datasets/master/csv/pima-indians-diabetes.csv'
#This dataset is originally from the National Institute of Diabetes and Digestive and Kidney Diseases. The objective of the dataset is to diagnostically predict whether or not a patient has diabetes, based on certain diagnostic measurements included in the dataset. Several constraints were placed on the selection of these instances from a larger database. In particular, all patients here are females at least 21 years old of Pima Indian heritage.
#https://www.kaggle.com/uciml/pima-indians-diabetes-database
#he datasets consists of several medical predictor variables and one target variable, Outcome. Predictor variables includes the number of pregnancies the patient has had, their BMI, insulin level, age, and so on.
# load dataset
pima = pd.read_csv(url, header=None, names=col_names)
pima.head()
pima.label.value_counts() #how many are diabetic - 268
pima.shape
.7 * 768  #70% of 768 go into train set rest to test

#%%% : Feature Selection
#need to divide given columns into two types of variables dependent(or target variable) and independent variable(or feature variables).

#split dataset in features and target variable
feature_cols = ['pregnant', 'insulin', 'bmi', 'age', 'glucose', 'bp', 'pedigree']
X = pima[feature_cols] # Features - bmi, age etc
y = pima.label # Target variable : has diabetes =1
#predict y on X
#%%% Splitting Data
#To understand model performance, dividing the dataset into a training set and a test set is a good strategy.
#Let's split the dataset by using function train_test_split(). You need to pass 3 parameters features, target, and test_set size.
# Split dataset into training set and test set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1) 
# 70% training and 30% test : each for train and test (X & y)
X_train.head()

#%%%: Building Decision Tree Model :create a Decision Tree Model using Scikit-learn.
# Create Decision Tree classifer object
clf = DecisionTreeClassifier()
# Train Decision Tree Classifer
clf = clf.fit(X_train,y_train)
y_train
#Predict the response for test dataset
y_pred = clf.predict(X_test)
y_pred
#%%% : Evaluating Model
# estimate, how accurately the classifier or model can predict the type of cultivars.# Accuracy can be computed by comparing actual test set values and predicted values.
# Model Accuracy, how often is the classifier correct?
print("Accuracy:",metrics.accuracy_score(y_test, y_pred))
#classification rate of 67.53%, considered as good accuracy. You can improve this accuracy by tuning the parameters in the Decision Tree Algorithm.
from sklearn.metrics import confusion_matrix
confusion_matrix = confusion_matrix(y_test, y_pred)
print(confusion_matrix)
from sklearn.metrics import classification_report
print(classification_report(y_test, y_pred))
#%%% 
y_test.shape, y_pred.shape
y_test.head()
y_pred[0:6]
#%%%
from graphviz import Source
from sklearn import tree
from IPython.display import SVG
#libraries & path of graphviz
import os
os.environ["PATH"] += os.pathsep + 'c:/Program Files (x86)/Graphviz2.38/bin/'
#%%
graph1 = Source(tree.export_graphviz(clf, out_file=None, class_names= ['0', '1']  , filled = True))
display(SVG(graph1.pipe(format='svg')))
#change labels names
graph2 = Source( tree.export_graphviz(clf, out_file=None, feature_names=X.columns, filled=True, class_names=['NoDiabetis','Diabetis']))
graph2
#change max_depth : 1 to 4
Source(tree.export_graphviz(clf, out_file=None, max_depth=1, feature_names=X.columns, class_names=['NonDB','DB'], label='all', filled=True, leaves_parallel=True, impurity=True, node_ids=True, proportion=True, rotate=True, rounded=True, special_characters=False, precision=1))
#https://stackoverflow.com/questions/27817994/visualizing-decision-tree-in-scikit-learn
# This is for saving image in file system
#https://scikit-learn.org/stable/modules/generated/sklearn.tree.export_graphviz.html

#visualise using dotfile

#True should be returned. goto location and see the file

#%%%  Create Decision Tree classifer object
#change max_depth at the time of creation and method
#criterio= entropy, gini
clf3 = DecisionTreeClassifier(criterion="entropy", max_depth=3)
# Train Decision Tree Classifer
clf3 = clf3.fit(X_train,y_train)
#Visualise
Source(tree.export_graphviz(clf3, out_file=None, class_names= ['0', '1']  , filled = True, feature_names=X.columns,node_ids=True))
#display(SVG(graph3b.pipe(format='svg')))
X_train[0:1]  
#Class:1 : glucose > 127, glucose < 158, bmi, age,
#Predict the response for test dataset
y_pred3 = clf3.predict(X_test)
len(X_test)
y_pred3
len(y_pred3)
# Model Accuracy, how often is the classifier correct?
print("Accuracy:",metrics.accuracy_score(y_test, y_pred3))
#classification rate increased to 77.05%, which is better accuracy than the previous model.

#----
clf4 = DecisionTreeClassifier(criterion="gini", max_depth=3)
# Train Decision Tree Classifer
clf4 = clf4.fit(X_train,y_train)
y_pred4 = clf4.predict(X_test)
Source(tree.export_graphviz(clf4, out_file=None, class_names= ['0', '1']  , filled = True, feature_names=X.columns))
#display(SVG(graph4b.pipe(format='svg')))
print("Accuracy:",metrics.accuracy_score(y_test, y_pred4))


#%%% : Features
#Decision trees are easy to interpret and visualize.
#It can easily capture Non-linear patterns.
#It requires fewer data preprocessing from the user, for example, there is no need to normalize columns.
#It can be used for feature engineering such as predicting missing values, suitable for variable selection.
#The decision tree has no assumptions about distribution because of the non-parametric nature of the algorithm
#%%% : Cons
#Sensitive to noisy data. It can overfit noisy data.
#The small variation(or variance) in data can result in the different decision tree. This can be reduced by bagging and boosting algorithms.
#Decision trees are biased with imbalance dataset, so it is recommended that balance out the dataset before creating the decision tree.


#%%% : Visualizing Decision Trees
#You can use Scikit-learn's export_graphviz function for display the tree within a Jupyter notebook. For plotting tree, you also need to install graphviz and pydotplus.
#pip install graphviz
#pip install pydotplus
#export_graphviz function converts decision tree classifier into dot file and pydotplus convert this dot file to png or displayable form
from sklearn.tree import export_graphviz
from io import StringIO
from IPython.display import Image  
import pydotplus

dot_data = StringIO()

export_graphviz(clf, out_file=dot_data, filled=True, rounded=True, special_characters=True,feature_names = feature_cols, class_names=['0', '1'])
graph = pydotplus.graph_from_dot_data(dot_data.getvalue())  
graph.write_png('diabetes.png')
Image(graph.create_png())

g


#%%%%
#Optimizing Decision Tree Performance
#criterion : optional (default=”gini”) or Choose attribute selection measure: This parameter allows us to use the different-different attribute selection measure. Supported criteria are “gini” for the Gini index and “entropy” for the information gain.

#splitter : string, optional (default=”best”) or Split Strategy: This parameter allows us to choose the split strategy. Supported strategies are “best” to choose the best split and “random” to choose the best random split.

#max_depth : int or None, optional (default=None) or Maximum Depth of a Tree: The maximum depth of the tree. If None, then nodes are expanded until all the leaves contain less than min_samples_split samples. The higher value of maximum depth causes overfitting, and a lower value causes underfitting (Source).

#%%%% - short summary
# Create Decision Tree classifer object
clf = DecisionTreeClassifier(criterion="entropy", max_depth=3)

# Train Decision Tree Classifer
clf = clf.fit(X_train,y_train)

#Predict the response for test dataset
y_pred = clf.predict(X_test)

# Model Accuracy, how often is the classifier correct?
print("Accuracy:",metrics.accuracy_score(y_test, y_pred))
