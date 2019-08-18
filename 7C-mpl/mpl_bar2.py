# -*- coding: utf-8 -*-
#Created on Thu Jun 20 12:17:42 2019 : dhiraj@sony
#Grouped Bar Plot

from pydataset import data
mtcars = data('mtcars')
mtcars.head()

df = mtcars
df.columns

#which are category columns

#convert relevant columns to categories
catCols = ['cyl','gear', 'am','vs','carb']
df[catCols] = df[catCols].astype('category')
df.dtypes

#grouby one columns
df.groupby(by='gear', as_index=True)
df.groupby('gear').size()

df.groupby('gear').groups  #car into which gear group

gearGP1 = df.groupby('gear')
gearGP1
gearGP1.size()

#SQL Style 
gearGP2 = df.groupby(by='gear', as_index=False)
#instead of gear 3,4,5 we have now numbers 0,1,2
gearGP2
gearGP2.size()

gearGP2.first()  #first entries
df.head(3)

gearGP2.get_group(4)  #cars with gear4 , only1 


#rotate the view
gearGP2.size().plot.bar()
gearGP2.size().plot.barh()


#muli level Groups
gearGP3 = df.groupby(['gear','cyl'])
sum3 = gearGP3.size()
sum3.unstack()
sum3.unstack(fill_value=0)

type(sum3)
