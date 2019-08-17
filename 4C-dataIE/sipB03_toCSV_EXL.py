# -*- coding: utf-8 -*-
#Python write to file

#csv
#excel
#googlesheets


import statsmodels.api as sm
iris = sm.datasets.get_rdataset(dataname='iris', package='datasets')
iris.data
iris.data.head()
df1 = iris.data
type(df1)
#https://vincentarelbundock.github.io/Rdatasets/datasets.html
mtcars = sm.datasets.get_rdataset(dataname='mtcars', package='datasets')
mtcars.data
mtcars.data.head()
df2 = mtcars.data
type(df2)

#
import pandas as pd
#check the cwd. file will get saved there
df2.to_excel('exceloutput.xlsx')
#save only when file is not opened
df1.to_excel('exceloutput.xlsx','iris')
df2.to_excel('exceloutput.xlsx', engine='xlsxwriter')
df1.to_excel("E:/pywork/pydata/exceloutput2.xlsx",'iris')
#see direction of / and check if folders exist


#multiple sheets
with pd.ExcelWriter('exceloutput2.xlsx') as writer:
    df1.to_excel(writer, sheet_name='iris', header=True)
    df2.to_excel(writer, sheet_name='mtcars', header=False)
    
    

#CSV

df1.to_csv('csvoutput1.csv', header=False)
df2.to_csv('csvoutput2.csv', header=True)


#list files in the folder
import os
os.listdir(os.curdir)
os.getcwd()  #current working dir
os.chdir("..")
os.getcwd()  #current working dir
os.listdir(os.curdir)
os.chdir("data")
os.getcwd()  #current working dir
os.listdir(os.curdir)
