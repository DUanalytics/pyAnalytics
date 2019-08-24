#myplot.py
import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(0, 10, 100)
#0 to 10 in 100 parts
np.linspace(1,10,10)
x
np.sin(x)
#fig = plt.figure()
plt.plot(x, np.sin(x))
plt.savefig('plot1.png') #save should always be before plt.show
plt.savefig('E:/analytics/plots/plot1.png')
#amend to your folder in your drive :E:/analytics/plots
plt.show(); # import when running from script

