#python : DUP - Topic : NOS 8101

#standard libaries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pydataset import data
import seaborn as sns

urlData ='https://raw.githubusercontent.com/DUanalytics/datasets/master/csv/mtcars.csv'

df1 = pd.read_csv(urlData) #read csv from web
df1.head()
df1.dtypes

#Import selected rows and columns
df2 = pd.read_csv(urlData, usecols=['mpg','wt', 'hp'])
df2.head()
df2.columns = ['Col1', 'Col2', 'Col3']
df2.head()
df3 = pd.read_csv(urlData, skiprows=1, nrows=10, names=['MPG','CYL','DISP'], usecols=[1,2,3], dtype=['float64','category', 'Int64'])
df3.head()

#summary
#!!!!PC1.	Identify the objective of the analysis
#To apply statistical analysis and technologies on data to find trends and solve problems

#PC2.	define the type of data to be imported
# while importing data from csv, excel, web or other sources, user has to know the metadata of the data being imported. Then user can plan to select particular columns or data type of data

##PC3.	define the volume of data to be imported
# even the volume in terms of rows and columns can be df
#PC4.	define the key variables to be imported
#PC5.	identify suitable sources for the data
#PC6.	perform operations to acquire the data and store it in datasets or data frames
#PC7.	populate metadata for the imported data
#PC8.	validate imported data using appropriate tools & processes 
#PC9.	validate the desired output with the relevant stakeholders within the organization, if required