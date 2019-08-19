#Topic: Prediction - Linear Regression
#-----------------------------
#https://scikit-learn.org/stable/auto_examples/linear_model/plot_ols.html
#libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#for Linear Regression
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error, r2_score

# Load the diabetes dataset
diabetes = datasets.load_diabetes()
#https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_diabetes.html
type(diabetes)  #bunch type
diabetes.head()  #will not work
diabetes.data[0:3,0:4] 
#Bunch is a subclass of dict; it supports all the methods a dict does:Dictionary-like object, the interesting attributes are: ‘data’, the data to learn, ‘target’, the regression target for each sample,
#data has features, target has DV value# Use only one feature
diabetes_X = diabetes.data[:, np.newaxis, 2]
#https://docs.scipy.org/doc/numpy/reference/constants.html#numpy.newaxis
diabetes_X
# Split the data into training/testing sets
diabetes_X_train = diabetes_X[:-20]
diabetes_X_test = diabetes_X[-20:]
len(diabetes_X_train)
len(diabetes_X_test)

# Split the targets into training/testing sets
diabetes.target
diabetes_y_train = diabetes.target[:-20]
diabetes_y_test = diabetes.target[-20:]

# Create linear regression object from sklearn import linear_model
regr = linear_model.LinearRegression()
#select linear regression
regr

# Train the model using the training sets
regr.fit(diabetes_X_train, diabetes_y_train)

# Make predictions using the testing set
diabetes_y_pred = regr.predict(diabetes_X_test)

# The coefficients
print('Coefficients: \n', regr.coef_)

#from sklearn.metrics import mean_squared_error, r2_score
# The mean squared error
print("Mean squared error: %.2f" % mean_squared_error( diabetes_y_test, diabetes_y_pred))

# Explained variance score: 1 is perfect prediction
print('Variance score: %.2f' % r2_score(diabetes_y_test, diabetes_y_pred))


# Plot outputs  : select all at once and run
plt.scatter(diabetes_X_test, diabetes_y_test,  color='black')
plt.plot(diabetes_X_test, diabetes_y_pred, color='blue', linewidth=3)

plt.xticks(())
plt.yticks(())

plt.show()