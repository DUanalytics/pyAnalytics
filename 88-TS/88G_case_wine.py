#Topic: Time Series - Wine Data
#-----------------------------
#https://www.alkaline-ml.com/pmdarima/user_guide.html
#https://www.alkaline-ml.com/pmdarima/auto_examples/example_simple_fit.html#sphx-glr-auto-examples-example-simple-fit-py
import pmdarima as pm
import numpy as np
from matplotlib import pyplot as plt

# ########################################
# Load the data and split it into separate pieces
data = pm.datasets.load_wineind()
train, test = data[:150], data[150:]
train
test
# Fit a simple auto_arima model
arima = pm.auto_arima(train, error_action='ignore', trace=1,                      seasonal=True, m=12)
arima
######################################################
# Plot actual test vs. forecasts:
x = np.arange(test.shape[0])
x
plt.scatter(x, test, marker='x')
plt.plot(x, arima.predict(n_periods=test.shape[0]))
plt.title('Actual test samples vs. forecasts')
plt.show();
#---------------------
test
predict1 = np.round(arima.predict(n_periods=len(test)))
np.column_stack([test, predict1])
#np.hstack(([test, predict1]))
np.concatenate([test[None,:],predict1[None,:]]).T

#%%%%
#https://www.alkaline-ml.com/pmdarima/auto_examples/arima/example_persisting_a_model.html
import pmdarima as pm
import joblib  # for persistence
import os
#############################################################
# Load the data and split it into separate pieces
y = pm.datasets.load_wineind()
train, test = y[:125], y[125:]

# Fit an ARIMA
arima = pm.ARIMA(order=(1, 1, 2), seasonal_order=(0, 1, 1, 12))
arima.fit(y)

##############################################################
# Persist a model and create predictions after re-loading it
#run together till end
pickle_tgt = "arima.pkl"
try:
    # Pickle it
    joblib.dump(arima, pickle_tgt, compress=3)

    # Load the model up, create predictions
    arima_loaded = joblib.load(pickle_tgt)
    preds = arima_loaded.predict(n_periods=test.shape[0])
    print("Predictions: %r" % preds)

finally:
    # Remove the pickle file at the end of this example
    try:
        os.unlink(pickle_tgt)
    except OSError:
        pass
#end here
preds
