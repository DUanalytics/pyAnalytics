#python : DUP - Topic : TS Components & Arima

#model
#y(t) = Level + Trend + Seasonality + Noise #Additive Model
#y(t) = Level * Trend * Seasonality * Noise #multiplicative Model
#from statsmodels.tsa.seasonal import seasonal_decompose
#result = seasonal_decompose(series, model='additive')
#pd.DataFrame ({'trend':result.trend, 'seasonal' :result.seasonal, 'residue':result.resid, 'observed':result.observed})
#Level: The average value in the series.
#Trend: The increasing or decreasing value in the series.
#Seasonality: The repeating short-term cycle in the series.
#Noise: The random variation in the series.
#the trend (long term direction), the seasonal (systematic, calendar related movements) and the irregular/noise (unsystematic, short term fluctuations). 

#https://machinelearningmastery.com/decompose-time-series-data-trend-seasonality/

#---------------------------------------

# Importing required libraries
import numpy as np
import pandas as pd
import matplotlib.pylot as plt
from statsmodels.tsa.seasonal import seasonal_decompose
  
# Read the AirPassengers dataset
url='https://raw.githubusercontent.com/DUanalytics/datasets/master/csv/AirPassengers.csv'
airline = pd.read_csv(url, index_col ='Month', parse_dates = True)
airline.shape
# Print the first five rows of the dataset
airline.head()
  
# ETS Decomposition
result = seasonal_decompose(airline['Passengers'], model = 'multiplicative')
result  
result.summary()
result
print(result.trend), print(result.seasonal),print(result.resid), print(result.observed)
#Actual Values = Product of (Seasonal * Trend * Resid)
combined= pd.DataFrame ({'trend':result.trend, 'seasonal' :result.seasonal, 'residue':result.resid, 'observed':result.observed, 'actual':pd.Series(airline['Passengers'])})
combined.head()
# ETS plot 
result.plot()



#https://ionides.github.io/531w20/midterm_project/project37/Midterm_project.html

#auto arima
# To install the library
#pip install pmdarima
  
# Import the library
from pmdarima import auto_arima
  
# Ignore harmless warnings
import warnings
warnings.filterwarnings("ignore")
  
# Fit auto_arima function to AirPassengers dataset
stepwise_fit = auto_arima(airline['Passengers'], start_p = 1, start_q = 1,
 max_p = 3, max_q = 3, m = 12,  start_P = 0, seasonal = True, d = None, D = 1, trace = True,   error_action ='ignore', suppress_warnings = True ,  stepwise = True) 
# we don't want to know if an order does not work ,  # we don't want convergence warnings  # set to stepwise
  
# To print the summary
stepwise_fit.summary()

## Split data into train / test sets
train = airline.iloc[:len(airline)-12]
train
test = airline.iloc[len(airline)-12:] # set one year(12 months) for testing
test  
# Fit a SARIMAX(0, 1, 1)x(2, 1, 1, 12) on the training set
from statsmodels.tsa.statespace.sarimax import SARIMAX
  
model = SARIMAX(train['Passengers'], order = (0, 1, 1), seasonal_order =(2, 1, 1, 12))
  
result = model.fit()
result.summary()

#Code : Predictions of ARIMA Model against the test set
start = len(train)
end = len(train) + len(test) - 1
  
# Predictions for one-year against the test set
predictions = result.predict(start, end,  typ ='levels').rename( "Predictions")
  
# plot predictions and actual values
predictions.plot(legend = True)
test['Passengers'].plot(legend = True)


#Code : Evaluate the model using MSE and RMSE
# Load specific evaluation tools
from sklearn.metrics import mean_squared_error
from statsmodels.tools.eval_measures import rmse
  
# Calculate root mean squared error
rmse(test["Passengers"], predictions)
  
# Calculate mean squared error
mean_squared_error(test["Passengers"], predictions)

#Code : Forecast using ARIMA Model


# Train the model on the full dataset
model = model = SARIMAX(airline['Passengers'], order = (0, 1, 1), seasonal_order =(2, 1, 1, 12))
result = model.fit()
  
# Forecast for the next 3 years
forecast = result.predict(start = len(airline),  end = (len(airline)-1) + 3 * 12, typ = 'levels').rename('Forecast')
  
# Plot the forecast values
airline['Passengers'].plot(figsize = (12, 5), legend = True)
forecast.plot(legend = True)

#read 
#https://www.geeksforgeeks.org/python-arima-model-for-time-series-forecasting/
#https://www.machinelearningplus.com/time-series/time-series-analysis-python/