#Topic:IIM  - Graph
#-----------------------------
#libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
plt?

#%%basic scatter plot
x = [5,7,8,7,2,17,2,9,4,11,12,9,6]
y = [99,86,87,88,111,86,103,87,94,78,77,85,86]

plt.scatter(x, y)
plt.show();

#%%
#dataset
from pydataset import data
mtcars = data('mtcars')
#conda upgrade --all -y
df=mtcars

#%% scatter plot
#dim - x, y, shape(s), color(c), tranpsarency(alpha)
df.describe #summary
df.dtypes  #data types
df.columns
df['wt']; df['mpg']
plt.scatter(x='wt', y='mpg', data=df)
plt.show();

df.carb.value_counts()
#color, transparency, shape
plt.scatter?
plt.scatter(x='wt', y='mpg', s='hp', alpha=.5, c='carb', data=df)
plt.legend(loc='upper left')
plt.show();


#%%tips data
import matplotlib.pyplot as plt
import seaborn as sns

sns.set() #default settings
tips_df = sns.load_dataset('tips')
tips_df
tips_df.columns
tips_df.total_bill
total_bill = tips_df.total_bill.to_numpy()
tip = tips_df.tip.to_numpy()
tip
plt.scatter(total_bill, tip)
plt.show();

#%% labels
plt.scatter(total_bill, tip)
plt.title(label='Total Bill vs Tip')
plt.xlabel('Total Bill')
plt.ylabel('Tip')
plt.show();


#%% marker size
plt.scatter(total_bill, tip, s=1)
plt.show();
plt.scatter(total_bill, tip, s=100)
plt.show();

size_of_table = tips_df['size'].to_numpy()
size_of_table
size_of_table_scaled = [ 3*s**2 for s in size_of_table]
size_of_table_scaled

plt.scatter(total_bill, tip, s=size_of_table_scaled)
plt.show();


#%% legend
scatter = plt.scatter(total_bill, tip, s=size_of_table_scaled)
handles, labels = scatter.legend_elements(prop='sizes')
plt.legend(handles, labels)
plt.show();

df
scatter = plt.scatter('wt', 'mpg', s='hp', data=df)
handles, labels = scatter.legend_elements(prop='sizes')
plt.xlabel('wt')
plt.ylabel('mpg')
plt.legend(handles, labels)
plt.show();


#%% color
plt.scatter(total_bill, tip, color='b')

tips_df.head()
non_smoking_total_bill = tips_df.total_bill[tips_df.smoker =='No']
non_smoking_total_bill

plt.scatter(non_smoking_total_bill, non_smoking_tip, label='Non-Smoking')
plt.scatter(smoking_total_bill, smoking_tip, label='Smoking')
plt.show()


