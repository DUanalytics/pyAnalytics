#python : Topic : Numpy

#standard libaries
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#scalar
x0 = np.random.randint(10); x0
x0.shape
#1-Dim
x1 = np.random.randint(10, size=6); x1
x1.shape

#2-Dim
x2 = np.random.randint( 10, size=(3,4)) ;x2
x2.shape

#3-Dim
x3 = np.random.randint(10, size=(3,4,5)) ; x3
x3.shape

#Print those values
x0; x1;x2;x3

#%%%
#0-Dim
x0[0] ; x0[1]  #error
x0  #this will work

#1-Dim
x1 = np.random.randint(10, size=6); x1
x1[0]  #first value
x1[1:5]  #2nd to 5th

#2-Dim
x2 = np.random.randint( 10, size=(3,4)) ;x2
x2[0]
x2[0,1]  #1st row, 2nd col
x2[0:,0:]  #all
x2  #full array
x2[0:1,0:]  #1st row
x2[:1, :]
x2[0:,0:1]  #1st col
x2[:, :1]

x2[:2, :3] #first 2 rows, first 3 columns
x2[1,-2]
x2

#alternate items
x2[::, ::] #all
x2[::2, ::] #alternative rows
x2[::, ::2] #alternative cols
x2[:2, ::2] #alternative cols with first 3 rows
x2

#3-Dim
x3 = np.random.randint(10, size=(3,4,5)) ; x3
x3  #all
x3[::] #all
x3[1::] #2nd matrix onwards
x3[::2]  #alternative matrix
x3[1:2:] #2nd matrix
x3[0,0,0]  #first cell
x3[2,3,4]  #last cell of array
x3[0]  #first matrix
x3[0,1]  #first matrix, 2nd row
x3[1,2] #2nd matrix, 3rd row
x3

#%%%
#functions to create arrays
zeros = np.zeros(shape=(2,3))
zeros 

ones = np.ones(shape=(3,2))
ones  

constant = np.full(shape=(3,3), fill_value=99, dtype='int')
constant
constant.dtype

identityMatrix = np.eye(2)
identityMatrix

randomMatrix = np.random.random(size=(2,3))
randomMatrix
randomMatrix.dtype


#%%% Mathematics
import numpy as np
x = np.array([[1,2], [3,4]], dtype=np.int32)
y = np.array([[5,6], [7,8]], dtype=np.float32)
x
y  #float with decimal point
x+y
np.add(x, y)
x-y
np.subtract(x, y)
x * y
np.multiply(x, 2)
np.multiply(x,y )
x/ y
np.divide(x, 2)
np.divide(x, y)

np.sqrt(x)

x.dot(2)
np.dot(x,2)

#%%%
x
np.sum(x)
np.sum(x, axis=0)  #col
np.sum(x, axis=1)  #row

x.T  #transpose

#empty matrix with shape of x 
np.empty_like(x)

np.tile(x, (2,1))
np.tile(x, (2,4))


#reshape
#The new shape should be compatible with the original shape. If an integer, then the result will be a 1-D array of that length. One shape dimension can be -1. In this case, the value is inferred from the length of the array and remaining dimensions.

x
#-1 - whatever is needed, adjust itself
np.reshape(x, newshape=(1,4))
np.reshape(x, newshape=(-1))  #horizontal
np.reshape(x, newshape=(4,1))  #vertical

#automatic reshaping
a = np.arange(30)
a
a.shape = 2, -1, 3 #row, col, matrix
#-1 - whatever is needed, adjust itself
a.shape
a

#create values in seq and give shape to array
np.arange(6).reshape((3, 2))

#add, delete, concatenate
import numpy as np
arr = np.array([1,2,3])
arr
arr2 = np.append(arr, [7,8])
arr2
arr3 = np.delete(arr2, [2,4])  #delete 2+1 & 4+1 position
arr3
arr4 = np.concatenate((arr3, np.array([8,9])), axis=0)
arr4  #note brackets

#linespace
a = np.linspace(0,10,4)
a #4 equi distance points betw 0 & 10
np.linspace(0,10,2)
np.linspace(0,10,3)
np.linspace(0,10,5)

#arange
a = np.arange(5)
a

c = np.arange(24).reshape(2,3,4)
c

#maths
a = np.random.random((2,3))
a  #random numbers between 0 & 1, shape 2 x 3
a.sum()
a.max()
a.min()
a.sum(axis=1) #2 rows, 2 values
a.min(axis=0)  #3 cols, 3 value
a
a.cumsum()
a.cumsum(axis=0)  #cum sum along each row
a.cumsum(axis=1)  #cum sum along each col

#
x= np.arange(0, 10, 2)
y = np.arange(5)
x, y
h = np.hstack([x,y])
h
v = np.vstack([x,y])
v

#Normal distributed values
mu, sigma = 2, .5
nd = np.random.normal(mu, sigma, 10000 )
nd
len(nd)
import matplotlib.pyplot as plt
plt.hist(nd, bins=20, density=1)
plt.show();

