#Multi Index
#-----------------------------
#%https://jakevdp.github.io/PythonDataScienceHandbook/03.05-hierarchical-indexing.html
#topics - Create index, multiIndex, Sort Multi Index, Filter ,
import pandas as pd
import numpy as np
#%%%

#Single Index
students1 = pd.DataFrame({'rollno':[100,102,103,105,110], 'name':['Kaustabh', 'Apoorva', 'Hitesh', 'Lalit', 'Vijay'], 'gender':['M','F','M','M','M'], 'marks':[60,72, 74, 80,72]})
students1
students1.index
#students1.reindex([200,300,400,500,600])
#default indexing created 
rollno=[100,108,103,105,110]
students2 = pd.DataFrame({'name':['Kaustabh', 'Apoorva', 'Hitesh', 'Lalit', 'Vijay'], 'gender':['M','F','M','M','M'], 'marks':[60,72, 74, 80,72]}, index=rollno)
students2
students2.index.rename('rollno', inplace=True)
students2
students2.index
#now index col is rollnos

students2.sort_index(ascending=False) #ascending=0
students2.sort_index() #ascending=1
students2.iloc['rollno'==110]

#DataFrame.sort_index(axis=0, level=None, ascending=True, inplace=False, kind=’quicksort’, na_position=’last’, sort_remaining=True, by=None)
#Searching
#Pandas Indexing using [ ], .loc[], .iloc[ ], .ix[ ]
#Dataframe.[ ] ; This function also known as indexing operator
#Dataframe.loc[ ] : This function is used for labels.
#Dataframe.iloc[ ] : This function is used for positions or integer based
#Dataframe.ix[] : This function is used for both label and integer based

students2['name']
students2.iloc[2]  #position - Hitesh
students2.loc[110]  #rollno  Vijay
students2.loc[[110,105]]  #rollnos in index
students2.loc[[110,105],'marks'] 
students2.iloc[0:2,0:4]  #integer positions
students2.iloc [:, [0, 2]] #all rows, two columns; postion
students2.ix[2]
students2.iat[1,2]   #	Access a single value for a row/column pair by integer position.
students2.xs(100)  #
#DataFrame.xs(key, axis=0, level=None, drop_level=True)[source]¶


#multiple Index

students3 = students2.set_index('gender', append=True)
students3
students3.index
students3.xs((100,'M'))

students3.iloc[0:3,0:2]
students3.loc[100,]
students3.loc[(100,'M'),]
students3.loc[(100,['M','F']),]
students3.loc[([100,110],['M','F']),]

#practise more

#swap Levels
students3.swaplevel(0, 1, axis=0)

#https://pandas.pydata.org/pandas-docs/stable/user_guide/advanced.html


#%%%

import pandas as pd
cities = ["Vienna", "Vienna", "Vienna",  "Hamburg", "Hamburg", "Hamburg",   "Berlin", "Berlin", "Berlin", "Zürich", "Zürich", "Zürich"]

index = [cities, ["country", "area", "population",                 "country", "area", "population",    "country", "area", "population", "country", "area", "population"]]

print(index)
data = ["Austria", 414.60,    1805681,   "Germany", 755.00,    1760433,      "Germany", 891.85,    3562166,   "Switzerland", 87.88, 378884]
city_series = pd.Series(data, index=index)
print(city_series)
city_series.reset_index()

city_series["Vienna"]["area"]
city_series["Vienna", "area"]
city_series["Hamburg",:]
city_series["Berlin":"Vienna"]  #index not sorted
city_series = city_series.sort_index()
city_series
city_series["Berlin":"Vienna"]
city_series[:, "area"]

#swapping
city_series = city_series.swaplevel()
city_series
city_series.sort_index(inplace=True)
city_series


"""
City   :  Institute
Delhi   : AIIT
Delhi   : ABS
Chandigarh : AIIT
Chandigarh  : ABS
Chandigarh  : ALS
"""

city=['Delhi','Delhi','Chandigarh', 'Chandigarh','Chandigarh']
institute =['AIIT', 'ABS', 'AIIT', 'ABS', 'ALS'] 
len(city), len(institute)
#------
dataForIndex = pd.DataFrame({'city':['Delhi','Delhi','Chandigarh', 'Chandigarh','Chandigarh'], 'institute':['AIIT', 'ABS', 'AIIT', 'ABS', 'ALS']})
dataForIndex
indexFromDF = pd.MultiIndex(levels=dataForIndex, codes=[[0,0,1,1,1], [0, 1, 0, 1, 2]])
midx = pd.MultiIndex(levels=[['Delhi', 'Chandigarh'], ['AIIT', 'ABS', 'ALS']],codes=[[0,0,1,1,1], [0, 1, 0, 1, 2]])
midx
d = [[100,120],[75,70],[120,105],[90,65],[80,55]]
d
df = pd.DataFrame(index=midx, columns=['Male', 'Female'], data=d)
df
df.index
df.drop(index='ABS')
df.drop(columns=['Male'], axis=1)
df.drop(index=['Delhi'], axis=0)
df.drop(index='ABS',level=1,axis=0)
df.drop(index='Delhi',level=0,axis=0)
df.drop(index=['Delhi','Chandigarh'],level=1,axis=0)  #no effect
df.drop(index=['Delhi','Chandigarh'],level=0,axis=0)  #no data
df.drop(index=['AIIT'],level=1,axis=0)  #no data



df.drop(index=['AIIT'], axis=0)
