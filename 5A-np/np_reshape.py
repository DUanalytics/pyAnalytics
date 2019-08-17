#Numpy - Reshape
#-----------------------------
#%

# -*- coding: utf-8 -*-
"Created on Fri Jun  7 07:57:28 2019 @author: dhiraj@dell
"
#-----------------------------
#%

#%

# Prerequisite: Import numpy
import numpy as np
 
# Get a 2d matrix and print shape
arr = np.array([[11, 12, 13, 14, 15],  [21, 22, 23, 24, 25]])
arr 
arr.shape
#>> (2, 5)

Reshaping numpy array (vector to matrix)
# Create a numpy array
arr = np.arange(9)
arr
# Reshaping to 3x3 Matrix 
arr = arr.reshape(3, 3) 
arr 
# Check new shape
arr.shape
#>> (3, 3)


Reshaping numpy array (matrix to tensor)
# Matrix
arr = np.array([[11, 12, 13, 14],                [21, 22, 23 ,24],                [31, 32, 33 ,34],                [41, 42, 43 ,44]])

# Reshaped to Tensor
arr = arr.reshape(4,4,1)
arr


#%%
# Reshaping Illustration
arr = np.array([[1, 1, 1, 1],  [2, 2, 2, 2],  [3, 3, 3, 3]])
 
# Check original shape    
print(arr.shape)
#>> (3, 4)
 
# Reshape to (4,3)
arr = arr.reshape(4,3)
arr

# Reshape to (6,2)
arr = arr.reshape(6,2)
arr
# Reshape to (2, 6)
arr = arr.reshape(2, 6)
arr
 
# Reshape to (1, 12)
arr = arr.reshape(1, 12)
arr
 
# Reshape to (12, 1)
arr = arr.reshape(12, 1)
arr
