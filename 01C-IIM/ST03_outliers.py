#Topic: Outlier Analysis
#-----------------------------
#why analyse - The presence of outliers in a classification or regression dataset can result in a poor fit and lower predictive modeling performance.
#an outlier is an observation point that is distant from other observations.
#libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#samle data
marks1 = [3,50,74,76,81,54,85,67,77,41]
len(marks1)

import seaborn as sns
sns.boxplot(x=marks1)
plt.show();

marks2 = [61,45,66,57,64,56,77,64,67,11]

plt.scatter(x=marks1, y=marks2)
plt.show();


#z score
from scipy import stats

z = np.abs(stats.zscore(marks1))
print(z)

np.where(z > 3) #outliers
np.where(z > 2)


#quantile
marks2, type(marks2)
np.sort(marks2)
np.quantile([marks2], q=[.25, .5, .75,1])
pd.Series(marks1).quantile()  #default 0.25
Q1 = pd.Series(marks1).quantile(0.25)
Q3 = pd.Series(marks1).quantile(0.75)
Q1, Q3
IQR = Q3 - Q1
IQR
IQR2 = stats.iqr(pd.Series(marks1))   #iqr from function in py
IQR2

#outlier : < Q1 - IQR or > Q3 + IQR
(marks1 < Q1-1.5 * IQR) | (marks1 > Q3+ 1.5 * IQR)

#dataframe
from pydataset import data 
data('Boston')
boston = data('Boston')

boston.head()
boston.columns
#box plot
sns.boxplot(x=boston['dis'])
# plot shows three points between 10 to 12, these are outliers as there are not included in the box of other observation i.e no where near the quartiles.

#scatterplot
boston.columns
fig, ax = plt.subplots(figsize=(16,8))
ax.scatter(boston['indus'], boston['tax'])
ax.set_xlabel('Proportion of non-retail business acres per town')
ax.set_ylabel('Full-value property-tax rate per $10,000')
plt.show();
#most of data points are lying bottom left side but there are points which are far from the population like top right corner.

#Z-score
z = np.abs(stats.zscore(boston))
print(z)
#difficult to say which data point is an outlier. Let’s try and define a threshold to identify an outlier.
threshold = 3
print(np.where(z > threshold))
#confused by the results. The first array contains the list of row numbers and second array respective column numbers, which mean z[55][1] have a Z-score higher than 3
print(z[55][1])

#IQR
Q1 = boston.quantile(0.25)
Q3 = boston.quantile(0.75)
IQR = Q3 - Q1
print(IQR) # of each column
#The below code will give an output with some true and false values. The data point where we have False that means these values are valid whereas True indicates presence of an outlier.
print((boston < (Q1 - 1.5 * IQR)) |(boston > (Q3 + 1.5 * IQR)))
pd.set_option('display.max_rows', None)
print((boston < (Q1 - 1.5 * IQR)) |(boston > (Q3 + 1.5 * IQR)))
dfTF = (boston < (Q1 - 1.5 * IQR)) |(boston > (Q3 + 1.5 * IQR))

dfTF.shape
sns.boxplot(x=boston.crim)
dfTF.sum(axis=0)
dfTF.sum(axis=1)

dfTF.crim.value_counts()

#Z-score
#want to remove or filter the outliers and get the clean data. This can be done with just one line code as we have already calculated the Z-score.
boston
z
DF1 = (boston < (Q1 - 1.5 * IQR)) |(boston > (Q3 + 1.5 * IQR))
DF1
DF1.head()
dfTF
dfTF[(z < 2).all(axis=1)]
z>3

boston_wo = boston[(z < 3).all(axis=1)]
boston_wo.head()
boston.shape  #shape of original data with outliers
boston_wo.shape #after removing outliers
sns.boxplot(x=boston_wo.crim)
sns.boxplot(x=boston.crim)


boston_wo2 = boston[~((boston < (Q1 - 1.5 * IQR)) |(boston > (Q3 + 1.5 * IQR))).any(axis=1)]
boston_wo2.shape

#some outliers still cropped up... how to remove them
#

#https://towardsdatascience.com/ways-to-detect-and-remove-the-outliers-404d16608dba
#https://haridas.in/outlier-removal-clustering.html
