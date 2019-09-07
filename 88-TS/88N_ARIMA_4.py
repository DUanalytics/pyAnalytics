#ARMA 
#-----------------------------
#%
#https://machinelearningmastery.com/time-series-forecasting-methods-in-python-cheat-sheet/
#The Autoregressive Moving Average (ARMA) method models the next step in the sequence as a linear function of the observations and resiudal errors at prior time steps.
#It combines both Autoregression (AR) and Moving Average (MA) models.
#The notation for the model involves specifying the order for the AR(p) and MA(q) models as parameters to an ARMA function, e.g. ARMA(p, q). An ARIMA model can be used to develop AR or MA models.
#The method is suitable for univariate time series without trend and seasonal components.
# ARMA example

from statsmodels.tsa.arima_model import ARMA
from random import random
# contrived dataset
data = [random() for x in range(1, 100)]
# fit model
model = ARMA(data, order=(2, 1))
model_fit = model.fit(disp=False)
# make prediction
yhat = model_fit.predict(len(data), len(data))
print(yhat)
