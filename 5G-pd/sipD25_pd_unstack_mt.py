# -*- coding: utf-8 -*-
#Created on Thu Jun 20 15:02:14 2019 : dhiraj@sony
#unstack
#https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.unstack.html

import pandas as pd
import numpy as np

from pydataset import data
mtcars = data('mtcars')
mtcars.head()
df = mtcars
#unstack DF
df.unstack()
df.index  #names are row names
#columnwise value : column - rowname - value

#if the level is not Multindex, the output will be a series.
#group and then do stack
#single Column , cannot stack. single column is a Series
group1 = df.groupby('cyl').size()
type(group1)
#Series
group1.unstack()
#error  : it is index not a columnname
group1.reset_index().unstack()

group1a = df.groupby('cyl', as_index=False ). size()
group1a
type(group1a)
group1a.plot.bar()

#Group on two columns
#unstack works well here...
group2 = df.groupby(['cyl','gear']).size()
group2  #two level index - cyl - gear
group2.unstack()
group2.reset_index()
group2.index
group2.index.remove_unused_levels()

group2.reset_index().unstack()  #not so well organised

##Group on 3  columns
#unstack works well here...
group3 = df.groupby(['cyl','gear', 'am']).size()
group3  #multilevel indexing - cyl - gear - am
group3.unstack()
group3.reset_index()
group3.index
group3.index.remove_unused_levels()

group3.reset_index().unstack()  #not so well organised
group3.unstack(level=0) #cyl
group3.unstack(level=1, fill_value=0)  #gear
#fill missing values with 0
group3.unstack(level=2)  #am
#Returns a DF with multi level index
