#Size of Plots
#-----------------------------
#%
from matplotlib import pyplot as plt
import seaborn as sns    

from pydataset import data
mtcars = data('mtcars')
mtcars.head()
mtcars.columns
catMTCARS = ['gear','cyl','am','carb','vs']
mtcars[catMTCARS] = mtcars[catMTCARS].astype('category')

plt.figure(figsize=(5,2))
sns.countplot(data=mtcars, x='gear')

plt.figure(figsize=(3,5))
sns.countplot(data=mtcars, x='gear')
#---
#needs one numeric
g = sns.catplot(data=mtcars, x='gear', y='mpg', hue='am')
g.fig.set_figheight(6)
g.fig.set_figheight(3)

#---
sns.lmplot()), use the size and aspect

#
sns.catplot(data=mtcars, x='gear', y='mpg',  hue='am', height=5, aspect=1/1)


#
sns.countplot(data=mtcars, x='gear')
plt.gcf().set_size_inches(4, 3)

#
fig, ax = plt.subplots()
# the size of A4 paper
fig.set_size_inches(5, 4)
sns.violinplot(data=mtcars[['mpg','wt']], inner="points", ax=ax)    
sns.despine()


#
# figure size in inches
from matplotlib import rcParams
rcParams['figure.figsize'] = 5,4
sns.countplot(data=mtcars, x='gear')

rcParams['figure.figsize'] = 3,6
sns.countplot(data=mtcars, x='cyl')


#options early

a4_dims = (11.7, 8.27)  #a4 size
fig, ax = plt.subplots(figsize=a4_dims)
sns.violinplot(ax=ax, data=mtcars['mpg'])


#
corr = mtcars.corr()
corr
plt.subplots(figsize=(20,15))
sns.heatmap(corr)

#
fig, ax = plt.subplots(1,1,figsize=(10,7))
ax=plt.subplot(111)
sns.heatmap(corr,ax=ax)