# -*- coding: utf-8 -*-
#
#-----------------------------
#%
#stratified boxplot using the by keyword argument to create groupings.
import pandas as pd
df = pd.DataFrame(np.random.rand(10, 2), columns=['Col1', 'Col2'])
df
df['X'] = pd.Series(['A', 'A', 'A', 'A', 'A', 'B', 'B', 'B', 'B', 'B'])
bp = df.boxplot(by='X')
#
df = pd.DataFrame(np.random.rand(10, 3), columns=['Col1', 'Col2', 'Col3'])
df
df['X'] = pd.Series(['A', 'A', 'A', 'A', 'A', 'B', 'B', 'B', 'B', 'B'])

df['Y'] = pd.Series(['A', 'B', 'A', 'B', 'A', 'B', 'A', 'B', 'A', 'B'])

bp = df.boxplot(column=['Col1', 'Col2'], by=['X', 'Y'], figsize=(10,6))


#groupby
np.random.seed(1234)
df_box = pd.DataFrame(np.random.randn(50, 2))
df_box
df_box['g'] = np.random.choice(['A', 'B'], size=50)
df_box
df_box.loc[df_box['g'] == 'B', 1] += 3
df_box
bp = df_box.boxplot(by='g')
bp = df_box.groupby('g').boxplot()


#Area Plots
df = pd.DataFrame(np.random.rand(10, 4), columns=['a', 'b', 'c', 'd'])
df
df.plot.area()
df.plot.area(stacked=False)

#Stacked Plot
df = pd.DataFrame(np.random.rand(50, 4), columns=['a', 'b', 'c', 'd'])
df
df.plot.scatter(x='a', y='b')
#
ax = df.plot.scatter(x='a', y='b', color='DarkBlue', label='Group 1');
df.plot.scatter(x='c', y='d', color='DarkGreen', label='Group 2', ax=ax)

df.plot.scatter(x='a', y='b', c='c', s=50)
df.plot.scatter(x='a', y='b', s=df['c'] * 200)

#Hexa
df = pd.DataFrame(np.random.randn(1000, 2), columns=['a', 'b'])
df
df['b'] = df['b'] + np.arange(1000)
df
df.plot.hexbin(x='a', y='b', gridsize=25)
#
df = pd.DataFrame(np.random.randn(1000, 2), columns=['a', 'b'])
df['b'] = df['b'] = df['b'] + np.arange(1000)
df['z'] = np.random.uniform(0, 3, 1000)
df.plot.hexbin(x='a', y='b', C='z', reduce_C_function=np.max, gridsize=25)


#Pie
series = pd.Series(3 * np.random.rand(4),index=['a', 'b', 'c', 'd'], name='series')
series.plot.pie(figsize=(6, 6))
#
df = pd.DataFrame(3 * np.random.rand(4, 2), index=['a', 'b', 'c', 'd'], columns=['x', 'y'])
df
df.plot.pie(subplots=True, figsize=(8, 4))
#
series.plot.pie(labels=['AA', 'BB', 'CC', 'DD'], colors=['r', 'g', 'b', 'c'], autopct='%.2f', fontsize=20, figsize=(6, 6))

#
series = pd.Series([0.1] * 4, index=['a', 'b', 'c', 'd'], name='series2')
series
series.plot.pie(figsize=(6, 6))


#Plotting Tools
from pandas.plotting import scatter_matrix

df = pd.DataFrame(np.random.randn(1000, 4), columns=['a', 'b', 'c', 'd'])
df
scatter_matrix(df, alpha=0.2, figsize=(6, 6), diagonal='kde')


#Density Plots
ser = pd.Series(np.random.randn(1000))
ser
ser.plot.kde()


#Andrews Curve
from pandas.plotting import andrews_curves
from pydataset import data
iris = data('iris')
iris.head()
andrews_curves(iris, 'Species')


#Parallel Coordinates
from pandas.plotting import parallel_coordinates
from pydataset import data
iris = data('iris')
parallel_coordinates(iris, 'Species')


#Lag Plot
from pandas.plotting import lag_plot
spacing = np.linspace(-99 * np.pi, 99 * np.pi, num=1000)
spacing
data = pd.Series(0.1 * np.random.rand(1000) + 0.9 * np.sin(spacing))
data
lag_plot(data)

#Autocorrelation Plot
from pandas.plotting import autocorrelation_plot
spacing = np.linspace(-9 * np.pi, 9 * np.pi, num=1000)
data = pd.Series(0.7 * np.random.rand(1000) + 0.3 * np.sin(spacing))
autocorrelation_plot(data)

#Bootstrap Plot
from pandas.plotting import bootstrap_plot
data = pd.Series(np.random.rand(1000))
bootstrap_plot(data, size=50, samples=500, color='grey')
