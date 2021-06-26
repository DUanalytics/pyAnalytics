#python : DUP - Topic : TS Arima Forecasting
#https://pypi.org/project/pmdarima/
#Fitting a simple auto-ARIMA on the wineind dataset:
import pmdarima as pm
from pmdarima.model_selection import train_test_split
import numpy as np
import matplotlib.pyplot as plt

# Load/split your data
y = pm.datasets.load_wineind()
y
train, test = train_test_split(y, train_size=150)
train, len(train)
test, len(test)
test.shape  #26 steps ahead to be predicted, not years or months
# Fit your model
model = pm.auto_arima(train, seasonal=True, m=12)
#takes time to process

# make your forecasts
forecasts = model.predict(test.shape[0])  # predict N steps into the future
forecasts

# Visualize the forecasts (blue=train, green=forecasts)
x = np.arange(y.shape[0])
plt.plot(x[:150], train, c='blue')
plt.plot(x[150:], forecasts, c='green')
plt.show();



#another library
#https://machinelearningmastery.com/arima-for-time-series-forecasting-with-python/
from pandas import datetime
from pandas import read_csv
from pandas import DataFrame
from statsmodels.tsa.arima.model import ARIMA
from matplotlib import pyplot
# load dataset
def parser(x):	return datetime.strptime('190'+x, '%Y-%m')
url = 'https://raw.githubusercontent.com/jbrownlee/Datasets/master/shampoo.csv'
series = read_csv(url, header=0, index_col=0, parse_dates=True, squeeze=True, date_parser=parser)
series #dates as index
series.index = series.index.to_period('M')
series  #only months now in index
type(series)
series.describe()

# fit model
model = ARIMA(series, order=(5,1,0))
model_fit = model.fit()

# summary of fit model
print(model_fit.summary())
# line plot of residuals
residuals = DataFrame(model_fit.resid)
residuals.plot()
pyplot.show()
# density plot of residuals
residuals.plot(kind='kde')
pyplot.show()
# summary stats of residuals
print(residuals.describe())


#steps
# 1. Visualize the Time Series Data
# 2. Identify if the date is stationary
# 3. Plot the Correlation and Auto Correlation Charts
# 4. Construct the ARIMA Model or Seasonal ARIMA based on the data

