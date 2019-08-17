#
#-----------------------------
#%
import numpy as np
import matplotlib.pyplot as plt

x = np.arange(1,10)
x
y = np.arange(11,12)
y
x_mesh, y_mesh = np.meshgrid(x, y)
x_mesh
y_mesh
plt.scatter(x_mesh, y_mesh)


#Complicated coordinates
x = np.arange(1,101)
y = np.arange(100,201)
x_mesh, y_mesh = np.meshgrid(x, y)
x_mesh
y_mesh
plt.scatter(x_mesh, y_mesh)


