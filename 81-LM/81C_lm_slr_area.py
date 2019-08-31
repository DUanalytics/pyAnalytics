#Topic: Simple Linear Regression - Area - Rent
#-----------------------------
#https://raw.githubusercontent.com/DUanalytics/pyAnalytics/master/8B-LM/lm_slr_area.py
#libraries
import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split
import pandas as pd
import seaborn as sns
sns.set_style('darkgrid')
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
X2 = sm.add_constant(X) #Adds a column of ones to an array
model3 = sm.OLS(y, X2).fit() #output, input
model3.summary()
predictions3 = model3.predict(X2)
predictions3

#%% Model4
#https://www.learndatasci.com/tutorials/predicting-housing-prices-linear-regression-using-python-pandas-statsmodels/

from statsmodels.formula.api import ols
data.columns
model4 = ols('Y ~ X', data=data).fit()
model4.summary()
fig= plt.figure(figsize=(15,8))
fig = sm.graphics.plot_regress_exog(model4, 'X', fig=fig)
fig
X,y
#diagnostic plots
fig, ax = plt.subplots()
fig = sm.graphics.plot_fit(model4,"X", ax=ax)
ax.set_ylabel("Rent")
ax.set_xlabel("Area")
ax.set_title("Linear Regression")
plt.show();

#%%% #Model5
import statsmodels.api as sm
data = sm.datasets.statecrime.load_pandas().data
data.head()
murder = data['murder']
X = data[['poverty', 'hs_grad']]
X["constant"] = 1 #constant term
y = murder
modelframe = sm.OLS(y, X)
model5 = modelframe.fit()
#Create a plot just for the variable ‘Poverty’:
fig, ax = plt.subplots()
fig = sm.graphics.plot_fit(model5, "poverty", ax=ax)
ax.set_ylabel("Murder Rate")
ax.set_xlabel("Poverty Level")
ax.set_title("Linear Regression")
plt.show();
#https://www.statsmodels.org/stable/generated/statsmodels.graphics.regressionplots.plot_fit.html
