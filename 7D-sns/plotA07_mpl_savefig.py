# -*- coding: utf-8 -*-
#Matplot Save Figure
#-----------------------------
import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(0, 10, 100)
fig = plt.figure()
plt.plot(x, np.sin(x))
plt.plot(x, np.cos(x))
fig.savefig('myplotfig.png')
#plt.show() # import when running from script

#Check if the figure has been saved
from IPython.display import Image
Image('myplotfig.png')


#Other filetypes
fig.canvas.get_supported_filetypes()
