#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime
import seaborn as sns
from statsmodels.tsa.seasonal import seasonal_decompose
from statsmodels.tsa.statespace.sarimax import SARIMAX

sns.set(rc={"figure.dpi":300, 'savefig.dpi':300})
plt.rcParams['figure.dpi'] = 300
plt.rcParams['savefig.dpi'] = 300
pd.set_option('display.max_columns',15)


# In[2]:

df = pd.read_csv("E:/analytics/KT/store.csv")
df.describe()
df.columns
# In[3]:

print(df.head())
print("\n\nChecking dtype and number of non-null values")
print(df.info())
print("\n\nChecking that dataset contains any null value by using 'isnull' function")
print(df.isnull().sum())


# In[4]:


df['Sales'] = df['Price']*df['Weekly_Units_Sold']   #Adding Weekly sales column

df['Date'] = pd.to_datetime(df['Date'])                    #Changing dtype of 'Date' from object to datetime
df.set_index('Date', inplace=True)                         #Setting index as Date column

df['year'] = df.index.year                                 #Adding year column
df['month'] = df.index.month                               #Adding month column
df['day'] = df.index.day                                   #Adding day column
df['week_of_year'] = df.index.weekofyear                   #Adding week column

print(df.head())

# ### Adding promotion column

# In[5]:
#create a function for this

def f(d):
    if d['Base Price'] == d['Price']:
        x = 0
    elif d['Base Price'] > d['Price']:
        x = 1  #promotions
    else:
        x = -1
    return x
df.columns
df['promotion'] = df.apply(f, axis=1)
df.promotion.value_counts()  #666 transcations of promotions
print(df.head())

# In[6]:

df.reset_index(inplace=True)
print(df.columns)


# ### Now let's check number of week present in dataset

# In[6]:

x=list(df.week_of_year.unique())
x.sort()
print("Weeks in datasets",x, "\n\n")
print(len(x), ": Total number of weeks\n\n")

print(df.week_of_year.value_counts())        #Checking number of occurance

# ### As number of occurance isn't same for all, means there is more than one year in dataset.

# In[7]:

print(df.Store.value_counts(), "\n\n")                  #Checking whether all store occurance number is same
print(df.groupby(['Store','Product']).size())           #Checking the number of store and product occurance

#%%%
# ## Making df1 in which weekly sales is arranged yearly followed by store wise and weeks.

df1 = df.groupby(['year', 'Store', 'week_of_year']).agg({'Sales':'sum'})
df1.reset_index(inplace=True)

print(df1.year.value_counts())
df.query('year == 2010')
df.query('year == 2010').Store.value_counts()
print(df1.iloc[:369].Store.value_counts())                     #2010
print(df1.iloc[369:369+405].Store.value_counts())              #2011
df.query('year == 2011').Store.value_counts()
print(df1.iloc[405+369:369+369+405].Store.value_counts())      #2012
df.query('year == 2012').Store.value_counts()

# # Weekly Sales of each store in 2010, 2011, and 2012

# In[174]:

#Weekly Sales of each store in 2010

Week1  = df1['week_of_year'].iloc[0:41].tolist()
Week1
Week2  = df1['week_of_year'].iloc[41*1:41*2].tolist()
Week3  = df1['week_of_year'].iloc[41*2:41*3].tolist()
Week4  = df1['week_of_year'].iloc[41*3:41*4].tolist()
Week5  = df1['week_of_year'].iloc[41*4:41*5].tolist()
Week6  = df1['week_of_year'].iloc[41*5:41*6].tolist()
Week7  = df1['week_of_year'].iloc[41*6:41*7].tolist()
Week8  = df1['week_of_year'].iloc[41*7:41*8].tolist()
Week9  = df1['week_of_year'].iloc[41*8:41*9].tolist()

Sales1   = df1['Sales'].iloc[0:41].tolist()
Sales1
Sales2   = df1['Sales'].iloc[41*1:41*2].tolist()
Sales3   = df1['Sales'].iloc[41*2:41*3].tolist()
Sales4   = df1['Sales'].iloc[41*3:41*4].tolist()
Sales5   = df1['Sales'].iloc[41*4:41*5].tolist()
Sales6   = df1['Sales'].iloc[41*5:41*6].tolist()
Sales7   = df1['Sales'].iloc[41*6:41*7].tolist()
Sales8   = df1['Sales'].iloc[41*7:41*8].tolist()
Sales9   = df1['Sales'].iloc[41*8:41*9].tolist()
df.columns
# extracting the week from the date
df['Date'].dt.week
df.groupby(['Product', pd.Grouper(key='Date', freq='W')])['Weekly_Units_Sold'].sum().reset_index().sort_values('Date')
df['weekNo'] = df['Date'].dt.isocalendar().week
dfWeekStore = df.groupby(['Store', 'weekNo'])['Weekly_Units_Sold'].sum().reset_index().sort_values('Store')
dfWeekStore.head()
dfWeekStore.plot.line(x='weekNo', y='Store')

y = []
z = []
for i in range(1,53,3):
    y.append(i)
for i in range(1000,34000,4000):
    z.append(i)

plt.plot(Week1, Sales1, label = 'Store 1 Sales')
plt.plot(Week2, Sales2, label = 'Store 2 Sales')
plt.plot(Week3, Sales3, label = 'Store 3 Sales')
plt.plot(Week4, Sales4, label = 'Store 4 Sales')
plt.plot(Week5, Sales5, label = 'Store 5 Sales')
plt.plot(Week6, Sales6, label = 'Store 6 Sales')
plt.plot(Week7, Sales7, label = 'Store 7 Sales')
plt.plot(Week8, Sales8, label = 'Store 8 Sales')
plt.plot(Week9, Sales9, label = 'Store 9 Sales')
plt.xlabel('Week Number')
plt.ylabel('Sales')
plt.legend(loc='upper left')
plt.xticks(y)
plt.yticks(z)
plt.title('Weekly sales data of each store in 2010')
plt.show();


# In[11]:


# Weekly sales of each store in 2011

Week1  = df1['week_of_year'].iloc[41*9:369+(45*1)].tolist()
Week1
Week2  = df1['week_of_year'].iloc[369+(45*1):369+(45*2)].tolist()
Week3  = df1['week_of_year'].iloc[369+(45*2):369+(45*3)].tolist()
Week4  = df1['week_of_year'].iloc[369+(45*3):369+(45*4)].tolist()
Week5  = df1['week_of_year'].iloc[369+(45*4):369+(45*5)].tolist()
Week6  = df1['week_of_year'].iloc[369+(45*5):369+(45*6)].tolist()
Week7  = df1['week_of_year'].iloc[369+(45*6):369+(45*7)].tolist()
Week8  = df1['week_of_year'].iloc[369+(45*7):369+(45*8)].tolist()
Week9  = df1['week_of_year'].iloc[369+(45*8):369+(45*9)].tolist()

Sales1   = df1['Sales'].iloc[41*9:369+(45*1)].tolist()
Sales2   = df1['Sales'].iloc[369+(45*1):369+(45*2)].tolist()
Sales3   = df1['Sales'].iloc[369+(45*2):369+(45*3)].tolist()
Sales4   = df1['Sales'].iloc[369+(45*3):369+(45*4)].tolist()
Sales5   = df1['Sales'].iloc[369+(45*4):369+(45*5)].tolist()
Sales6   = df1['Sales'].iloc[369+(45*5):369+(45*6)].tolist()
Sales7   = df1['Sales'].iloc[369+(45*6):369+(45*7)].tolist()
Sales8   = df1['Sales'].iloc[369+(45*7):369+(45*8)].tolist()
Sales9   = df1['Sales'].iloc[369+(45*8):369+(45*9)].tolist()

y = []
z = []
for i in range(1,53,3):
    y.append(i)
for i in range(1000,30000,4000):
    z.append(i)

plt.plot(Week1, Sales1, label = 'Store 1 Sales')
plt.plot(Week2, Sales2, label = 'Store 2 Sales')
plt.plot(Week3, Sales3, label = 'Store 3 Sales')
plt.plot(Week4, Sales4, label = 'Store 4 Sales')
plt.plot(Week5, Sales5, label = 'Store 5 Sales')
plt.plot(Week6, Sales6, label = 'Store 6 Sales')
plt.plot(Week7, Sales7, label = 'Store 7 Sales')
plt.plot(Week8, Sales8, label = 'Store 8 Sales')
plt.plot(Week9, Sales9, label = 'Store 9 Sales')
plt.xlabel('Week Number')
plt.ylabel('Sales')
plt.legend(loc='upper left')
plt.xticks(y)
plt.yticks(z)
plt.title('Weekly sales data of each store in 2011')
plt.show();


