#Panda Introduction and Topics
#-----------------------------
#%library
import pandas as pd
print(dir(pd), end =', ')
len(dir(pd))
#initial
#help
pd.read_csv?

#read from dataset
from pydataset import data
mtcars = data('mtcars')
mtcars.head()

#write to csv
mtcars.to_csv('data/mtcarsCSV.csv')

#read a csv/ excel
df = pd.read_csv('data/mtcarsCSV.csv')
df.shape
#should be able to read from CSV/ only data table

#create Panda Series


#create Pandas DF

string1 = "student"
string1
for dhiraj in range(1, 21):    print(string1 + str(dhiraj))

#You can get this error if you have variable str and trying to call str() function.
list1 = [1,2,3,4,5]
list2=['Student']
'student'.join(map(lambda x: x + str(list1), str(list1) ))
'student'.join(lambda x: x + str(list1))
#Groupy


#pandas plots
