#Topic ----Multiple Linear Regression in Python
#Link : https://datatofish.com/multiple-linear-regression-python/
#Imp Note : Before applying linear regression models, make sure to check that a linear relationship exists between the dependent variable (i.e., what you are trying to predict) and the independent variable/s (i.e., the input variable/s).
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style('darkgrid')


#%%%
#Dictionary DS 
Stock_Market = {'Year': [2017,2017,2017,2017,2017,2017,2017, 2017,2017, 2017, 2017,2017, 2016, 2016,2016, 2016,2016,2016,2016,2016, 2016,2016,2016,2016], 'Month': [12, 11,10,9,8,7,6,5,4, 3,2,1,12,11,10,9,8,7,6,5,4,3,2,1], 'Interest_Rate': [2.75,2.5,2.5,2.5, 2.5,2.5,2.5,2.25, 2.25,2.25,2,2,2,1.75,1.75,1.75,1.75,1.75, 1.75,1.75,1.75,1.75,1.75,1.75], 'Unemployment_Rate': [5.3,5.3,5.3,5.3, 5.4,5.6,5.5,5.5, 5.5,5.6,5.7,5.9,6,5.9,5.8,6.1,6.2,6.1,6.1,6.1, 5.9,6.2,6.2,6.1], 'Stock_Index_Price': [1464,1394,1357, 1293,1256, 1254,1234,1195,1159, 1167,1130,1075,1047,965,943, 958,971,949,884, 866,876,822,704,719]   }
#Data Frame 
df = pd.DataFrame(Stock_Market, columns=['Year','Month','Interest_Rate', 'Unemployment_Rate', 'Stock_Index_Price'])
#%%Checking for Linearity
#Before you execute a linear regression model, it is advisable to validate that certain assumptions are met. You may want to check that a linear relationship exists between the dependent variable and the independent variable/s.
#check that a linear relationship exists between: Through Plots
#The Stock_Index_Price (dependent variable) and the Interest_Rate (independent variable); and The Stock_Index_Price (dependent variable) and the Unemployment_Rate (independent variable)

#plot between Interest Rate and Stock Price 
plt.scatter(df['Interest_Rate'], df['Stock_Index_Price'], color='red')
plt.title('Stock Index Price Vs Interest Rate', fontsize=14)
plt.xlabel('Interest Rate', fontsize=14)
plt.ylabel('Stock Index Price', fontsize=14)
plt.grid(True)
plt.show();
#plot between Unemployment Rate and Stock Price  
plt.scatter(df['Unemployment_Rate'], df['Stock_Index_Price'], color='green')
plt.title('Stock Index Price Vs Unemployment Rate', fontsize=14)
plt.xlabel('Unemployment Rate', fontsize=14)
plt.ylabel('Stock Index Price', fontsize=14)
plt.grid(True)
plt.show();
#As you can see, a linear relationship exists in both cases:
#In the first case, when interest rates go up, the stock index price also goes up
#In the second case, when unemployment rates go up, the stock index price goes down (here we still have a linear relationship, but with a negative slope)
#Next, we are going to perform the actual multiple linear regression in Python.

#%%% MLR
from sklearn import linear_model
#Stock Prices ~ Interest_Rate + Unemployment_Rate
X = df[['Interest_Rate','Unemployment_Rate']].astype(float)
X.head()
# here we have 2 input variables for multiple regression. If you just want to use one variable for simple linear regression, then use X = df['Interest_Rate'] for example.Alternatively, you may add additional variables within the brackets
Y = df['Stock_Index_Price'].astype(float) # output variable (what we are trying to predict)
Y.head()
# with sklearn
skmodel1 = linear_model.LinearRegression()
skmodel1.fit(X, Y)
print('Intercept: \n', skmodel1.intercept_)
print('Coefficients: \n', skmodel1.coef_)
predictedY1 = skmodel1.predict(X)
predictedY1
#The mean squared error
from sklearn.metrics import mean_squared_error, r2_score
mean_squared_error(Y,predictedY1)
r2_score(Y, predictedY1)

#%%% sm model
import statsmodels.api as sm
X,Y
smmodel2 = sm.OLS(Y, X).fit()
predictions2 = smmodel2.predict(X)
predictions2
smmodel2.summary()

# add constant
X2 = sm.add_constant(X) #Adds a column of ones to an array
#https://www.statsmodels.org/stable/generated/statsmodels.tools.tools.add_constant.html
model3 = sm.OLS(Y, X2).fit() #output, input
model3.summary()
predictions3 = model3.predict(X2)
predictions3
#equation : Stock_Price = 1798 + Interest_Rate * 345 - Unemployment_Rate * 250
df.head()
Interest_Rate = 2.75;  Unemployment_Rate = 5.3
Stock_Price = 1798 + Interest_Rate * 345 - Unemployment_Rate * 250
Stock_Price

#%%%
from statsmodels.formula.api import ols
X.head()
Y.head()
df.head()
df.columns
model4a = 'Stock_Index_Price ~ Interest_Rate + Unemployment_Rate'
model4b = ols(model4a, data=df).fit()
model4b.summary()

fig= plt.figure(figsize=(15,8))
fig = sm.graphics.plot_regress_exog(model4b, 'Interest_Rate', fig=fig)
fig

#%%%Component-Component plus Residual (CCPR) Plots
#The CCPR plot provides a way to judge the effect of one regressor on the response variable by taking into account the effects of the other independent variables. The partial residuals plot is defined as Residuals+BiXi   versus Xi. The component adds BiXi versus Xi to show where the fitted line would lie. Care should be taken if Xi is highly correlated with any of the other independent variables. If this is the case, the variance evident in the plot will be an underestimate of the true variance.
fig, ax = plt.subplots(figsize=(12, 8))
fig = sm.graphics.plot_ccpr(model4b, "Interest_Rate", ax=ax)
#relationship between the variation in Stock explained by Interest conditional seems to be linear, though you can see there are some observations that are exerting considerable influence on the relationship. We can quickly look at more than one variable by using plot_ccpr_grid.
#More than 1 variable
fig = plt.figure(figsize=(12, 8))
fig = sm.graphics.plot_ccpr_grid(model4b, fig=fig)

#Regression Plots
#The plot_regress_exog function is a convenience function that gives a 2x2 plot containing the dependent variable and fitted values with confidence intervals vs. the independent variable chosen, the residuals of the model vs. the chosen independent variable, a partial regression plot, and a CCPR plot. This function can be used for quickly checking modeling assumptions with respect to a single regressor.

fig = plt.figure(figsize=(12,8))
fig = sm.graphics.plot_regress_exog(model4b, "Interest_Rate", fig=fig)

#%%% Fit Plot
#Fit Plot : The plot_fit function plots the fitted values versus a chosen independent variable. It includes prediction confidence intervals and optionally plots the true dependent variable.
fig, ax = plt.subplots(figsize=(12, 8))
fig = sm.graphics.plot_fit(model4b, "Interest_Rate", ax=ax) 


#%%%Links
#https://www.statsmodels.org/dev/examples/notebooks/generated/regression_plots.html
dta= pd.read_csv("http://www.stat.ufl.edu/~aa/social/csv_files/statewide-crime-2.csv")
dta = dta.set_index("State", inplace=True).dropna()


#%%%
#%%% Forcing categorical: eg ‘Gender’ is automatically detected as a categorical variable, and thus each of its different values are treated as different entities.
#An integer column can be forced to be treated as categorical using:
##model = ols('VIQ ~ C(Gender)', data).fit()