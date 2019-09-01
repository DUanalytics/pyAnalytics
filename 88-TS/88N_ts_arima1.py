#ARIMA
#-----------------------------
#%
#Autoregressive Integrated Moving Average (ARIMA)
#The Autoregressive Integrated Moving Average (ARIMA) method models the next step in the sequence as a linear function of the differenced observations and residual errors at prior time steps.
#
#It combines both Autoregression (AR) and Moving Average (MA) models as well as a differencing pre-processing step of the sequence to make the sequence stationary, called integration (I).
#
#The notation for the model involves specifying the order for the AR(p), I(d), and MA(q) models as parameters to an ARIMA function, e.g. ARIMA(p, d, q). An ARIMA model can also be used to develop AR, MA, and ARMA models.
#
#The method is suitable for univariate time series with trend and without seasonal components

# ARIMA example
from statsmodels.tsa.arima_model import ARIMA
from random import random

# contrived dataset
data = [x + random() for x in range(1, 100)]

# fit model
model = ARIMA(data, order=(1, 1, 1))
model_fit = model.fit(disp=False)
# make prediction
yhat = model_fit.predict(len(data), len(data), typ='levels')
print(yhat)
