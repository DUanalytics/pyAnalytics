#python : Topic :Decision Tree using mtcars

#standard libaries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pydataset import data
import seaborn as sns
df = data('mtcars')
df.head()
#from sklearn.tree import DecisionTreeClassifier, export_graphviz
from sklearn.model_selection import train_test_split
from sklearn import metrics, tree
df['am'].value_counts()
df.columns

#classification
#predict if transmission of car is 0 or 1 on basis of mpg, hp, wt
X1 = df[['mpg','hp','wt']]
Y1 = df[['am']]
Y1.value_counts()

#for splitting into train and test 
from sklearn.model_selection import train_test_split
X1_train, X1_test, Y1_train, Y1_test = train_test_split(X1, Y1, test_size=.20)
X1_train.shape
X1_test.shape

#classification tree
from sklearn.tree import DecisionTreeClassifier
clsModel = DecisionTreeClassifier()  #model with parameter
clsModel.fit(X1_train, Y1_train)
ypred1 = clsModel.predict(X1_test)
len(ypred1)
ypred1
Y1_test

#Visualise
text_representation = tree.export_text(clsModel)
print(text_representation)
tree.plot_tree?

fig = plt.figure(figsize=(30,20))
tree.plot_tree(clsModel)
plt.show();

tree.plot_tree(clsModel, max_depth=1, filled=True)

fig = plt.figure(figsize=(30,20))
tree.plot_tree(clsModel,  feature_names=['mpg','hp','wt'],   class_names= ['auto(0)','manual(1)'],  filled=True, node_ids=True)  
plt.show();
#(The plot_tree returns annotations for the plot, to not show them in the notebook I assigned returned value to _.)
_ = tree.plot_tree(clsModel,  feature_names=['mpg','hp','wt'],   class_names= ['am'],  filled=True)  

#To save the figure to the .png file:
fig.savefig("classtreee.png")


from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
classification_report(y_true=Y1_test, y_pred= ypred1)
confusion_matrix(y_true=Y1_test, y_pred=ypred1)
accuracy_score(y_true=Y1_test, y_pred=ypred1)
np.array(Y1_test)
np.array(ypred1).reshape((-1,1))
df1 = Y1_test
df1['ypred1'] = ypred1
df1

newData1 = X1.sample(4)
newData1
clsModel.predict(newData1)

#%% Regression Tree
#regression
#predict if mpg (numerical value) on basis of am, hp, wt
X2 = df[['am','hp','wt']]
Y2 = df[['mpg']]
np.mean(Y2)
from sklearn.tree import DecisionTreeRegressor
X2.shape
X2_train, X2_test, Y2_train, Y2_test = train_test_split(X2, Y2, test_size=.20)
X2_train.shape
X2_test.shape
regrModel = DecisionTreeRegressor()  #model with parameter
regrModel.fit(X2_train, Y2_train)

#visualise
text_representation = tree.export_text(regrModel)
print(text_representation)
fnames = ['am','hp','wt']
fig = plt.figure(figsize=(40,30))
tree.plot_tree(regrModel, feature_names=fnames, filled=True)
plt.show();

fig = plt.figure(figsize=(20,10))
tree.plot_tree(regrModel, feature_names=['am','hp','wt'], filled=True, max_depth=2, fontsize=20, node_ids=True)
plt.show();

Y2_train[X2_train['hp'] <= 92].aggregate({'mpg':np.mean})
Y2_train[(X2_train['hp'] > 92) & (X2_train['hp'] <= 177.5)]
Y2_train[(X2_train['hp'] > 92) & (X2_train['hp'] <= 177.5)]['mpg'].aggregate([np.mean, 'count'])
Y2_train[X2_train['hp'] <= 177.5].agg({'mpg':np.mean, 'mpg':'count'})

#depthwise
tree.plot_tree(regrModel, feature_names=['am','hp','wt'], filled=True, max_depth=0, proportion=True, node_ids=True, fontsize=10)

tree.plot_tree?
#https://scikit-learn.org/stable/modules/generated/sklearn.tree.plot_tree.html

#predict
ypred2 = regrModel.predict(X2_test)
ypred2
len(ypred2)
Y2_test
type(ypred2)
type(Y2_test)

df2 = Y2_test
df2
df2['ypred2'] = ypred2
df2
df2['mpg'].values
#Root Mean Squared Error (RMSE)
np.sqrt(metrics.mean_squared_error(y_true=Y2_test, y_pred=ypred2))
np.sqrt(metrics.mean_squared_error(y_true=df2['mpg'].values, y_pred=df2['ypred2'].values))
#predict for unknown data
newData2 = X2.sample(4)
newData2
regrModel.predict(newData2)



#https://mljar.com/blog/visualize-decision-tree/
