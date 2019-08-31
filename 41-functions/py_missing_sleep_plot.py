#Plotting Missing Values
#-----------------------------
#%
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sleep1 = pd.read_csv('data/sleep.csv')
sleep1.head()

sleep = sleep1.copy()

sns.heatmap(sleep.isnull(), cbar=False)
#NonD, Dream, Sleep, Span, Gest have missing values
sleep.isna().sum()


#
#  pip install missingno
import missingno as msno

msno.matrix(sleep)
#In addition to the heatmap, there is a bar on the right side of this diagram. This is a line plot for each row's data completeness.
msno.heatmap(sleep)
#missingno.heatmap visualizes the correlation matrix about the locations of missing values in columns.

#%%
dataset = sleep.copy()
total = dataset.isnull().sum().sort_values(ascending=False)
percent = (dataset.isnull().sum()/dataset.isnull().count()).sort_values( ascending=False)
missing_data = pd.concat([total, percent], axis=1, keys=['Total', 'Percent'])
f, ax = plt.subplots(figsize=(15, 6))
plt.xticks(rotation='90')
sns.barplot(x=missing_data.index, y=missing_data['Percent'])
plt.xlabel('Features', fontsize=15)
plt.ylabel('Percent of missing values', fontsize=15)
plt.title('Percent missing data by feature', fontsize=15)
missing_data.head()

#https://towardsdatascience.com/handling-missing-values-in-machine-learning-part-1-dda69d4f88ca


#impu