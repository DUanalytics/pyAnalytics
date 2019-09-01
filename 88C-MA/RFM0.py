#Topic: Before RFM
#-----------------------------
#libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

customerID = np.arange(1,11)
customerID
len(customerID)
np.random.seed(1234)
spend = np.random.randint(50,100, size=10)
spend
len(customerID)
np.mean(spend)
#combine to DF
df = pd.DataFrame({'custID':customerID, 'spend':spend})
df.head()

#%%% Monentisation (M)
spend_quartiles = pd.qcut(df['spend'], q=4, labels=range(1,5))
df['spend_quartile'] = spend_quartiles
df.sort_values('spend')

#%% Recency (R)
customerID = np.arange(1,11)
import random
#random.sample(list(customerID), k=20)
custID = random.choices(list(customerID), k=50)  #with replacement
daysbefore = np.random.randint(5,100, size=50)
df2 = pd.DataFrame({'custID':custID, 'daysbefore':daysbefore})
df2.head()
df2.loc[df2['custID']==10,].sort_values('daysbefore')       
df2[["daysbefore", "custID"]].groupby(["custID"]).nth(0)    
df2.groupby(["custID"]).apply(lambda x: x.sort_values(["daysbefore"], ascending = True)).reset_index(drop=True)
g=df2.sort_values(by=['custID','daysbefore'], axis=0).groupby('custID', as_index=False)
g.nth(0) 
df2b=g.first()
df2b
g.agg({'daysbefore' : 'first'})
#---
# Create numbered labels
r_labels = list(range(4, 0, -1))
r_labels
# Divide into groups based on quartiles
recency_quartiles = pd.qcut(df2b['daysbefore'], q=4, labels=r_labels)
recency_quartiles
# Create new column
df2b['Recency_Quartile'] = recency_quartiles
# Sort recency values from lowest to highest
df2b.sort_values('daysbefore')
#---
# Create string labels
r_labels2 = ['Active','Lapsed','Inactive','Churned']
# Divide into groups based on quartiles
recency_quartiles2 = pd.qcut(df2b['daysbefore'], q=4, labels=r_labels2)
# Create new column
df2b['Recency_Quartile2'] = recency_quartiles2
# Sort values from lowest to highest
df2b.sort_values('daysbefore')


#%% Frequency (F)

