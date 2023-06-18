# -*- coding: utf-8 -*-
#Created by DU 
#Topic : Pandas Options
#%%%
#libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import datetime as dt
import pydataset as data
#%%%Options
## Generally used options
print(pd.options.display.max_rows, pd.options.display.precision)  #Default options
pd.set_option("display.max_rows", 100)
pd.set_option("display.precision", 2)
print(pd.options.display.max_rows, pd.options.display.precision)

#%%%
pd.describe_option("display.max_rows")
#%%%
pd.describe_option()
#%%%

#%%%

#%%%

#%%%
