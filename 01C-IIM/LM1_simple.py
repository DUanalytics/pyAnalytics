#Topic:Linear Model - Steps
#-----------------------------
#libraries

#S1- libraries
import numpy as np
from sklearn.linear_model import LinearRegression


#S2 - data
x = np.array([5,15,25,35,45,55]).reshape((-1,1))  #making 2 dim
x  #IV
y = np.array([5,20,14,32,22, 38])  #1 dim
y #DV #(y can 2 dim also : y.reshape((-1,1)))

#S3 - Model
model = LinearRegression()  #create blank model
#other options- fit_intercept (y/N), normalise i/p var
model.fit(x,y)  #find optimal values of weights b0, b1 using x & y, .fit() fits the model

model = LinearRegression().fit(x,y) #another way  #2 lines into 1

#S4 - Results
r_sq = model.score(x, y)
r_sq #coeff of determination : > .6 is good
model.intercept_  #bo
model.coef_  #b1
y = 5.6 + .54 * x  #mathematical equation
#if x is increased by 1 units, y increased by .54 units; when x=0, y=5.6 (constant value)


#S5 Predict
y_pred = model.predict(x)  #predict on trained data 
y_pred
print(y_pred, sep='\t ')
y_pred2 = model.intercept_ + model.coef_ * x
print(y_pred2, sep='\t ')


#new values
x_new = np.arange(5).reshape((-1,1))
x_new
y_new = model.predict(x_new)
print(y_new, sep ='\t ')


#%% MUltiple Linear Regression
import numpy as np
from sklearn.linear_model import LinearRegression
x = [[0,1], [5,1], [15,2], [25,2], [35,11], [45,15], [55,34], [60,35]]
x
y = [4,5,20,14,32,22,38,43]
y
x, y = np.array(x), np.array(y)
x #2 dim ; MLR - 2 variable, 2 dim(LxB) with 2 columns
y #1 dim
x.shape, y.shape

#S3: Model & Fit
model = LinearRegression().fit(x,y)
model.score(x,y)  #R2 
model.intercept_ # constant
model.coef_ #b0, b1
#keeping one IV constant(x1), if x2 increases by 1 unit, y increases by .28 units and so on

#S4 : predict
y_pred = model.predict(x)
y_pred
y_pred2 = model.intercept_ + np.sum(model.coef_ * x, axis=1)
y_pred2
y_pred - y_pred2

#new data
x_new = np.arange(10). reshape((-1,2))
x_new
y_new = model.predict(x_new)
y_new



#%% Stats Models

import numpy as np
import statsmodels.api as sm

from statsmodels.tools import add_constant
x = [[0,1], [5,1], [15,2], [25,2], [35,11], [45,15], [55,34], [60,35]]
x
y = [4,5,20,14,32,22,38,43]
y

x= sm.add_constant(x)  #constant term of 1 added
x
model3 = sm.OLS(y,x)
model3
results = model3.fit()
results
results.summary()
results.rsquared  #coeff of determination
results.rsquared_adj 
results.params  #bo, b1, b2

results.fittedvalues
results.predict(x)


#%%AIC & BIC  
#https://pypi.org/project/RegscorePy
#pip install RegscorePy
import RegscorePy
#aic(y, y_pred, p)
RegscorePy.aic.aic(y=y, y_pred= results.predict(x), p=1)
RegscorePy.bic.bic(y=y, y_pred= results.predict(x), p=1)
