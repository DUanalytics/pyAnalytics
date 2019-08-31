#Grouped Bar Plot
#-----------------------------
#%A grouped barplot is used when you have several groups, and subgroups into these groups. 
import seaborn as sns
import matplotlib.pyplot as plt
dataset_mtcars = sm.datasets.get_rdataset(dataname='mtcars', package='datasets')
dataset_mtcars.data.head()
df = dataset_mtcars.data
df.columns

sns.factorplot(x='gear', y='cyl', hue='am', data=df, kind='bar')

#new function
sns.catplot(x='gear', y='cyl', hue='am', data=df, kind='bar')



#titanic
sns.set(style="whitegrid")

# Load the example Titanic dataset
titanic = sns.load_dataset("titanic")

# Draw a nested barplot to show survival for class and sex
g = sns.catplot(x="class", y="survived", hue="sex", data=titanic, height=6, kind="bar", palette="muted")
g.despine(left=True)
g.set_ylabels("survival probability")


#%%
# libraries
import numpy as np
import matplotlib.pyplot as plt
 
# set width of bar
barWidth = 0.25
 
# set height of bar
bars1 = [12, 30, 1, 8, 22]
bars2 = [28, 6, 16, 5, 10]
bars3 = [29, 3, 24, 25, 17]
 
# Set position of bar on X axis
r1 = np.arange(len(bars1))
r2 = [x + barWidth for x in r1]
r3 = [x + barWidth for x in r2]
 
# Make the plot
plt.bar(r1, bars1, color='#7f6d5f', width=barWidth, edgecolor='white', label='var1')
plt.bar(r2, bars2, color='#557f2d', width=barWidth, edgecolor='white', label='var2')
plt.bar(r3, bars3, color='#2d7f5e', width=barWidth, edgecolor='white', label='var3')
 
# Add xticks on the middle of the group bars
plt.xlabel('group', fontweight='bold')
plt.xticks([r + barWidth for r in range(len(bars1))], ['A', 'B', 'C', 'D', 'E'])
 
# Create legend & Show graphic
plt.legend()
plt.show()
#https://python-graph-gallery.com/11-grouped-barplot/

#https://python-graph-gallery.com/barplot/
