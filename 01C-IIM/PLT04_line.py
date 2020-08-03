#Topic: Line Plot
#-----------------------------
#libraries

import matplotlib.pyplot as plt

# #structure
# plt.plot(xAxis,yAxis)
# plt.title('title name')
# plt.xlabel('xAxis name')
# plt.ylabel('yAxis name')
# plt.show();

#%% List Data
Year = [1920,1930,1940,1950,1960,1970,1980,1990,2000,2010]
Unemployment_Rate = [9.8,12,8,7.2,6.9,7,6.5,6.2,5.5,6.3]
Year
Unemployment_Rate
 
plt.plot(Year, Unemployment_Rate)
plt.title('Unemployment Rate Vs Year')
plt.xlabel('Year')
plt.ylabel('Unemployment Rate')
plt.show();


#styles
plt.plot(Year, Unemployment_Rate, color='red', marker='o')
plt.title('Unemployment Rate Vs Year', fontsize=14)
plt.xlabel('Year', fontsize=14)
plt.ylabel('Unemployment Rate', fontsize=14)
plt.grid(True)
plt.show();





#%% Pandas DF
import pandas as pd
Data = {'Year': [1920,1930,1940,1950,1960,1970,1980,1990,2000,2010], 'Unemployment_Rate': [9.8,12,8,7.2,6.9,7,6.5,6.2,5.5,6.3]}
Data  
df = pd.DataFrame(Data,columns=['Year','Unemployment_Rate'])
df  

plt.plot(df['Year'], df['Unemployment_Rate'], color='red', marker='o')
plt.title('Unemployment Rate Vs Year', fontsize=14)
plt.xlabel('Year', fontsize=14)
plt.ylabel('Unemployment Rate', fontsize=14)
plt.grid(True)
plt.show()