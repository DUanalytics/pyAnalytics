#Topic: Matplotlib - Daily
#Matplotlib is a plotting library. In this section give a brief introduction to the matplotlib.pyplot module, which provides a plotting system similar to that of MATLAB.


#PlottingThe most important function in matplotlib is plot, which allows you to plot 2D data. Here is a simple example:

import numpy as np
import matplotlib.pyplot as plt

# Compute the x and y coordinates for points on a sine curve
x = np.arange(0, 3 * np.pi, 0.1)
y = np.sin(x)

# Plot the points using matplotlib
plt.plot(x, y)
plt.show()  # You must call plt.show() to make graphics appear.

#Running this code produces the  plot:


#With just a little bit of extra work we can easily plot multiple lines at once, and add a title, legend, and axis labels:

import numpy as np
import matplotlib.pyplot as plt

# Compute the x and y coordinates for points on sine and cosine curves
x = np.arange(0, 3 * np.pi, 0.1)
y_sin = np.sin(x)
y_cos = np.cos(x)

# Plot the points using matplotlib : run these  lines together upto plt.show
plt.plot(x, y_sin)
plt.plot(x, y_cos)
plt.xlabel('x axis label')
plt.ylabel('y axis label')
plt.title('Sine and Cosine')
plt.legend(['Sine', 'Cosine'])
plt.show();

#You can read much more about the plot function in the documentation.
#http://matplotlib.org/api/pyplot_api.html#matplotlib.pyplot.plot

#%%Subplots You can plot different things in the same figure using the subplot function. Here is an example:

import numpy as np
import matplotlib.pyplot as plt

# Compute the x and y coordinates for points on sine and cosine curves
x = np.arange(0, 3 * np.pi, 0.1)
y_sin = np.sin(x)
y_cos = np.cos(x)

# Set up a subplot grid that has height 2 and width 1,
# and set the first such subplot as active. run together upto plt.show()
plt.subplot(2, 1, 1)

# Make the first plot
plt.plot(x, y_sin)
plt.title('Sine')

# Set the second subplot as active, and make the second plot.
plt.subplot(2, 1, 2)
plt.plot(x, y_cos)
plt.title('Cosine')

# Show the figure.
plt.show();

#You can read much more about the subplot function in the documentation.
#http://matplotlib.org/api/pyplot_api.html#matplotlib.pyplot.subplot

#Images :You can use the imshow function to show images. Here is an example:

import numpy as np
from scipy.misc import imread, imresize
from skimage import io

import matplotlib.pyplot as plt
#http://www.petsworld.in/blog/wp-content/uploads/2014/09/cat.jpg
#download this image into a folder in your project
#img = imread('images/cat.jpg')
img = io.imread('images/cat.jpg')
img_tinted = img * [1, 0.95, 0.9]

# Show the original image: run upto plot.show
plt.subplot(1, 2, 1)
plt.imshow(img)

# Show the tinted image
plt.subplot(1, 2, 2)

# A slight gotcha with imshow is that it might give strange results
# if presented with data that is not uint8. To work around this, we
# explicitly cast the image to uint8 before displaying it.
plt.imshow(np.uint8(img_tinted))
plt.show();