# In[12]:


# Weekly sale of each store in 2012

Week1  = df1['week_of_year'].iloc[369+(45*9) : 369+(45*9)+(41*1)].tolist()
Week2  = df1['week_of_year'].iloc[369+(45*9)+(41*1) : 369+(45*9)+(41*2)].tolist()
Week3  = df1['week_of_year'].iloc[369+(45*9)+(41*2) : 369+(45*9)+(41*3)].tolist()
Week4  = df1['week_of_year'].iloc[369+(45*9)+(41*3) : 369+(45*9)+(41*4)].tolist()
Week5  = df1['week_of_year'].iloc[369+(45*9)+(41*4) : 369+(45*9)+(41*5)].tolist()
Week6  = df1['week_of_year'].iloc[369+(45*9)+(41*5) : 369+(45*9)+(41*6)].tolist()
Week7  = df1['week_of_year'].iloc[369+(45*9)+(41*6) : 369+(45*9)+(41*7)].tolist()
Week8  = df1['week_of_year'].iloc[369+(45*9)+(41*7) : 369+(45*9)+(41*8)].tolist()
Week9  = df1['week_of_year'].iloc[369+(45*9)+(41*8) : 369+(45*9)+(41*9)].tolist()

Sales1   = df1['Sales'].iloc[369+(45*9) : 369+(45*9)+(41*1)].tolist()
Sales2   = df1['Sales'].iloc[369+(45*9)+(41*1) : 369+(45*9)+(41*2)].tolist()
Sales3   = df1['Sales'].iloc[369+(45*9)+(41*2) : 369+(45*9)+(41*3)].tolist()
Sales4   = df1['Sales'].iloc[369+(45*9)+(41*3) : 369+(45*9)+(41*4)].tolist()
Sales5   = df1['Sales'].iloc[369+(45*9)+(41*4) : 369+(45*9)+(41*5)].tolist()
Sales6   = df1['Sales'].iloc[369+(45*9)+(41*5) : 369+(45*9)+(41*6)].tolist()
Sales7   = df1['Sales'].iloc[369+(45*9)+(41*6) : 369+(45*9)+(41*7)].tolist()
Sales8   = df1['Sales'].iloc[369+(45*9)+(41*7) : 369+(45*9)+(41*8)].tolist()
Sales9   = df1['Sales'].iloc[369+(45*9)+(41*8) : 369+(45*9)+(41*9)].tolist()

y = []
z = []
for i in range(1,53,3):
    y.append(i)
for i in range(1000,38000,5000):
    z.append(i)

plt.plot(Week1, Sales1, label = 'Store 1 Sales')
plt.plot(Week2, Sales2, label = 'Store 2 Sales')
plt.plot(Week3, Sales3, label = 'Store 3 Sales')
plt.plot(Week4, Sales4, label = 'Store 4 Sales')
plt.plot(Week5, Sales5, label = 'Store 5 Sales')
plt.plot(Week6, Sales6, label = 'Store 6 Sales')
plt.plot(Week7, Sales7, label = 'Store 7 Sales')
plt.plot(Week8, Sales8, label = 'Store 8 Sales')
plt.plot(Week9, Sales9, label = 'Store 9 Sales')
plt.xlabel('Week Number')
plt.ylabel('Sales')
plt.legend(loc='upper left')
plt.xticks(y)
plt.yticks(z)
plt.title('Weekly sales data of each store in 2012')
plt.show();



# # Weekly Unit Sold in each store in 2010, 2011, and 2012

# In[175]:


df1 = df.groupby(['year', 'Store', 'week_of_year']).agg({'Weekly_Units_Sold':'sum'})
df1.reset_index(inplace=True)

print(df1.year.value_counts())
print(df1.iloc[:369].Store.value_counts())                     #2010
print(df1.iloc[369:369+405].Store.value_counts())              #2011
print(df1.iloc[405+369:369+369+405].Store.value_counts())      #2012


# In[14]:


#Weekly unit sold store wise in 2010

Week1  = df1['week_of_year'].iloc[0:41].tolist()
Week2  = df1['week_of_year'].iloc[41*1:41*2].tolist()
Week3  = df1['week_of_year'].iloc[41*2:41*3].tolist()
Week4  = df1['week_of_year'].iloc[41*3:41*4].tolist()
Week5  = df1['week_of_year'].iloc[41*4:41*5].tolist()
Week6  = df1['week_of_year'].iloc[41*5:41*6].tolist()
Week7  = df1['week_of_year'].iloc[41*6:41*7].tolist()
Week8  = df1['week_of_year'].iloc[41*7:41*8].tolist()
Week9  = df1['week_of_year'].iloc[41*8:41*9].tolist()

Sales1   = df1['Weekly_Units_Sold'].iloc[0:41].tolist()
Sales2   = df1['Weekly_Units_Sold'].iloc[41*1:41*2].tolist()
Sales3   = df1['Weekly_Units_Sold'].iloc[41*2:41*3].tolist()
Sales4   = df1['Weekly_Units_Sold'].iloc[41*3:41*4].tolist()
Sales5   = df1['Weekly_Units_Sold'].iloc[41*4:41*5].tolist()
Sales6   = df1['Weekly_Units_Sold'].iloc[41*5:41*6].tolist()
Sales7   = df1['Weekly_Units_Sold'].iloc[41*6:41*7].tolist()
Sales8   = df1['Weekly_Units_Sold'].iloc[41*7:41*8].tolist()
Sales9   = df1['Weekly_Units_Sold'].iloc[41*8:41*9].tolist()

y = []
z = []
for i in range(1,53,3):
    y.append(i)
for i in range(0,5000,500):
    z.append(i)

plt.plot(Week1, Sales1, label = 'Store 1 Sales')
plt.plot(Week2, Sales2, label = 'Store 2 Sales')
plt.plot(Week3, Sales3, label = 'Store 3 Sales')
plt.plot(Week4, Sales4, label = 'Store 4 Sales')
plt.plot(Week5, Sales5, label = 'Store 5 Sales')
plt.plot(Week6, Sales6, label = 'Store 6 Sales')
plt.plot(Week7, Sales7, label = 'Store 7 Sales')
plt.plot(Week8, Sales8, label = 'Store 8 Sales')
plt.plot(Week9, Sales9, label = 'Store 9 Sales')
plt.xlabel('Week Number')
plt.ylabel('Sales')
plt.legend(loc='upper right')
plt.xticks(y)
plt.yticks(z)
plt.title('Weekly unit sold data of each store in 2010')
plt.show()


# In[15]:


#Weekly unit sold store wise in 2011

Week1  = df1['week_of_year'].iloc[41*9:369+(45*1)].tolist()
Week2  = df1['week_of_year'].iloc[369+(45*1):369+(45*2)].tolist()
Week3  = df1['week_of_year'].iloc[369+(45*2):369+(45*3)].tolist()
Week4  = df1['week_of_year'].iloc[369+(45*3):369+(45*4)].tolist()
Week5  = df1['week_of_year'].iloc[369+(45*4):369+(45*5)].tolist()
Week6  = df1['week_of_year'].iloc[369+(45*5):369+(45*6)].tolist()
Week7  = df1['week_of_year'].iloc[369+(45*6):369+(45*7)].tolist()
Week8  = df1['week_of_year'].iloc[369+(45*7):369+(45*8)].tolist()
Week9  = df1['week_of_year'].iloc[369+(45*8):369+(45*9)].tolist()

