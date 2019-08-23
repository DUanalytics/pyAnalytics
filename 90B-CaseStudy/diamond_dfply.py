# -*- coding: utf-8 -*-
##dfply with diamond dataset

from dfply import *
import pandas as pd
import numpy as np

#dfply has dataset diamonds
dfply.data.diamonds
dfply.data.diamonds.shape
#53K rows, 10 columns

#explore dataset
diamonds >> head(5)
diamonds >> tail(6)

#groupby
#first 2 from each group of cut column
diamonds >> group_by(X.cut) >> head(2)

#ungroup
diamonds >> group_by(X.cut) >> head(2) >> ungroup()  >> head(5)
#see use of head(2) and head(5)

#selecting and dropping
diamonds >> select(X.carat, X.cut) >> head(2)
diamonds.columns
diamonds >> select(0, X.carat, 'depth') >> head(2)
diamonds >> select(0,1,2,3,4,8)
diamonds >> select('carat','depth')
diamonds >> select(0,3, X.carat, 'depth') >> head(5)
#0-carat, 3-clarity
#display by columnnames in quote, X.columnname, columnindex

diamonds >> select(0, [X.color, [[X.depth]]])  >> head(5)
#flatten in selected functions - later ??

#dropping
diamonds >> drop(0, 1, [4,5]) >> head(2)
diamonds.columns

#%%
#contains
diamonds.columns
diamonds.dtypes
#column names - not working
diamonds >> select_containing('c') >> head(2)
diamonds >> starts_endswith("c")
diamonds >> drop_endswith("c")
diamonds >> drop_containing('c') >> head(2)

#Selecting ranges - NOT WORKING ????
diamonds >> select_between(X.dept, 'price') >> head(2)
diamonds >> select_to(X.x) >> head(2)
diamonds >> select_through(X.x) >> head(2)

#Transformation/ variable creation
#shift price to lower row
diamonds >> mutate(price_shift = X.price.shift(1)) >> head(5)

#multiple mutate
diamonds >> group_by(X.cut)  >> mutate(price_shift = X.price.shift(1)) >> head(2)

#transmuate -creates and selects : check output
diamonds >> select('x','y','z') >> head(5)
diamonds >> transmute (x_times_y = X.x * X.y , y_times_z = X.y * X.z) >> head(5)
3.98 * 3.98, 3.98 * 2.43

diamonds >> group_by(X.cut) >> transmute(price_shift = X.price.shift(1)) >> head(5)


#Summarisation
diamonds >> group_by(X.cut) >> summarize(price_mean = np.mean(X.price), price_first = X.price.values[0])

import numpy as np
diamonds >> group_by(X.color) >> summarize_each([np.mean, np.std, np.var], X.price, X.depth, X.x)

#printing all columns
pd.set_option('display.max_columns',None)
#0- tells pandas to display the table only if all the columns can be squezzed into the width of your console
pd.set_option('display.max_rows',10)
diamonds
diamonds.columns.tolist()
diamonds.columns.values
pd.set_option('display.width', 200)
#default is 80
diamonds
diamonds[5:]
diamonds[-5:]
diamonds[:]
diamonds.head()

#%%
#subsetting
diamonds >> sample(n=4, replace=False)
diamonds >> sample(frac=.0001, replace=False)

#unique values
diamonds.cut.unique
diamonds >> select('cut') >> distinct()
diamonds.columns
(diamonds >> select('cut') >> distinct()).shape
(diamonds >> select('depth') >> distinct()).shape

#row slicing
diamonds >> group_by(X.color) >> row_slice([1,7])

#mask with boolean logic
diamonds >> mask(X.cut == 'Ideal') >> head()
diamonds >> mask(X.cut == 'Ideal', X.color == 'E', X.table < 55, X.price > 500)
diamonds >> mask(X.cut == 'Ideal', X.color == 'E', X.table < 55, X.price > 500)
diamonds.cut.groupby
diamonds >> mask((X.cut == 'Ideal') & (X.color == 'E')) #and
diamonds >> mask((X.cut == 'Ideal') | (X.color == 'E')) #or
diamonds >> mask((X.cut == 'Ideal') | (X.cut == 'Fair')) #or


#reshaping
#rename columns
diamonds >> rename(CUT = X.cut, CLARITY = X.clarity) >> head(5)
diamonds >> rename(CuTTing = 'cut') >> select(0,1,2,3,4,5) >> head(5)

#arrange/ sorting
diamonds >> arrange(X.table, X.price) >> head(10)
diamonds >> arrange(X.table, X.price, ascending=False) >> head(10)
diamonds >> arrange(X.table, X.price, ascending=False) >> head(10)
diamonds >> arrange(X.table, -X.price) >> head(10) #ascending & descending


