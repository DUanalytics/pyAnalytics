#Time Series Case Study
#-----------------------------
#%

import warnings
import itertools
import numpy as np
import matplotlib.pyplot as plt
warnings.filterwarnings("ignore")
plt.style.use('fivethirtyeight')
import pandas as pd
import statsmodels.api as sm
import matplotlib
matplotlib.rcParams['axes.labelsize'] = 14
matplotlib.rcParams['xtick.labelsize'] = 12
matplotlib.rcParams['ytick.labelsize'] = 12
matplotlib.rcParams['text.color'] = 'k'

#%%
df = pd.read_excel("data/Superstore.xls")  #by default sheet1
df.head()
df.columns
df.shape
furniture = df.loc[df['Category'] == 'Furniture']
#only furniture 4 yr old data
furniture['Order Date'].min()
furniture['Order Date'].max()  #latest sale date

#Data Preprocessing - remove unwanted cols
cols = ['Row ID', 'Order ID', 'Ship Date', 'Ship Mode', 'Customer ID', 'Customer Name', 'Segment', 'Country', 'City', 'State', 'Postal Code', 'Region', 'Product ID', 'Category', 'Sub-Category', 'Product Name', 'Quantity', 'Discount', 'Profit']

furniture.drop(cols, axis=1, inplace=True)
furniture = furniture.sort_values('Order Date')
furniture.head() #order date, Sales Value, by order no
furniture.isnull().sum()  #no missing values

#%%
furniture = furniture.groupby('Order Date')['Sales'].sum().reset_index()
furniture.head()  #order no gone, group by date, sum the values
#create new index with Date data
#Indexing with Time Series Data

furniture = furniture.set_index('Order Date')
furniture.index
furniture.head()

#quick view of sample data
#https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.resample.html
y = furniture['Sales'].resample('MS').mean()
#'3T', MS - monthstart
y


#Visualise
y.plot(figsize=(15, 6))
plt.show()
#Some distinguishable patterns appear when we plot the data. The time-series has seasonality pattern, such as sales are always low at the beginning of the year and high at the end of the year. There is always an upward trend within any single year with a couple of low months in the mid of the year.


#
from pylab import rcParams
rcParams['figure.figsize'] = 18, 8
decomposition = sm.tsa.seasonal_decompose(y, model='additive')
fig = decomposition.plot()
plt.show()

#he plot above clearly shows that the sales of furniture is unstable, along with its obvious seasonality.


#ARIMA - practise
#https://towardsdatascience.com/an-end-to-end-project-on-time-series-analysis-and-forecasting-with-python-4835e6bf050b
