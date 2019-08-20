#Topic ---- Dividing Data into Train and Test 

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pydataset import data
mtcars = data('mtcars')
data=mtcars
data.head()
data.columns
data.dtypes
data.shape
#%%% Sample by number
s1 = data.sample(10)
s1
#%%%
X=np.arange(10).reshape((5, 2))
y=range(5)
X
y
list(y)
X, y = np.arange(10).reshape((5, 2)), range(5)
X, list(y)
#split X and y
X_train, X_test, y_train, y_test = train_test_split( X, y, test_size=0.33, random_state=42)
X_train
y_train
X_test
y_test
#target variable
train_test_split(y, shuffle=True)
train_test_split(y, shuffle=False)

#%%%
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris
# Load dataset.
iris = load_iris()
type(iris)  #Bunch

X, y = iris.data, iris.target
X
y
#these numpy objects, no head; multi-dim matrices
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2, random_state=123)
X_train
X_train.shape
X_test
X_test.shape
y_train
y_test
#%% split data into training and test data.- specify train and test size
train_X, test_X, train_y, test_y = train_test_split(X, y, train_size=0.5, test_size=0.5,                        random_state =123)
print("Labels for training and testing data")
print(train_y)
print(test_y)
     

#%%%
from sklearn import linear_model as lm
from statsmodels.formula.api import ols
from pydataset import data
mtcars = data('mtcars')
df1 = mtcars[['mpg','wt','hp']]
MTmodel1 = ols("mpg ~ wt + hp", data=df1).fit()
print(MTmodel1.summary())
predictionM1 = MTmodel1.predict()
predictionM1

fig= plt.figure(figsize=(15,8))
fig = sm.graphics.plot_regress_exog(MTmodel1, 'wt', fig=fig)

fig, ax = plt.subplots(figsize=(12, 8))
fig = sm.graphics.plot_fit(MTmodel1, "wt", ax=ax) 

fig, ax = plt.subplots(figsize=(12, 8))
fig = sm.graphics.plot_ccpr(MTmodel1, "wt", ax=ax)

fig = plt.figure(figsize=(12, 8))
fig = sm.graphics.plot_ccpr_grid(MTmodel1, fig=fig)

fig = plt.figure(figsize=(12, 8))
fig = sm.graphics.plot_ccpr_grid(MTmodel1, fig=fig)

#fig, ax = plt.subplots()
#fig = sm.graphics.plot_fit(MTmodel1, 0, ax=ax)
#----
IV = df1[['wt','hp']].values
IV
DV= df1['mpg'].values
DV
IV_train, IV_test, DV_train, DV_test = train_test_split(IV, DV,test_size=0.2, random_state=123)
IV_train

MTmodel2a = linear_model.LinearRegression()
MTmodel2a.fit(IV_train, DV_train)
MTmodel2a.intercept_
MTmodel2a.coef_
predicted2a = MTmodel2a.predict(IV_test)
predicted2a
#The mean squared error
from sklearn.metrics import mean_squared_error, r2_score
mean_squared_error(DV_test, predicted2a)
r2_score(DV_test, predicted2a)


#%%%% Links
#https://pythonprogramminglanguage.com/training-and-test-data/

#%%% Links
#https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html


