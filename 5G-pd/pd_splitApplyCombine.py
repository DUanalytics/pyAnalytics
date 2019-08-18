#Pandas Group - SPlit
#-----------------------------
#%
from pydataset import data
mtcars = data('mtcars')
mtcars.head()
import pandas as pd
import numpy as np
#Group by Objects
mtcars.groupby('cyl')

#Column indexing
mtcars.groupby('cyl')['mpg']
#selected a column after group; no computation done
mtcars.groupby('cyl')['mpg'].mean() #mean

#Iteration over groups
for( cylinders, groups) in mtcars.groupby('cyl'):
    print('Shape of ', cylinders, '  is ', groups.shape)

#Describe
mtcars.groupby('cyl')['mpg'].describe()

#Aggregate, Filter, Transform, Apply
mtcars.groupby('cyl').aggregate(['min', np.median, max])
mtcars.groupby('cyl')['mpg'].aggregate(['min', np.median, max])
mtcars.groupby('cyl')['mpg'].aggregate([np.min, sum, np.max])
#some functions are in base library,some in numpy; np are faster
#dictionary mapping : Note curly bracket {} instead of [ ]
mtcars.groupby('cyl')['mpg'].aggregate({'Minimum':np.min, 'MAX':np.max})

#Filtering
def my_filter(x): return x['mpg'].mean() > 23 
mtcars.groupby('cyl')['mpg'].mean()
mtcars.groupby('cyl').filter(my_filter)
#all cars in particular cyl type, where average mean > 23
#ie all cars in 4 cyl

#transformation
mtcars.groupby('cyl')[['mpg','hp','wt']].transform(lambda x: x/ x.mean())
#for all cars, divide each column by its mean from each group
mtcars.groupby('cyl')[['mpg','hp','wt']].transform(lambda x: x - x.mean())
#normalised values

#apply: only 1 function
mtcars.groupby('cyl')[['mpg','hp','wt']].apply(max)
#apply applies a function to all columns of the groups
def my_norm(x) :
    x['mpg'] = x['mpg'] / x['wt'].sum()
    return x
mtcars.groupby('cyl')[['mpg','hp','wt']].apply(my_norm)
#divide mpg by sum of wts of cars its group

#split key : first create a split key equal to length
import random
clist = ['Class-1', 'Class-2', 'Class-3']
splitKeys = random.choices(clist, k=32)  #32 cars
splitKeys
mtcars.groupby(splitKeys).mean()
#create adhoc keys and then do grouping

#any function for group
mtcars.groupby(str.lower).mean()
mtcars.index
