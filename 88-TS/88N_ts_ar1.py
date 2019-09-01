#Auto Regressive
#-----------------------------
#%
#Autoregression (AR)
#The autoregression (AR) method models the next step in the sequence as a linear function of the observations at prior time steps.
#
#The notation for the model involves specifying the order of the model p as a parameter to the AR function, e.g. AR(p). For example, AR(1) is a first-order autoregression model.
#
#The method is suitable for univariate time series without trend and seasonal components.

# AR example
from statsmodels.tsa.ar_model import AR
from random import random
# contrived dataset
data = [x + random() for x in range(1, 100)]
# fit model
model = AR(data)
model_fit = model.fit()
# make prediction
yhat = model_fit.predict(len(data), len(data))
print(yhat)
