#Topic : Numpy - Matrix
#-----------------------------
#%
import numpy as np
x1=np.array([1.0,2.0,3.0,4.0,5.0])
x1
np.shape(x1)

#https://docs.scipy.org/doc/numpy/reference/generated/numpy.matrix.html
#this method not recommended
x2=np.matrix([1.0,2.0,3.0,4.0,5.0])
x2
print(x2)
np.shape(x2)

x3 = np.matrix([[1,2],[3,4]])
x3
x3.shape