#gather
gather1 = (diamonds >> gather('variable', 'value', ['price', 'depth','x','y','z'])) #only selected columns
diamonds.columns.tolist()
diamonds.head()
gather1.head()
#gather1 >> group_by('variable') >> summarise()
#gather(key, value, *columns) : melts specified coln
diamonds >> gather('variable','value') >> head(5)
diamonds >> gather('variable','value')

#elongated 
#without any columns specified, entire DF will be transformed into 2 key:value pair columns

elongated = diamonds >> gather('variable', 'value', add_id=True)
elongated >> head()
elongated

#%%
#spread
widened = elongated >> spread(X.variable, X.value)
widened >> head(5)
widened.dtypes


#%%
#Joins
a = pd.DataFrame({ 'x1':['A','B','D','F'], 'x2':[1,2,3,5]})
a
b = pd.DataFrame({ 'x1':['A','B','D','E'], 'x3':[True, False, True, True]})
b

a >> inner_join(b, by='x1')  #inner
a >> outer_join(b, by='x1') #outer / full join
a >> full_join(b, by='x1') #outer / full join
a >> left_join(b, by='x1') # left - all of a
a >> right_join(b, by='x1') # left - all of b

#sets
c = pd.DataFrame({ 'x1':['A','L','M','F'], 'x2':[1,12,13,15]})
a >> union(c)
a >> intersect(c)
a >> set_diff(c)

#bind
a >> bind_rows(b, join='inner')
a >> bind_rows(b, join='outer')
a >> bind_rows(c, join='outer')
a >> bind_rows(c, join='inner')
a >> bind_cols(b)

#
diamonds >> row_slice([1,2])
diamonds.iloc[0:5,2:4] 
diamonds.iloc[[0,5],[2,4]]  #0 to 4th row, 3 & 4th column
diamonds.iloc[[0]]  #first row
diamonds.iloc[[0,1]]  #first 2 rows
diamonds.iloc[0:5,]  #first 5 rows, all columns
diamonds.iloc[[True, True, False, True] , [True,True, False,True]]
diamonds >> row_slice(range([1,10]))


#
diamonds >> select_endswith('t') >> head(1)



#
diamonds >> bind_rows(diamonds)
diamonds >> bind_cols(diamonds)
diamonds.columns
diamonds >> between(X.price,1,5)
diamonds >> select(X.price) >> cumsum(X.price)
diamonds >> select(X.price) >> mutate(price_btwn = between(X.price, 330, 340)) >> head()

diamonds >> select(X.price) >> mutate(price_drank = dense_rank(X.price)) >> head(6)

diamonds >> select(X.price) >> mutate(price_mrank = min_rank(X.price)) >> head(6)
diamonds >> select(X.price) >> mutate(price_cummin = cummin(X.price)) >> head(6)
diamonds >> select(X.price) >> mutate(price_cumprod = cumprod(X.price)) >> head(6)
diamonds >> select(X.price) >> mutate(price_cumsum = cumsum(X.price)) >> head(6)
diamonds >> select(X.price) >> mutate(price_cummean = cummean(X.price)) >> head(6)

#mean of series
diamonds >> group_by(X.cut) >> summarize(price_mean = mean(X.price), price_median = median(X.price))
diamonds >> group_by(X.cut) >> summarize(price_first = first(X.price))
diamonds >> group_by(X.cut) >> summarize(price_last = last(X.price))
diamonds >> group_by(X.cut) >> summarize(price_penultimate = nth(X.price, -2))
diamonds >> group_by(X.cut) >> summarize(price_penultimate = nth(X.price, 2, order_by=None))
diamonds >> group_by(X.cut) >> summarize(price_penultimate = nth(X.price, 2, order_by=None))
diamonds >> group_by(X.cut) >> summarize(price_ndistinct = n_distinct(X.price))
diamonds >> group_by(X.cut) >> summarize(price_iqr = IQR(X.price))
diamonds >> group_by(X.cut) >> summarize(price_colmin = colmin(X.price), price_colmax = colmax(X.price))

diamonds >> group_by(X.cut) >> summarize(price_var = var(X.price), price_sd = sd(X.price))



#unit and seperate

d = pd.DataFrame({'name':['Dhiraj Sharma', 'Kanika Joshi','Upen Shah']})
d
d >> separate(X.name, ['firstname','lastname'])
#other options - convert, extra, fill
d >> separate(X.name, ['firstname','lastname'], remove=False)
e = d >> separate(X.name, ['firstname','lastname'])
e
e >> unite('fullname', X.firstname, X.lastname)
e >> unite('fullname', X.firstname, X.lastname, remove=False, sep='*')

#distinct
diamonds >> distinct(X.color)
diamonds >> distinct(X.color, X.cut)

#select from : not working
diamonds >> mutate(x_plus=X.x +X.y, y_div_z = (X.y/ X.z)) >> select_from('x')
mutate?

