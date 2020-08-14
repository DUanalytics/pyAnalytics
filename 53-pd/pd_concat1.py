#python : Topic : Pandas Concatenate - join DF vertically / horizontally
#standard libaries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pydataset import data
import seaborn as sns

mtcars = data('mtcars')
mtcars
sn = [ i for i in range(1,32,1)]
sn
'car' + '1'
'car' + str(1)
#mtcars.apply(lambda x: 'car' + str(x.loc['cyl']), axis=1)
carID = ['car' + str(i) for i in range(1,33,1)]
len(carID)
mtcars['carID'] = carID
mtcars.head()
mtcars2 = mtcars[['carID','mpg','hp']].copy()
mtcars2['mpg'] = mtcars2.mpg * 2
mtcars2['hp'] = mtcars2.hp * .75
mtcars2.head()

#copy of original DF
mtcars3 = mtcars.copy()

# Stack the DataFrames on top of each other
vertical_stack = pd.concat([mtcars, mtcars3], axis=0)
vertical_stack
#64 rows x 12 columns
vertical_stack.shape
vertical_stack.reset_index() #to remove repeating car names
#now index is serno of row
# Write DataFrame to CSV
vertical_stack.to_csv('data/out.csv', index=False)

# Place the DataFrames side by side
horizontal_stack = pd.concat([mtcars, mtcars3], axis=1)
horizontal_stack
#32 rows x 24 columns
horizontal_stack.shape

#
horizontal_stack2 = pd.concat([mtcars, mtcars2], axis=1)
horizontal_stack2.head()
horizontal_stack2.shape
