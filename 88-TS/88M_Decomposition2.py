#TS - Decompoistion
#-----------------------------
#%
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

import statsmodels.api as sm

df = pd.DataFrame(np.random.random((500,5)))
df
df.index = pd.DatetimeIndex(freq='w', start=0, periods=500)
df.head(3)

decom = sm.tsa.seasonal_decompose(df[0])
decom.plot()
plt.show()


#https://stackoverflow.com/questions/34342370/analysing-time-series-in-python-pandas-formatting-error-statsmodels