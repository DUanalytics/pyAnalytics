#Pandas Panel Data - mtcars
#-----------------------------
from pydataset import data
mtcars = data('mtcars')
mtcars.head()

mtcars.values
mtcars.index
mtcars.columns
mtcars.dtypes
mtcars[['cyl','vs', 'am', 'gear','carb']] = mtcars[['cyl','vs', 'am', 'gear','carb']].astype('category')
data = mtcars.values
data
mtindexDF1 = pd.DataFrame({'TYPE':['NUMERIC','CATEGORY','NUMERIC', 'NUMERIC','NUMERIC', 'NUMERIC', 'NUMERIC', 'CATEGORY','CATEGORY', 'CATEGORY', 'CATEGORY' ], 'COLNAME': ['mpg', 'cyl','disp', 'hp', 'drat', 'wt', 'qsec', 'vs', 'am', 'gear','carb']}) 
mtindexDF1
mtindex1 = pd.MultiIndex.from_frame(mtindexDF1)
mtindex1
pdMTCARS1 = pd.DataFrame(data, columns=mtindex1)
pdMTCARS1.head(2)

pdMTCARS1(['TYPE', 'COLNAME']).sort_index.sort_values(['TYPE', 'COLNAME'], ascending=True, inplace=True)
pdMTCARS1.sort_index()
df = pdMTCARS1.sample(5)
#----
#DataFrame.sort_index(axis=0, level=None, ascending=True, inplace=False, kind=’quicksort’, na_position=’last’, sort_remaining=True, by=None)
#
df
df.sort_index(axis = 0)  #rownames
df.sort_index(axis = 1)   #columnames - level0 : CAT, NUM
# sorting based on column labels 
df.sort_index(axis = 1, level=1)  # Level 1 of column names- am, carb
df.sort_index(axis = 1, level=[1,0]).columns
df.query('mpg > 25')
df.swaplevel(0, 1, axis=1)  #levels in columns changed
df.reorder_levels([1,0], axis=1)
df

#https://pandas.pydata.org/pandas-docs/version/0.15/advanced.html
df.mean
df.mean(level=0)
df.mean(level=0, axis=1)
df.mean(level=1, axis=1)
df2 = pd.concat([df,df])
df2
df2.mean(level=1, axis=1)
df2.mean(level=0, axis=1)
df2.align(df, level=0)  #join
df.align(df, level=0) #show them together
df.align(df, level=1)
df.align(df, level=1, axis=0)
df.align(df, level=1, axis=1)
df
df.xs('disp', level='COLNAME', axis=1)
df.xs('NUMERIC', level='TYPE', axis=1)
df.xs('CATEGORY', level='TYPE', axis=1)
df.sort_index(axis=1)
df.sort_index(level=[1],axis=1)
df.sort_index(level=[0],axis=1)
df.sort_index(level=[0,1],axis=1)
df.sort_index(level=[1,0],axis=1)
df.loc[:,(slice(None),'am')]
df.loc[:,(slice(None),['vs','am'])]
df.loc[:,(slice('CATEGORY'),['vs','am'])]  #needs to be sorted
df.sort_index(level=[0,1],axis=1).loc[:,(slice('CATEGORY'),['vs','am'])]
#
df
df.xs(('NUMERIC', 'mpg'), level=('TYPE', 'COLNAME'), axis=1)
df.xs(('NUMERIC', 'hp'), level=('TYPE', 'COLNAME'), axis=1)
df.xs(('NUMERIC', 'am'), level=('TYPE', 'COLNAME'), axis=1)  #error

df.loc[(slice(None)),:]

df.columns = df.columns.droplevel()
df
df = pdMTCARS1.sample(5)
df.columns = [col[1] for col in df.columns]
df
df = pdMTCARS1.sample(5)
df
df.columns = ['_'.join(col) for col in df.columns]
df
#when some levels have empty levels
df = pdMTCARS1.sample(5)
df
df.columns = [col[0] if col[1] == '' else col[1] for col in df.columns]
df

df = pdMTCARS1.sample(5)
df
df = df.xs('CATEGORY', axis=1, drop_level=True)
df #only numeric left

#
df = pdMTCARS1.sample(5)
df
df.columns = [['mpg', 'cyl','disp', 'hp', 'drat', 'wt', 'qsec', 'vs', 'am', 'gear','carb']]
df

#
#A small trick using sum with level=1(work when level=1 is all unique)
df = pdMTCARS1.sample(5)
df.sum(level=1,axis=1)
df.columns=df.columns.get_level_values(1)
df
#
df = pdMTCARS1.sample(5)
df
df.droplevel(0, axis=1) 
#
df = pdMTCARS1.sample(5)
df
#
#sum by multiindex - columns
df.sum(axis=1)
df.sum(axis=0)
df
#df.groupby(level=0)['mpg'].sum().reset_index()
#df.groupby(['gear'], level=1, axis=1)['mpg','hp'].sum()
#df.groupby([['cyl','gear']]).sum()[['mpg']]

#------
#can we create index in random order
type2 = ['CATEGORY'] * 5 + ['NUMERIC']*6
type2
colname2 = ['cyl','vs', 'am', 'gear','carb'] + ['mpg','disp', 'hp', 'drat', 'wt', 'qsec']
colname2
mtindexDF2 = pd.DataFrame({'TYPE':type2,'COLNAME': colname2}) 
mtindexDF2
mtindex2 = pd.MultiIndex.from_frame(mtindexDF2)
mtindex2
data2 = mtcars[colname2].values
pdMTCARS2 = pd.DataFrame(data2, columns=mtindex2)
pdMTCARS2.head(2)

DF = pdMTCARS2.sample(5)
DF.xs(('NUMERIC', 'hp'), level=('TYPE', 'COLNAME'), axis=1)
DF.loc[:,(slice(None),['vs','am'])]
DF.xs('NUMERIC', level='TYPE', axis=1)
DF.xs('CATEGORY', level='TYPE', axis=1)

DF2 = DF.set_index('gear')
DF2.drop_levels()
DF.loc[(slice(1,7), ['mpg','hp']),:]
#DataFrame.set_index(self, keys, drop=True, append=False, inplace=False, verify_integrity=False)[source]


#The reason that the MultiIndex matters is that it can allow you to do grouping, selection, and reshaping operations as we will describe below and in subsequent areas of the documentation. As you will see in later sections, you can find yourself working with hierarchically-indexed data without creating a MultiIndex explicitly yourself. However, when loading data from a file, you may wish to generate your own MultiIndex when preparing the data set.
