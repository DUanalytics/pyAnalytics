#Topic ----

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pydataset import data
iris = data('iris')
data=iris
data.head()
data.columns
data.dtypes
data.shape
#%%%https://scipy-lectures.org/packages/statistics/index.html#paired-tests-repeated-measurements-on-the-same-individuals
model = ols('Sepal.Width ~ Petal.Length + Petal.Width', data).fit()
print(model.summary()) 

# Post-hoc hypothesis testing: analysis of variance (ANOVA)
print(model.f_test([0, 1, -1, 0]))  
#%%%
sns.pairplot(data, vars=['Sepal.Length', 'Sepal.Width', 'Petal.Length', 'Petal.Width'],   kind='reg') 
sns.pairplot(data, vars=['Sepal.Length', 'Sepal.Width', 'Petal.Length', 'Petal.Width'],   kind='reg',  hue='Species')
sns.lmplot(y='Sepal.Length', x='Sepal.Width', data=data)


#https://scipy-lectures.org/packages/statistics/index.html#paired-tests-repeated-measurements-on-the-same-individuals
#%%%