Sales1   = df1['Weekly_Units_Sold'].iloc[41*9:369+(45*1)].tolist()
Sales2   = df1['Weekly_Units_Sold'].iloc[369+(45*1):369+(45*2)].tolist()
Sales3   = df1['Weekly_Units_Sold'].iloc[369+(45*2):369+(45*3)].tolist()
Sales4   = df1['Weekly_Units_Sold'].iloc[369+(45*3):369+(45*4)].tolist()
Sales5   = df1['Weekly_Units_Sold'].iloc[369+(45*4):369+(45*5)].tolist()
Sales6   = df1['Weekly_Units_Sold'].iloc[369+(45*5):369+(45*6)].tolist()
Sales7   = df1['Weekly_Units_Sold'].iloc[369+(45*6):369+(45*7)].tolist()
Sales8   = df1['Weekly_Units_Sold'].iloc[369+(45*7):369+(45*8)].tolist()
Sales9   = df1['Weekly_Units_Sold'].iloc[369+(45*8):369+(45*9)].tolist()

y = []
z = []
for i in range(1,53,3):
    y.append(i)
for i in range(0,4100,500):
    z.append(i)

plt.plot(Week1, Sales1, label = 'Store 1 Sales')
plt.plot(Week2, Sales2, label = 'Store 2 Sales')
plt.plot(Week3, Sales3, label = 'Store 3 Sales')
plt.plot(Week4, Sales4, label = 'Store 4 Sales')
plt.plot(Week5, Sales5, label = 'Store 5 Sales')
plt.plot(Week6, Sales6, label = 'Store 6 Sales')
plt.plot(Week7, Sales7, label = 'Store 7 Sales')
plt.plot(Week8, Sales8, label = 'Store 8 Sales')
plt.plot(Week9, Sales9, label = 'Store 9 Sales')
plt.xlabel('Week Number')
plt.ylabel('Sales')
plt.legend(loc='upper right')
plt.xticks(y)
plt.yticks(z)
plt.title('Weekly unit sold data of each store in 2011')
plt.show()


# In[17]:


#Weekly unit sold store wise in 2012

Week1  = df1['week_of_year'].iloc[369+(45*9) : 369+(45*9)+(41*1)].tolist()
Week2  = df1['week_of_year'].iloc[369+(45*9)+(41*1) : 369+(45*9)+(41*2)].tolist()
Week3  = df1['week_of_year'].iloc[369+(45*9)+(41*2) : 369+(45*9)+(41*3)].tolist()
Week4  = df1['week_of_year'].iloc[369+(45*9)+(41*3) : 369+(45*9)+(41*4)].tolist()
Week5  = df1['week_of_year'].iloc[369+(45*9)+(41*4) : 369+(45*9)+(41*5)].tolist()
Week6  = df1['week_of_year'].iloc[369+(45*9)+(41*5) : 369+(45*9)+(41*6)].tolist()
Week7  = df1['week_of_year'].iloc[369+(45*9)+(41*6) : 369+(45*9)+(41*7)].tolist()
Week8  = df1['week_of_year'].iloc[369+(45*9)+(41*7) : 369+(45*9)+(41*8)].tolist()
Week9  = df1['week_of_year'].iloc[369+(45*9)+(41*8) : 369+(45*9)+(41*9)].tolist()

Sales1   = df1['Weekly_Units_Sold'].iloc[369+(45*9) : 369+(45*9)+(41*1)].tolist()
Sales2   = df1['Weekly_Units_Sold'].iloc[369+(45*9)+(41*1) : 369+(45*9)+(41*2)].tolist()
Sales3   = df1['Weekly_Units_Sold'].iloc[369+(45*9)+(41*2) : 369+(45*9)+(41*3)].tolist()
Sales4   = df1['Weekly_Units_Sold'].iloc[369+(45*9)+(41*3) : 369+(45*9)+(41*4)].tolist()
Sales5   = df1['Weekly_Units_Sold'].iloc[369+(45*9)+(41*4) : 369+(45*9)+(41*5)].tolist()
Sales6   = df1['Weekly_Units_Sold'].iloc[369+(45*9)+(41*5) : 369+(45*9)+(41*6)].tolist()
Sales7   = df1['Weekly_Units_Sold'].iloc[369+(45*9)+(41*6) : 369+(45*9)+(41*7)].tolist()
Sales8   = df1['Weekly_Units_Sold'].iloc[369+(45*9)+(41*7) : 369+(45*9)+(41*8)].tolist()
Sales9   = df1['Weekly_Units_Sold'].iloc[369+(45*9)+(41*8) : 369+(45*9)+(41*9)].tolist()

y = []
z = []
for i in range(1,53,3):
    y.append(i)
for i in range(0,4100,500):
    z.append(i)

plt.plot(Week1, Sales1, label = 'Store 1 Sales')
plt.plot(Week2, Sales2, label = 'Store 2 Sales')
plt.plot(Week3, Sales3, label = 'Store 3 Sales')
plt.plot(Week4, Sales4, label = 'Store 4 Sales')
plt.plot(Week5, Sales5, label = 'Store 5 Sales')
plt.plot(Week6, Sales6, label = 'Store 6 Sales')
plt.plot(Week7, Sales7, label = 'Store 7 Sales')
plt.plot(Week8, Sales8, label = 'Store 8 Sales')
plt.plot(Week9, Sales9, label = 'Store 9 Sales')
plt.xlabel('Week Number')
plt.ylabel('Sales')
plt.legend(loc='upper right')
plt.xticks(y)
plt.yticks(z)
plt.title('Weekly unit sold data of each store in 2012')
plt.show()


# # Weekly Sales, product wise, in 2010, 2011, and 2012

# In[176]:


df2 = df.groupby(['year', 'Product', 'week_of_year']).agg({'Sales':'sum'})
df2.reset_index(inplace=True)


# In[177]:


print(df2.year.value_counts())
print(df2.iloc[:123].Product.value_counts())                    #2010
print(df2.iloc[123:123+135].Product.value_counts())             #2011
print(df2.iloc[123+135:123+135+123].Product.value_counts())     #2012


# In[20]:


#Weekly sales product wise in 2010

Week1  = df2['week_of_year'].iloc[0 : 41].tolist()
Week2  = df2['week_of_year'].iloc[41 : 41*2].tolist()
Week3  = df2['week_of_year'].iloc[41*2 : 41*3].tolist()

Sales1   = df2['Sales'].iloc[0 : 41].tolist()
Sales2   = df2['Sales'].iloc[41 : 41*2].tolist()
Sales3   = df2['Sales'].iloc[41*2 :41*3].tolist()

y = []
z = []
for i in range(1,53,3):
    y.append(i)
for i in range(9000,70000,6000):
    z.append(i)

plt.plot(Week1, Sales1, label = 'Product 1 Sales')
plt.plot(Week2, Sales2, label = 'Product 2 Sales')
plt.plot(Week3, Sales3, label = 'Product 3 Sales')
plt.xlabel('Week Number')
plt.ylabel('Sales')
plt.legend(loc='upper left')
plt.xticks(y)
plt.yticks(z)
plt.title('Weekly sales data of each product in 2010')
plt.show()


# In[21]:


#Weekly sales product wise in 2011

Week1  = df2['week_of_year'].iloc[41*3 : 123+45].tolist()
Week2  = df2['week_of_year'].iloc[123+45 : 123+45+45].tolist()
Week3  = df2['week_of_year'].iloc[123+45+45 : 123+45+45+45].tolist()

Sales1   = df2['Sales'].iloc[41*3 : 123+45].tolist()
Sales2   = df2['Sales'].iloc[123+45 : 123+45+45].tolist()
Sales3   = df2['Sales'].iloc[123+45+45 : 123+45+45+45].tolist()

y = []
z = []
for i in range(1,53,3):
    y.append(i)
for i in range(9000,70000,6000):
    z.append(i)

plt.plot(Week1, Sales1, label = 'Product 1 Sales')
plt.plot(Week2, Sales2, label = 'Product 2 Sales')
plt.plot(Week3, Sales3, label = 'Product 3 Sales')
plt.xlabel('Week Number')
plt.ylabel('Sales')
plt.legend(loc='upper left')
plt.xticks(y)
plt.yticks(z)
plt.title('Weekly sales data of each product in 2011')
plt.show()


# In[22]:


#Weekly sales product wise in 2012

Week1  = df2['week_of_year'].iloc[123+45+45+45 : 123+(45*3)+41].tolist()
Week2  = df2['week_of_year'].iloc[123+(45*3)+41 : 123+(45*3)+(41*2)].tolist()
Week3  = df2['week_of_year'].iloc[123+(45*3)+(41*2) : 123+(45*3)+(41*3)].tolist()

