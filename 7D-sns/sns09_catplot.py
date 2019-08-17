#Factor Plot in seaborn
#-----------------------------
#%

#https://seaborn.pydata.org/generated/seaborn.catplot.html
#seaborn.catplot(x=None, y=None, hue=None, data=None, row=None, col=None, col_wrap=None, estimator=<function mean>, ci=95, n_boot=1000, units=None, order=None, hue_order=None, row_order=None, col_order=None, kind='strip', height=5, aspect=1, orient=None, color=None, palette=None, legend=True, legend_out=True, sharex=True, sharey=True, margin_titles=False, facet_kws=None, **kwargs)¶


from pydataset import data
mtcars = data('mtcars')
mtcars.head()

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

mtcars.columns

catcols = ['cyl', 'vs', 'am', 'gear', 'carb']
mtcars[catcols] = mtcars[catcols].astype('category')
mtcars.dtypes

#-----------------
# 1 dim count
mtcars.gear.value_counts().plot(kind='bar')

#
#gear vs cyl - how many cars
df = mtcars.copy()
df.groupby(['gear','cyl']).size()
df.groupby(['gear','cyl']).size().reset_index(inplace=True)
df.groupby(['gear','cyl']).size()
df.groupby(['gear','cyl']).size().reset_index()
df1 = df.groupby(['gear','cyl'] ).size().reset_index().rename( columns={'gear':'gears','cyl' : 'cylinder', 0:'Total'})
df1
sns.barplot(x='gears', y='cylinder', data=df1)
#
df2 = df.groupby(['gear','cyl','am'] ).size().reset_index().rename( columns={'gear':'gears','cyl' : 'cylinder', 'am': 'Transmission', 0:'Total'})
df2
sns.barplot(x='gears', y='cylinder', hue='Transmission', data=df2)
sns.barplot(x='gears', y='cylinder', hue='Transmission', data=df2, order=[4,3,5])








#------------
sns.catplot(x="gear", kind="count", data=mtcars)

g = sns.catplot("gear", col="cyl", col_wrap=4, data=mtcars, kind="count", height=2.5, aspect=.8)

#
g = sns.catplot(x="cyl", y="mpg", hue="gear", data=mtcars)


#either x or y should be numeric
#
g = sns.catplot(x="cyl", y="mpg", hue="am", data=mtcars, kind="violin")
#
g = sns.catplot(x="cyl", y="mpg", hue="am", col="carb", data=mtcars)
g = sns.catplot(x="cyl", y="mpg", hue="am", row="gear", data=mtcars, height=2.5, aspect=1.5)
#
#Use a different height and aspect ratio for the facets:
g = sns.catplot(col="carb", x="gear", col_wrap=4, data=mtcars, kind="count", height=2.5, aspect=.8)  #change col_wrap to see effect#Make many column facets and wrap them into the rows of the grid:


#plot horizontally
g = sns.catplot(x="mpg", y="cyl", hue="am", row="gear", data=mtcars, orient="h", height=2, aspect=3, palette="Set3", kind="violin", dodge=True, cut=0, bw=.2)


#formatting
mtcars.groupby(['gear','am']).size().reset_index()
mtcars.groupby(['gear','am']).agg({'mpg':np.mean}).reset_index()

g = sns.catplot(x="gear", y="mpg", col="am", data=mtcars, saturation=.5, kind="point", ci=None, aspect=1.2 , margin_titles =True, height=4)
g.set_axis_labels("Gear", "Mileage")
g.set_xticklabels(["Gear3", "Gear4", "Gear5"])
g.set_titles("{col_name} {col_var}")
g.set(ylim=(0, 30))
g.despine(left=True)

#

#jitter
sns.catplot(x='am', y='mpg', data=mtcars,jitter=0.25)
#Box and Jitter
sns.catplot(x='am', y='mpg', kind='box', data=mtcars)
sns.stripplot(x='am', y='mpg', data=mtcars, jitter=0.2, color='k')
#Boxen
sns.catplot(x='am', y='mpg', data=mtcars,height=4, aspect=1.5, kind='boxen')
#point with hue
sns.catplot(x="am", y="mpg", hue="gear", kind="point",         data=mtcars[mtcars.cyl.isin([2,3,4])])

#point plot
sns.pointplot(x='gear',y='mpg', data=mtcars)
sns.pointplot(x='gear',y='mpg', data=mtcars, estimator=np.mean)
sns.pointplot(x='gear',y='mpg', data=mtcars, estimator=np.mean, ci=68)
sns.pointplot(x='gear',y='mpg', data=mtcars, estimator=np.mean, ci='sd')
sns.pointplot(x='gear',y='mpg', data=mtcars, estimator=np.mean, capsize=.3) #caps” to the error bars:
sns.pointplot(x='gear',y='mpg', data=mtcars, estimator=np.mean,  palette="Blues_d")
#https://seaborn.pydata.org/generated/seaborn.barplot.html
sns.pointplot(x='gear',y='mpg', data=mtcars, estimator=np.max)
sns.pointplot(x='gear',y='mpg', data=mtcars, estimator=np.min)
from numpy import median
sns.pointplot(x='gear',y='mpg', data=mtcars, estimator=median)
