# -*- coding: utf-8 -*-
#Created on Thu Jun 20 16:37:50 2019 : dhiraj@sony

import pandas as pd
import numpy as np
 
#index
header = pd.MultiIndex.from_product([['Semester1','Semester2'],['Maths','Science']])
#data
d=([[12,45,67,56],[78,89,45,67],[45,67,89,90],[67,44,56,55]])

header
d
type(header)
type(d)
header.index
#Stack() Function in dataframe stacks the column to rows at level 1 (default).
 
df = pd.DataFrame(d, index=['Alisa','Bobby','Cathrine','Jack'], columns=header)
df

# stack the dataframe

stacked_df=df.stack()
stacked_df

#Unstack the dataframe:
#unstack() Function in dataframe unstacks the row to columns . Basically it’s a reverse of stacking

# unstack the dataframe
unstacked_df = stacked_df.unstack()
unstacked_df

#Stack the dataframe at level 0:
#Stack() Function with level 0 argument stacks the column semester.
# stack the dataframe of column at level 0
df
stacked_df_lvl=df.stack(level=0)
stacked_df_lvl

#unstack the dataframe :
stacked_df_lvl
unstacked_df1 = stacked_df_lvl.unstack()
unstacked_df1

#http://www.datasciencemadesimple.com/reshape-using-stack-unstack-function-pandas-python/