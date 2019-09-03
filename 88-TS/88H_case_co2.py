#Topic ---- Time Series - CO2 Trends
#https://www.digitalocean.com/community/tutorials/a-guide-to-time-series-forecasting-with-arima-in-python-3
#Libraries
import numpy as np
import pandas as pd
import itertools
import matplotlib.pyplot as plt
import warnings
import statsmodels.api as sm
#pip install statsmodels --upgrade
plt.style.use('fivethirtyeight')
#%%%
data = sm.datasets.co2.load_pandas()
help(sm.datasets.co2)
#https://www.statsmodels.org/dev/datasets/generated/co2.html
#Number of observations: 2225
#Number of variables: 2; Variable name definitions:
#    date - sample date in YYMMDD format
#    co2 - CO2 Concentration ppmv
#The data returned by load_pandas contains the dates as the index.
#https://cdiac.ess-dive.lbl.gov/trends/co2/sio-keel-flask/sio-keel-flaskmlo_c.html

data.head()  #no head
data.data.head()   # Amount of CO2 for certain time series
y= data.data
y.to_csv('data/co2.csv')
(d)
y.columns
y.dtypes
y.shape  #2284 : 
y.index.min(), y.index.max()
#1958 to 2001
y_copy = y.copy()
#%%% Data to monthly summary : month start
y = y['co2'].resample('MS').mean()
y
y.isnull()
y.isnull().sum(axis=0)  #rows with missing values : fill it
y = y.fillna(y.bfill())
y.isnull().sum(axis=0)  #nil missing now
y.head(5).append(y.tail(6))
y.shape
#%%%  Visualise
y.plot(figsize=(15,6))
#Seasonal pattern  + increasing trend

#%% Forecasting : predicting - ARIMA
#Auto Regressive Integrated Moving Average  - predict future points 
#Threee distinct integers (p, d, q) used to parameteris ARIMA
#denoted by ARIMA(p, d, q)
#p = auto-regressive part  : effect of past values in our model (eg. it is likely to be warm tomorrow, if it was warm last 3 days)
#d = integrated part : amount of differencing (no of past time points to subtract from current value). eg. It is likely to same temperature if the differences in the last 3 days has been very small... it is sometimes called smoothening
#q = moving average : set the error of the model as a linear combination of the error values observed at previous points in the past

#%%%
#when dealing with seasonal effects we make use of seasonal ARIMA
#denoted as ARIMA(p,d,q) - seasonal parameters : (P, D, Q)s - same with seasonal component
# s - periodicity of TS : 4 - Qtrys, 12-yearly
#%%% Find values of p, d, q 
# R has automated ways of finding these parameters
#define p, d, q to take any value between 0 to 2
p = range(0,2)
p = d = q = range(0,2)
#Generate different combinations of p, d, q triplets
pdq = list(itertools.product(p, d, q))
#Generate all different combinations of seasonal p, q & triplets
seasonal_pdq = [(x[0], x[1], x[2], 12)  for x in list(itertools.product(p, d, q))]
seasonal_pdq
#different combination
print('SARIMAX: {} x {}'.format(pdq[1], seasonal_pdq[1]))
pdq[1], seasonal_pdq[1]
pdq[1], seasonal_pdq[2]
pdq[2], seasonal_pdq[3]
pdq[3], seasonal_pdq[4]
#now find the right combination
#%%%  Find the right combination ..... read this later

#lets assume SARIMAX(1,1,1) x (1,1,1,12) yields lowest AIC value.... 
#this becomes optimal situation

#%%%

mod = sm.tsa.statespace.SARIMAX(y, order=(1,1,1), seasonal_order=(1,1,1,12), enforce_stationarity=False, enforce_invertibility = False)
mod
results = mod.fit()
results
results.summary().tables
print(results.summary().tables[1])
#check for significance of each various : P>|z| : (<0.05)
#weight of each coefficient : ma.L1 
#%%% Checking on assumption - Plot
results.plot_diagnostics(figsize=(15,12))
plt.show();

#check...
#%%% Forecasting
y.index.min(), y.index.max() 
y['1998']
pred = results.get_prediction()
pred2_ci = pred.conf_int()
pred2_ci
pred  = results.get_prediction(start = pd.to_datetime('1998-01-01'), dynamic=False)
pred_ci = pred.conf_int()

#next lines together
ax = y['1990':].plot(label='observed')
pred.predicted_mean.plot(ax=ax, label='One-step ahead Forecast', alpha=.7)

ax.fill_between(pred_ci.index,  pred_ci.iloc[:, 0],  pred_ci.iloc[:, 1], color='k', alpha=.2)

