# -*- coding: utf-8 -*-
#Heat Map
#A heatmap contains values representing various shades of the same colour for each value to be plotted. Usually the darker shades of the chart represent higher values than the lighter shade. For a very different value a completely different colour can also be used.
#The below example is a two-dimensional plot of values which are mapped to the indices and columns of the chart.

from pandas import DataFrame
import matplotlib.pyplot as plt

#https://seaborn.pydata.org/generated/seaborn.heatmap.html
import numpy as np; np.random.seed(0)
import seaborn as sns; sns.set()
uniform_data = np.random.rand(10, 12)
ax = sns.heatmap(uniform_data)

#Plot a heatmap for data centered on 0 with a diverging colormap:

normal_data = np.random.randn(10, 12)
normal_data
ax = sns.heatmap(normal_data, center=0)

#Plot a dataframe with meaningful row and column labels:

flights = sns.load_dataset("flights")
flights
#change the shape of data
flights1 = flights.pivot("month", "year", "passengers")
flights1
ax = sns.heatmap(flights1)
#highest is white, lowest is red

#Annotate each cell with the numeric value using integer formatting:
ax = sns.heatmap(flights1, annot=True, fmt="d")

#Add lines between each cell:
ax = sns.heatmap(flights1, linewidths=.5)

#Use a different colormap:
ax = sns.heatmap(flights1, cmap="YlGnBu")

#Center the colormap at a specific value:
ax = sns.heatmap(flights1, center=flights1.loc["January", 1955])

#Don’t draw a colorbar:
ax = sns.heatmap(flights1, cbar=False)

#Use different axes for the colorbar:
grid_kws = {"height_ratios": (.9, .05), "hspace": .3}
f, (ax, cbar_ax) = plt.subplots(2, gridspec_kw=grid_kws)
ax = sns.heatmap(flights1, ax=ax,   cbar_ax=cbar_ax, cbar_kws={"orientation": "horizontal"})
#legend of values :high is white