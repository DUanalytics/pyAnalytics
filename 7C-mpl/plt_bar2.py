#Topic: Bar Plot
#-----------------------------
#libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#df = pd.read_csv('data/mtcars.csv')
from pydataset import data
mtcars = data('mtcars')
mtcars.head()
df = mtcars

gpGear = df.groupby('gear' ).size().reset_index().rename( columns={ 'gear': 'Gear',0:'Count'})     
gpGear

plt.figure()    
plt.bar(x='Gear', height='Count', data=gpGear, color= ['b','g','r'], alpha=0.3, align='center')
plt.xticks((3,4,5), ('Gear3','Gear4','Gear5'))
plt.xlabel('Gear')
plt.ylabel('Count')
plt.tick_params(axis='x', which='both', bottom=True, top=True, labelbottom=True)
plt.tick_params(axis='y', which='both', left=True, right=True, labelbottom=True)
plt.xticks(rotation=-30)
plt.savefig('graphs/Energy_Flow.png', bbox_inches='tight')
plt.show()    


#=
import seaborn as sns
gpGear.columns
plt.figure(figsize=(10,5))
chart = sns.countplot( data=df, x='gear', palette='Set1')


#Horz Plots
plt.figure()    
plt.barh(y='Gear', width='Count', data=gpGear, color= ['b','g','r'], alpha=0.3, align='center', tick_label=['Gear3','Gear4','Gear5'])
plt.show() 

#multiple bars

https://stackoverflow.com/questions/14270391/python-matplotlib-multiple-bars
data = [[5., 25., 50., 20.],  [4., 23., 51., 17.],  [6., 22., 52., 19.]]

X = np.arange(4)
plt.bar(X + 0.00, data[0], color = 'b', width = 0.25)
plt.bar(X + 0.25, data[1], color = 'g', width = 0.25)
plt.bar(X + 0.50, data[2], color = 'r', width = 0.25)

plt.show()

#
data = [[5., 25., 50., 20.],  [4., 23., 51., 17.],   [6., 22., 52., 19.]]

color_list = ['b', 'g', 'r']
gap = .8 / len(data)
for i, row in enumerate(data):
  X = np.arange(len(row))
  plt.bar(X + i * gap, row, width = gap,color = color_list[i % len(color_list)])
plt.show()
# The iterator enumerate returns both the current row and its index. Generating the position of each bar for one bar chart is done with a list comprehension. T


#Stacked Bar
A = [5., 30., 45., 22.]
B = [5., 25., 50., 20.]
X = range(4)
plt.bar(X, A, color = 'b')
plt.bar(X, B, color = 'r', bottom = A)
#plt.bar(X, B, color = 'r', top = A)
plt.show()


#
A = np.array([5., 30., 45., 22.])
B = np.array([5., 25., 50., 20.])
C = np.array([1.,  2.,  1.,  1.])
X = np.arange(4)
plt.bar(X, A, color = 'b')
plt.bar(X, B, color = 'g', bottom = A)
plt.bar(X, C, color = 'r', bottom = A + B)
plt.show()

#
data=np.array([[5.,30.,45.,22.],[5.,25.,50.,20.],[1.,2.,1.,1.]])
data.shape
color_list = ['b', 'g', 'r']
X = np.arange(data.shape[1])
for i in range(data.shape[0]):
    plt.bar(X, data[i],  bottom = np.sum(data[:i], axis = 0),    color = color_list[i % len(color_list)])
plt.show()

#---
women_pop = np.array([5., 30., 45., 22.])
men_pop     = np.array( [5., 25., 50., 20.])
X = np.arange(4)
plt.barh(X, women_pop, color = 'r')
plt.barh(X, -men_pop, color = 'b')
plt.show()

#
data = [5, 25, 50, 20]
plt.pie(data)
plt.show()

#---

#The below code will create two plots. The parameters that .subplot take are (row, column, no. of plots).
plt.subplot(2,1,1)
bar1 = plt.bar(x=gpGear['Gear'], height=gpGear['Count'])
plt.ylabel('Gear of Cars')
plt.xticks([],[])
plt.subplot(2,1,2)
bar2 =plt.bar(x=gpGear['Gear'], height=gpGear['Count']*2)
plt.ylabel('Another Bar')
plt.xticks(x=['Gear3','Gear4','Gear5'], rotation='vertical')
plt.show()