#Topic - Case Study - Student Data- Index and Grouping
#%%%
import pandas as pd
import numpy as np
pd.set_option('display.max_columns',15)
student1 = pd.read_csv('data/student1.csv') 
student1.shape

student1.dtypes
student1.columns
#dob should be datetime
student1.dob.head()
#convert into date

from datetime import datetime as dt
dt.strptime('2019-7-4', '%Y-%m-%d')
student1['dob'] = dt.strftime(student1.dob, '%d-%b-%y')  #error
#need to use pandas date time conversion
student1['dob'] = pd.to_datetime(student1['dob'], format='%d-%b-%y')
student1.dtypes
catcols = ['gender', 'cat', 'class12', 'course', 'branch', 'city']
student1[catcols] = student1[catcols].astype('category')
student1.dtypes

#data ready for summarisation
student1
#default index
student1.to_clipboard()
#stage1 : copy to googlesheet

student1.columns
#create index as rollno
student1.set_index('rollno', inplace=True)
#stage2 : copy to gsheet
student1.to_clipboard()
student1.index
student1.columns  #rollno deleted from columns
# 

#create a index of course and batch (admyr)
student2 = student1.reset_index()
student2.head()  #rollno back as column
student2a = student2.set_index(['course','admyr'])
student2a.head()
student2a.to_clipboard()
#stage3
#filter from this indexed data
student2a['gender']
student2a[['branch','gender']]
student2a
student2a.loc['BTECH']
student2a.loc['BTECH',2012]
student2a.loc[['BTECH','MBA'], ['branch','gender']]
student2a.query('2009 < admyr < 2013')
student2a.query('2012 <= admyr < 2013')
student2a.query("2012 <= admyr < 2013 & course == 'MTECH'") #note double quotes
student2a.query("admyr == 2012 & course == 'BTECH'") #note double quotes
student2a.loc[student2a.branch == "CS"]

#%%%
#sorting values
student2a.age.sort_values()
student2a.sort_values(['gender','age'], ascending=True)
student2a.sort_values(['gender','age'], ascending=[True,False])

#sorting index

student2a.sort_index()
student2a.sort_index(level=0)  #first course then admyr
student2a.sort_index(level=1)  #first year then course
student2a.sort_index(level=[1,0], ascending=[True, False])
student2a.sort_index(level=['admyr','course'], ascending=[True, False])
#name and level works
student2a
student2a.index
#using slice
student2a.loc[:,['rollno','gender']]
student2a.sort_index(level=[0,1],inplace=True)
student2a.loc[(slice('BBA'),slice(None)),['rollno','gender']]  #data should be sorted
student2a.loc[(slice('BBA'),slice(2010)),['rollno','gender']] #no student
student2a.loc[(slice('BBA'),slice(2012)),['rollno','gender']]
student2a.loc[(slice('BBA','MBA'),slice(2012)),['rollno','gender']] #BBA to MBA
student2a.loc[(slice('BBA','BTECH'),slice(2012)),['rollno','gender']] #this will ok
student2a.loc[(slice(None),slice(2012)),['rollno','gender']] #upto 2012
student2a.loc[(slice(None),slice(2012,2012)),['rollno','gender']] # only 2012

#student2a.loc[(slice('BBA','MBA'),slice('2012')),:]



#index in columns and rows - student3

student1.columns
student1.shape
secLevel = student1.columns
firstLevel = ['Personal'] * 8 + ['Academics'] * 8
firstLevel
secLevel

dfcol = pd.DataFrame({'Level1': firstLevel, 'Level2':secLevel})
dfcol
data = student1.values
data

pd.MultiIndex.from_frame(dfcol)

newDF = pd.DataFrame(student1.values, columns= pd.MultiIndex.from_frame( dfcol))
newDF
#now we can correctly create index
newDF.head(5)
#it is working only on course
#newDF.loc[slice(1:5),]
newDF.index
#newDF.index(axis=0)
newDF.reset_index()
newDF.columns.droplevel()
newDF.columns = newDF.columns.droplevel(0)
newDF.head(5)

#another way

newDF.columns = student1.columns 
newDF.head(5)

#Another Trick
newDF = pd.DataFrame(student1.values, columns= pd.MultiIndex.from_frame( dfcol))
newDF
newDF.sum(level=1,axis=1)
newDF.columns=newDF.columns.get_level_values(1)
newDF.head()

#drop levels -errors
newDF.droplevel(level=0, axis=1).head(3)
newDF.droplevel(level=1, axis=1).head(3) #all of level0

#
#https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.MultiIndex.droplevel.html

