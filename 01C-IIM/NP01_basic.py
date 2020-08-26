#python : Topic : Numpy

#standard libaries
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#scalar
x0 = np.random.randint(10); x0
#1-Dim
x1 = np.random.randint(10, size=6); x1
#2-Dim
x2 = np.random.randint( 10, size=(3,4)) ;x2
#3-Dim
x3 = np.random.randint(10, size=(3,4,5)) ; x3

#Print those values
x0; x1;x2;x3

#0-Dim
x0[0] ; x0[1]  #error
x0  #this will work
#1-Dim
x1[0]
x1[1:5]
#2-Dim
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


#