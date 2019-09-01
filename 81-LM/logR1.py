# -*- coding: utf-8 -*-
"""
Tue May  8 21:04:16 2018: Dhiraj
"""
#Logistic Regression
#http://blog.yhat.com/posts/logistic-regression-python-rodeo.html

import pandas as pd
import statsmodels.api as sm
import pylab as pl
import numpy as np

#data
#df = pd.read_csv("http://www.ats.ucla.edu/stat/data/binary.csv")
df = pd.read_csv('https://stats.idre.ucla.edu/stat/data/binary.csv')
df

df.columns
df.describe()
df.std()
pd.crosstab(df['admit'], df['rank'], rownames = ['admit'])
df.hist();pl.show()

#dummy variables for rank
dummy_ranks = pd.get_dummies(df['rank'], prefix='rank')
dummy_ranks.head()

cols_to_keep = ['admit', 'gre', 'gpa']
data = df[cols_to_keep].join(dummy_ranks.loc[:, 'rank_2':])
data

#manually add intercept
data['intercept'] = 1.0

#train
train_cols = data.columns[1:]
train_cols

logit = sm.Logit(data['admit'], data[train_cols])
result = logit.fit()
result.summary2()

result.conf_int()
np.exp(result.params)

params = result.params
conf = result.conf_int()
conf
conf['OR'] = params
conf.columns = ['2.5%', '97.5%', 'OR']
np.exp(conf)


#Deeper
gres = np.linspace(data['gre'].min(), data['gre'].max(), 10)
gres
gpas = np.linspace(data['gpa'].min(), data['gpa'].max(), 10)
gpas
