#python : Topic : Graphs
#standard libaries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pydataset import data
import seaborn as sns

#additional
from pandas.plotting import autocorrelation_plot, scatter_matrix, parallel_coordinates, lag_plot

#data
CarDatabase = sns.load_dataset('mpg')
MealDatabase = sns.load_dataset('tips')
AttentionDatabase = sns.load_dataset('attention')

#hexbi plots

plt.scatter(CarDatabase.acceleration, CarDatabase.horsepower, marker ='^')
plt.show();

CarDatabase.plot.hexbin(x='acceleration', y='horsepower', gridsize=10, cmap = 'YlGnBu')
plt.show();

#heatmap
sns.heatmap(CarDatabase.corr(), annot=True, cmap='YlGnBu')
plt.show();

#Auto correlation
autocorrelation_plot(MealDatabase.total_bill)
plt.show();