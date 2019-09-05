#Topic:
#-----------------------------
#libraries
#https://www.alkaline-ml.com/pmdarima/tips_and_tricks.html

#The auto_arima function fits the best ARIMA model to a univariate time series according to a provided information criterion (either AIC, AICc, BIC or HQIC). The function performs a search (either stepwise or parallelized) over possible model & seasonal orders within the constraints provided, and selects the parameters that minimize the given metric.
#The auto_arima function can be daunting. There are a lot of parameters to tune, and the outcome is heavily dependent on a number of them. In this section, we lay out several considerations you’ll want to make when you fit your ARIMA models.
#ARIMA models are made up of three different terms:
#p: The order of the auto-regressive (AR) model.
#d: The degree of differencing.
#q: The order of the moving average (MA) model.

#Often times, ARIMA models are written in the form ARIMA(p,d,q), where a model with no differencing term, e.g., ARIMA(1,0,12), would be an ARMA (made up of an auto-regressive term and a moving average term, but no integrative term, hence no “I”).

#in pmdarima.ARIMA, these parameters are specified in the order argument as a tuple:

order = (1, 0, 12)  # p=1, d=0, q=12
order = (1, 1, 3)  # p=1, d=1, q=3
#The parameters p and q can be iteratively searched-for with the auto_arima function, but the differencing term, d, requires a special set of tests of stationarity to estimate.

#%%% Understanding differencing (d)
An integrative term, d, is typically only used in the case of non-stationary data. Stationarity in a time series indicates that a series’ statistical attributes, such as mean, variance, etc., are constant over time (i.e., it exhibits low heteroskedasticity.

A stationary time series is far more easy to learn and forecast from. With the d parameter, you can force the ARIMA model to adjust for non-stationarity on its own, without having to worry about doing so manually.

The value of d determines the number of periods to lag the response prior to computing differences. E.g.,

from pmdarima.utils import c, diff

# lag 1, diff 1
x = c(10, 4, 2, 9, 34)
diff(x, lag=1, differences=1)
# Returns: array([ -6.,  -2.,   7.,  25.], dtype=float32)
#lag and differences are not the same!

diff(x, lag=1, differences=2)
# Returns: array([ 4.,  9., 18.], dtype=float32)

diff(x, lag=2, differences=1)
# Returns: array([-8.,  5., 32.], dtype=float32
#The lag corresponds to the offset in the time period lag, whereas the differences parameter is the number of times the differences are computed. Therefore, e.g., for differences=2, the procedure is essentially computing the difference twice:
x = c(10, 4, 2, 9, 34)
x# 1
x[1:], x[:-1]
x_lag = x[1:]  # first lag
x_lag
x[:-1]
x = x_lag - x[:-1]  # first difference
# x = [ -6.,  -2.,   7.,  25.]
(4-10), (2-4), (9-2), (34-9) 
x
# 2
x_lag = x[1:]  # second lag
x_lag
x[:-1]
x = x_lag - x[:-1]
# x = [ 4.,  9., 18.]
(-2 - (-6)), (7 - (-2)), (18-7)  #check this

#%%% Stationary
import pmdarima as pm
from pmdarima import datasets

y = datasets.load_lynx()
pm.plot_acf(y)

from pmdarima.arima.stationarity import ADFTest

# Test whether we should difference at the alpha=0.05
# significance level
adf_test = ADFTest(alpha=0.05)
p_val, should_diff = adf_test.should_diff(y)  # (0.01, False)
p_val

#The verdict, per the ADF test, is that we should not difference. Pmdarima also provides a more handy interface for estimating your d parameter more directly. This is the preferred public method for accessing tests of stationarity:
from pmdarima.arima.utils import ndiffs

# Estimate the number of differences using an ADF test:
n_adf = ndiffs(y, test='adf')  # -> 0

# Or a KPSS test (auto_arima default):
n_kpss = ndiffs(y, test='kpss')  # -> 0

# Or a PP test:
n_pp = ndiffs(y, test='pp')  # -> 0
assert n_adf == n_kpss == n_pp == 0

#The easiest way to make your data stationary in the case of ARIMA models is to allow auto_arima to work its magic, estimate the appropriate d value, and difference the time series accordingly. However, other common transformations for enforcing stationarity include (sometimes in combination with one another):
#
#Square root or N-th root transformations
#De-trending your time series
#Differencing your time series one or more times
#Log transformations
#%%%%
from pmdarima.datasets import load_lynx
from pmdarima.arima.utils import nsdiffs

# load lynx
lynx = load_lynx()

# estimate number of seasonal differences using a Canova-Hansen test
D = nsdiffs(lynx,
            m=10,  # commonly requires knowledge of dataset
            max_D=12,
            test='ch')  # -> 0

# or use the OCSB test (by default)
nsdiffs(lynx,
        m=10,
        max_D=12,
        test='ocsb') 
 # -> 0
 
#%%%The m parameter is the number of observations per seasonal cycle, and is one that must be known apriori. Typically, m will correspond to some recurrent periodicity such as:
#7 - daily, 12 - monthly ,52 - weekly
#Depending on how it’s set, it can dramatically impact the outcome of an ARIMA model. For instance, consider the wineind dataset when fit with m=1 vs. m=12:

import pmdarima as pm

data = pm.datasets.load_wineind()
train, test = data[:150], data[150:]

# Fit two different ARIMAs
m1 = pm.auto_arima(train, error_action='ignore', seasonal=True, m=1)
m12 = pm.auto_arima(train, error_action='ignore', seasonal=True, m=12) 

import matplotlib.pyplot as plt

fig, axes = plt.subplots(1, 2, figsize=(12, 8))
x = np.arange(test.shape[0])

# Plot m=1
axes[0].scatter(x, test, marker='x')
axes[0].plot(x, m1.predict(n_periods=test.shape[0]))
axes[0].set_title('Test samples vs. forecasts (m=1)')

# Plot m=12
axes[1].scatter(x, test, marker='x')
axes[1].plot(x, m12.predict(n_periods=test.shape[0]))
axes[1].set_title('Test samples vs. forecasts (m=12)')

plt.show();
 