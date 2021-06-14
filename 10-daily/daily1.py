#Daily Practise File
#-----------------------------
#Data Structures
#List - ordered collection of items, mutable(changeable) : [square ]
list1 = [1,2,3,4,5,'a','Dhiraj',"Upadhyaya",True]  #list type of object with data
list1  #print when through spyder
type(list1)  #type of object
print(list1)  #print when running complete file
list1
sorted([100000,5,3,2,4,5,324,43,4,4,3,23,434,53442,244,2245224,523])
list2 = ['f','c','d','e',"f"]
list2
list2.count('f')
list2.count('d')
len(list2)
dir(list)
dir(tuple)
dir(list) #functions which can be operated on list type of DS
sorted(list2)
list2
list2[2]  #index starts from 0,1,...
list2[2] = 'Z'  #list is mutable, ie. values can be changed
list2
#%%mutatble - changed, immutable- cannot be changed
#tuple - multiple type of objects like list, immutable: ( round brackets) : no changes
tuple1 = (1, 2, 'a', 'b')
tuple1
type(tuple1)
tuple1[1]
tuple1[1] = 0  #changes not possible, immutable
tuple1 = (5,45)
tuple1  #overwriting is possible
#%%
#Dictionary - key-value pairs : { curly bracket and colon key:value}
dict1 = {1:'Ramesh', 2:'Suresh', 3:'Priyanka'}
dict1
type(dict1)

car = { 'brand':'Honda', 'model': 'Jazz', 'year' : 2017}
type(car)
car
#access
car['brand']
car['year']
car.get('year')
dir(car)
#dir?  # help
dir   #select the text and press control + I
car['brand'] = 'MARUTI'
car  #mutable , value can be changed

#%%frozen Dictionaries
#pip install frozendict   #install this library
from frozendict import frozendict
fd = frozendict({ 'brand': 'Honda' })
fd
fd['brand'] = 'HYUNDIA'   #immutatble

#%% { curly bracket, comma}
#Set - ordered collection of simple items, immutable
set1 = set(['india', 'pakistan', 'england', 'australia','india'])
set1
type(set1)

set2 = {'INDIA','PAKISTAN',  "INDIA"}  #better way
set2
set3 = {'Australia', 'South Africa', 'INDIA'}
set3
sorted(set3)
set2.union(set3) #set2 | set3
#A.intersection(B)
set2.intersection(set3) #set2 & set

type(set2)
print(set2)
dir(set2)  #functions in set, cannot be subscript set2[1]

#%%%frozen ( round bracket, comma)
#frozen set- accepts iterable object as input parameter.
tupleFZ1 = (1, 2, 3, 4, 5, 6, 7, 8, 9, 9, 9) 
tupleFZ1
type(tupleFZ1)  

# converting tuple to frozenset 
frozenset1 = frozenset(tupleFZ1) 
frozenset1  #only one 9
type(frozenset1)

dict1 = {1: 'Ramesh', 2: 'Suresh', 3: 'Priyanka'}
dict1
frozenset2 = frozenset(dict1)
type(frozenset2)
frozenset2 #keys of dictionary made as frozen set

#%% #Strings : 'single quote'  or "doublequote"
#strings as text in string; immutable
str1 = 'Python Programming'
type(str1)
print(str1)
str2="Yash"
str2.lower()
dir(str)
str2[1] = 'Z' #immutable , but new string can be assigned
str2 = 'Dhiraj'
str2

#list, tuple, dictionary, set, strings.
#%% - Sequence
#sequence - tuple and list are used
list1 = [1,2,3,4,5]
list2 = ['a','bb','ccc', 'dddd', 'eeeee']
list1
#for loop : indentations with colon : Run next 2 lines together
for i in list1:
    print(i)

  
for i in list1:    print(i , end ='\t')
print?  #help
for i in list2:    print(i, 'DU' , sep='-' , end ='xxx')
#a-DU-xxx ; i+sep+end
for i in list1:    print(i , 'HHHE', sep=' X ' , end ='\t')
print?
for i in list1:    print('Dhiraj ', i + 6)

tuple1 = (1, 2, 'a', 'b')
tuple1
list5 = ['a',1]
list5
for i in tuple1:    print(i, end ='\t')
range?  # start, stop, step; does not take keyword
range(1, 100, 2)  #nothing happens, though it generates 
for i in range(1, 100, 2):    print(i, end=' ')

