# -*- coding: utf-8 -*-
#
#-----------------------------
#%
#Multiple Plots

#https://python-data-science.readthedocs.io/en/latest/exploratory.html
#Multiple Plots
df.cyl.value_counts()
fig, axes = plt.subplots(ncols=3, nrows=1, figsize=(15, 5)) 
# note only for 1 row or 1 col, else need to flatten nested list in axes
gear = [4,6,8]
enumerate(axes)
axes
for cnt, ax in enumerate(axes):
    sns.countplot(x=gear[cnt], data=df, ax=ax, order= df[gear[cnt]].value_counts().index)

for ax in fig.axes:
    plt.sca(ax)
    plt.xticks(rotation=90)