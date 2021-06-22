#python : Topic :DT Practise in Class

#standard libaries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.tree import DecisionTreeClassifier, export_graphviz
from sklearn.model_selection import train_test_split
from sklearn import metrics, tree

url = url='https://raw.githubusercontent.com/DUanalytics/datasets/master/csv/diabetes.csv'

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
#%%%
#import, summary, split, model on train set, prediction of test set, confusion matrix, accuracy, predict on new or  unknown data

#prune tree - make tree shorter by cutting branches
help(DecisionTreeClassifier)
dtree = DecisionTreeClassifier(criterion='entropy', max_depth=3)
dtree.fit(X_train, y_train)
pred2 = dtree.predict(X_test)
print("Accuracy:",metrics.accuracy_score(y_test, pred2))
print(classification_report(y_test, pred2))
#https://scikit-learn.org/stable/modules/generated/sklearn.tree.export_text.html
text_representation2 = tree.export_text(dtree, feature_names=['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 'Insulin','BMI', 'DiabetesPedigreeFunction', 'Age'])
print(text_representation2)
data.columns
text_representation3 = tree.export_text(dtree, feature_names=['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 'Insulin','BMI', 'DiabetesPedigreeFunction', 'Age'],  decimals=0, show_weights=True, max_depth=3)  #keep changing depth values
print(text_representation3)


#%%regression tree in python
#data2 = pd.read_csv('E:/analytics/projects/pyanalytics/data/petrol_consumption.csv')
data2 = pd.read_csv('https://raw.githubusercontent.com/DUanalytics/pyAnalytics/master/data/petrol_consumption.csv')
data2.head()
data2.shape
data2.columns
#data preparation : X & Y
X2= data2.drop('Petrol_Consumption', axis=1) #axis=1 -> column
y2= data2['Petrol_Consumption']
X2.head()
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
newData2
regrModel.predict(newData2)

#visualise 
from graphviz import Source
from sklearn import tree
tree.plot_tree(decision_tree=regrModel)



#%%test code
treevis = tree.export_graphviz(clf, out_file=None, feature_names=['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 'Insulin','BMI', 'DiabetesPedigreeFunction', 'Age'],  class_names=['0','1'], filled=True, rounded=True, special_characters=True)
print(treevis)