#odd nos between x & y    

#%% do later
#zip - map the similar index of multiple containers 
# initializing lists 
name = [ "Dhiraj", "Kounal", "Akhil", "Pooja" ] 
rollno = [ 4, 1, 3, 2 ] 
marks = [ 90, 50, 60, 70 ] 
# using zip() to map values 
mapped = zip(name, rollno, marks) 
mapped
type(mapped)
# converting values to print as set 
mappedSet = set(mapped) 
mappedSet
namez, rollnoz, marksz = zip(*mappedSet)
namez
rollnoz
marksz
#combine and then split

#%% #numpy - array - same data type - numerical python
list1 = [1,2,3,5]
list1
import numpy
numpy.array([10,20])
numpy.array([list1])

import numpy as np #np is alias
np1 = np.arange(1,10)
np1

x=np.arange(start=1,stop=1000000,step=2)
len(x)
x[1:100]
x[1:50:10]
np
np.mean(np.arange(1,10000000))
np1
type(np1)
np?
#help on numpy 
dir(np)  #functions available in numpy
np.mean?  # help on mean function of numpy

np2 = np.array([ 90, 50, 60, 70 ])
np2
np.sort(np2)
dir(np)

np3 = np.array([[1,4],[3,1],[5,6],[10,50]])
np3
np3.shape

np3.reshape((-1,1))  #1 column from 2 column

#http://cs231n.github.io/python-numpy-tutorial/
#%% #pandas - dataframe, excel like
#https://mode.com/python-tutorial/pandas-dataframe/
#https://pandas.pydata.org/pandas-docs/stable/

import pandas as pd
pd?
dir(pd)

df1 = pd.DataFrame({'rollno':[1,2,3,4], 'name': [ "Dhiraj", "Kounal", "Akhil", "Pooja" ], 'marks':[ 40, 50, 60.5, 70 ], 'gender':['M', 'M','M', 'F']})
df1
type(df1) 

df1.columns  #columnanes
df1.index  #row ids/ names  - here auto created
df1.describe() #description of numerical values
df1.dtypes #data types
df1.shape  # rows and columns
df1.groupby('gender').size()
df1.groupby('gender')['marks'].mean()
df1.groupby('gender').aggregate({'marks': [np.mean, 'max','min','std','count']})

#%% #Graphs https://python-graph-gallery.com/
#https://matplotlib.org/

import matplotlib.pyplot as plt
df1.groupby('gender').size()
df1.groupby('gender').size().plot(kind='bar')

plt.hist(df1['marks'])

#https://seaborn.pydata.org/index.html
import seaborn as sns
# sns.set(style="ticks", color_codes=True)
iris = sns.load_dataset("iris")
iris.head()
iris.tail()
df1.groupby('gender').size()
iris.groupby('species').size().plot(kind='bar')
sns.pairplot(iris)  #relationship diagrams


#%% #Load Inbuilt Datasets

#pip install pydataset
from pydataset import data
data('iris')
data('mtcars')

#https://vincentarelbundock.github.io/Rdatasets/datasets.html
import statsmodels.api as sm
mtcars = sm.datasets.get_rdataset(dataname='mtcars', package= 'datasets')
mtcars.data.head()


#%%
#Load from Excel/ CSV and export to
data = mtcars.data
data.head(6)
type(data)
data.to_csv('mtcars.csv')
data.to_excel('mtcarsExcel.xlsx','sheet3', header=False)

#writing to multiple sheets
writer = pd.ExcelWriter('test.xlsx', engine='xlsxwriter')
# Write each dataframe to a different worksheet. you could write different string like above if you want
data.to_excel(writer, sheet_name='sheet1')
data.to_excel(writer, sheet_name='sheet2')
# Close the Pandas Excel writer and output the Excel file.
writer.save()

#%%
data.to_excel?
#load from CSV and Excel
data2a
data2a = pd.read_csv('mtcars.csv') #when csv is in project folder
data2a
data2b
data2b = pd.read_csv('E:/analytics/projects/pyanalytics/mtcars.csv')
data2b
#csv in any other location - full path
data2b
data2a.head()

data2c = pd.read_excel('mtcarsExcel.xlsx',header=0)
#header=None
data2c.head()



#end here....
#now practise numpy and pandas....