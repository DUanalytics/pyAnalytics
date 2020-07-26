#Topic: Create DF in python
#-----------------------------
#libraries
#two ways
#By typing the values in Python itself to create the DataFrame
#By importing the values from a file (such as an Excel / CSV file), and then creating the DataFrame in Python based on the values imported

#%% 1st Method
import pandas as pd

#data = {'First Column Name':  ['First value', 'Second value',...],
#        'Second Column Name': ['First value', 'Second value',...],  ....    }

#df = pd.DataFrame (data, columns = ['First Column Name','Second Column Name',...])
#don’t need to use quotes around numeric values (unless you wish to capture those values as strings).
cars = {'Brand': ['Honda Civic','Toyota Corolla','Ford Focus','Audi A4'], 'Price': [22000,25000,27000,35000]  }
cars 
type(cars)  #dictionary
df1 = pd.DataFrame(cars, columns = ['Brand', 'Price'])
df1.head()


#each row is represented by a number (also known as the index) starting from 0. Alternatively, you may assign another value/name to represent each row.
df1B = pd.DataFrame(cars, columns = ['Brand','Price'], index=['Car_1', 'Car_2', 'Car_3', 'Car_4'])
df1B
#%% writing to disk
df1.to_csv('E:/analytics/projects/pyanalytics/data/cars.csv')
df1.to_excel('E:/analytics/projects/pyanalytics/data/cars.xlsx')
path=r'E:/analytics/projects/pyanalytics/data/'
df1.to_csv(path+'cars2.csv')
import glob
print(glob.glob('E:/analytics/projects/pyanalytics/data/ca*.csv'))

import os
arr = os.listdir('data') #dir of project
print(arr)
 
 
#%%2nd Method
#import pandas as pd
#data = pd.read_excel(r'Path where the Excel file is stored\File name.xlsx') #for an earlier version of Excel use 'xls'
#df = pd.DataFrame(data, columns = ['First Column Name','Second Column Name',...])

import pandas as pd
cars = pd.read_excel(r'E:/analytics/projects/pyanalytics/data/cars.xlsx')
df2 = pd.DataFrame(cars, columns = ['Brand', 'Price'])
df2
df2['Price'].max()
