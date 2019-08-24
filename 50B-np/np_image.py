#Numpy on image
#-----------------------------
#%

from skimage import io
#load an image from your file : change path to suit the location
photo = io.imread('plot1.png')
type(photo)

import matplotlib.pyplot as plt
import numpy as np

plt.imshow(photo)
photo.shape

plt.imshow(photo[::-1])


plt.imshow(photo[:,::-1])

plt.imshow(photo[::2,::2])

plt.imshow(photo[:,::-1])

plt.imshow(photo[200:300, 200:300])
plt.imshow(photo)

plt.imshow(np.rot90(photo))
plt.imshow(np.flipud(photo))
plt.imshow(np.fliplr(photo)) #??