Sales1   = df2['Sales'].iloc[123+45+45+45 : 123+(45*3)+41].tolist()
Sales2   = df2['Sales'].iloc[123+(45*3)+41 : 123+(45*3)+(41*2)].tolist()
Sales3   = df2['Sales'].iloc[123+(45*3)+(41*2) : 123+(45*3)+(41*3)].tolist()

y = []
z = []
for i in range(1,53,3):
    y.append(i)
for i in range(9000,76000,6000):
    z.append(i)

plt.plot(Week1, Sales1, label = 'Product 1 Sales')
plt.plot(Week2, Sales2, label = 'Product 2 Sales')
plt.plot(Week3, Sales3, label = 'Product 3 Sales')
plt.xlabel('Week Number')
plt.ylabel('Sales')
plt.legend(loc='upper left')
plt.xticks(y)
plt.yticks(z)
plt.title('Weekly sales data of each product in 2012')
plt.show()


# # Weekly Unit Sold, product wise, in 2010, 2011, and 2012

# In[178]:


df2 = df.groupby(['year', 'Product', 'week_of_year']).agg({'Weekly_Units_Sold':'sum'})
df2.reset_index(inplace=True)


# In[179]:


print(df2.year.value_counts())
print(df2.iloc[:123].Product.value_counts())                    #2010
print(df2.iloc[123:123+135].Product.value_counts())             #2011
print(df2.iloc[123+135:123+135+123].Product.value_counts())     #2012


# In[25]:


# Weekly Unit Sold, Product wise, in 2010

Week1  = df2['week_of_year'].iloc[0 : 41].tolist()
Week2  = df2['week_of_year'].iloc[41 : 41*2].tolist()
Week3  = df2['week_of_year'].iloc[41*2 : 41*3].tolist()

Sales1   = df2['Weekly_Units_Sold'].iloc[0 : 41].tolist()
Sales2   = df2['Weekly_Units_Sold'].iloc[41 : 41*2].tolist()
Sales3   = df2['Weekly_Units_Sold'].iloc[41*2 :41*3].tolist()

y = []
z = []
for i in range(1,53,3):
    y.append(i)
for i in range(0,12100,1500):
    z.append(i)

plt.plot(Week1, Sales1, label = 'Product 1 Sales')
plt.plot(Week2, Sales2, label = 'Product 2 Sales')
plt.plot(Week3, Sales3, label = 'Product 3 Sales')
plt.xlabel('Week Number')
plt.ylabel('Sales')
plt.legend(loc='upper left')
plt.xticks(y)
plt.yticks(z)
plt.title('Weekly unit sold data of each product in 2010')
plt.show()


# In[27]:


# Weekly Unit Sold, Product wise, in 2011

Week1  = df2['week_of_year'].iloc[41*3 : 123+45].tolist()
Week2  = df2['week_of_year'].iloc[123+45 : 123+45+45].tolist()
Week3  = df2['week_of_year'].iloc[123+45+45 : 123+45+45+45].tolist()

Sales1   = df2['Weekly_Units_Sold'].iloc[41*3 : 123+45].tolist()
Sales2   = df2['Weekly_Units_Sold'].iloc[123+45 : 123+45+45].tolist()
Sales3   = df2['Weekly_Units_Sold'].iloc[123+45+45 : 123+45+45+45].tolist()

y = []
z = []
for i in range(1,53,3):
    y.append(i)
for i in range(0,12100,1500):
    z.append(i)

plt.plot(Week1, Sales1, label = 'Product 1 Sales')
plt.plot(Week2, Sales2, label = 'Product 2 Sales')
plt.plot(Week3, Sales3, label = 'Product 3 Sales')
plt.xlabel('Week Number')
plt.ylabel('Sales')
plt.legend(loc='upper left')
plt.xticks(y)
plt.yticks(z)
plt.title('Weekly unit sold data of each product in 2011')
plt.show()


# In[28]:


# Weekly Unit Sold, Product wise, in 2012

Week1  = df2['week_of_year'].iloc[123+45+45+45 : 123+(45*3)+41].tolist()
Week2  = df2['week_of_year'].iloc[123+(45*3)+41 : 123+(45*3)+(41*2)].tolist()
Week3  = df2['week_of_year'].iloc[123+(45*3)+(41*2) : 123+(45*3)+(41*3)].tolist()

Sales1   = df2['Weekly_Units_Sold'].iloc[123+45+45+45 : 123+(45*3)+41].tolist()
Sales2   = df2['Weekly_Units_Sold'].iloc[123+(45*3)+41 : 123+(45*3)+(41*2)].tolist()
Sales3   = df2['Weekly_Units_Sold'].iloc[123+(45*3)+(41*2) : 123+(45*3)+(41*3)].tolist()

y = []
z = []
for i in range(1,53,3):
    y.append(i)
for i in range(0,10600,1500):
    z.append(i)

plt.plot(Week1, Sales1, label = 'Product 1 Sales')
plt.plot(Week2, Sales2, label = 'Product 2 Sales')
plt.plot(Week3, Sales3, label = 'Product 3 Sales')
plt.xlabel('Week Number')
plt.ylabel('Sales')
plt.legend(loc='upper left')
plt.xticks(y)
plt.yticks(z)
plt.title('Weekly unit sold data of each product in 2012')
plt.show()


# # Monthly sales, store wise, in 2010, 2011, and 2012

# In[180]:


df3 = df.groupby(['year','Store','month']).agg({'Sales':'sum'})
df3.reset_index(inplace=True)


# In[181]:


print(df3.year.value_counts())
print(df3.iloc[:108].Store.value_counts())          #2010
print(df3.iloc[108:108*2].Store.value_counts())     #2011
print(df3.iloc[108*2:108*3].Store.value_counts())   #2012


# In[31]:


#Monthly sale, store-wise, in 2010

Month1  = df3['month'].iloc[:12].tolist()
Month2  = df3['month'].iloc[12:12*2].tolist()
Month3  = df3['month'].iloc[12*2:12*3].tolist()
Month4  = df3['month'].iloc[12*3:12*4].tolist()
Month5  = df3['month'].iloc[12*4:12*5].tolist()
Month6  = df3['month'].iloc[12*5:12*6].tolist()
Month7  = df3['month'].iloc[12*6:12*7].tolist()
Month8  = df3['month'].iloc[12*7:12*8].tolist()
Month9  = df3['month'].iloc[12*8:12*9].tolist()

Monthly_Sales1   = df3['Sales'].iloc[:12].tolist()
Monthly_Sales2   = df3['Sales'].iloc[12:12*2].tolist()
Monthly_Sales3   = df3['Sales'].iloc[12*2:12*3].tolist()
Monthly_Sales4   = df3['Sales'].iloc[12*3:12*4].tolist()
Monthly_Sales5   = df3['Sales'].iloc[12*4:12*5].tolist()
Monthly_Sales6   = df3['Sales'].iloc[12*5:12*6].tolist()
Monthly_Sales7   = df3['Sales'].iloc[12*6:12*7].tolist()
Monthly_Sales8   = df3['Sales'].iloc[12*7:12*8].tolist()
Monthly_Sales9   = df3['Sales'].iloc[12*8:12*9].tolist()

y = []
z = []
for i in range(1,13):
    y.append(i)
for i in range(1000,110000,15000):
    z.append(i)

plt.plot(Month1, Monthly_Sales1, label = 'Store 1 Sales')
plt.plot(Month2, Monthly_Sales2, label = 'Store 2 Sales')
plt.plot(Month3, Monthly_Sales3, label = 'Store 3 Sales')
plt.plot(Month4, Monthly_Sales4, label = 'Store 4 Sales')
plt.plot(Month5, Monthly_Sales5, label = 'Store 5 Sales')
plt.plot(Month6, Monthly_Sales6, label = 'Store 6 Sales')
plt.plot(Month7, Monthly_Sales7, label = 'Store 7 Sales')
plt.plot(Month8, Monthly_Sales8, label = 'Store 8 Sales')
plt.plot(Month9, Monthly_Sales9, label = 'Store 9 Sales')
plt.xlabel('Month Number')
plt.ylabel('Sales')
plt.legend(loc='upper left')
plt.xticks(y)
plt.yticks(z)
plt.title('Monthly sales data of each store in 2010')
plt.show()


# In[32]:


#Monthly sale, store wise, in 2011

