#Topic Time Series Basic

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#%%%
dates = pd.date_range('2020-09-01',periods=5, freq='D')
dates
sales = pd.Series([50,60,55,70,80], index=dates)
sales

#%%%
ma3 = sales.rolling(window=3).mean()
ma3
ma3c = sales.rolling(window=3, center=True).mean()
ma3c
#%%%
sales.shift(1)
sales - sales.shift(1)

from pmdarima.utils import c, diff
diff(sales, lag=1, differences=1)
sales - sales.shift(1)
#%%%%%
diff(sales, lag=2, differences=1)
sales - sales.shift(2)
#lag is the gap : 1 with 3, 2 with 4 and so on
#%%%%%
sales2 = sales.copy()
diff(sales, lag=1, differences=1)
sales2 - sales2.shift(1)

diff(sales, lag=1, differences=2)
sales2 = sales2 - sales2.shift(1)
sales2 - sales2.shift(1)

diff(sales, lag=1, differences=2)


#end here
