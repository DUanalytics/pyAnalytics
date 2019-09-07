#Topic ---- TS - ARIMA - simple case
#%%%
import pandas as pd
import numpy as np
from statsmodels.tsa.arima_model import ARIMA

dates = pd.date_range('2012-07-09','2012-07-30')
series = [43.,32.,63., 98.,65.,78.,23., 35.,78.,56.,45., 45.,56.,6.,63.,45., 64.,34.,76.,34., 14., 54. ]
res = pd.Series(series, index=dates)
r = ARIMA(res,(1,2,0))
r = r.fit()
pred = r.predict(start='2012-07-31', end='2012-08-31')
print(pred)

#https://stackoverflow.com/questions/36717603/predict-statsmodel-argument-error
#%%%

