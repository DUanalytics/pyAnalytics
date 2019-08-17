#General Introduction : based on mtcars data set
#%

url = "https://raw.githubusercontent.com/dupadhyaya/hheanalytics/master/data/mtcars.csv"
#mtcars is inbuilt data in R, exported csv, pushed to git and now importing it here

#load libraries
#import pandas as pd  #dataframe
import numpy as np # arrays type

#read from online csv
df = pd.read_csv(url)

#check
df.shape
df.head()

#category Columns
df.columns
catcolumns1 = ['cyl', 'vs', 'am', 'gear', 'carb']
catcolumns1
df[catcolumns1] = df[catcolumns1].astype('category')
df.dtypes

#describe data
df.describe()
df[catcolumns1].describe()
df.columns
df.describe(exclude=None)
df.describe(include='all')
df.describe(include=[np.number])
df.describe(include=[np.object])
df.describe(include=['category'])
df.describe(exclude=[np.number])
#now summarise

#Group By summaries

df.groupby('am').first()
group1 = df.groupby('am')
group1.first()
group1.get_group(0) 
group1.get_group(1) 
#group by 2 columns
group2 = df.groupby(['am','gear'])
as_index=False
group2.first()
group2.get_group((0,4))
group2.get_group((0,4)).reset_index()

#all columns - am & gear
group3 = df.groupby(['am','gear'], as_index=False)
group3.first()

#Other groupby summaries
#Grouping data with object attributes :
group3.groups

#sum of groups
group2.sum()

#sort Groups and then print values
df.groupby(['gear'], sort = True).sum()
df.groupby(['gear'], sort = False).sum()


#iteration within the group
group4 = df.groupby('cyl') 
for name, group in group4: 
    print(name) 
    print(group) 
    print() 
#Group 4 - then group data

for name, group in group3: 
    print(name) 
    print(group) 
    print() 
#Group 3 - then group data

#selecting a group
group4.get_group(6) 

#apply a function to group
group4.aggregate(np.sum) 
#apply to only 1 columns
group4['mpg'].agg([np.sum, np.mean, np.std]) 

#different functions to different variables
group4.agg({'mpg' : 'mean', 'wt' : 'sum', 'hp':'std'}) 

# using transform function : (value - meanofvalues) / std*10
group4.groups
sc = lambda x: (x - x.mean()) / x.std()*10
group4.transform(sc) 

#filter ???? check this 
group6 = df.groupby('cyl')
group6.filter(lambda x: len(x) >= 2) 
