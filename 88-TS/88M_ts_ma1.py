#Moving Average
#-----------------------------
#%https://machinelearningmastery.com/time-series-forecasting-methods-in-python-cheat-sheet/
#Moving Average (MA)
#The moving average (MA) method models the next step in the sequence as a linear function of the residual errors from a mean process at prior time steps.
#
#A moving average model is different from calculating the moving average of the time series.
#
#The notation for the model involves specifying the order of the model q as a parameter to the MA function, e.g. MA(q). For example, MA(1) is a first-order moving average model.
#
#The method is suitable for univariate time series without trend and seasonal components.


# MA example
from statsmodels.tsa.arima_model import ARMA
from random import random

# contrived dataset
data = [x + random() for x in range(1, 100)]
data

# fit model
model = ARMA(data, order=(0, 1))

model_fit = model.fit(disp=False)

# make prediction
yhat = model_fit.predict(len(data), len(data))

print(yhat)
