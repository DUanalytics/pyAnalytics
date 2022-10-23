#python : Topic :DT visualisation
#not working
#standard libaries
# Load libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier, export_graphviz
from sklearn.model_selection import train_test_split
from sklearn import metrics, tree
from graphviz import Source
from IPython.display import Image, SVG

url='https://raw.githubusercontent.com/DUanalytics/datasets/master/csv/diabetes.csv'

data = pd.read_csv(url)
data.head()
data.columns
data.groupby('Outcome').aggregate({'Glucose':np.mean, 'BMI':np.mean, 'Age':np.mean, 'BloodPressure':np.mean})
data.Outcome.value_counts() #how many are diabetic - 268
data.shape
X = data.drop('Outcome', axis=1) # Features 
y = data['Outcome'] # Target variable : has diabetes =1
X
y
#%%%split
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=100) 
X_train.Glucose.mean()
X_test.Glucose.mean()

X_train.shape, X_test.shape, y_train.shape, y_test.shape
# 70% training and 30% test : each for train and test (X & y)
X_train.head()

from sklearn.tree import DecisionTreeClassifier
clf = DecisionTreeClassifier()
help(clf)
# Train Decision Tree Classifer
clf = clf.fit(X_train, y_train)
y_train

#Predict the response for test dataset
y_pred = clf.predict(X_test)
y_pred
y_test
#accuracy-----
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred)
print(cm)
len(y_test)
(117+43)/231
print("Accuracy:", metrics.accuracy_score(y_test, y_pred))

from sklearn.metrics import classification_report
print(classification_report(y_test, y_pred))

#%%% 
y_test.shape, y_pred.shape
y_test.head()
y_pred[0:6]

data.columns[0:8]
#%%% Plot
#https://mljar.com/blog/visualize-decision-tree/
text_representation = tree.export_text(clf)
print(text_representation)
#----
fig = plt.figure(figsize=(25,20))
_ = tree.plot_tree(clf, feature_names=['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 'Insulin','BMI', 'DiabetesPedigreeFunction', 'Age'] , class_names=['NoD','Diabetis'], filled=True)

tree.plot_tree(clf)

tree.export_graphviz(clf, out_file='tree_limited.dot', feature_names=['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 'Insulin','BMI', 'DiabetesPedigreeFunction', 'Age'] , class_names=['NoD','Diabetis'], filled=True, rounded=True)
dot -Tpng tree_limited.dot -o tree_limited.png -Gdpi=600
#install dot utility
pip install pydot
import pydot
from graphviz import Digraph
dot
graph=pydotplus.graph_from_dot_data(out.getvalue())
Image(graph.create_png())
