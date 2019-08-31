#Topic: Statistics - Covariance
#-----------------------------
#Covariance provides the a measure of strength of correlation between two variable or more set of variables. The covariance matrix element Cij is the covariance of xi and xj. The element Cii is the variance of xi.
#If COV(xi, xj) = 0 then variables are uncorrelated
#If COV(xi, xj) > 0 then variables positively correlated
#If COV(xi, xj) > < 0 then variables negatively correlated

#numpy.cov(m, y=None, rowvar=True, bias=False, ddof=None, fweights=None, aweights=None)

#Parameters:
#m : [array_like] A 1D or 2D variables. variables are columns
#y : [array_like] It has the same form as that of m.
#rowvar : [bool, optional] If rowvar is True (default), then each row represents a variable, with observations in the columns. Otherwise, the relationship is transposed:
#bias : Default normalization is False. If bias is True it normalize the data points.

import numpy as np 
  
x = np.array([[0, 3, 4], [1, 2, 4], [3, 4, 5]]) 
x  
print("Shape of array:\n", np.shape(x)) 
  
print("Covarianace matrix of x:\n", np.cov(x)) 

#%%
x = [1.23, 2.12, 3.34, 4.5] 
y = [2.56, 2.89, 3.76, 3.95] 

# find out covariance with respect  columns 
cov_mat = np.stack((x, y), axis = 0)  
cov_mat  
print(np.cov(cov_mat)) 
#%%https://www.geeksforgeeks.org/python-numpy-cov-function/

#%% Pandas - Covariance
Series.cov(other, min_periods=None)

#https://www.geeksforgeeks.org/python-pandas-series-cov-to-find-covariance/

