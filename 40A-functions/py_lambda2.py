# -*- coding: utf-8 -*-
#lambda function
# small anonymous function
#take any number of arguments but can have one expression

#lamda arguments : expression
import pandas as pd
import numpy as np
#
x1 = lambda a : a + 10
x1(5)

x2 = lambda a, b, c : a + b + c
x2(1,2,3)

#used within other functions
#The power of lambda is better shown when you use them as an anonymous function inside another function
def func1(n):   return lambda a : a + n
func2 = func1(2)
func2(11)


#DF
import pandas as pd    
df = pd.DataFrame((np.random.rand(10, 4)*100), columns=list('ABCD'))
df
df.apply(lambda s: s)[:3]  #first 3 rows
df.apply(lambda s: s[0] + s[1])  #add first rows
df.apply(lambda s: s[0] + s[1], axis=1) #add first 2 columns

#Apply a square root function to every single cell in the whole data frame applymap() applies a function to every single element in the entire dataframe.# Return the square root of every cell in the dataframe
df
df.applymap(np.sqrt)


#
dict1 = {'name': ['Jason', 'Molly', 'Tina', 'Jake', 'Amy'],  'year': [2012, 2012, 2013, 2014, 2014],  'reports': [4, 24, 31, 2, 3], 'coverage': [25, 94, 57, 62, 70]}
type(dict1)

df2 = pd.DataFrame(dict1, index = ['Cochice', 'Pima', 'Santa Cruz', 'Maricopa', 'Yuma'])
df2
capitalizer = lambda x: x.upper()  #lambda function
df2['name'].apply(capitalizer)

#map() applies an operation over each element of a series
df2['name'].map(capitalizer)

# Drop the string variable so that applymap() can run
df2 = df2.drop('name', axis=1)
df2
df2.applymap(np.sqrt)
