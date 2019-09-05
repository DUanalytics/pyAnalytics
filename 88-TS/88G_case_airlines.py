#Topic: Time Series - Airlines
#-----------------------------
#libraries
#https://www.analyticsvidhya.com/blog/2018/08/auto-arima-time-series-modeling-python-r/
#The general steps to implement an ARIMA model are –
#
#Load the data: The first step for model building is of course to load the dataset
#Preprocessing: Depending on the dataset, the steps of preprocessing will be defined. This will include creating timestamps, converting the dtype of date/time column, making the series univariate, etc.
#Make series stationary: In order to satisfy the assumption, it is necessary to make the series stationary. This would include checking the stationarity of the series and performing required transformations
#Determine d value: For making the series stationary, the number of times the difference operation was performed will be taken as the d value
#Create ACF and PACF plots: This is the most important step in ARIMA implementation. ACF PACF plots are used to determine the input parameters for our ARIMA model
#Determine the p and q values: Read the values of p and q from the plots in the previous step
#Fit ARIMA model: Using the processed data and parameter values we calculated from the previous steps, fit the ARIMA model
#Predict values on validation set: Predict the future values
#Calculate RMSE: To check the performance of the model, check the RMSE value using the predictions and actual values on the validation set

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#load the data
url = 'https://raw.githubusercontent.com/DUanalytics/datasets/master/csv/airline.csv'
data = pd.read_csv('data/airline.csv')
data
#divide into train and validation set
train = data[:int(0.7*(len(data)))]
valid = data[int(0.7*(len(data))):]
train.shape, valid.shape

#preprocessing (since arima takes univariate series as input)
train.drop('month',axis=1,inplace=True)
valid.drop('month',axis=1,inplace=True)

#plotting the data
train['passengers'].plot()
valid['passengers'].plot()

#building the model
#pip install pmdarima
#https://pypi.org/project/pmdarima/
#from pyramid.arima import auto_arima
from pmdarima.arima import auto_arima
#https://www.alkaline-ml.com/pmdarima/modules/classes.html#module-pmdarima.datasets
model = auto_arima(train, trace=True, error_action='ignore', suppress_warnings=True)
model.fit(train)

forecast = model.predict(n_periods=len(valid))
forecast = pd.DataFrame(forecast,index = valid.index, columns=['Prediction'])
forecast.head()
#plot the predictions for validation set
plt.plot(train, label='Train')
plt.plot(valid, label='Valid')
plt.plot(forecast, label='Prediction')
plt.show();
