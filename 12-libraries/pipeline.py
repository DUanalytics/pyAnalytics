# -*- coding: utf-8 -*-
#Created by DU 
#Topic : Pipeline
#https://www.geeksforgeeks.org/create-a-pipeline-in-pandas/
#Pipelines play a useful role in transforming and manipulating tons of data. Pipeline are a sequence of data processing mechanisms. Pandas pipeline feature allows us to string together various user-defined Python functions in order to build a pipeline of data processing. There are two ways to create a Pipeline in pandas. By calling .pipe() function and by importing pdpipe package. 
#Through pandas pipeline function i.e. pipe() function we can call more than one function at a time and in a single line for data processing. Let’s understand and create a pipeline by using the pipe() function.
#%%%
#libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import datetime as dt
from pydataset import data
#%%%
# Create empty dataframe
df = pd.DataFrame()
 
# Creating a simple dataframe
df['name'] = ['Reema', 'Shyam', 'Jai', 'Nimisha', 'Rohit', 'Riya']
df['gender'] = ['Female', 'Male', 'Male','Female', 'Male', 'Female']
df['age'] = [31, 32, 19, 23, 28, 33]
 
# View dataframe
df
#%%%
# function to find mean
def mean_age_by_group(dataframe, col):
    # groups the data by a column and
    # returns the mean age per group
    return dataframe.groupby(col).mean()
#%%%
# function to convert to uppercase
def uppercase_column_name(dataframe):
    # Converts all the column names into uppercase
    dataframe.columns = dataframe.columns.str.upper()
     
    # And returns them
    return dataframe 
#%%%
#Create a pipeline that applies both the functions created above
pipeline = df.pipe(mean_age_by_group, col= 'gender').pipe( uppercase_column_name)
df 
# calling pipeline
pipeline
df.pipe(mean_age_by_group, col= 'gender').reset_index().pipe( uppercase_column_name)
#%%%
#!pip install pdpipe
#%%%
# importing the package
import pdpipe as pdp
#import pandas as pd
 
# creating a empty dataframe named dataset
dataset = pd.DataFrame()
 
# Creating a simple dataframe
dataset['name'] = ['Reema', 'Shyam', 'Jai', 'Nimisha', 'Rohit', 'Riya']
dataset['gender'] = ['Female', 'Male', 'Male','Female', 'Male', 'Female']
dataset['age'] = [31, 32, 19, 23, 28, 33]
dataset['department'] = ['Accounts', 'Management','IT', 'IT', 'Management','Advertising']
dataset['index'] = [1, 2, 3, 4, 5, 6]
# View dataframe
dataset
#%%%
# creating a pipeline and
# dropping the unwanted column
dropCol = pdp.ColDrop("index").apply(dataset)
# display the new dataframe
# after column drop
dropCol
dataset
