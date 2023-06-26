#
#-----------------------------
#%
import matplotlib.pyplot as plt

# simulating a pandas df['type'] column
types = ['apple', 'orange', 'apple', 'pear', 'apple', 'orange', 'apple', 'pear']
x_coords = [10, 10, 5, 4, 3, 20, 19, 21]
y_coords = [21, 23, 12, 21, 10, 20, 14, 2]

for i, type in enumerate(types):
    x = x_coords[i]
    y = y_coords[i]
    plt.scatter(x, y, marker='x', color='red')
    plt.text(x+0.3, y+0.3, type, fontsize=9)
plt.show()


#------
import pandas as pd
from pydataset import data
mtcars = data('mtcars')
mtcars.head()
plt.scatter(mtcars.wt, mtcars.mpg)
#plt.annotate(text='figure pixels', xy =(mtcars.wt, mtcars.mpg), xytext=(.1, .1))
plt.text(x=4, y=15,s='Hi')
plt.show();

fig, ax = plt.subplots()
plt.scatter(mtcars.wt, mtcars.mpg)
for k, v in mtcars[['wt','mpg']].iterrows():
   ax.annotate(k, v)
plt.text(x=4, y=15,s='Hi')
plt.show();

fig, ax = plt.subplots()
plt.scatter(mtcars.wt, mtcars.mpg)
for index, row in mtcars[['wt','mpg']].iterrows():
   ax.annotate(index, row)
plt.text(x=4, y=15,s='Hi')
plt.show();

fig, ax = plt.subplots()
plt.scatter(mtcars.wt, mtcars.mpg)
for index, row in mtcars[['wt','mpg']].iterrows():
   ax.annotate(str(row['wt'])+ ',' + str(row['mpg']), row)
plt.text(x=4, y=15,s='Hi')
plt.show();

fig, ax = plt.subplots()
plt.scatter(mtcars.wt, mtcars.mpg)
for index, row in mtcars[['wt','mpg']].iterrows():
   ax.annotate(','.join([str(row['wt']),str(row['mpg']+2)]), row)
plt.show();

fig, ax = plt.subplots()
plt.scatter(mtcars.wt, mtcars.mpg)
for index, row in mtcars.iterrows():
   ax.annotate(','.join([str(row['wt']),str(row['mpg']+2)]), row[['wt','mpg']])
plt.show();

fig, ax = plt.subplots()
plt.scatter(mtcars.wt, mtcars.mpg)
for index, row in mtcars.iterrows():
   ax.annotate(text= ','.join([str(row['wt']),str(row['mpg']+2)]), xy= row[['wt','mpg']])
plt.show();

fig, ax = plt.subplots()
plt.scatter(mtcars.wt, mtcars.mpg)
for index, row in mtcars.iterrows():
   ax.annotate(text= ','.join([str(row['wt']),str(row['mpg']+2)]), xy= row[['wt','mpg']], xycoords='data')
plt.show();

fig, ax = plt.subplots()
plt.scatter(mtcars.wt, mtcars.mpg)
for index, row in mtcars.iterrows():
   ax.annotate(text= ','.join([str(row['wt']),str(row['mpg']+2)]), xy= row[['wt','mpg']], xycoords='data', textcoords = 'offset pixels')
plt.show();

for k, v in mtcars[['wt','mpg']].iterrows():   print(k, v)
itr = next(mtcars.iterrows())[2]
itr[0]  #index
itr[1]   #data
mtcars.head()

plt.clear()
plt.clf()
plt.cla()
plt.close('all') #imp
for i in mtcars.iterrows(): print(i, sep='\t')

for i, j in mtcars.T.items(): print(i)
for i, j in mtcars.iterrows(): print(i)
for i, j in mtcars.iterrows(): print(j)

for i, j in mtcars.iterrows(): print(i,j)
for row in mtcars.iterrows(): print(row)

for index, row in mtcars.iterrows():
  print(row['mpg'], row['wt'])