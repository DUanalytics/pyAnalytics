#Panda Series
#-----------------------------
#%

import pandas as pd

pd.Series?

import numpy as np
#create np array

#pd.Series is a single column data with index values
np1 = np.array([1,3,5,10,12])
np1
np1.index  #no index - error
np1[0:3] #index are position values index square bracket
#panda series
np1[[1,4]]
ps1 = pd.Series([1,2,4,8,11])
ps1
#see the shape of output; columnar with default index
ps1[0:3]  #this also works
np.arange(0,5,1)
ps1.index  #this also
#here index is in series, but user defined index values can be given
ps2 = pd.Series([1,4,2,5,6], index=['bba', 'mba','phd', 'a','dhiraj' ], dtype='int32')
ps2
ps2[0:3]  #this still works even though index names have been given
ps2['bba']
ps2[['bba','dhiraj','a']]  #this way also it works
ps2['bba':'a']  #this also works : it founds its internal positions
ps2['a':'bba']  #this does not ; should be in increasing order
ps2[0:5:2]  #alternate index position
ps2.index.names
ps2.index.get_level_values  #it is only one level
#index is important to understand Panda Series and Dataframe

ps2.sample(2)  #any 2 rows
#we can give multiple / multi level indexing also

