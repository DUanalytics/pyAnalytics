# -*- coding: utf-8 -*-
#Boxplots and paired differences

import pandas
import matplotlib.pyplot as plt
#data
from pydataset import data
mtcars = data('mtcars')
mtcars.head()

#Example 1
plt.figure()
mtcars.boxplot(column=['mpg'])
plt.yticks(5)
plt.show()

#Different dataset
import pandas as pd
data = pd.read_csv('data/brain_size.csv', sep=';', na_values='.')
# Box plot of FSIQ and PIQ (different measures od IQ)
plt.figure(figsize=(4, 3))
data.boxplot(column=['FSIQ', 'PIQ'])
# Boxplot of the difference
plt.figure(figsize=(4, 3))
plt.boxplot(data['FSIQ'] - data['PIQ'])
plt.xticks((1, ), ('FSIQ - PIQ', ))
plt.show()

#end 
#boxplot category wise
