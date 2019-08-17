# -*- coding: utf-8 -*-
#Created on Fri Jun 14 19:31:48 2019 @author: dhiraj@dell sip
#Graph and Plots
#-----------------------------
#%

import numpy as np
import pandas as pd

import matplotlib.pyplot as plt

plt.bar(['M','F'], [30,10])
plt.barh(['M','F'], [30,10])

plt.bar(['M','F'], [30,10], color = ['r', 'g'])

#with other options
plt.bar(['M','F'], [30,10], color = ['r', 'g'])
plt.title("Student Proportion")
plt.grid(True)
plt.show()  #used if running as file

#now create a dataframe object
df = pd.DataFrame({'gender':['M','F'], 'strength':[25,10]})
df
df.plot(kind='bar')  #legend, labels ?
#save in object
ax = df.plot(kind='bar', grid=True, legend=True, title=' Title of Graph', figsize=[10,5])
ax.set_xlabel('Gender')
ax.set_ylabel('Gender')

#M2
plt.bar(df.gender, df.strength) #use column anmes

plt.bar(df.gender, df.strength, color = ['red','g'])  #list color
plt.bar(df.gender, df.strength, color = ('red','g'))  #tuple color

#complete plot
plt.bar(df.gender, df.strength, color = ['red','g'])
plt.title('Str of Students')
plt.grid(True)
plt.xlabel('Gender')
plt.ylabel('Count')
plt.xticks(df.gender,rotation=45,fontsize=20)
plt.yticks([0,5,10,15,20,25,30],rotation=45,fontsize=20)
plt.bar(df)


#what if both columns are numeric
# x axis values 
x = [1,2,3,4,5,6] 
# corresponding y axis values 
y = [2,4,1,5,2,6] 

plt.plot(x,y)
# plotting the points  
plt.plot(x, y, color='green', linestyle='dashed', linewidth = 3,   marker='o', markerfacecolor='blue', markersize=12) 
  
# setting x and y axis range 
plt.ylim(1,8) 
plt.xlim(1,8) 

# naming the x axis 
plt.xlabel('x - axis') 
# naming the y axis 
plt.ylabel('y - axis') 
  
# giving a title to my graph 
plt.title('Some cool customizations!') 
  
# function to show the plot 
plt.show() 