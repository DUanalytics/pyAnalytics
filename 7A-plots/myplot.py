# -*- coding: utf-8 -*-
#myplot.py
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 10, 100)
x
np.sin(x)
#fig = plt.figure()
plt.plot(x, np.sin(x))
plt.show() # import when running from script