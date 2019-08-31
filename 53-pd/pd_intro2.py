# -*- coding: utf-8 -*-
#pandas

import pandas as pd
print(pd.__version__)

#panda series - single column values
ps1=pd.Series([1,34,64,23,35])
#creates row index also
ps1
ps1.values
ps1.index
ps1[1]
ps1[1:4]
#assign new index when creating data
ps2=pd.Series([1,34,64,23,35], index=['a','b','c','d','e'])
ps2
ps3=pd.Series([1,34,64,23,35], index=['a','b','c','d','d'])
ps3
pd.Series([1,34,64,23,35], index=[1,7,9,11])
pd.Series([1,34,64,23,35], index=[1,7,9,11,12])
ps2['c']
ps3['d']  #two values
ps2['a':'e']
#another way

ps4 = pd.Series({'a':1,'b':34,'c':64,'d':23,'e':35})
ps4

#indexing in Series
ps4[0]
ps4['a']
ps4[1:4]
ps4['a':'c']
ps4.loc['a']  #explicit index
ps4.iloc[1:3]  #implicit index 0,1,..
ps4.ix[1:3]  #depreciated
ps4[['a','c']]  #fancy indexing (selected)
ps4
ps4[ps4 > 30]
ps4[(ps4 > 30) & (ps4 < 50)]
ps4.keys
'a' in ps4   #index values check
ps4['a'] = 99  #change / mutate
ps4
#%%

#pandas data frame - multi column
#first create two series
course = pd.Series(['BTech','MTech','BBA','MBA'])
strength = pd.Series([100, 50, 200, 75])
fees = pd.Series([2.5, 3, 2, 4])
course, strength, fees
pd1 = pd.DataFrame([course, strength,fees])
pd1  #not the correct method of DF

pd2 = pd.DataFrame({'course':course, 'strength':strength, 'fees':fees})
#count ?
pd2 #better way
pd2.index
pd2.columns
pd2.values
pd2['course']
pd2.keys
pd2[1:3] #row
pd2[0:1] #row

#indexeers - loc, iloc, ix

pd2[:]
pd2
pd2.course
pd2.count  # all values ???
pd2.strength
pd2.fees


pd2.course is pd2['course']  #same method of access check

pd2.loc[1:3]
pd2.iloc[1:2]  #no explicit here
pd2.ix[1:3]  #being depreciated  avoid using this

pd2.loc[pd2.course=='MBA', ]
pd2.loc[pd2.course=='MBA', 'course':'fees']
pd2.loc[pd2.course=='MBA', ['course','fees']]
pd2.iloc[1,2]
pd2.iloc[1,2] = 3.5
pd2

pd2[pd2.fees > 3]



#index alignment - Pd 117 - do later

#%%
#Operating on data
import numpy as np
import pandas as pd
rng = np.random.RandomState(1)
ser = pd.Series(rng.randint(0,10,4))
ser

#df
rng = np.random.RandomState(1)
df = pd.DataFrame(rng.randint(0,10,(3,4)))
df
rng = np.random.RandomState(1)
df = pd.DataFrame(rng.randint(0,10,(3,4)), columns=['A','B','C','D'])
df

#missing data
pd2
placed = pd.Series([None,np.nan, 100, np.nan])
placed
np.sum(placed)  #working
np.nansum(placed)  #better approach with na values

course = pd.Series(['BTech','MTech','BBA','MBA'])
strength = pd.Series([100, 50, 200, 75])
fees = pd.Series([2.5, 3, 2, 4])

pd3 = pd.DataFrame({'course':course, 'strength':strength, 'fees':fees, 'placed':placed})
pd3
pd3.placed.sum()
pd3.strength.sum()
pd3.placed.max()

placed
placed.isnull()
placed.notnull()
placed.dropna()

#new dataframe from list values
pd4 = pd.DataFrame([['dhiraj', 50, 'M', 10000], ['kanika', 28, None, 5000], ['tanvi', 20, 'F', None], ['poonam',45,'F',None],['upen',None,'M',None]])
pd4
pd4.dropna()  #row with any an NA value / completecases
pd4.dropna(axis='columns')  #only those columns with NA
pd4.dropna(axis=1)
pd4.dropna(axis='rows')  #rows
pd4.dropna(axis='columns', how='all')  #all None columns
pd4.dropna(axis='columns', thresh=3)  #min non NA values in columns
pd4.dropna(axis='rows', thresh=3)  #min min NA values in rows

