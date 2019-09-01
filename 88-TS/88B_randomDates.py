#Topic: Random Dates
#-----------------------------
#libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#df = pd.read_csv('data/mtcars.csv')
from pydataset import data
mtcars = data('mtcars')
mtcars.head()
df = mtcars

#https://stackoverflow.com/questions/50559078/generating-random-dates-within-a-given-range-in-pandas

def random_dates(start, end, n, seed=1, replace=False):
    dates = pd.date_range(start, end).to_series()
    return dates.sample(n, replace=replace, random_state=seed)

random_dates("20170101","20171223", 10, seed=1)



list1 = []
for x in range(0,365):    list1.append(x)
list1
date = pd.DataFrame(pd.to_datetime(list1, unit='D',origin=pd.Timestamp('2018-01-01')))
date

import pandas as pd
import numpy as np

np.random.seed(0)
# create an array of 5 dates starting at '2015-02-24', one per minute
rng = pd.date_range('2015-02-24', periods=5, freq='M')
rng
df1 = pd.DataFrame({ 'Date': rng, 'Val': np.random.randn(len(rng)) }) 
df1



#
Alias     Description
B         business day frequency  
C         custom business day frequency (experimental)  
D         calendar day frequency  
W         weekly frequency  
M         month end frequency  
BM        business month end frequency  
CBM       custom business month end frequency  
MS        month start frequency  
BMS       business month start frequency  
CBMS      custom business month start frequency  
Q         quarter end frequency  
BQ        business quarter endfrequency  
QS        quarter start frequency  
BQS       business quarter start frequency  
A         year end frequency  
BA        business year end frequency  
AS        year start frequency  
BAS       business year start frequency  
BH        business hour frequency  
H         hourly frequency  
T, min    minutely frequency  
S         secondly frequency  
L, ms     milliseconds  
U, us     microseconds  
N         nanoseconds 