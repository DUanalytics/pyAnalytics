#Pandas Filtering Data 
#-----------------------------
#%

from pydataset import data
mtcars = data('mtcars')
mtcars.head()

#loc
mtcars.loc['Mazda RX4', ]
mtcars.loc['Mazda RX4', 'cyl']
mtcars.loc['Mazda RX4', :]
mtcars.loc[['Mazda RX4','Datson 710'], ['cyl','gear']]
mtcars.loc[:, ('cyl','gear')]
#iloc

mtcars.iloc[1,]
mtcars.iloc[1, 2]
mtcars.iloc[1, 2:4]
mtcars.iloc[[1,2], 2:4]

#idx

idx = pd.IndexSlice
mtcars.loc[idx[:, 'Mazda RX4'], idx[:, 'cyl']]

#rows
mtcars.index
mtcars['Mazda RX4':'Datsun 710']
mtcars[0:3]


#columns



#isin
employees.loc[employees['Occupation'].isin(['Chemist','Programmer'])])
mtcars.gear.value_counts()
mtcars.loc[mtcars['gear'].isin([4,5])]
