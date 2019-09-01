#Topic:Py All Models
#-----------------------------
#libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pydataset import data
#Data
mtcars = data('mtcars')
mtcars.head()
df = mtcars
#%%%
#Linear Regression
from sklearn import linear_model as lm
from statsmodels.formula.api import ols
df1 = df[['mpg','wt','hp']]
df1.head()
MTmodel1 = ols("mpg ~ wt + hp", data=df1).fit()
print(MTmodel1.summary())
predictionM1 = MTmodel1.predict()
predictionM1
# Method 2 - sklearn
IV = df1[['wt','hp']].values
IV
DV= df1['mpg'].values
DV
IV_train, IV_test, DV_train, DV_test = train_test_split(IV, DV,test_size=0.2, random_state=123)
IV_train, IV_test, DV_train, DV_test
from sklearn import linear_model
MTmodel2a = linear_model.LinearRegression()
MTmodel2a.fit(IV_train, DV_train)  #putting data to model
#MTmodel2a.summary()  #no summary in sklearn
MTmodel2a.intercept_
MTmodel2a.coef_
predicted2a = MTmodel2a.predict(IV_test)
predicted2a
DV_test
r2_score(DV_train, MTmodel2a.predict(IV_train))
#The mean squared error
from sklearn.metrics import mean_squared_error, r2_score
mean_squared_error(DV_test, predicted2a)
r2_score(DV_test, predicted2a)  

#%%% Logistic Regression

from sklearn.linear_model import LogisticRegression
#create an instance and fit the model 
logmodel = LogisticRegression()
# Data
#predict am from mpg, hp, wt
df2 = df[['am','hp','wt','mpg']]
df2.head()
X_train, X_test, y_train, y_test = train_test_split ( df2.drop('am',axis=1), df2['am'], test_size=0.30,  random_state=101)
X_train.shape, X_test.shape, y_train.shape, y_test.shape

logmodel.fit(X_train, y_train)
X_test
y_test
predictions = logmodel.predict(X_test)
predictions
#
from sklearn.metrics import classification_report
print(classification_report(y_test,predictions))

from sklearn.metrics import confusion_matrix
print(confusion_matrix(y_test, predictions))

#%%%%  Decision Tree



#%%% Clustering


#%%% Time Series
