#python : Topic :graph1

#standard libaries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#pip install pydataset
from pydataset import data
import seaborn as sns


#Figures now render in the Plots pane by default. To make them also appear inline in the Console, uncheck "Mute Inline Plotting" under the Plots pane options menu. 

df = data('mtcars')
plt.style.use('ggplot')

x = [1,2,3,4,5]
y = [10,12,8,9,15]
plt.plot(x, y, color='r', label='traffic', linewidth=1.5)
plt.axis([1,6,7,20])
plt.title('Traffic over days')
plt.xlabel('day')
plt.ylabel('Cars')
plt.legend()
plt.show();
