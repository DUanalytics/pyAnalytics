#Topic:
#-----------------------------
#libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from pydataset import data
mtcars = data('mtcars')
mtcars.head()
df = mtcars
df.to_csv('data/mtcars.csv')
df
#
df = pd.read_csv('https://raw.githubusercontent.com/duanalytics/datasets/master/csv/mtcars.csv')
df

type(df)
#list, tuple, dict, sets, numpy, pandas - DS
df.columns
df.shape
df.describe
df.head()
#better mileage
#summary mileage each type
