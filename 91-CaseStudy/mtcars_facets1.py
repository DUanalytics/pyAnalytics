# -*- coding: utf-8 -*-
#https://seaborn.pydata.org/tutorial/axis_grids.html
#-----------------------------
#%

import seaborn as sns
import matplotlib.pyplot as plt
sns.set(style="ticks")

from pydataset import data
mtcars = data('mtcars')
mtcars.head()
mtcars.cyl.value_counts()
#no of cylinders
g = sns.FacetGrid(mtcars, col="cyl")
plt.figure(figsize=(6, 5))

g = sns.FacetGrid(mtcars, col="cyl")
g.map(plt.hist, "mpg");

#
g = sns.FacetGrid(mtcars, col="cyl", hue="gear")
g.map(plt.scatter, "wt", "mpg", alpha=.7)
g.add_legend();

#
#
g = sns.FacetGrid(mtcars, row='vs', col="cyl", hue="gear")
g.map(plt.scatter, "wt", "mpg", alpha=.7)
g.add_legend();

#
g = sns.FacetGrid(mtcars, row="am", col="cyl", margin_titles=True)
g.map(sns.regplot, "wt", "mpg", color=".3", fit_reg=False, x_jitter=.1)
g.add_legend();

# Barplot
g = sns.FacetGrid(mtcars, row='am', col="gear", height=4, aspect=.5)
g.map(sns.barplot, "cyl", "vs")
g.add_legend();
#
mtcars.groupby(['cyl','gear']).size()
#You cannot rename  cyl as it is index
mtcars.groupby(['cyl','gear'], as_index=False).size()
sum1=mtcars.groupby(['cyl','gear']).size().reset_index().rename(columns={'cyl':'Cyl','gear' : 'Gear', 0:'TotalCars'})
sum1
type(sum1)
sum1
sum1.columns
g = sns.FacetGrid(sum1, row="Cyl", col="Gear", hue='Cyl', height=3)
g.map(sns.barplot, 'Cyl', 'TotalCars')
g.legend();

# Dist Plot
geartypes = mtcars.gear.value_counts().index
geartypes
g = sns.FacetGrid(mtcars, row="gear", col='am', row_order=geartypes, height=1.7, aspect=2)
g.map(sns.distplot, "mpg", hist=True, rug=True);
g.add_legend();

# scatter
mtcars[['am','vs']] = mtcars[['am','vs']].astype('category')
mtcars.dtypes

g = sns.FacetGrid(mtcars, row='gear', hue="am", height=5)
g.map(plt.scatter, "wt", "mpg", s=50, alpha=.7, linewidth=.5, edgecolor="white")
g.add_legend();

# Scatter
g = sns.FacetGrid(mtcars, col='vs',hue="am", palette="Set1", height=4, hue_kws={"marker": ["^", "v"]})
g.map(plt.scatter, "mpg", "wt", s=100, linewidth=.5, edgecolor="white")
g.add_legend();

# Point Plot
attend = sns.load_dataset("attention").query("subject <= 12")
lowmpg = mtcars.query('mpg < 25')
lowmpg
g = sns.FacetGrid(mtcars, col="gear", hue='gear' ,col_wrap=4, height=3, ylim=(0, 10)) #col_wrap
g.map(sns.pointplot, "mpg", "wt", color=".5", ci=None);
#

with sns.axes_style("white"):
    g = sns.FacetGrid(mtcars, row="gear", col="am", margin_titles=True, height=2.5)
g.map(plt.scatter, "wt", 'mpg', color="#334488", edgecolor="white", lw=.5);
g.set_axis_labels("Wt", "MPG");
g.set(xticks=[10, 30, 50], yticks=[2, 6, 10]);
g.fig.subplots_adjust(wspace=.02, hspace=.02);

# Scatter
g = sns.FacetGrid(tips, col="smoker", margin_titles=True, height=4)
g.map(plt.scatter, "total_bill", "tip", color="#338844", edgecolor="white", s=50, lw=1)
for ax in g.axes.flat:
    ax.plot((0, 50), (0, .2 * 50), c=".2", ls="--")
g.set(xlim=(0, 60), ylim=(0, 14));

# quantile
from scipy import stats
def quantile_plot(x, **kwargs):
    qntls, xr = stats.probplot(x, fit=False)
    plt.scatter(xr, qntls, **kwargs)

g = sns.FacetGrid(tips, col="sex", height=4)
g.map(quantile_plot, "total_bill");

# qqplot
def qqplot(x, y, **kwargs):
    _, xr = stats.probplot(x, fit=False)
    _, yr = stats.probplot(y, fit=False)
    plt.scatter(xr, yr, **kwargs)

g = sns.FacetGrid(tips, col="smoker", height=4)
g.map(qqplot, "total_bill", "tip");

#qq plot
g = sns.FacetGrid(tips, hue="time", col="sex", height=4)
g.map(qqplot, "total_bill", "tip")
g.add_legend();

#
g = sns.FacetGrid(tips, hue="time", col="sex", height=4,   hue_kws={"marker": ["s", "D"]})
g.map(qqplot, "total_bill", "tip", s=40, edgecolor="w")
g.add_legend();

#
def hexbin(x, y, color, **kwargs):
    cmap = sns.light_palette(color, as_cmap=True)
    plt.hexbin(x, y, gridsize=10, cmap=cmap, **kwargs)

with sns.axes_style("dark"):
    g = sns.FacetGrid(mtcars, hue="gear", row='gear', col="cyl", height=4)
g.map(hexbin, "wt", "mpg");


#%%
cmap = sns.color_palette("Set3")
sns.boxplot(x='cyl', y='mpg', data=mtcars, palette=cmap);
plt.xticks(rotation=45);