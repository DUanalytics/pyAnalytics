#Topic:Regression Tree
#-----------------------------
#libraries
import pandas as pd
import numpy as np
from sklearn import tree
X = [[0, 0], [2, 2]]
y = [0.5, 2.5]

clf = tree.DecisionTreeRegressor()
clf = clf.fit(X, y)
clf.predict([[1, 1]])
#array([0.5])

from sklearn import tree
#what is package expected in placement drive
age = [23, 25, 30, 31, 27]
experience = [0,1,5, 2, 3]
salary = [15, 30, 40, 34, 30]
mnc = ['N','Y','N','Y','Y']
data = pd.DataFrame({'age':age, 'experience':experience, 'salary':salary,'mnc':mnc})
data

X1A = np.array(data[['age', 'experience']])
X1A
Y1A = np.array(data[['salary']])
Y1A
Y1B = np.array(data[['mnc']])
Y1B

clfR2 = tree.DecisionTreeRegressor()
clfR2 = clf2.fit(X1A, Y1A)
clfR2.predict([[26, 2]])   #salary expected is 30 
clfR2.predict_proba()

clfC2 = tree.DecisionTreeClassifier()
clfC2 = clf.fit(X1A, Y1B)
Y1B1 = np.array(pd.get_dummies(data['mnc']))
Y1B1
clfC2 = clf.fit(X1A, Y1B1)
clfC2.predict([[26, 2]])
data
clfC2.predict(X1A)
tree.predict_proba(clfC2)

data
IVs = ['age','experience']
DV1 = ['salary']
DV2 = ['mnc']

#plotting trees
#lot_tree(*args, decision_tree, max_depth=None, feature_names=None, class_names=None, label='all', filled=False, impurity=True, node_ids=False, proportion=False, rotate='deprecated', rounded=False, precision=3, ax=None, fontsize=None)

#regression tree
tree.plot_tree(clfR2)#class names not avl
tree.plot_tree(clfR2, feature_names=IVs, class_names=DV1, filled=True, node_ids=True, proportion=True, fontsize=10)

#classification tree
tree.plot_tree(clfC2)
tree.plot_tree(clfC2, feature_names=IVs, class_names=['Y','N'], filled=True, node_ids=True, proportion=True, fontsize=10)





# Confusion matrix for class 
from sklearn.metrics import confusion_matrix
confusion_matrix(y_true= Y1B, y_pred= clfC2.predict(X1A))

#R2 value for Regression Tree
clfR2.predict(X1A)
Y1A
clfR2.score(X1A, Y1A) #predict correctly
clfR2.get_depth()

tree.plot_tree?
