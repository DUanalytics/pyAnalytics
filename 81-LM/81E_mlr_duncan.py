#Topic ----Linear Regression - Car Data
#https://www.statsmodels.org/dev/examples/notebooks/generated/regression_plots.html#Partial-Regression-Plots
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm
from statsmodels.formula.api import ols
#from statsmodels.compat import lzip
#%%%Load the Data
#use a utility function to load any R dataset available from the great Rdatasets package.
prestige = sm.datasets.get_rdataset("Duncan", "carData", cache=True).data
#https://www.statsmodels.org/devel/datasets/index.html
#.get_rdataset(dataname, package='datasets', cache=False)[source]
prestige.head()
prestige.columns
prestige.shape
prestige.describe()
prestige.type.value_counts()
prestige.index.value_counts()

#%%%
prestige_model = ols("prestige ~ income + education", data=prestige).fit()
print(prestige_model.summary())

#%%Influence plots
#Influence plots show the (externally) studentized residuals vs. the leverage of each observation as measured by the hat matrix
fig, ax = plt.subplots(figsize=(12,8))
fig = sm.graphics.influence_plot(prestige_model, ax=ax, criterion="cooks")
#The influence of each point can be visualized by the criterion keyword argument. Options are Cook’s distance and DFFITS, two measures of influence.
#there are a few worrisome observations. Both contractor and reporter have low leverage but a large residual. RR.engineer has small residual and large leverage. Conductor and minister have both high leverage and large residuals, and, therefore, large influence.
#%%%Partial Regression Plots
#Since we are doing multivariate regressions, we cannot just look at individual bivariate plots to discern relationships. Instead, we want to look at the relationship of the dependent variable and independent variables conditional on the other independent variables. We can do this through using partial regression plots, otherwise known as added variable plots.
fig, ax = plt.subplots(figsize=(12,8))
fig = sm.graphics.plot_partregress("prestige", "income", ["income", "education"], data=prestige, ax=ax, obs_labels=True)
#prestige & income on 
fix, ax = plt.subplots(figsize=(12,14))
fig = sm.graphics.plot_partregress("prestige", "income", ["education"], data=prestige, ax=ax)
#partial regression plot confirms the influence of conductor, minister, and RR.engineer on the partial relationship between income and prestige. The cases greatly decrease the effect of income on prestige. Dropping these cases confirms this.
#%%% Subset
subset = ~prestige.index.isin(["conductor", "RR.engineer", "minister"])
prestige_model2 = ols("prestige ~ income + education", data=prestige, subset=subset).fit()
print(prestige_model2.summary()) #R2- .87
print(prestige_model.summary())  #R2- .82

#%%%
#quick check of all the regressors, you can use plot_partregress_grid. These plots will not label the points, but you can use them to identify problems and then use plot_partregress to get more information.
fig = plt.figure(figsize=(12,8))
fig = sm.graphics.plot_partregress_grid(prestige_model, fig=fig)

#%%%Component-Component plus Residual (CCPR) Plots
#The CCPR plot provides a way to judge the effect of one regressor on the response variable by taking into account the effects of the other independent variables
fig, ax = plt.subplots(figsize=(12, 8))
fig = sm.graphics.plot_ccpr(prestige_model, "education", ax=ax)
#relationship between the variation in prestige explained by education conditional on income seems to be linear, though you can see there are some observations that are exerting considerable influence on the relationship. We can quickly look at more than one variable by using plot_ccpr_grid.
fig = plt.figure(figsize=(12, 8))
fig = sm.graphics.plot_ccpr_grid(prestige_model, fig=fig)
#%%%Regression Plots
#The plot_regress_exog function is a convenience function that gives a 2x2 plot containing the dependent variable and fitted values with confidence intervals vs. the independent variable chosen, the residuals of the model vs. the chosen independent variable, a partial regression plot, and a CCPR plot. This function can be used for quickly checking modeling assumptions with respect to a single regressor.
fig = plt.figure(figsize=(12,8))
fig = sm.graphics.plot_regress_exog(prestige_model, "education", fig=fig)

#%%%Fit Plot
#The plot_fit function plots the fitted values versus a chosen independent variable. It includes prediction confidence intervals and optionally plots the true dependent variable.
fig, ax = plt.subplots(figsize=(12, 8))
fig = sm.graphics.plot_fit(prestige_model, "education", ax=ax)

#%%% Dataset
# =============================================================================
# #The ``Duncan`` data frame has 45 rows and 4 columns. Data on the prestige and other characteristics of 45 U. S. occupations in 1950.
# #Usage: Duncan
# #Format :This data frame contains the following columns:
# #type :   Type of occupation. A factor with the following levels: ``prof``,   professional and managerial; ``wc``, white-collar; ``bc``,   blue-collar.
# #income:   Percentage of occupational incumbents in the 1950 US Census who    earned $3,500 or more per year (about $36,000 in 2017 US dollars).
# #education :    Percentage of occupational incumbents in 1950 who were high school graduates (which, were we cynical, we would say is roughly equivalent    to a PhD in 2017)
# #prestige :    Percentage of respondents in a social survey who rated the occupation as “good” or better in prestige
# =============================================================================
