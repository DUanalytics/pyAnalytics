f#Matplot Lib -Features
#-----------------------------
#%

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0,10,1000)
x
#just the plot
plt.plot(x, np.sin(x))

#Axis - manual
plt.plot(x, np.sin(x))
plt.xlim(-1, 15)
plt.ylim(-1.5, 1.5)

#Axis - Reverse
plt.plot(x, np.sin(x))
plt.xlim(-1, 11)
plt.ylim(1.5, -1.5)

#%%%
#Axis - Together -spelling AXIS
plt.plot(x, np.sin(x))
plt.axis([-1, 11,-2, 2])
#[xmin xmax ymin ymax]
#%%%
#Axis - tight
plt.plot(x, np.sin(x))
plt.axis('tight')

#Axis - equal aspect ratio
plt.plot(x, np.sin(x))
plt.axis('equal')


#%%%Label Plots
#titles & axis
plt.plot(x, np.sin(x))
plt.title('Sine Curve')
plt.xlabel('X Label')
plt.ylabel('Y Label')

#Multiple Curves, single line label
plt.plot(x, np.sin(x), label='X Curve')
plt.plot(x, np.cos(x), label='Y Curve')
plt.title('Sine and Cos Curve')
plt.ylabel("dhiraj Upadhyaya")
plt.xlabel("Anil Jadon")
plt.axis('equal')
plt.legend()



#axis plot
import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(0,10,1000)
ax= plt.axes()
ax.plot(x, np.sin(x))
ax.set( xlim=(0,10) , ylim = (-2, 2), xlabel = 'X Label', ylabel = 'Y Label', title = ' Plot with Sin and Cos Curve');
