#Topic: Common Plots
#-----------------------------
#libraries https://pythonplot.com/#bar-count

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#pip install plotnine #similar to ggplots
#https://plotnine.readthedocs.io/en/stable/index.html
import plotnine  #ggplot type

from plotnine import ggplot, geom_point, aes, stat_smooth, facet_wrap
plotnine.facet_wrap?
from plotnine.data import mtcars

(ggplot(mtcars, aes('wt', 'mpg', color='factor(gear)')) + geom_point() + stat_smooth(method='lm') + facet_wrap('~gear'))

from plotnine import *
(ggplot(mtcars, aes('factor(cyl)', fill='factor(am)')) + geom_bar( position='fill') )

(ggplot(mtcars, aes('factor(cyl)', fill='factor(am)')) + geom_bar(position='fill') + geom_text(aes(label='stat(count)'), stat='count', position='fill' ))

(ggplot(mpg)+ aes(x='manufacturer') + geom_bar(size=20) + coord_flip() + labs(y='Count', x='Manufacturer', title='Number of Cars by Make'))
#https://plotnine.readthedocs.io/en/stable/tutorials/miscellaneous-order-plot-series.html


from pydataset import data
data()
mtcars = data('mtcars')
data1 = mtcars.copy()
data1.head()

mpg = data('mpg')
data2 = mpg.copy()
data2.head()

#barplot
(mpg['manufacturer'].value_counts(sort=False).plot.barh().set_title('Number of Cars by Make'))

#histogram
(mpg['cty'].plot.hist(bins=12))
plt.hist('cty', bins=12, data=mpg)

ggplot(mpg) +  aes(x='cty') +  geom_histogram(binwidth=2)  #plotnine



#scatter plot
(mpg.plot.scatter(x='displ', y='hwy').set(title='Engine Displacement in Liters vs Highway MPG', xlabel='Engine Displacement in Liters', ylabel='Highway MPG'))

#time series
#ts=?
#ts.set_index('date')['value'].plot()

#facetplot
fig, ax = plt.subplots()
for c, df in mpg.groupby('class'):    ax.scatter(df['displ'], df['hwy'], label=c)
ax.legend()
ax.set_title('Engine Displacement in Liters vs Highway MPG')
ax.set_xlabel('Engine Displacement in Liters')
ax.set_ylabel('Highway MPG')
plt.show();

#seaborn
import seaborn as sns
(sns.FacetGrid( mpg, hue='class', size=10).map(plt.scatter, 'displ', 'hwy').add_legend().set(  title='Engine Displacement in Liters vs Highway MPG', xlabel='Engine Displacement in Liters', ylabel='Highway MPG'))


#scatter plot with CV size
ax = (mpg.plot.scatter(x='cty', y='hwy', s=10*mpg['cyl'], alpha=.5))
ax.set_title('Engine Displacement in Liters vs Highway MPG')
ax.set_xlabel('Engine Displacement in Liters')
ax.set_ylabel('Highway MPG')


#facet plot - 1V
(mpg.pipe(sns.FacetGrid, col='class', col_wrap=4, aspect=.5, size=6).map(plt.scatter, 'displ', 'hwy', s=20).fig.subplots_adjust(wspace=.2, hspace=.2))

#facet plot - 2 V
(mpg.pipe(sns.FacetGrid, col='cyl', row='drv', aspect=.9, size=4).map(plt.scatter, 'displ', 'hwy', s=20).fig.subplots_adjust(wspace=.02, hspace=.02))

#scatter with CI
sns.lmplot(x='displ', y='hwy', data=mpg, size=12)


#barplot - pandas
diamonds = data('diamonds')
diamonds.groupby(['cut', 'clarity']).size().unstack().plot.bar(stacked=True)

#dodged bar plot
(diamonds.groupby(['cut', 'clarity']).size().unstack().plot.bar())

#stacked kde plot
fig, ax = plt.subplots()
ax.set_xlim(55, 70)
for cut in diamonds['cut'].unique():
    s = diamonds[diamonds['cut'] == cut]['depth']
    s.plot.kde(ax=ax, label=cut)
ax.legend()
plt.show();



