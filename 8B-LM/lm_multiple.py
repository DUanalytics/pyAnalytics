#Topic:
#-----------------------------
#libraries

import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error, r2_score
import pandas as pd

# Load the diabetes dataset
url='https://github.com/DUanalytics/datasets/blob/master/csv/areaRent.csv'
data = pd.read_csv(url)
data

#data has features, target has DV value Use only one feature
X = data.X.values
X
X=X.reshape(-1,1)
X
y = data.Y.values
y=y.reshape(-1,1)
y

# Create linear regression object from sklearn import linear_model
regr = linear_model.LinearRegression()
#select linear regression

# Train the model using the training sets
regr.fit(X,y)

# Make predictions using the testing set
y_pred = regr.predict(X)
y_pred
# The coefficients
print('Coefficients: \n', regr.coef_)

#from sklearn.metrics import mean_squared_error, r2_score
# The mean squared error
print("Mean squared error: %.2f" % mean_squared_error(y,y_pred))

# Explained variance score: 1 is perfect prediction
print('Variance score: %.2f' % r2_score(y, y_pred))


# Plot outputs  : select all at once and run
plt.scatter(X, y,  color='black')
plt.plot(X, y_pred, color='blue', linewidth=3)

plt.xticks(())
plt.yticks(())
plt.show();


#%%
import statsmodels.api as sm
X
y
model = sm.OLS(y, X).fit()
predictions = model.predict(X)
predictions
model.summary()

# add constant
X2 = sm.add_constant(X)
model2 = sm.OLS(y, X2).fit() #output, input
model2.summary()
predictions = model2.predict(X2)
predictions
y
#%%
from sklearn import linear_model
lm = linear_model.LinearRegression()
model3 = lm.fit(X, y)
print(model3)
model3.summary()  #no summary
lm.score(X,y)  #R2
lm.coef_   #b1 coef
lm.intercept_ #b0 coef


#%%
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


#%% Error
y
fig, ax = plt.subplots(figsize=(10,7))
ax.plot(X, y,'o', figsize=(10,7))
ax.plot(X,y, 'o', label='data')
ax.plot(X, model4.fittedvalues, 'g--', label='OLS')