#Missing Values
#-----------------------------
#%
import pandas as pd
import numpy as np
print(np.NaN == None)
# In a condition we cannot get hold of a NaN value 
print(np.nan == np.nan)
# But we can hold None just like strings ["missing”, “not available”, “NA”]
print(None == None)
#The problem is that if we do not remove the NaNs then, we are in for double jeopardy. Firstly we already are suffering from loss of true data and secondly if not handled with care NaNs start ‘devouring’ our true data and might get propagated throughout the data-set as we proceed. Let's instantiate two series and see.
# Creating series
allmissing = pd.Series([None, None, np.nan, np.nan])
allmissing

twomissing   = pd.Series([1, np.nan, 2, np.nan])
twomissing

#operation
allmissing + twomissing  #no addition
allmissing / twomissing  #no operation

# Conflicting outputs : nooutput
sum(allmissing)
sum(twomissing)
allmissing.sum()  #output
twomissing.sum()

#DF: # Notice 3 different NaNs here
df = pd.DataFrame(data=[[1, 2, np.nan,3], [np.NaN,  None,  np.NAN,  np.nan], [4,5,'NA',  '#$%'], [6, 7, np.nan, 8],["missing", 9,   np.nan,   10],[11, 12,   np.nan,  "not available"] ], index= 'i0,i1,i2,i3,i4,i5'.split(','), columns='c0,c1, c2,c3'.split(','))
df
df['c3'].isnull()
#only 1 in column c3

#end----------------


#https://medium.com/free-code-camp/the-penalty-of-missing-values-in-data-science-91b756f95a32