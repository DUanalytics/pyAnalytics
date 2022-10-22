#python : DUP - Topic :Statistics

#standard libaries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pydataset import data
import seaborn as sns

#mean, mode, median
#sd, var, skewness, quantiles


#%%Quantile

import numpy as np
data1 = 

#np.quantile(a [array], q[seq of quantiles], axis [along axis or default], out[ output], keepdims)

a= np.array([[10,7,4], [3,2,1]])
a
np.quantile(a, .5)
np.quantile(a, axis=0, q=.5)
np.quantile(a,  q=.5, axis=1)
np.quantile(a,  q=.5, axis=1, keepdims=True)


#%% Average
np.average(a)
a
np.average(a, axis=1)
np.average(a, axis=0)
np.average(a, axis=0, weights = np.array([.3, .7]))


#%% Mean
np.mean(a)
np.mean(a, axis=1)
a
np.mean(a, axis=1 , where=[True, True, False])

#%%%
np.std(a)
np.std(a, axis=0)
np.std(a, dtype='int32')


#%% Median
np.median(a)
np.median(a, axis=1)

#%%  quantile
np.quantile(a, q=[.1, .25,.5,.75,1])
np.quantile(a, q=[.25,.5,.75], axis=1)
a
np.percentile(a, q=[10,20,30,40,50,80,100])


#%%sd
np.std(a)
np.var(a)
np.cov(a)

#%%Mode
import statistics
statistics.mode([12,3,3,4])

#%%
sk1 =[1,2,3,4,5]
sk2 = [2,8,0,41,9,9,0]
from scipy.stats import skew, kurtosis
skew(a)
skew(a, axis=1)
skew(sk1)
skew(sk2)

kurtosis(sk1)
kurtosis(sk2)
