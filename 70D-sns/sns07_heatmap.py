#Seaborn Heatmap
#-----------------------------
#%https://seaborn.pydata.org/generated/seaborn.heatmap.html

import numpy as np
np.random.seed(0)
import seaborn as sns
sns.set()

uniform_data = np.random.rand(10, 12)
ax = sns.heatmap(uniform_data)

#Change the limits of the colormap:

ax = sns.heatmap(uniform_data, vmin=0, vmax=1)

#Plot a heatmap for data centered on 0 with a diverging colormap:

normal_data = np.random.randn(10, 12)
ax = sns.heatmap(normal_data, center=0)

#Plot a dataframe with meaningful row and column labels:

flights = sns.load_dataset("flights")
flights = flights.pivot("month", "year", "passengers")
flights
ax = sns.heatmap(flights)

#Annotate each cell with the numeric value using integer formatting:
ax = sns.heatmap(flights, annot=True, fmt="d")

#Add lines between each cell:
ax = sns.heatmap(flights, linewidths=.5)

#Use a different colormap:
ax = sns.heatmap(flights, cmap="YlGnBu")

#Center the colormap at a specific value:
ax = sns.heatmap(flights, center=flights.loc["January", 1955])

#Plot every other column label and don’t plot row labels:
data = np.random.randn(50, 20)
ax = sns.heatmap(data, xticklabels=2, yticklabels=False)

#Don’t draw a colorbar:

ax = sns.heatmap(flights, cbar=False)
