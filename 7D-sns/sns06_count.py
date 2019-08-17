#Seaborn - CountPlot
#-----------------------------
#%https://seaborn.pydata.org/generated/seaborn.countplot.html
import seaborn as sns
sns.set(style="darkgrid")
titanic = sns.load_dataset("titanic")
ax = sns.countplot(x="class", data=titanic)

#values
ax = sns.countplot(x="class", hue="who", data=titanic)

#horiz
ax = sns.countplot(y="class", hue="who", data=titanic)

#Use a different color palette:
ax = sns.countplot(x="who", data=titanic, palette="Set3")

titanic.head()
#plt.bar keyword arguments for a different look:
ax = sns.countplot(x="who", data=titanic, facecolor=(0, 0, 0, 0), linewidth=5, edgecolor=sns.color_palette("dark", 3))

#Facet
#Use catplot() to combine a countplot() and a FacetGrid. This allows grouping within additional categorical variables. Using catplot() is safer than using FacetGrid directly, as it ensures synchronization of variable order across facets
g = sns.catplot(x="class", hue="who", col="survived", data=titanic, kind="count", height=4, aspect=.7);


#seaborn.countplot(x=None, y=None, hue=None, data=None, order=None, hue_order=None, orient=None, color=None, palette=None, saturation=0.75, dodge=True, ax=None, **kwargs)¶
