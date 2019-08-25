#Basic statistics on MT Cars
import pandas as pd
import numpy as np

#read data
#df = pd.read_csv('data/mtcars.csv')
from pydataset import data
mtcars = data('mtcars')
mtcars.head()
df=mtcars
df.describe()
df.dtypes()
#data distributions for 
df.columns

#%%% =========================================
# #Skewness: It represents the shape of the distribution.
#Skewness can be quantified to define the extent to which a distribution differs from a normal distribution.
#For calculating skewness by using df.skew() python inbuilt function.

df.mpg
df.mpg.skew()  #positive : right skewed
df.mpg.plot(kind='hist')
df.mpg.plot(kind='density')
df.wt.plot(kind='density')
#%%%
#Kurtosis: Kurtosis is the measure of thickness or heaviness of the given distribution.#Its actually represents the height of the distribution.
#The distribution with kurtosis equal to 3 is known as mesokurtic. A random variable which follows normal distribution has kurtosis 3.
#If the kurtosis is less than three, the distribution is called as platykurtic. Here,the distribution has shorter and thinner tails than normal distribution.
#If the kurtosis is greater than three, the distribution is called as leptykurtic. Here, the distribution has longer and fatter tails than normal distribution.
#For calculating kurtosis by using df.kurtosis() python inbuilt function.
# ========

df.kurtosis()
df.mpg.plot(kind='hist')
df.mpg.plot(kind='density')

df.mpg.kurtosis()

#end 

df["mpg"].plot.kde() 
df["mpg"].plot.kde(bw_method=0.5)# bandwidth
df["mpg"].plot.kde(bw_method=0.1) 
df[["wt", "mpg"]].plot.kde()
# next 2 lines together: hist normed-True
df["mpg"].plot.kde()
df["mpg"].plot.hist(normed=True) # Histogram will now be normalized

fig, 
df.dtypes
#All columns
fig = plt.figure(figsize=(10, 6))
plt.subplot(2, 2, 1) # matrix of 2 x 2 plots : first plot
df["mpg"].plot.kde() 
plt.title('Mileage')
plt.subplot(2, 2, 2) # matrix of 2 x 2 plots : 2nd plot
df.wt.plot.kde() 
plt.title('Weight')
plt.subplot(2, 2, 3) # matrix of 2 x 2 plots : 3nd plot
df.hp.plot.kde() 
plt.title('Horse Power')
plt.subplot(2, 2, 4) # matrix of 2 x 2 plots : 4th plot
df["disp"].plot.kde() 
plt.title('Displacement')
plt.show();


#pd.melt(df, id_vars=['A'], value_vars=['B'])
df2 = pd.melt(df)
import seaborn as sns
g = sns.FacetGrid(df2)
g = g.map(plt.hist)