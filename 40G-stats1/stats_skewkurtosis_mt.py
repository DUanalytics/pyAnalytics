# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np

#read data
#df = pd.read_csv('data/mtcars.csv')
from pydataset import data
mtcars = data('mtcars')
mtcars.head()
df=mtcars
df.describe()
dt.dtypes()

#data distributions for 
df.columns

#%%% =========================================
# #Skewness: It represents the shape of the distribution.
#Skewness can be quantified to define the extent to which a distribution differs from a normal distribution.
#For calculating skewness by using df.skew() python inbuilt function.
#

df.mpg
df.mpg.skew()
df.mpg.plot(kind='hist')


#
# #Kurtosis: Kurtosis is the measure of thickness or heaviness of the given distribution.
#Its actually represents the height of the distribution.
#The distribution with kurtosis equal to3 is known as mesokurtic. A random variable which follows normal distribution has kurtosis 3.
#If the kurtosis is less than three, the distribution is called as platykurtic. Here,the distribution has shorter and thinner tails than normal distribution.
#If the kurtosis is greater than three, the distribution is called as leptykurtic. Here, the distribution has longer and fatter tails than normal distribution.
#For calculating kurtosis by using df.kurtosis() python inbuilt function.
# ========

df.kurtosis()
df.mpg.kurtosis()

