#python : DUP - Topic : Doubts from students

#standard libaries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pydataset import data
import seaborn as sns

mtcars = data('mtcars')
mtcars.head()
mtcars1 = mtcars
mtcarsDF = mtcars.copy()
id(mtcars)
id(mtcarsDF)
id(mtcars1)
help(id)

#group by - aggregate various statistics and sort by column aggregate

mtcarsDF[['mpg','gear','wt']]
mtcarsDF[['mpg','gear','wt']].groupby('gear')
mtcarsDF[['mpg','gear','wt']].groupby('gear').mean()
mtcarsDF[['mpg','gear','wt']].groupby('gear').min()
mtcarsDF[['mpg','gear','wt']].groupby('gear').agg([np.mean])
mtcarsDF[['mpg','gear','wt']].groupby('gear').agg([np.mean, min])
mtcarsDF[['mpg','gear','wt']].groupby('gear').agg([np.mean, min]).reset_index()
mtcarsDF[['mpg','gear','wt']].groupby('gear', as_index=False).agg([np.mean, min]).reset_index()

mtcarsDF[['mpg','gear','cyl', 'wt']].groupby(['gear','cyl']).agg({'mpg':[np.mean, min]})

gpMT = mtcarsDF[['mpg','gear','cyl','wt']].groupby(['gear','cyl']).agg({'mpg':[np.mean, min, max], 'wt':[np.std,max]}).round(2).reset_index()
gpMT
gpMT.columns = gpMT.columns.droplevel()
gpMT
gpMT.set_axis(['gear','cyl', 'mpg_mean', 'mpg_min', 'mpg_max', 'wt_std', 'wt_max'] , axis=1, inplace=True)
#gpMT.columns = ['gear', 'cyl', 'mpg_mean','mpg_min','mpg_max','wt_std','wt_max']
gpMT
gpMT.head()
gpMT.sort_values(by=['cyl','wt_max'])


#%%
#dfply
#pip install dfply  #install this library first from anaconda
from dfply import *
mtcarsDF2 = mtcars.copy()
id(mtcarsDF)
id(mtcarsDF2)
pd.set_option('display.max_columns', None)
mtcarsDF2.head()
mtcarsDF2 >> arrange(X.cyl, X.mpg)
mtcarsDF2 >> group_by(X.gear, X.am, X.cyl) >> summarize(meanWT= X.wt.mean(), maxHP = X.hp.max()) >> ungroup()  >> arrange(X.cyl) 


#pip install dplython  #install this library first from anaconda
from dplython import *
mtcarsDF3 = DplyFrame(mtcarsDF2)
mtcarsDF3 >> sample_n(10)
mtcarsDF3 >> select(X.mpg, X.wt)
mtcarsDF3 >> group_by(X.cyl, X.gear)  >> summarize(meanWt = X.mpg.mean(), meanHP = X.hp.max()) >> arrange(X.meanHP)
mtcarsDF3 >> mutate(newMPG = X.mpg * 2)  >> select(X.mpg, X.newMPG, X.wt)  >> head(5)
type(mtcarsDF3)


#https://towardsdatascience.com/dplyr-style-data-manipulation-with-pipes-in-python-380dcb137000
#https://github.com/kieferk/dfply