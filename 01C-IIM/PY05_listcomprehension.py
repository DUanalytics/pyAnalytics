#Topic: Association Rule Analysis
#-----------------------------
#libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#creating sample data
TID =[1,2,3,4,6,7,8,9]
items = [['I1,I2,I5'], ['I2,I4'], ['I2,I3'], ['I1,I2,I4'], ['I1,I3'], ['I2,I3'],['I1,I2,I3,I5'], ['I1,I2,I3']]
items

item1 = 'I1,I2,I5'
item1.split(',')

type(items)
for i in items: print(i)
    newlist.append([i.split(',')[0])



itemSale = pd.DataFrame({'TID':TID, 'items':items})
itemSale

#data
#data = pd.read_csv('data/bookstore.csv')
data = itemSale
data.head()

#split transaction strings into lists
transactions = data['items'].apply(lambda t: [t.split() for x in t])
#convert DF to List of Strings
transactionsList = list(transactions)
transacationsList
transacationsList[0]
transactionsList.count([I1','I2'])
