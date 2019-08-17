# -*- coding: utf-8 -*-
#import from mysql and plot
import mysql.connector as sql
import pandas as pd

db_connection = sql.connect(host='localhost', database='dulms', user='du', password='mysql123')
df8 = pd.read_sql('SELECT * FROM pd8', con=db_connection)
df8

import matplotlib as mpl
import matplotlib.pyplot as plt
df8.gender.value_counts()
df8.gender.value_counts().plot(kind='bar')
df8.groupby(['city', 'course', 'gender']).size().unstack(fill_value=0)
group1=df8.groupby(['city']).size()
group1
group1.plot(kind='barh')
group1.plot(kind='bar')
group1.plot(kind='pie')

#plot
fig = plt.figure()
ax = plt.axes()
ax.plot(df.marks1,df.marks2, marker='o')
#fig.savefig('plot1.png')
df8b =df8.sort_values(ascending=False, by='marks1')
fig = plt.figure()
ax = plt.axes()
ax.plot(df8b.marks1,df8b.marks2, marker='o')

plt.scatter(df8b.marks1, df8b.marks2)
plt.scatter(df8b.marks1, df8.fees)

#
plt.scatter(df8b.marks1, df8b.fees, c='red')

import seaborn as sns
#sns.pairplot(x_vars=df2.marks1, y_vars=df2.fees, data=df2, hue="gender", size=5)



from pandas import Timestamp
#from ggplot import *  #timestamp error
ggplot(aes(x='x', y='y', color='label'), data=df) + geom_point(size=50) + theme_bw()
ggplot(diamonds, aes(x='price', color='clarity')) + geom_density() +  scale_color_brewer(type='div', palette=7) +    facet_wrap('cut')


#%%
import numpy as np
df = pd.DataFrame(    np.random.normal(10, 1, 30).reshape(10, 3),    index=pd.date_range('2010-01-01', freq='M', periods=10),    columns=('one', 'two', 'three'))
df
df['key1'] = (4, 4, 4, 6, 6, 6, 8, 8, 8, 8)

sns.pairplot(x_vars=["one"], y_vars=["two"], data=df, hue="key1", size=5)
sns.pairplot(vars=["one","two","three"], data=df, hue="key1", size=5)




#%%%
# Generate Data
num = 20
x, y = np.random.random((2, num))
labels = np.random.choice(['a', 'b', 'c'], num)
df = pd.DataFrame(dict(x=x, y=y, label=labels))
#Altair code
from altair import Chart
c = Chart(df)
c.mark_circle().encode(x='x', y='y', color='label')


#%%
import matplotlib.pyplot as plt
from mlxtend.plotting import category_scatter
df.columns
df.head()
fig = category_scatter(x='x', y='y', label_col='label',                        data=df, legend_loc='upper left')
df8b.columns

fig = category_scatter(x='marks1', y='marks2', label_col='gender',                        data=df8b, legend_loc='upper left')
fig = category_scatter(x='marks1', y='marks2', label_col='course',                      data=df8b, legend_loc='upper right')
#this is good
#http://rasbt.github.io/mlxtend/user_guide/plotting/category_scatter/


# library & dataset
import seaborn as sns
df = sns.load_dataset('iris')
 
# Use the 'hue' argument to provide a factor variable
sns.lmplot( x="sepal_length", y="sepal_width", data=df, fit_reg=False, hue='species', legend=False)
# Move the legend to an empty part of the plot
plt.legend(loc='lower right')
 
#sns.plt.show()

# Use the 'hue' argument to provide a factor variable
import seaborn as sns
sns.lmplot( x="marks1", y="fees", data=df8b, fit_reg=False, hue='course', legend=False)
plt.legend(loc='lower right')
sns.plt.show()

sns.lmplot( x="marks1", y="fees", data=df8b, fit_reg=False, hue='course', legend=False, markers=["o", "x", "1"])
plt.legend(loc='lower right')

sns.lmplot( x="marks1", y="marks2", data=df8b, fit_reg=False, hue='course', legend=False, palette="Set2")
plt.legend(loc='upper right')
ax = plt.gca()
ax.set_title("Main Title")

#control color
sns.lmplot( x="marks1", y="marks2", data=df8b, fit_reg=False, hue='gender', legend=True, palette=dict(M="r", F="g"), )
plt.title("Marks vs Marks2")

                                                                                                       
                                                                                                       