# -*- coding: utf-8 -*-
"""
Wed May  9 21:44:51 2018: Dhiraj
"""
#auto.arima in Python
#https://medium.com/@josemarcialportilla/using-python-and-auto-arima-to-forecast-seasonal-time-series-90877adff03c

#%%
#pip install pyramid-arima
#https://github.com/tgsmith61591/pyramid
#from pyramid.arima import auto_arima
#https://github.com/tgsmith61591/pyramid/blob/master/examples/quick_start_example.ipynb
import numpy as np
import pyramid

print('numpy version: %r' % np.__version__)
print('pyramid version: %r' % pyramid.__version__)
forecast::wineind
from pyramid.arima import ARIMA

fit = ARIMA(order=(1, 1, 1), seasonal_order=(0, 1, 1, 12)).fit(y=wineind)