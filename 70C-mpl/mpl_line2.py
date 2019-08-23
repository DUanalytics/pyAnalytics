# -*- coding: utf-8 -*-
#Matplot Lib Pg 217
import matplotlib as mpl
import matplotlib.pyplot as plt

plt.style.use('classic')

#Script myplot.py
import matlotlib.pyplot as plt
import numpy as np
x = np.linspace(0,10,100)
plt.plot(x, np.sin(x))
plt.plot(x, np.cos(x))
plt.show()  # 1 per sission

#IPython shell - type in ipython
%matplotlib
import matplotlib.pyplot as plt
#plt.draw(), plt.show() not requd
plt.draw()
plt.plot(x, np.sin(x))
plt.plot(x, np.cos(x))

# IPython Notebook : Jupiter Notebook
#http://localhost:8888/notebooks/myplot3.ipynb
%matplotlib inline
import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(0,10,100)
fig = plt.figure()
plt.plot(x, np.sin(x),'-')
plt.plot(x, np.cos(x),'--');
plt.show()

#Saving Figures
plt.savefig('myfigure.png')

#confirm
from IPython.display import Image
Image('myfigure.png')

fig = plt.figure()
fig.canvas.get_supported_filetypes()



#Two Interfaces
plt.figure()
plt.subplot(2,1,1)
plt.plot(x,np.sin(x))
plt.subplot(2,1,2)
plt.plot(x,np.cos(x))



#Object Oriented Interface
fig, ax = plt.subplots(2)
ax[0].plot(x, np.sin(x))
ax[1].plot(x, np.cos(x))


#Simple Line Plots
import matplotlib.pyplot as plt
plt.style.use('seaborn-whitegrid')
import numpy as np
fig = plt.figure()
ax = plt.axes()
x = np.linspace(1,10,1000)
ax.plot(x, np.sin(x))
plt.plot(x, np.sin(x))

plt.plot(x, np.sin(x))
plt.plot(x, np.cos(x));

#Adjusting the Plot
%matplotlib inline
plt.plot(x, np.sin(x - 0), color='blue')
plt.plot(x, np.sin(x - 1), color='g')
plt.plot(x, np.sin(x - 2), color='0.75')
plt.plot(x, np.sin(x - 3), color='#FFDD44')
plt.plot(x, np.sin(x - 4), color=(1.0, 0.2, 0.3))
plt.plot(x, np.sin(x - 5), color='chartreuse')

#linestype
plt.plot(x, x+0, linestyle='solid')
plt.plot(x, x+1, linestyle='dashed')
plt.plot(x, x+2, linestyle='dashdot')
plt.plot(x, x+3, linestyle='dotted')
plt.plot(x, x+0, linestyle='-')
plt.plot(x, x+0, linestyle='--')
plt.plot(x, x+0, linestyle='-.')
plt.plot(x, x+0, linestyle=':')
