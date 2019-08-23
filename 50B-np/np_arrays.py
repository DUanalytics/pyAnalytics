#Topic: Numpy  - array
#-----------------------------
#libraries

#the heart of a Numpy library is the array object or the ndarray object (n-dimensional array). You will use Numpy arrays to perform logical, statistical, and Fourier transforms. As part of working with Numpy, one of the first things you will do is create Numpy arrays. 
#There are three different ways to create Numpy arrays:
#Using Numpy functions
#Conversion from other Python structures like lists
#Using special library functions

import numpy as np

#using numpy
#Creating a One-dimensional Array
import numpy as np
array = np.arange(20)
array
array.shape
array[3]
#Numpy Arrays are mutable, which means that you can change the value of an element in the array after an array has been initialized.
array[3] = 100
print(array)


#Creating a Two-dimensional Array
#If you only use the arange function, it will output a one-dimensional array. To make it a two-dimensional array, chain its output with the reshape function
array2 = np.arange(20).reshape(4,5)
array2
array2.shape
#Since we get two values, this is a two-dimensional array. To access an element in a two-dimensional array, you need to specify an index for both the row and the column.
array2[3][4]

#Creating a Three-dimensional Array and Beyond
array3 = np.arange(27).reshape(3,3,3)
array3
#The number of elements in the array (27) must be the product of its dimensions (3*3*3). To cross-check if it is a three-dimensional array, you can use the shape property.
array3.shape


#arange
#using the arange function, you can create an array with a particular sequence between a defined start and end values
np.arange(10, 35, 3)

#%%
#Using Other Numpy Functions
#Other than arange function, you can also use other helpful functions like zerosand ones to quickly create and populate an array.
#Use the zeros function to create an array filled with zeros. The parameters to the function represent the number of rows and columns (or its dimensions).
np.zeros((2,4))
np.ones((3,4))
#The empty function creates an array. Its initial content is random and depends on the state of the memory.
np.empty((2,3))
# full function creates a n * n array filled with the given value.
np.full((2,2), 3)
# eye function lets you create a n * n matrix with the diagonal 1s and the others 0.
np.eye(3,3)
#function linspace returns evenly spaced numbers over a specified interval. For example, the below function returns four equally spaced numbers between the interval 0 and 10.
np.linspace(0, 10, num=4)

#%%
#Conversion from Python Lists
#Other than using Numpy functions, you can also create an array directly from a Python list. Pass a Python list to the array function to create a Numpy array:
array5 = np.array([4,5,6])
array5
#create a Python list and pass its variable name to create a Numpy array.
list1 = [4,5,6]
list1
array6 = np.array(list1)
array6
#both the variables, array and list, are a of type Python list and Numpy array respectively.
type(list1)
type(array6)

#%%%
#To create a two-dimensional array, pass a sequence of lists to the array function.
array7 = np.array([(1,2,3), (4,5,6)])
array7
array7.shape

#%%Using Special Library Functions
#You can also use special library functions to create arrays. For example, to create an array filled with random values between 0 and 1, use random function. This is particularly useful for problems where you need a random state to get started.
np.random.random((2,2))

#Creating and populating a Numpy array is the first step to using Numpy to perform fast numeric array computations. Armed with different tools for creating arrays, you are now well set to perform basic array operations.

#Links
#https://www.pluralsight.com/guides/different-ways-create-numpy-arrays
