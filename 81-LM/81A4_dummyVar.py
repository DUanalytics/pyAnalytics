#Topic: Linear Regresstion with Continuous and Categorical Variables
#-----------------------------
#libraries

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#df = pd.read_csv('data/mtcars.csv')
from pydataset import data
mtcars = data('mtcars')
mtcars.head()
df = mtcars

from statsmodels.formula.api import ols
model1 = ols('mpg ~ wt + C(gear) +C(am)', data=df).fit()
model1.summary()

#%%%%
X = df[['mpg','gear','am']]
X = pd.get_dummies(data=X, drop_first=True)
X
Y = df['mpg']

from sklearn import linear_model
from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = .20, random_state = 40)
X_train
X_test
model2 = linear_model.LinearRegression()
# Do not use fit_intercept = False if you have removed 1 column after dummy encoding
model2.fit(X_train, Y_train)
predicted2 = model2.predict(X_test)
predicted2    
    
#https://stackoverflow.com/questions/50733014/linear-regression-with-dummy-categorical-variables
#https://songhuiming.github.io/pages/2017/01/21/linear-regression-in-python-chapter-3-regression-with-categorical-predictors/
#https://medium.com/data-py-blog/multiple-linear-regression-in-python-329e60cdc7ab
#https://medium.com/@manjabogicevic/multiple-linear-regression-using-python-b99754591ac0
#https://datascience.stackexchange.com/questions/14666/why-after-adding-categorical-data-the-linear-regression-fails
    