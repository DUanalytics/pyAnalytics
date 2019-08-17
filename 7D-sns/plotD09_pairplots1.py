# -*- coding: utf-8 -*-
#Pair Plot
#-----------------------------

import seaborn as sns
import matplotlib.pyplot as plt
sns.set(style="ticks")

iris = sns.load_dataset("iris")

g = sns.PairGrid(iris)
g.map(plt.scatter);


#
g = sns.PairGrid(iris)
g.map_diag(plt.hist)
g.map_offdiag(plt.scatter);


#
g = sns.PairGrid(iris, hue="species")
g.map_diag(plt.hist)
g.map_offdiag(plt.scatter)
g.add_legend();

#
g = sns.PairGrid(iris, vars=["sepal_length", "sepal_width"], hue="species")
g.map(plt.scatter);

#
g = sns.PairGrid(iris)
g.map_upper(plt.scatter)
g.map_lower(sns.kdeplot)
g.map_diag(sns.kdeplot, lw=3, legend=False);

#
g = sns.PairGrid(tips, y_vars=["tip"], x_vars=["total_bill", "size"], height=4)
g.map(sns.regplot, color=".3")
g.set(ylim=(-1, 11), yticks=[0, 5, 10]);

#
g = sns.PairGrid(tips, hue="size", palette="GnBu_d")
g.map(plt.scatter, s=50, edgecolor="white")
g.add_legend();

#
sns.pairplot(iris, hue="species", height=2.5);

#
g = sns.pairplot(iris, hue="species", palette="Set2", diag_kind="kde", height=2.5)
#https://seaborn.pydata.org/tutorial/axis_grids.html