Month1  = df3['month'].iloc[12*9:12*10].tolist()
Month2  = df3['month'].iloc[12*10:12*11].tolist()
Month3  = df3['month'].iloc[12*11:12*12].tolist()
Month4  = df3['month'].iloc[12*12:12*13].tolist()
Month5  = df3['month'].iloc[12*13:12*14].tolist()
Month6  = df3['month'].iloc[12*14:12*15].tolist()
Month7  = df3['month'].iloc[12*15:12*16].tolist()
Month8  = df3['month'].iloc[12*16:12*17].tolist()
Month9  = df3['month'].iloc[12*17:12*18].tolist()

Monthly_Sales1   = df3['Sales'].iloc[12*9:12*10].tolist()
Monthly_Sales2   = df3['Sales'].iloc[12*10:12*11].tolist()
Monthly_Sales3   = df3['Sales'].iloc[12*11:12*12].tolist()
Monthly_Sales4   = df3['Sales'].iloc[12*12:12*13].tolist()
Monthly_Sales5   = df3['Sales'].iloc[12*13:12*14].tolist()
Monthly_Sales6   = df3['Sales'].iloc[12*14:12*15].tolist()
Monthly_Sales7   = df3['Sales'].iloc[12*15:12*16].tolist()
Monthly_Sales8   = df3['Sales'].iloc[12*16:12*17].tolist()
Monthly_Sales9   = df3['Sales'].iloc[12*17:12*18].tolist()

y = []
z = []
for i in range(1,13):
    y.append(i)
for i in range(1000,110000,15000):
    z.append(i)

plt.plot(Month1, Monthly_Sales1, label = 'Store 1 Sales')
plt.plot(Month2, Monthly_Sales2, label = 'Store 2 Sales')
plt.plot(Month3, Monthly_Sales3, label = 'Store 3 Sales')
plt.plot(Month4, Monthly_Sales4, label = 'Store 4 Sales')
plt.plot(Month5, Monthly_Sales5, label = 'Store 5 Sales')
plt.plot(Month6, Monthly_Sales6, label = 'Store 6 Sales')
plt.plot(Month7, Monthly_Sales7, label = 'Store 7 Sales')
plt.plot(Month8, Monthly_Sales8, label = 'Store 8 Sales')
plt.plot(Month9, Monthly_Sales9, label = 'Store 9 Sales')
plt.xlabel('Month Number')
plt.ylabel('Sales')
plt.legend(loc='upper left')
plt.xticks(y)
plt.yticks(z)
plt.title('Monthly sales data of each store in 2011')
plt.show()


# In[33]:


#Monthly sale, store wise, in 2012

Month1  = df3['month'].iloc[12*18:12*19].tolist()
Month2  = df3['month'].iloc[12*19:12*20].tolist()
Month3  = df3['month'].iloc[12*20:12*21].tolist()
Month4  = df3['month'].iloc[12*21:12*22].tolist()
Month5  = df3['month'].iloc[12*22:12*23].tolist()
Month6  = df3['month'].iloc[12*23:12*24].tolist()
Month7  = df3['month'].iloc[12*24:12*25].tolist()
Month8  = df3['month'].iloc[12*25:12*26].tolist()
Month9  = df3['month'].iloc[12*26:12*27].tolist()

Monthly_Sales1   = df3['Sales'].iloc[12*18:12*19].tolist()
Monthly_Sales2   = df3['Sales'].iloc[12*19:12*20].tolist()
Monthly_Sales3   = df3['Sales'].iloc[12*20:12*21].tolist()
Monthly_Sales4   = df3['Sales'].iloc[12*21:12*22].tolist()
Monthly_Sales5   = df3['Sales'].iloc[12*22:12*23].tolist()
Monthly_Sales6   = df3['Sales'].iloc[12*23:12*24].tolist()
Monthly_Sales7   = df3['Sales'].iloc[12*24:12*25].tolist()
Monthly_Sales8   = df3['Sales'].iloc[12*25:12*26].tolist()
Monthly_Sales9   = df3['Sales'].iloc[12*26:12*27].tolist()

y = []
z = []
for i in range(1,13):
    y.append(i)
for i in range(1000,110000,15000):
    z.append(i)

plt.plot(Month1, Monthly_Sales1, label = 'Store 1 Sales')
plt.plot(Month2, Monthly_Sales2, label = 'Store 2 Sales')
plt.plot(Month3, Monthly_Sales3, label = 'Store 3 Sales')
plt.plot(Month4, Monthly_Sales4, label = 'Store 4 Sales')
plt.plot(Month5, Monthly_Sales5, label = 'Store 5 Sales')
plt.plot(Month6, Monthly_Sales6, label = 'Store 6 Sales')
plt.plot(Month7, Monthly_Sales7, label = 'Store 7 Sales')
plt.plot(Month8, Monthly_Sales8, label = 'Store 8 Sales')
plt.plot(Month9, Monthly_Sales9, label = 'Store 9 Sales')
plt.xlabel('Month Number')
plt.ylabel('Sales')
plt.legend(loc='upper left')
plt.xticks(y)
plt.yticks(z)
plt.title('Monthly sales data of each store in 2012')
plt.show()


# # Monthly unit sold, store wise, in 2010, 2011, and 2012

# In[182]:


df3 = df.groupby(['year','Store','month']).agg({'Weekly_Units_Sold':'sum'})
df3.reset_index(inplace=True)


# In[183]:


print(df3.year.value_counts())
print(df3.iloc[:108].Store.value_counts())          #2010
print(df3.iloc[108:108*2].Store.value_counts())     #2011
print(df3.iloc[108*2:108*3].Store.value_counts())   #2012


# In[36]:


# Monthly unit sold, store wise, in 2010

Month1  = df3['month'].iloc[:12].tolist()
Month2  = df3['month'].iloc[12:12*2].tolist()
Month3  = df3['month'].iloc[12*2:12*3].tolist()
Month4  = df3['month'].iloc[12*3:12*4].tolist()
Month5  = df3['month'].iloc[12*4:12*5].tolist()
Month6  = df3['month'].iloc[12*5:12*6].tolist()
Month7  = df3['month'].iloc[12*6:12*7].tolist()
Month8  = df3['month'].iloc[12*7:12*8].tolist()
Month9  = df3['month'].iloc[12*8:12*9].tolist()

Monthly_Sales1   = df3['Weekly_Units_Sold'].iloc[:12].tolist()
Monthly_Sales2   = df3['Weekly_Units_Sold'].iloc[12:12*2].tolist()
Monthly_Sales3   = df3['Weekly_Units_Sold'].iloc[12*2:12*3].tolist()
Monthly_Sales4   = df3['Weekly_Units_Sold'].iloc[12*3:12*4].tolist()
Monthly_Sales5   = df3['Weekly_Units_Sold'].iloc[12*4:12*5].tolist()
Monthly_Sales6   = df3['Weekly_Units_Sold'].iloc[12*5:12*6].tolist()
Monthly_Sales7   = df3['Weekly_Units_Sold'].iloc[12*6:12*7].tolist()
Monthly_Sales8   = df3['Weekly_Units_Sold'].iloc[12*7:12*8].tolist()
Monthly_Sales9   = df3['Weekly_Units_Sold'].iloc[12*8:12*9].tolist()

y = []
z = []
for i in range(1,13):
    y.append(i)
for i in range(0,13100,1000):
    z.append(i)

plt.plot(Month1, Monthly_Sales1, label = 'Store 1 Sales')
plt.plot(Month2, Monthly_Sales2, label = 'Store 2 Sales')
plt.plot(Month3, Monthly_Sales3, label = 'Store 3 Sales')
plt.plot(Month4, Monthly_Sales4, label = 'Store 4 Sales')
plt.plot(Month5, Monthly_Sales5, label = 'Store 5 Sales')
plt.plot(Month6, Monthly_Sales6, label = 'Store 6 Sales')
plt.plot(Month7, Monthly_Sales7, label = 'Store 7 Sales')
plt.plot(Month8, Monthly_Sales8, label = 'Store 8 Sales')
plt.plot(Month9, Monthly_Sales9, label = 'Store 9 Sales')
plt.xlabel('Month Number')
plt.ylabel('Sales')
plt.legend(loc='upper left')
plt.xticks(y)
plt.yticks(z)
plt.title('Monthly unit sold data of each store in 2010')
plt.show()


