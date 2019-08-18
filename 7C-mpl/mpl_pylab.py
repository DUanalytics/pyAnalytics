#Py Lab - Not Recommended
#-----------------------------
#%
from matplotlib.pylab import *

# you can now use both pyplot and numpy
# functions as if they had been imported

# from numpy namespace
x = linspace(0,10,9)

# from numpy.random namespace
y = randn(9)

# from pyplot namespace
scatter(x,y)
show()