#filling na values
placed
placed.fillna(0)
placed.fillna(method='ffill')
placed.fillna(method='bfill')

#DF fill
pd4
pd4.fillna(method='ffill', axis=1)
pd4.fillna(method='ffill', axis=0)


#MultiIndex  - Later
#pag 130

x= [1,2,3]
y= [4,5,6]
z= [7,8,9]
x,y,z
np.concatenate([x,y,z])
np.concatenate([x,y,z], axis=0) #they are single dim arrays
np.concatenate([x,y,z], axis=1)  #will not work

x=[[1,2,3],[4,5,6]]
y=[[10,11,12],[13,14,15]]
x
np.concatenate([x,y], axis=1) #cbind
np.concatenate([x,y], axis=0)  #rbind

#DF
grades1 = pd.DataFrame(['A':'A1','B1'])
from pandas import pd

grades1 = {'subject1': ['A1','B1','A2','A3'],'subject2': ['A2','A1','B2','B3']   }
df1 = pd.DataFrame(grades1,columns= ['subject1', 'subject2'])
df1

grades2 = {'subject3': ['A1','B1','A2','A3'],'subject4': ['A2','A1','B2','B3']   }
df2 = pd.DataFrame(grades2,columns= ['subject3', 'subject4'])
df2
#join
pd.concat([df1,df2])
pd.concat([df1,df2], axis=0)
pd.concat([df1,df2], axis=1)
pd.concat([df1,df2], ignore_index=True)  #index values in order
pd.concat([df1,df2], keys=['x','y'])  #adding multiple index


print (df)


#Join
rollno = pd.Series(range(1,11))
rollno
name = pd.Series(["student" + str(i) for i in range(1,11)])
name
genderlist  = ['M','F'] 
import random
gender = random.choices(genderlist, k=10)
gender
random.choices( population=genderlist,weights=[0.4, 0.6],k=10)
#numpy.random.choice(items, trials, p=probs)
np.random.choice(a=genderlist, size=10,replace=True, p=[.2,.8])
marks1 = np.random.randint(40,100,size=10)
pd5 = pd.DataFrame({'rollno':rollno, 'name':name, 'gender':gender, 'marks1':marks1})
pd5
#course = random.choices( population=['BBA','MBA','BTECH'] ,weights=[0.4, 0.3,0.3],k=10)
course = np.random.choice(a=['BBA','MBA','BTECH'], size=10,replace=True, p=[.4,.3,.3])
course
marks2 = np.random.randint(40,100,size=10)
pd6 = pd.DataFrame({'rollno':rollno, 'course':course, 'marks2':marks2})
pd6
fees = pd.DataFrame({'course':['BBA','MBA','BTECH'], 'fees':[100000, 200000, 150000]})
fees
#1 to 1
pd.merge(pd5, pd6)
pd.merge(pd5, pd6, on='rollno')
#many to 1
pd6
pd.merge(pd6, fees)
#
pd6b = pd.DataFrame({'rollno1':rollno, 'course':course, 'marks3':marks2})
pd6b 
pd.merge(pd5, pd6b, left_on='rollno', right_on='rollno1')
pd.merge(pd5, pd6b, left_on='rollno', right_on='rollno1').drop('rollno1', axis=1)  #drop redundant coln

#with indices defined
pd5a = pd5.set_index('rollno')
pd5a
pd6a = pd6.set_index('rollno')
pd6a
pd.merge(pd5a, pd6a, left_index=True, right_index=True)
pd5a.join(pd6a)

pd.merge(pd5a, pd6, left_index=True, right_on='rollno')
#set arithmetic
pd.merge(pd5, pd6, how='inner')
pd.merge(pd6, fees, how='outer')
pd.merge(pd6, fees, how='left')
pd.merge(pd5, pd6, on='rollno', suffixes=['_L', '_R'])
#Melt and cast - reshape






