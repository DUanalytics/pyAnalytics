#Labelling Points
#-----------------------------
import matplotlib.pyplot as plt
import numpy as np
plt.clf() #clear area
# using some dummy data for this example
xs = np.arange(0,10,1)
ys = np.random.normal(loc=2.0, scale=0.8, size=10)
plt.plot(xs,ys)
# text is left-aligned
plt.text(2,4,'This text starts at point (2,4)')
# text is right-aligned
plt.text(8,3,'This text ends at point (8,3) ', horizontalalignment= 'right')
plt.xticks(np.arange(0,10,1))
plt.yticks(np.arange(0,5,0.5))
plt.show();