# In[37]:


# Monthly unit sold, store wise, in 2011

Month1  = df3['month'].iloc[12*9:12*10].tolist()
Month2  = df3['month'].iloc[12*10:12*11].tolist()
Month3  = df3['month'].iloc[12*11:12*12].tolist()
Month4  = df3['month'].iloc[12*12:12*13].tolist()
Month5  = df3['month'].iloc[12*13:12*14].tolist()
Month6  = df3['month'].iloc[12*14:12*15].tolist()
Month7  = df3['month'].iloc[12*15:12*16].tolist()
Month8  = df3['month'].iloc[12*16:12*17].tolist()
Month9  = df3['month'].iloc[12*17:12*18].tolist()

Monthly_Sales1   = df3['Weekly_Units_Sold'].iloc[12*9:12*10].tolist()
Monthly_Sales2   = df3['Weekly_Units_Sold'].iloc[12*10:12*11].tolist()
Monthly_Sales3   = df3['Weekly_Units_Sold'].iloc[12*11:12*12].tolist()
Monthly_Sales4   = df3['Weekly_Units_Sold'].iloc[12*12:12*13].tolist()
Monthly_Sales5   = df3['Weekly_Units_Sold'].iloc[12*13:12*14].tolist()
Monthly_Sales6   = df3['Weekly_Units_Sold'].iloc[12*14:12*15].tolist()
Monthly_Sales7   = df3['Weekly_Units_Sold'].iloc[12*15:12*16].tolist()
Monthly_Sales8   = df3['Weekly_Units_Sold'].iloc[12*16:12*17].tolist()
Monthly_Sales9   = df3['Weekly_Units_Sold'].iloc[12*17:12*18].tolist()

y = []
z = []
for i in range(1,13):
    y.append(i)
for i in range(0,13100,1000):
    z.append(i)

plt.plot(Month1, Monthly_Sales1, label = 'Store 1 Sales')
plt.plot(Month2, Monthly_Sales2, label = 'Store 2 Sales')
plt.plot(Month3, Monthly_Sales3, label = 'Store 3 Sales')
plt.plot(Month4, Monthly_Sales4, label = 'Store 4 Sales')
plt.plot(Month5, Monthly_Sales5, label = 'Store 5 Sales')
plt.plot(Month6, Monthly_Sales6, label = 'Store 6 Sales')
plt.plot(Month7, Monthly_Sales7, label = 'Store 7 Sales')
plt.plot(Month8, Monthly_Sales8, label = 'Store 8 Sales')
plt.plot(Month9, Monthly_Sales9, label = 'Store 9 Sales')
plt.xlabel('Month Number')
plt.ylabel('Sales')
plt.legend(loc='upper left')
plt.xticks(y)
plt.yticks(z)
plt.title('Monthly unit sold data of each store in 2011')
plt.show()


# In[38]:


# Monthly unit sold, store wise, in 2012

Month1  = df3['month'].iloc[12*18:12*19].tolist()
Month2  = df3['month'].iloc[12*19:12*20].tolist()
Month3  = df3['month'].iloc[12*20:12*21].tolist()
Month4  = df3['month'].iloc[12*21:12*22].tolist()
Month5  = df3['month'].iloc[12*22:12*23].tolist()
Month6  = df3['month'].iloc[12*23:12*24].tolist()
Month7  = df3['month'].iloc[12*24:12*25].tolist()
Month8  = df3['month'].iloc[12*25:12*26].tolist()
Month9  = df3['month'].iloc[12*26:12*27].tolist()

Monthly_Sales1   = df3['Weekly_Units_Sold'].iloc[12*18:12*19].tolist()
Monthly_Sales2   = df3['Weekly_Units_Sold'].iloc[12*19:12*20].tolist()
Monthly_Sales3   = df3['Weekly_Units_Sold'].iloc[12*20:12*21].tolist()
Monthly_Sales4   = df3['Weekly_Units_Sold'].iloc[12*21:12*22].tolist()
Monthly_Sales5   = df3['Weekly_Units_Sold'].iloc[12*22:12*23].tolist()
Monthly_Sales6   = df3['Weekly_Units_Sold'].iloc[12*23:12*24].tolist()
Monthly_Sales7   = df3['Weekly_Units_Sold'].iloc[12*24:12*25].tolist()
Monthly_Sales8   = df3['Weekly_Units_Sold'].iloc[12*25:12*26].tolist()
Monthly_Sales9   = df3['Weekly_Units_Sold'].iloc[12*26:12*27].tolist()
y = []
z = []
for i in range(1,13):
    y.append(i)
for i in range(0,13100,1000):
    z.append(i)

plt.plot(Month1, Monthly_Sales1, label = 'Store 1 Sales')
plt.plot(Month2, Monthly_Sales2, label = 'Store 2 Sales')
plt.plot(Month3, Monthly_Sales3, label = 'Store 3 Sales')
plt.plot(Month4, Monthly_Sales4, label = 'Store 4 Sales')
plt.plot(Month5, Monthly_Sales5, label = 'Store 5 Sales')
plt.plot(Month6, Monthly_Sales6, label = 'Store 6 Sales')
plt.plot(Month7, Monthly_Sales7, label = 'Store 7 Sales')
plt.plot(Month8, Monthly_Sales8, label = 'Store 8 Sales')
plt.plot(Month9, Monthly_Sales9, label = 'Store 9 Sales')
plt.xlabel('Month Number')
plt.ylabel('Sales')
plt.legend(loc='upper left')
plt.xticks(y)
plt.yticks(z)
plt.title('Monthly unit sold data of each store in 2012')
plt.show()


# # Monthly sales, product wise, in 2010, 2011, and 2012

# In[184]:


df3 = df.groupby(['year','Product','month']).agg({'Sales':'sum'})
df3.reset_index(inplace=True)


# In[185]:


print(df3.year.value_counts())
print(df3.iloc[:36].Product.value_counts())
print(df3.iloc[36:36*2].Product.value_counts())
print(df3.iloc[36*2:36*3].Product.value_counts())


# In[41]:


#Monthly sale Product-wise in 2010

Month1  = df3['month'].iloc[:12].tolist()
Month2  = df3['month'].iloc[12:12*2].tolist()
Month3  = df3['month'].iloc[12*2:12*3].tolist()

Monthly_Sales1   = df3['Sales'].iloc[:12].tolist()
Monthly_Sales2   = df3['Sales'].iloc[12:12*2].tolist()
Monthly_Sales3   = df3['Sales'].iloc[12*2:12*3].tolist()

y = []
z = []
for i in range(1,13):
    y.append(i)
for i in range(1000,200000,20000):
    z.append(i)

plt.plot(Month1, Monthly_Sales1, label = 'Product 1 Sales')
plt.plot(Month2, Monthly_Sales2, label = 'Product 2 Sales')
plt.plot(Month3, Monthly_Sales3, label = 'Product 3 Sales')
plt.xlabel('Month Number')
plt.ylabel('Sales')
plt.legend(loc='upper left')
plt.xticks(y)
plt.yticks(z)
plt.title('Monthly sales data of each Product in 2010')
plt.show()


# In[42]:


#Monthly sale Product-wise in 2011

Month1  = df3['month'].iloc[12*3:12*4].tolist()
Month2  = df3['month'].iloc[12*4:12*5].tolist()
Month3  = df3['month'].iloc[12*5:12*6].tolist()

Monthly_Sales1   = df3['Sales'].iloc[12*3:12*4].tolist()
Monthly_Sales2   = df3['Sales'].iloc[12*4:12*5].tolist()
Monthly_Sales3   = df3['Sales'].iloc[12*5:12*6].tolist()

y = []
z = []
for i in range(1,13):
    y.append(i)
for i in range(21000,200000,20000):
    z.append(i)

plt.plot(Month1, Monthly_Sales1, label = 'Product 1 Sales')
plt.plot(Month2, Monthly_Sales2, label = 'Product 2 Sales')
plt.plot(Month3, Monthly_Sales3, label = 'Product 3 Sales')
plt.xlabel('Month Number')
plt.ylabel('Sales')
plt.legend(loc='upper left')
plt.xticks(y)
plt.yticks(z)
plt.title('Monthly sales data of each Product in 2011')
plt.show()


# In[43]:


#Monthly sale Product-wise in 2012