pd4
import numexpr
pd4.columns
pd4.columns = ['name', 'age','gender','fees']
pd4
pd4.age
pd4[pd4.age > 20]
pd4.age.isnull().any()
pd4.isnull()
pd4.isnull().any()
pd4.head(3)
pd4.dropna()
#pd4.dropna(inplace=True) #???? carefull it will make changes to original
pd4.sort_values(ascending=False, by='age')
pd4 = pd.DataFrame([['dhiraj', 50, 'M', 10000], ['kanika', 28, None, 5000], ['tanvi', 20, 'F', None], ['poonam',45,'F',None],['upen',None,'M',None]])
pd4
pd4.columns = ['name', 'age','gender','fees']
pd4.sort_values(ascending=False, by='name')
pd4
pd4.sort_values(ascending=False, by='name',inplace=True)
pd4 #change original DF
pd4.sort_values(ascending=False, by=['age'])
pd4.sort_values(ascending=False, by=['fees'], na_position='first')
pd4.sort_values(ascending=True, by=['fees','age'])
pd4.sort_values(ascending=[True,False], by=['gender','age'])
#pd4.sort() #depreciated

pd4.shape

#%%
#summary on DF: create fairly large data
import pandas as pd
import numpy as np

rollno = pd.Series(range(1,1001))
rollno
name = pd.Series(["student" + str(i) for i in range(1,1001)])
name
genderlist  = ['M','F'] 
import random
#gender = random.choices(genderlist, k=1000)
gender= np.random.choice(a=genderlist, size=1000,replace=True, p=[.6,.4])
gender
import collections
collections.Counter(gender)

marks1 = np.random.randint(40,100,size=1000)
marks2 = np.random.randint(40,100,size=1000)
fees = np.random.randint(50000,100000,size=1000)
fees.mean()
course = np.random.choice(a=['BBA','MBA','BTECH'], size=1000,replace=True, p=[.4,.3,.3])
collections.Counter(course)
city = np.random.choice(a=['Delhi', 'Gurugram','Noida','Faridabad'], size=1000, replace=True, p=[.4,.2,.2,.2])
collections.Counter(city)


pd8 = pd.DataFrame({'rollno':rollno, 'name':name, 'course':course, 'gender':gender, 'marks1':marks1,'marks2':marks2, 'fees':fees,'city':city})
pd8
pd8.head()
#start
pd8.head()
pd8.tail()
pd8.describe()
pd8['gender'].value_counts()  #if col has spaces
pd8.gender.value_counts()
#all columns
pd8.apply(pd.value_counts)
pd8.apply(pd.value_counts).fillna(0)
pd8.groupby('course').size()
pd8.groupby('course').count()

#conver cat columns
pd8.columns
cats = ['course', 'gender','city']
pd8[cats] = pd8[cats].astype('category')
pd8[cats].describe()


pd8.groupby(['city','course', 'gender']).size().unstack(fill_value=0)
pd8.groupby(['city','course', 'gender']).count()

pd8.pivot_table(index=['city','course'], columns='gender', aggfunc='size', fill_value=0)
pd.crosstab([pd8.city, pd8.course], pd8.gender)
pd8.groupby(['city','course','gender'])['gender'].size().unstack().fillna(0).astype(int)
pd8.groupby(['city', 'course', 'gender']).size().unstack(fill_value=0)

#depends on time taken to execute
%timeit pd8.groupby(['city', 'course', 'gender']).size().unstack(fill_value=0)

#aggregate, fileter, transform apply
pd8.columns
pd8.marks1.min()
pd8['marks1'].min()
pd8.groupby(['course']).size()

pd8.groupby(['course']).get_group('MBA')

pd8.groupby('course').aggregate('min', np.median, max)
pd8.groupby(['course']).count()
pd8.groupby('course', as_index=False).agg({"marks1": "sum"})
pd8.groupby('course', as_index=True).agg({"marks1": "sum"}) #makes course as index

pd8.groupby('course', as_index=False).agg({"marks1": {"SUM1":"sum" ,"MEAN1":'mean'}, "marks2": {"SUM2":"sum" ,"MEAN2":'mean'}})
pd8.groupby(['course','gender']).agg({"marks1": [min, max, np.mean], "marks2": [min, max, np.median, 'first'], "gender": ['count']})  #np.mean - numpy object

aggregations = {"marks1": {"SUM1":"sum" ,"MEAN1":'mean'}, "marks2": {"SUM2":"sum" ,"MEAN2":'mean'}}
aggregations
pd8.groupby['course'].aggr(aggregations)


pd8['marks1'].apply(lambda x: x > 70).value_counts()
def gthan(x): return x > 70
pd8['marks1'].apply(gthan).value_counts()

