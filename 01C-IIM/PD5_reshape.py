#Topic: Reshape Functions
#-----------------------------
#libraries

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#create DF of studnts
rollno = pd.Series(range(1,11))
rollno
#name = pd.Series(["student" + str(i) for i in range(1,11)])
name = pd.Series(['Alex', 'Vamsee', 'Ritwik','Shweta','Karthik', 'Kamakshi', 'Ankit', 'Neharika','Neha','Ravi'])
name
len(name)
gender = pd.Series(['M','M','M', 'F','M','F','M', 'F','F','M'])
gender


groupCBAPs  = ['G1','G2'] 
import random
group = random.choices(groupCBAPs, k=10)
group

random.choices( population=groupCBAPs,weights=[0.4, 0.6],k=10)
#numpy.random.choice(items, trials, p=probs)
np.random.choice(a=groupCBAP, size=10,replace=True, p=[.2,.8])
marks1 = np.random.randint(40,100,size=10)
#course = random.choices( population=['MBA','MBAex','FPM'] ,weights=[0.4, 0.3,0.3],k=10)
course = np.random.choice(a=['MBA','MBAex','FPM'], size=10,replace=True, p=[.4,.3,.3])
course

student1 = pd.DataFrame({'rollno':rollno, 'name':name, 'course':course, 'gender':gender, 'marks1':marks1})
student1


#Lets create another DF with different set of marks
marks2 = np.random.randint(40,100,size=10)
student2 = pd.DataFrame({'rollno':rollno, 'marks2':marks2})
student2

fees = pd.DataFrame({'course':['MBA','MBAex','FPM'], 'fees':[100000, 200000, 150000]})
fees

#1 to 1
pd.merge(student1, student2) #auto find out merge var
pd.merge(student1, student2, on='rollno')

#many to 1
fees.head()
student1.head()

pd.merge(student1, fees, on='course')


#reshaped
student3 = pd.merge(student1, student2)
student3
#long format
student3Melt = student3.melt(id_vars=['rollno', 'name', 'course', 'gender'], var_name='subject', value_name='marks')
student3Melt.head()
student3Melt.groupby(['gender', 'subject'])['marks'].agg(func=['mean', 'min'])

#long to wide



#pivot format
student3a = student3[['name', 'course', 'marks1', 'marks2']]
student3a.head()
student3.pivot_table(student3a, index = ['name','course'])


#missing Values

student4 = pd.DataFrame([['dhiraj', 54, 'M', 10000], ['kanika', 28, None, 5000], ['tanvi', 20, 'F', None], ['kounal',45,'M',None],['akhil',None,'M',None]])
student4

student4.columns = ['name', 'age','gender','fees']
student4.sort_values(ascending=False, by='name')  #temporary sort

student4

student4.sort_values(ascending=False, by='name',inplace=True)  #permanent sort
student4 #change original DF
student4.sort_values(ascending=False, by=['age'])
student4.sort_values(ascending=False, by=['fees'], na_position='first')  #put na first
student4.sort_values(ascending=True, by=['fees','age'])
student4.sort_values(ascending=[True,False], by=['gender','age'])  #mixed sort A, D
student4.shape

#copy to clipboard
student4.to_clipboard(sep=',')
student4.to_clipboard(sep=',', index=False)
student4.to_csv(index=True, path_or_buf = 'student4.csv')
student4.to_excel("student4.xlsx")
student4.to_excel("student4B.xlsx",sheet_name='s1', index=False)  



