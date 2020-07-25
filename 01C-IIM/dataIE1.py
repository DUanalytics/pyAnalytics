#Topic: Import data from URL and Gsheet
#-----------------------------
#libraries
#https://pandas.pydata.org/Pandas_Cheat_Sheet.pdf


import pandas as pd
#link https://docs.google.com/spreadsheets/d/1X2AjCyh1Kcs-CA8ilGZyBZBobuFP7cSS9D-3a5LK6sk/edit#gid=1858159025

student = pd.read_csv('https://docs.google.com/spreadsheets/d/1X2AjCyh1Kcs-CA8ilGZyBZBobuFP7cSS9D-3a5LK6sk' + '/export?gid=1858159025&format=csv',  index_col=0 )
student.head(5)
student.shape
type(student)

student.columns

#CSV file in web
#link https://raw.githubusercontent.com/DUanalytics/datasets/master/csv/salesdata.csv

pd.read_csv?
sales = pd.DataFrame(pd.read_csv('https://raw.githubusercontent.com/DUanalytics/datasets/master/csv/salesdata.csv', index_col=None))
sales.head(5)
sales.shape
type(sales)

sales.columns

sales.groupby('month')['sales'].agg('mean')

sales.head()
sales2 = sales.drop(columns=['Unnamed: 0'], axis=1)
sales2.head
sales2.reset_index()
sales2.columns
sales.describe
pd.melt('sales2')
pd.pivot?
pd.pivot(data='sales', columns='month', index=['product_id'])

sales3 = pd.concat([sales2, sales2])
sales3.head()
sales.describe
