#Case Study on mtcars dataset in Python	download data

#Download data
import statsmodels.api as sm
#https://vincentarelbundock.github.io/Rdatasets/datasets.html
dataset_mtcars = sm.datasets.get_rdataset(dataname='mtcars', package='datasets')
dataset_mtcars.data.head()
mtcars = dataset_mtcars.data
#structure

#summary

#print first / last few rows


#print number of rows

#number of columns


#print names of columns

#Filter Rows
#cars with cyl=8

#cars with mpg <= 27

#rows match auto tx

#First Row

#last Row


# 1st, 4th, 7th, 25th row + 1st 6th 7th columns.


# first 5 rows and 5th, 6th, 7th columns of data frame

#rows between 25 and 3rd last

#alternative rows and alternative column

#find row with Mazda RX4 Wag and columns cyl, am

#find row betwee Merc 280 and Volvo 142E Mazda RX4 Wag and columns cyl, am


# mpg > 23 or wt < 2


#using lambda for above


#with or condition

#find unique rows of cyl, am, gear


#create new columns: first make a copy of mtcars to mtcars2

#keeps other cols and divide displacement by 61

# multiple mpg * 1.5 and save as original column

