#Topic: Simple Linear Regression - Area - Rent
#-----------------------------
#libraries

import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error, r2_score
import pandas as pd

# Load the diabetes dataset
url1 = "https://raw.githubusercontent.com/DUanalytics/datasets/master/csv/"
url2a = "slr1.csv"
url2b = "women1.csv"
url = url1 + url2a
url
data = pd.read_csv(url)
#data = pd.read_csv('data/slr1.csv')
data

#data has features, target has DV value Use only one feature
X = data.X.values
X
X=X.reshape(-1,1)
X
y = data.Y.values
y=y.reshape(-1,1)
y

#%%%
from sklearn import linear_model
lm = linear_model.LinearRegression()
model1 = lm.fit(X, y)
print(model1)
model1.score(X,y)  #R2
#Coefficients
model1.coef_   #b1 coef
model1.intercept_ #b0 coef
y_pred1 = model1.predict(X)
y_pred1
#The mean squared error
mean_squared_error(y,y_pred1)
r2_score(y, y_pred1)
print('Variance score: %.2f' % r2_score(y, y_pred1))
# Plot outputs  : select all at once and run
plt.scatter(X, y,  color='black')
plt.plot(X, y_pred1, color='blue', linewidth=3)
plt.xticks(())
plt.yticks(())
plt.show();


#%% Model 2
import statsmodels.api as sm
X,y
model2 = sm.OLS(y, X).fit()
predictions2 = model2.predict(X)
predictions2
model2.summary()
# add constant
X2 = sm.add_constant(X)
model3 = sm.OLS(y, X2).fit() #output, input
model3.summary()
predictions3 = model3.predict(X2)
predictions3

#%% Model4
#https://www.learndatasci.com/tutorials/predicting-housing-prices-linear-regression-using-python-pandas-statsmodels/

from statsmodels.formula.api import ols
data
model4 = ols('Y ~ X', data=data).fit()
model4.summary()

import matplotlib.pyplot as plt
import seaborn as sns
#%matplotlib inline
sns.set_style('darkgrid')

fig= plt.figure(figsize=(15,8))
fig = sm.graphics.plot_regress_exog(model4, 'X', fig=fig)
fig
#diagnostic plots


