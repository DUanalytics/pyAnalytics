#Topic: Numpy Histogram
#-----------------------------
#Compute the histogram of a set of data.
#https://docs.scipy.org/doc/numpy/reference/generated/numpy.histogram.html
#NumPy has a numpy.histogram() function that is a graphical representation of the frequency distribution of data. Rectangles of equal horizontal size corresponding to class interval called bin and variable height corresponding to frequency

import numpy as np
#numpy.histogram() function takes the input array and bins as two parameters. The successive elements in bin array act as the boundary of each bin.

#All but the last (righthand-most) bin is half-open. In other words, if bins is:
[1, 2, 3, 4]
#then the first bin is [1, 2) (including 1, but excluding 2) and the second [2, 3). The last bin, however, is [3, 4], which includes 4.

x = [1,1,1,1,2,2,2]
np.histogram(x, bins=2)
#count 1s=4, 2s-3 : [1 to 1.5]-4, [1.6 to 2.0]-3

x = [1,2,1,1,6,7,8]
np.histogram(x, bins=2)
#1 to 4.5 : 4, 4.6 to 8 : 3

x = np.arange(1,11)
x
np.histogram(x, bins=2)
#1 to 5.5 : 5, 5.6 to 10 : 5
x
np.histogram(x, bins=[0,4,10])
#0 to 3.9 : 4, 4.01 to 10 : 6
#[include] (donot include): default [1,4):[4,10]
np.histogram(x, bins=[0,4.1,10])

np.histogram(x, bins=[0,3,9,10])

#%%
a = np.array([22,87,5,43,56,73,55,54,11,20,51,5,79,31,27]) 
np.histogram(a,bins = [0,20,40,60,80,100]) 
hist,bins = np.histogram(a,bins = [0,20,40,60,80,100]) 
print(hist) #0-20:3, 20-40:4, 40-60:5, 60-80:2, 80-100:1
print(bins)


#%%%
from matplotlib import pyplot as plt 
import numpy as np  
   
a = np.array([22,87,5,43,56,73,55,54,11,20,51,5,79,31,27]) 
np.histogram(a,bins = [0,20,40,60,80,100]) 
plt.hist(a, bins = [0,20,40,60,80,100]) 
plt.title("histogram") 
plt.show();


#Links
#https://www.datacamp.com/community/tutorials/histograms-matplotlib
#https://datatofish.com/plot-histogram-python/
#https://matplotlib.org/3.1.1/gallery/statistics/histogram_multihist.html