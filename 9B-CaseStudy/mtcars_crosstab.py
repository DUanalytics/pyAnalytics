# mtcars - Cross Tab
#%%%
import pandas as pd
import seaborn as sns
# Read in the CSV file and convert "?" to NaN
df1 = pd.read_csv('data\mtcars.csv')
df1.head()
df1.columns

#cross tab - two cols
pd.crosstab(df1.cyl, df1.gear)

#df1.pivot_table(index='cyl', columns='gear')
#with margin total
pd.crosstab(df1.cyl, df1.gear, margins=True, margins_name="Total")
pd.crosstab(df1.cyl, [df1.gear, df1.am])
#multiple cols - left and top: with col names
pd.crosstab([df1.cyl, df1.vs], [df1.gear, df1.am], rownames=['Cylinder', "Engine Type"], colnames=['Gear', "Transmission Type"],  dropna=False)

xtab1 = pd.crosstab([df1.cyl, df1.vs], [df1.gear, df1.am], rownames=['Cylinder', "Engine Type"], colnames=['Gear', "Transmission Type"],  dropna=False)
xtab1


#heat map - which car are more 
sns.heatmap(xtab1,  cmap="YlGnBu", annot=True, cbar=False)


#another way
#pd.crosstab(a, [b, c], rownames=['a'], colnames=['b', 'c'])
df1.columns
xtab2 = pd.crosstab(df1.gear, [df1.am, df1.vs], rownames=['GEAR'], colnames=['AM','VS'])
sns.heatmap(xtab2,  cmap="YlGnBu", annot=True, cbar=False)

#https://pandas.pydata.org/pandas-docs/version/0.23.4/generated/pandas.crosstab.html
pandas.crosstab(index, columns, values=None, rownames=None, colnames=None, aggfunc=None, margins=False, margins_name='All', dropna=True, normalize=False)[source]
