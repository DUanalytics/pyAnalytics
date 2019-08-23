#GCF - GCF stands for Get Current Figure
#-----------------------------
#%

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0,10,9)
y = np.randn(9)
# this call creates a figure in the background
plt.scatter(x,y)
# this allows you to retrieve the figure created by the call to scatter() above
fig = plt.gcf()
fig.set_size_inches(6,2)
plt.show()

#GCA
import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(0,10,9)
y = np.randn(9)
# this call creates a figure in the background
plt.scatter(x,y)
# this allows you to retrieve the axis in the figure created by the call to scatter() above
axis = plt.gca()
axis.set_ylim(-3,3)
plt.show()


#plt.cla() / plt.clf()Permalink
#cla stands for 'clear current axes' and clf stands for 'clear current figure'
plt.cla()
plt.clf()
#These methods are used to clear the current figure (plt.clf()) or the current axes (plt.cla()).

#It's common to call these methods just before defining a chart so that previous plots don't interfere with the next ones.