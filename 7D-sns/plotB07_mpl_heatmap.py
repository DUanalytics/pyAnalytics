# -*- coding: utf-8 -*-
#Heat Map
#A heatmap contains values representing various shades of the same colour for each value to be plotted. Usually the darker shades of the chart represent higher values than the lighter shade. For a very different value a completely different colour can also be used.
#The below example is a two-dimensional plot of values which are mapped to the indices and columns of the chart.

from pandas import DataFrame
import matplotlib.pyplot as plt

#data for 4 columns
data=[{2,3,4,1},{6,3,5,2},{6,3,5,4},{3,7,5,4},{2,8,1,5}]
Index= ['I1', 'I2','I3','I4','I5']  #Index values
Cols = ['C1', 'C2', 'C3','C4']  #columns
df = DataFrame(data, index=Index, columns=Cols)
df
plt.pcolor(df)
plt.show()
#1-darkest, 8 - lightest
    
#https://matplotlib.org/3.1.0/gallery/images_contours_and_fields/image_annotated_heatmap.html

#https://seaborn.pydata.org/generated/seaborn.heatmap.html
import numpy as np; np.random.seed(0)
import seaborn as sns; sns.set()
uniform_data = np.random.rand(10, 12)
ax = sns.heatmap(uniform_data)
