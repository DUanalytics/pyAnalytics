#Topic: Tree Plot
#-----------------------------
#https://python-graph-gallery.com/treemap/
#libraries
#Treemaps display hierarchical data as a set of nested rectangles. Each group is represented by a rectangle, which area is proportional to its value. Using color schemes, it is possible to represent several dimensions: groups, subgroups… 

#libraries
import matplotlib.pyplot as plt
#pip install squarify
import squarify # pip install squarify (algorithm for treemap)
 
# Change color
squarify.plot(sizes=[13,22,35,5], label=["group A", "group B", "group C", "group D"], color=["red","green","blue", "grey"], alpha=.4 )
plt.axis('off')
plt.show();


#mtcars - distribution of Gears
import matplotlib.pyplot as plt
from pydataset import data
mtcars = data('mtcars')
data=mtcars.copy()

gcount = data.gear.value_counts()
squarify.plot(sizes=gcount, label=["Gear3", "Gear4", "Gear5"], color=["red","green","blue"], alpha=.4 )
plt.axis('off')
plt.show();

squarify.plot(sizes=data.am.value_counts(), alpha=.4 )
plt.axis('off')
plt.show();

data.groupby('am')['am'].agg(['count'])
data.groupby('am').size()
gcount2 = data.groupby('am').size()
gcount2.index?
squarify.plot(sizes=gcount2, label=gcount2.index, color=['red','green'], alpha=.4 )
plt.axis('off')
plt.show();