pd8['marks1'].apply(gthan).value_counts().plot(kind='barh', stacked=True, figsize=[16,6], colormap='winter')

#copy to clipboard
pd8.to_clipboard(sep=',')
pd8.to_clipboard(sep=',', index=False)
pd8b=pd.read_clipboard(sep=',')
pd8b
pd8b.columns
pd8.to_csv(index=True, path_or_buf = 'pd8.csv')
pd8.to_excel("pd8.xlsx")
pd8.to_excel("pd8.xlsx",sheet_name='pd8', index=False)  
#write to more than one sheet in the workbook, it is necessary to specify an ExcelWriter object:
with pd.ExcelWriter('pd8b.xlsx') as writer:  
    pd8.to_excel(writer, sheet_name='sheet1', index=False)
    pd8.to_excel(writer, sheet_name='sheet2')
pd8.to_excel('pd8b.xlsx', engine='xlsxwriter')


def filter_func(x): return x['fees'].mean > 75000
pd8.groupby('course').mean()
pd8.groupby('course').transform(lambda x: x - x.mean())
pd8.groupby(list(pd8.select_dtypes(exclude=[np.number]))).agg(np.median).reset_index()
pd8.groupby('course').agg({'marks1':np.median,'marks2':np.median,'gender':'first','fees':'last'}).reset_index() 



#pivot table
import numpy as np
import pandas as pd
import seaborn as sns
titanic = sns.load_dataset('titanic')
titanic.head()

titanic.groupby('sex')
titanic.groupby('sex')['survived'].sum()
titanic.groupby('sex')[['survived']].sum()
titanic.groupby(['sex','class'])[['survived']].sum()
titanic.groupby(['sex','class'])[['survived']].sum().unstack()

titanic.pivot_table('survived', index='sex', columns='class', aggfunc='sum')
pd8.columns
pd8.pivot_table('gender', index=['course'], columns='city', aggfunc='count')
#fees
pd8.fees.plot(kind='hist')
pd8.marks1.plot(kind='hist')
m1 = pd.cut(pd8['marks1'],[0,40,60,80,100])
m1#
pd8.pivot_table('course', index=['gender',m1], columns='city', aggfunc='count' )
pd8.pivot_table('course', index=['gender',m1], columns='city', aggfunc='count' ).unstack()
pd8.pivot_table('course', index=['gender',m1], columns='city', aggfunc='count' ).unstack().plot(kind='bar')


pd8.pivot_table('marks1', index=['course'], columns='gender', aggfunc='mean')
pd8.pivot_table('marks1', index=['course'], columns='gender', aggfunc={'mean'})
pd8.pivot_table('marks1', index=['course'], columns='gender', aggfunc={'mean','min'})
pd8.pivot_table(values='marks1', index=['course'], columns='gender', aggfunc={'mean','min','max'})
pd8.pivot_table(values=['marks1','marks2'], index=['course'], columns='gender', aggfunc={'mean'})

pd8.pivot_table(values=['marks1','marks2'], index=['course'], columns='gender', aggfunc={'marks1':['mean'], 'marks2':['max','min', np.mean]})

pd8.pivot_table('course', index=['gender'], columns='city', aggfunc='count', margins=True )   #category columns



#
np.percentile(pd8['marks1'], [25,50,75])

import matplotlib as plt
sns.set()
pd8.pivot_table('city', index=['course'], columns='gender', aggfunc='count')
pd8.pivot_table('city', index=['course'], columns='gender', aggfunc='count' ).plot(kind='bar')

plot.legend(loc='center left')
graphdata =pd8.pivot_table(values=['marks1'], index=['course'], columns='gender', aggfunc='mean')
graphdata.plot(kind='bar', legend=True)
graphdata.plot.bar(stacked=True)
graphdata.plot.barh(stacked=True)
#‘bar’ or ‘barh’ for bar plots
#‘hist’ for histogram
#‘box’ for boxplot
#‘kde’ or ‘density’ for density plots
#‘area’ for area plots
#‘scatter’ for scatter plots
#‘hexbin’ for hexagonal bin plots
#‘pie’ for pie plots
#For example, a bar plot can be created the following way:
#graphdata.plot.hist(alpha=0.5)
#https://pandas.pydata.org/pandas-docs/stable/user_guide/visualization.html
