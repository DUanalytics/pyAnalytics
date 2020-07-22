#Topic: Assignment Submissions
#-----------------------------
#libraries

#Arunabesh Chakraborty
#import pandas
import pandas as pd
#load the csv file
data = pd.read_csv('data/denco.csv')
data.head()
data.tail(10)
#most loyal customers
data['custname'].value_counts().head(10)

#Which customers contribute the most to their revenue
data.groupby('custname')['revenue'].sum().sort_values(ascending=False).head(1)

#What part numbers bring in to significant portion of revenue
data.groupby('partnum')['revenue'].sum().sort_values(ascending=False).head()

#What parts have the highest profit margin ?
data.groupby('partnum')['margin'].sum().sort_values(ascending=False).head()

#Who are their top buying customers?
data.groupby('custname')['revenue'].sum().sort_values(ascending=False).head()
#Who are the customers who are bringing more revenue?
