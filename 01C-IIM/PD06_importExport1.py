#python : Topic :Import and Export - Excel

#standard libaries
#import numpy as np
import pandas as pd
#import matplotlib.pyplot as plt
#from pydataset import data
#import seaborn as sns

import os
os.listdir('data')

# Read the file
df1 = pd.read_csv("mtcars.csv")

# Output the number of rows
print("Total rows: {0}".format(len(df1)))

# See which headers are available
print(list(df1))

#%%Excel
os.listdir('data')
df21 = pd.read_excel (r'data\pythondata.xlsx')
print (df21)

import xlrd
xls = xlrd.open_workbook(r'data\pythondata.xlsx', on_demand=True)
print(xls.sheet_names())

df22 = pd.read_excel (r'data\pythondata.xlsx', sheet_name='student1')
df22.head()


#links
#https://realpython.com/working-with-large-excel-files-in-pandas/