ax.set_xlabel('Date')
ax.set_ylabel('CO2 Levels')
plt.legend()
plt.show();
#our forecasts align with the true values very well, showing an overall increase trend.
#%%%

y_forecasted = pred.predicted_mean
y_truth = y['1998-01-01':]
y_truth
# Compute the mean square error
mse = ((y_forecasted - y_truth) ** 2).mean()
print('The Mean Squared Error of our forecasts is {}'.format(round(mse, 2)))
#The MSE of our one-step ahead forecasts yields a value of 0.07, which is very low as it is close to 0. An MSE of 0 would that the estimator is predicting observations of the parameter with perfect accuracy, which would be an ideal scenario but it not typically possible.

#%%%
#However, a better representation of our true predictive power can be obtained using dynamic forecasts. In this case, we only use information from the time series up to a certain point, and after that, forecasts are generated using values from previous forecasted time points.
#In the code chunk below, we specify to start computing the dynamic forecasts and confidence intervals from January 1998 onwards.
pred_dynamic = results.get_prediction(start=pd.to_datetime('1998-01-01'), dynamic=True, full_results=True)
pred_dynamic_ci = pred_dynamic.conf_int()
##Plotting the observed and forecasted values of the time series, we see that the overall forecasts are accurate even when using dynamic forecasts. All forecasted values (red line) match pretty closely to the ground truth (blue line), and are well within the confidence intervals of our forecast.

ax = y['1990':].plot(label='observed', figsize=(20, 15))
pred_dynamic.predicted_mean.plot(label='Dynamic Forecast', ax=ax)
ax.fill_between(pred_dynamic_ci.index,
                pred_dynamic_ci.iloc[:, 0],
                pred_dynamic_ci.iloc[:, 1], color='k', alpha=.25)

ax.fill_betweenx(ax.get_ylim(), pd.to_datetime('1998-01-01'), y.index[-1],
                 alpha=.1, zorder=-1)
ax.set_xlabel('Date')
ax.set_ylabel('CO2 Levels')
plt.legend()
plt.show();

#%%%Once again, we quantify the predictive performance of our forecasts by computing the MSE:

# Extract the predicted and true values of our time series
y_forecasted = pred_dynamic.predicted_mean
y_truth = y['1998-01-01':]

# Compute the mean square error
mse = ((y_forecasted - y_truth) ** 2).mean()
print('The Mean Squared Error of our forecasts is {}'.format(round(mse, 2)))

#The predicted values obtained from the dynamic forecasts yield an MSE of 1.01. This is slightly higher than the one-step ahead, which is to be expected given that we are relying on less historical data from the time series.
#Both the one-step ahead and dynamic forecasts confirm that this time series model is valid. However, much of the interest around time series forecasting is the ability to forecast future values way ahead in time.

#%%% Step 7 — Producing and Visualizing Forecasts
#In the final step of this tutorial, we describe how to leverage our seasonal ARIMA time series model to forecast future values. The get_forecast() attribute of our time series object can compute forecasted values for a specified number of steps ahead.

# Get forecast 500 steps ahead in future
pred_uc = results.get_forecast(steps=500)

# Get confidence intervals of forecasts
pred_ci = pred_uc.conf_int()
#We can use the output of this code to plot the time series and forecasts of its future values.
ax = y.plot(label='observed', figsize=(20, 15))
pred_uc.predicted_mean.plot(ax=ax, label='Forecast')
ax.fill_between(pred_ci.index,
                pred_ci.iloc[:, 0],
                pred_ci.iloc[:, 1], color='k', alpha=.25)
ax.set_xlabel('Date')
ax.set_ylabel('CO2 Levels')
plt.legend()
plt.show();

#Both the forecasts and associated confidence interval that we have generated can now be used to further understand the time series and foresee what to expect. Our forecasts show that the time series is expected to continue increasing at a steady pace.
#As we forecast further out into the future, it is natural for us to become less confident in our values. This is reflected by the confidence intervals generated by our model, which grow larger as we move further out into the future.

#%%%
#we described how to implement a seasonal ARIMA model in Python. We made extensive use of the pandas and statsmodels libraries and showed how to run model diagnostics, as well as how to produce forecasts of the CO2 time series.
#Here are a few other things you could try:
#Change the start date of your dynamic forecasts to see how this affects the overall quality of your forecasts.
#Try more combinations of parameters to see if you can improve the goodness-of-fit of your model.
#Select a different metric to select the best model. For example, we used the AIC measure to find the best model, but you could seek to optimize the out-of-sample mean square error instead.
#For more practice, you could also try to load another time series dataset to produce your own forecasts.