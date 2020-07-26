#Topic: Bar Plot
#-----------------------------
#libraries

import matplotlib.pyplot as plt

#structure
# plt.bar(xAxis,yAxis)
# plt.title('title name')
# plt.xlabel('xAxis name')
# plt.ylabel('yAxis name')
# plt.show();

#%% List data
Country = ['USA','Canada','Germany','UK','France']
GDP_Per_Capita = [45000,42000,52000,49000,47000]

#run together
plt.bar(Country, GDP_Per_Capita)
plt.title('Country Vs GDP Per Capita')
plt.xlabel('Country')
plt.ylabel('GDP Per Capita')
plt.show();

#%%%
New_Colors = ['green','blue','purple','brown','teal']
plt.bar(Country, GDP_Per_Capita, color=New_Colors)
plt.title('Country Vs GDP Per Capita', fontsize=14)
plt.xlabel('Country', fontsize=14)
plt.ylabel('GDP Per Capita', fontsize=14)
plt.grid(True)
plt.show();

#%% DF data
import pandas as pd
   
Data = {'Country': ['USA','Canada','Germany','UK','France'], 'GDP_Per_Capita': [45000,42000,52000,49000,47000]    }
df = pd.DataFrame(Data,columns=['Country','GDP_Per_Capita'])

New_Colors = ['green','blue','purple','brown','teal']
plt.bar(df['Country'], df['GDP_Per_Capita'], color=New_Colors)
plt.title('Country Vs GDP Per Capita', fontsize=14)
plt.xlabel('Country', fontsize=14)
plt.ylabel('GDP Per Capita', fontsize=14)
plt.grid(True)
plt.show();
