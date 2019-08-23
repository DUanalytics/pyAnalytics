#Iris Violin Plot
#-----------------------------
#%

import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import seaborn as sns # data visualisation and plotting
import matplotlib.pyplot as plt # data plotting
import warnings

# Seaborn default configuration
sns.set_style("darkgrid")

# set the custom size for my graphs
sns.set(rc={'figure.figsize':(8.7,6.27)})

# filter all warnings
warnings.filterwarnings('ignore') 

# set max column to 999 for displaying in pandas
pd.options.display.max_columns=999 

# Input data files are available in the "../input/" directory.
# For example, running this (by clicking run or pressing Shift+Enter) will list the files in the input directory

import os
print(os.listdir("data"))

data = pd.read_csv('data\iris.csv')

rows, col = data.shape
print("Rows : %s, column : %s" % (rows, col))

data.columns
data.name

#snsdata = data.drop(['Id'], axis=1)
snsdata = data
snsdata.rename(columns={'name':'species'}, inplace=True)
snsdata.columns

g = sns.pairplot(snsdata, hue='species', markers='x')
g = g.map_upper(plt.scatter)
g = g.map_lower(sns.kdeplot)


#%%%
snsdata.columns
sns.violinplot(x='sepal_length', y='species', data=snsdata, inner='stick', palette='autumn')
plt.show()

sns.violinplot(x='sepal_width', y='species', data=snsdata, inner='stick', palette='autumn')
plt.show()

sns.violinplot(x='petal_length', y='species', data=snsdata, inner='stick', palette='autumn')
plt.show()

sns.violinplot(x='petal_width', y='species', data=snsdata, inner='stick', palette='autumn')
plt.show()