Month1  = df3['month'].iloc[12*6:12*7].tolist()
Month2  = df3['month'].iloc[12*7:12*8].tolist()
Month3  = df3['month'].iloc[12*8:12*9].tolist()

Monthly_Sales1   = df3['Sales'].iloc[12*6:12*7].tolist()
Monthly_Sales2   = df3['Sales'].iloc[12*7:12*8].tolist()
Monthly_Sales3   = df3['Sales'].iloc[12*8:12*9].tolist()

y = []
z = []
for i in range(1,13):
    y.append(i)
for i in range(1000,200000,20000):
    z.append(i)

plt.plot(Month1, Monthly_Sales1, label = 'Product 1 Sales')
plt.plot(Month2, Monthly_Sales2, label = 'Product 2 Sales')
plt.plot(Month3, Monthly_Sales3, label = 'Product 3 Sales')
plt.xlabel('Month Number')
plt.ylabel('Sales')
plt.legend(loc='upper left')
plt.xticks(y)
plt.yticks(z)
plt.title('Monthly sales data of each Product in 2012')
plt.show()


# # Monthly unit sold, product wise, in 2010, 2011, and 2012

# In[186]:


df3 = df.groupby(['year','Product','month']).agg({'Weekly_Units_Sold':'sum'})
df3.reset_index(inplace=True)


# In[45]:


#Monthly unit sold, product wise, in 2010

Month1  = df3['month'].iloc[:12].tolist()
Month2  = df3['month'].iloc[12:12*2].tolist()
Month3  = df3['month'].iloc[12*2:12*3].tolist()

Monthly_Sales1   = df3['Weekly_Units_Sold'].iloc[:12].tolist()
Monthly_Sales2   = df3['Weekly_Units_Sold'].iloc[12:12*2].tolist()
Monthly_Sales3   = df3['Weekly_Units_Sold'].iloc[12*2:12*3].tolist()

y = []
z = []
for i in range(1,13):
    y.append(i)
for i in range(1000,20000,2000):
    z.append(i)

plt.plot(Month1, Monthly_Sales1, label = 'Product 1 Sales')
plt.plot(Month2, Monthly_Sales2, label = 'Product 2 Sales')
plt.plot(Month3, Monthly_Sales3, label = 'Product 3 Sales')
plt.xlabel('Month Number')
plt.ylabel('Sales')
plt.legend(loc='upper left')
plt.xticks(y)
plt.yticks(z)
plt.title('Monthly unit sold data of each Product in 2010')
plt.show()


# In[47]:


#Monthly unit sold, product wise, in 2011

Month1  = df3['month'].iloc[12*3:12*4].tolist()
Month2  = df3['month'].iloc[12*4:12*5].tolist()
Month3  = df3['month'].iloc[12*5:12*6].tolist()

Monthly_Sales1   = df3['Weekly_Units_Sold'].iloc[12*3:12*4].tolist()
Monthly_Sales2   = df3['Weekly_Units_Sold'].iloc[12*4:12*5].tolist()
Monthly_Sales3   = df3['Weekly_Units_Sold'].iloc[12*5:12*6].tolist()

y = []
z = []
for i in range(1,13):
    y.append(i)
for i in range(1000,26100,2000):
    z.append(i)

plt.plot(Month1, Monthly_Sales1, label = 'Product 1 Sales')
plt.plot(Month2, Monthly_Sales2, label = 'Product 2 Sales')
plt.plot(Month3, Monthly_Sales3, label = 'Product 3 Sales')
plt.xlabel('Month Number')
plt.ylabel('Sales')
plt.legend(loc='upper right')
plt.xticks(y)
plt.yticks(z)
plt.title('Monthly unit sold data of each Product in 2011')
plt.show()


# In[48]:


#Monthly unit sold, product wise, in 2012

Month1  = df3['month'].iloc[12*6:12*7].tolist()
Month2  = df3['month'].iloc[12*7:12*8].tolist()
Month3  = df3['month'].iloc[12*8:12*9].tolist()

Monthly_Sales1   = df3['Weekly_Units_Sold'].iloc[12*6:12*7].tolist()
Monthly_Sales2   = df3['Weekly_Units_Sold'].iloc[12*7:12*8].tolist()
Monthly_Sales3   = df3['Weekly_Units_Sold'].iloc[12*8:12*9].tolist()

y = []
z = []
for i in range(1,13):
    y.append(i)
for i in range(1000,26100,2000):
    z.append(i)

plt.plot(Month1, Monthly_Sales1, label = 'Product 1 Sales')
plt.plot(Month2, Monthly_Sales2, label = 'Product 2 Sales')
plt.plot(Month3, Monthly_Sales3, label = 'Product 3 Sales')
plt.xlabel('Month Number')
plt.ylabel('Sales')
plt.legend(loc='upper right')
plt.xticks(y)
plt.yticks(z)
plt.title('Monthly unit sold data of each Product in 2012')
plt.show()


# # Analysing Holidays

# In[49]:


plt.figure(figsize=(12,7))
sns.catplot(x='Product', y='Price', col='Is_Holiday', kind="bar", data=df)


# In[50]:


plt.figure(figsize=(12,7))
sns.catplot(x='Product', y='Weekly_Units_Sold', col='Is_Holiday', kind="bar", data=df)


# In[52]:


plt.figure(figsize=(12,7))
sns.catplot(x='Product', y='Sales', col='Is_Holiday', kind="bar", data=df)


# In[53]:


g = sns.PairGrid(df, y_vars=["Weekly_Units_Sold"], x_vars=["Price", "Is_Holiday"], height=4)
g.map(sns.regplot, color=".3")


# In[54]:


g = sns.FacetGrid(df, row="Is_Holiday", height=1.7, aspect=4)
g.map(sns.distplot, "Weekly_Units_Sold", rug=True)


# In[55]:


sns.factorplot(data= df,  x= 'Is_Holiday', y= 'Weekly_Units_Sold', hue= 'Product')


# In[56]:


g = sns.FacetGrid(df, col="Product", row="Is_Holiday", margin_titles=True, height=3)
g.map(plt.scatter, "Price", "Weekly_Units_Sold", color="#338844", edgecolor="white", s=50, lw=1)
g.set(xlim=(0, 30), ylim=(0, 2600))


# In[57]:


sns.factorplot(data= df, x= 'Is_Holiday', y= 'Weekly_Units_Sold', hue= 'Store')


# In[58]:


g = sns.FacetGrid(df, col="Store", hue="Product", margin_titles=True, col_wrap=3)
g.map(plt.scatter, 'Price', 'Weekly_Units_Sold', alpha=.7)
g.add_legend()


# In[59]:


g = sns.FacetGrid(df, row ='Store', col ='Is_Holiday', height=4, aspect=.8)
g.map(sns.barplot, "Product", "Weekly_Units_Sold")


# In[188]:


df1 = df.groupby(['year','Store','month']).agg({'Weekly_Units_Sold':'sum'})
df1.reset_index(inplace=True)
df1.year.value_counts()


# In[61]:


#2010
g = sns.FacetGrid(df1.iloc[0:108], col="Store", col_wrap=3, height=3, ylim=(0, 15000))
g.map(sns.pointplot, "month", "Weekly_Units_Sold", color=".3", ci=None, order = [1,2,3,4,5,6,7,8,9,10,11,12])


# In[62]:


#2011
g = sns.FacetGrid(df1.iloc[108:108*2], col="Store", col_wrap=3, height=3, ylim=(0, 15000))
g.map(sns.pointplot, "month", "Weekly_Units_Sold", color=".3", ci=None, order = [1,2,3,4,5,6,7,8,9,10,11,12])


# In[63]:


#2012
g = sns.FacetGrid(df1.iloc[108*2:108*3], col="Store", col_wrap=3, height=3, ylim=(0, 14000))
g.map(sns.pointplot, "month", "Weekly_Units_Sold", color=".3", ci=None, order = [1,2,3,4,5,6,7,8,9,10,11,12])


# In[190]:


#df1 = pd.read_csv("Product-wise monthly unit sales.csv")
df1A = df.groupby(['year','Product','month']).agg({'Weekly_Units_Sold':'sum'})
df1A.reset_index(inplace=True)
df1A.year.value_counts()


# In[65]:


#2010
g = sns.FacetGrid(df1.iloc[0:36], col="Product", col_wrap=3, height=3, ylim=(0, 25000))
g.map(sns.pointplot, "month", "Weekly_Units_Sold", color=".3", ci=None, order = [1,2,3,4,5,6,7,8,9,10,11,12])


# In[66]:


#2011
g = sns.FacetGrid(df1.iloc[36:36*2], col="Product", col_wrap=3, height=3, ylim=(0, 30000))
g.map(sns.pointplot, "month", "Weekly_Units_Sold", color=".3", ci=None, order = [1,2,3,4,5,6,7,8,9,10,11,12])


# In[67]:


#2012
g = sns.FacetGrid(df1.iloc[36*2:36*3], col="Product", col_wrap=3, height=3, ylim=(0, 25000))
g.map(sns.pointplot, "month", "Weekly_Units_Sold", color=".3", ci=None, order = [1,2,3,4,5,6,7,8,9,10,11,12])


# In[191]:


df1 = df.groupby(['year', 'month', 'Store', 'Product']).agg({'Weekly_Units_Sold':'sum'})
df1.reset_index(inplace=True)
print(df1.year.value_counts())


# In[78]:


g = sns.FacetGrid(df1.iloc[:324], col="Store", col_wrap=3, height=3, ylim=(0, 7000), hue='Product', palette="Set1")
g.map(sns.pointplot, "month", "Weekly_Units_Sold", ci=None, order = [1,2,3,4,5,6,7,8,9,10,11,12], alpha=.7)
g.add_legend()


# In[79]:


g = sns.FacetGrid(df1.iloc[324*1:324*2], col="Store", col_wrap=3, height=3, ylim=(0, 7000), hue='Product', palette="Set1")
g.map(sns.pointplot, "month", "Weekly_Units_Sold", ci=None, order = [1,2,3,4,5,6,7,8,9,10,11,12], alpha=.7)
g.add_legend()


# In[83]:


g = sns.FacetGrid(df1.iloc[324*2:324*3], col="Store", col_wrap=3, height=3, ylim=(0, 8000), hue='Product', palette="Set1")
g.map(sns.pointplot, "month", "Weekly_Units_Sold", ci=None, order = [1,2,3,4,5,6,7,8,9,10,11,12], alpha=.7)
g.add_legend()


# In[84]:


sns.factorplot(data= df, x= 'promotion', y= 'Weekly_Units_Sold', hue= 'Store')


# In[85]:


sns.factorplot(data= df, x= 'promotion', y= 'Weekly_Units_Sold', hue= 'Product')


# In[86]:


g = sns.FacetGrid(df, col="Store", hue="promotion", row='promotion')
g.map(plt.scatter, "Price", "Weekly_Units_Sold").add_legend()


# In[87]:


g = sns.FacetGrid(df, hue="promotion", col="Product", row='promotion', height=4)
g.map(plt.scatter, "Price", "Weekly_Units_Sold").add_legend()


# # Seasonality

# ## Seasonality Store wise

# In[7]:


df1A = df.groupby(['Store','Date']).agg({'Sales':'sum'})
df1A.reset_index(inplace=True)
df1A.set_index('Date',inplace=True)


# In[9]:


df1A.Store.value_counts()


# In[12]:


print("Store 1 seasonality")
result= seasonal_decompose(df1A.iloc[0:143].Sales, period=4)
result.plot()


# In[13]:


print("Store 2 seasonality")
result= seasonal_decompose(df1A.iloc[143*1:143*2].Sales, period=7)
result.plot()


# In[17]:


print("Store 3 seasonality")
result= seasonal_decompose(df1A.iloc[143*2:143*3].Sales, period=5)
result.plot()


# In[18]:


print("Store 4 seasonality")
result= seasonal_decompose(df1A.iloc[143*3:143*4].Sales, period=7)
result.plot()


# In[19]:

print("Store 5 seasonality")
result= seasonal_decompose(df1A.iloc[143*4:143*5].Sales, period=7)
result.plot()
storeNo=4
df1A.query('Store==4').Sales
df1A.query('Store==@storeNo').Sales  
seasonal_decompose(df1A.query('Store==@storeNo').Sales , period=7).plot()

storeNo=5
seasonal_decompose(df1A.query('Store==@storeNo').Sales , period=7).plot()
plt.title(label="Store No " + str(storeNo), fontsize=20, color="green")


# In[20]:


print("Store 6 seasonality")
result= seasonal_decompose(df1.iloc[143*5:143*6].Sales, period=7)
result.plot()
storeNo=6
seasonal_decompose(df1A.query('Store==@storeNo').Sales , period=7).plot()
plt.title(label="Store No " + str(storeNo), fontsize=20, color="green")

# In[25]:


print("Store 7 seasonality")
result= seasonal_decompose(df1.iloc[143*6:143*7].Sales, period=7)
result.plot()


# In[22]:


print("Store 8 seasonality")
result= seasonal_decompose(df1.iloc[143*7:143*8].Sales, period=7)
result.plot()


# In[23]:


print("Store 9 seasonality")
result= seasonal_decompose(df1.iloc[143*8:143*9].Sales, period=7)
result.plot()


# ## Seasonality product wise

# In[26]:


df1 = df.groupby(['Product', 'Date']).agg({'Sales':'sum'})
df1.reset_index(inplace=True)
df1['Date'] = pd.to_datetime(df1['Date'])
df1.set_index('Date', inplace=True)
print(df1.Product.value_counts())


# In[27]:


print("Product 1 seasonality")
result= seasonal_decompose(df1.iloc[143*0:143*1].Sales, period=7)
result.plot()


# In[28]:


print("Product 2 seasonality")
result= seasonal_decompose(df1.iloc[143*1:143*2].Sales, period=7)
result.plot()


# In[29]:


print("Product 3 seasonality")
result= seasonal_decompose(df1.iloc[143*2:143*3].Sales, period=7)
result.plot()


# # Future Prediction using SARIMAX, product wise

# In[33]:


df1 = df.groupby(['Product','Date']).agg({'Sales':'sum'})
df1.reset_index(inplace=True)
df1['Date'] = pd.to_datetime(df1['Date'])
df1.set_index('Date', inplace=True)
df1.Product.value_counts()


# In[42]:


model = SARIMAX(df1.iloc[143*0:143*1].Sales, order = (0, 1, 3), seasonal_order =(0, 1, 3, 52))
result = model.fit()
pred = result.predict(start = 0, end = (len(df1.iloc[143*0:143*1])-1))
forecast =result.predict(start=len(df1.iloc[143*0:143*1])-1,end=len(df1.iloc[143*0:143*1])+35)
daterng=pd.date_range(start='2012-12-10',end='2016-01-10',freq='M')

plt.plot(df1.iloc[143*0:143*1].index, df1.iloc[143*0:143*1].Sales)
plt.plot(df1.iloc[143*0:143*1].index, pred)
plt.plot(daterng,forecast)


# In[35]:


model = SARIMAX(df1.iloc[143*1:143*2].Sales, order = (0, 1, 3), seasonal_order =(0, 1, 3, 52))
result = model.fit()
pred = result.predict(start = 0, end = (len(df1.iloc[143*1:143*2])-1))
forecast =result.predict(start=len(df1.iloc[143*1:143*2])-2,end=len(df1.iloc[143*1:143*2])+35)
daterng=pd.date_range(start='2012-11-10',end='2016-01-10',freq='M')

plt.plot(df1.iloc[143*1:143*2].index, df1.iloc[143*1:143*2].Sales)
plt.plot(df1.iloc[143*1:143*2].index, pred)
plt.plot(daterng,forecast)


# In[36]:


model = SARIMAX(df1.iloc[143*2:143*3].Sales, order = (0, 1, 3), seasonal_order =(0, 1, 3, 52))
result = model.fit()
pred = result.predict(start = 0, end = (len(df1.iloc[143*2:143*3])-1))
forecast =result.predict(start=len(df1.iloc[143*2:143*3])-2,end=len(df1.iloc[143*2:143*3])+35)
daterng=pd.date_range(start='2012-11-10',end='2016-01-10',freq='M')

plt.plot(df1.iloc[143*2:143*3].index, df1.iloc[143*2:143*3].Sales)
plt.plot(df1.iloc[143*2:143*3].index, pred)
plt.plot(daterng,forecast)


# In[ ]:




