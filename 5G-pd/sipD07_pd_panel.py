#Pandas Panel Data
#-----------------------------
#%
import pandas as pd
import numpy as np

indexDF = pd.DataFrame([['SEM1', 'sub11'], ['SEM1', 'sub12'], ['SEM2', 'sub21'], ['SEM3', 'sub31'], ['SEM3', 'sub32'],['SEM3', 'sub33']],               columns =['SEMESTER', 'SUBJECTNO'])
indexDF
#6 data per row
index1 = pd.MultiIndex.from_frame(indexDF)


pdDF1 = pd.DataFrame(np.random.randint(50,80, size=(4, 6)), index=['S01', 'S02', 'S03','S04'], columns=index1)
pdDF1

# Students for which rows have to be created
indexDF2 = pd.DataFrame([['BBA', 'S01'], ['BBA', 'S02'], ['MBA', 'S21'], ['MBA', 'S22'], ['PHD', 'S31']], columns =['program', 'rollno'])
indexDF2
index2 = pd.MultiIndex.from_frame(indexDF2)

pdDF2 = pd.DataFrame(np.random.randint(50,80, size=(5, 6)), index=index2, columns=index1)
pdDF2
pdDF2.index.get_level_values 
#transpose
pdDF2.T


#this seems to a long method for creating long list

slist1 = [['BBA', 'BBA', 'MBA', 'MBA', 'PHD'], ['S01', 'S02', 'S21', 'S22', 'S31']]
stuples1 = list(zip(*slist1))
stuples1
index3 = pd.MultiIndex.from_tuples(stuples1, names=['course1', 'rollno2'])
pdDF3 = pd.DataFrame(np.random.randint(50,80, size=(5, 6)), index=index3, columns=index1)
pdDF3

#stack
pdDF3.stack(level='SEMESTER')
pdDF3.stack(level='SUBJECTNO')

pdDF3.stack(level=(0))
pdDF3.stack(level=(1))
pdDF3.stack(level=(0,1))
pdDF3.stack(level=(0,1)).transpose()
pdDF3.stack(level=(1,0)).transpose()



#https://lectures.quantecon.org/py/pandas_panel.html