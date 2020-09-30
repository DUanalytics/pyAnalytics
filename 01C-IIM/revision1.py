#python : Topic : Revision
#standard libaries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pydataset import data
import seaborn as sns


#Data Structures
list1 = [1,2,'a', 'b', 'Dhiraj', 'Kounal']
print(list1)

list1[1:4]

tuple1 = (1,5,9)
print(tuple1)

set1 = {'India', 'Pakistan' ,'England', 'India'}
print(set1)

dict1 = {'rollno':[1,2,3], 'name':['India','Pakistan','England'], 'captain': ['C1','C2','C3']}
print(dict1)
dict1['rollno']

#%%
import numpy as np
np.arange(1,10)

import pandas as pd
link1 = 'https://raw.githubusercontent.com/DUanalytics/datasets/master/csv/buyPC.csv'
df1 = pd.read_csv(link1)
df1.head()

from pydataset import data 
data('mtcars')
mtcars1 = data('mtcars')
mtcars1.describe()
mtcars1.columns
#summary
mtcars1.groupby(['cyl','gear']).agg({'mpg':'mean', 'gear':'size'})
pd.crosstab(mtcars1.cyl, mtcars1.gear)


import matplotlib.pyplot as plt
import seaborn as sns
sns.heatmap(mtcars1.corr(), annot=True)
mtcars1.gear.value_counts().plot(kind='bar')
mtcars1.plot.scatter(x='wt', y='mpg')
mtcars1.groupby(['gear','cyl']).size().unstack().plot.bar()

df_mtcars2 = mtcars1[['mpg','wt','hp']].copy()
df_mtcars2.head()
IV = df_mtcars2[['wt','hp']].values
DV = df_mtcars2[['mpg']].values

#linear Regression
from sklearn import linear_model
from sklearn.model_selection import train_test_split
LM1 = linear_model.LinearRegression()
LM1.fit(IV, DV)
LM1.intercept_
LM1.coef_
LM1.predict(IV)  #predicted values

from statsmodels.formula.api import ols
LM2 = ols("mpg ~ wt + hp", data=df_mtcars2).fit()
print(LM2.summary())
LM2.predict()

#%% split data into training and test data.- specify train and test size
train_X, test_X, train_y, test_y = train_test_split(IV, DV, train_size=0.5, test_size=0.5, random_state =123)
print("Labels for training and testing data")
print(train_y)
print(test_y)

LM3 = linear_model.LinearRegression()
train_X
train_y
LM3.fit(train_X, test_y)
LM3.intercept_
LM3.coef_
LM3.predict(test_X)

from sklearn.metrics import mean_squared_error, r2_score
mean_squared_error(test_y, LM3.predict(test_X))
r2_score(test_y, LM3.predict(test_X))


MTmodel1 = ols("mpg ~ wt + hp", data=df1).fit()
print(MTmodel1.summary())
predictionM1 = MTmodel1.predict()
predictionM1

#%%% Logistic Regression
from sklearn import linear_model
from sklearn.metrics import classification_report, confusion_matrix

IV2 = mtcars1[['wt','hp','mpg']].values
DV2 = mtcars1[['am']].values

LGM1 = linear_model.LogisticRegression(solver='liblinear', random_state=0).fit(IV2, DV2)
LGM1.classes_
LGM1.intercept_
LGM1.coef_  #odd ratio
LGM1.predict_proba(IV2) #predict prob
LGM1.predict(IV2)
confusion_matrix(DV2, LGM1.predict(IV2) )
classification_report(DV2, LGM1.predict(IV2) )
cm = confusion_matrix(DV2, LGM1.predict(IV2) )
sns.heatmap(cm, annot=True)

#decision tree
#predict if transmission of car is 0 or 1 on basis of mpg, hp, wt
IV3 = mtcars1[['mpg','hp','wt']]
DV3 = mtcars1[['am']]
DV3.value_counts()
train_X, test_X, train_y, test_y = train_test_split(IV3, DV3, test_size=.20)
train_X.shape
test_X.shape

from sklearn.tree import DecisionTreeClassifier
DT_clsModel = DecisionTreeClassifier().fit(train_X, train_y)
ypred1 = DT_clsModel.predict(test_X)
ypred1

from sklearn import metrics, tree
fig = plt.figure(figsize=(30,20))
tree.plot_tree(DT_clsModel)
plt.show();

#similarly do regresssion tree

#clustering
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
scalar = StandardScaler()
mtcars2 = mtcars1[['wt', 'mpg','hp']]
CLT_mtcars = mtcars2.values
CLT_scaled = scalar.fit_transform(CLT_mtcars)

kmeans = KMeans(n_clusters=2)  #hyper parameters
kmeans.fit(CLT_scaled)
kmeans.inertia_  #sum of sq distances of samples to their centeroid
kmeans.cluster_centers_
kmeans.labels_
kmeans.n_iter_  #iterations to stabilise the clusters
kmeans.predict(CLT_scaled)

clusterNos = kmeans.labels_
clusterNos
mtcars2.groupby([clusterNos]).mean()
mtcars1.groupby('am').agg({'wt':np.mean, 'mpg':np.mean, 'hp':np.mean})
#auto and manual cars average

