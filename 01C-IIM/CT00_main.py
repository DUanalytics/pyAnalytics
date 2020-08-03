#Topic: Clustering
#-----------------------------
#making groups and find group properties
#libraries

#kmeans - minimise distance of points in the cluster with their centeroid

import pandas as pd
import numpy as np
import random as rd
import matplotlib.pyplot as plt

#data 
#data = pd.read_csv('data/clustering.csv')
url='https://raw.githubusercontent.com/DUanalytics/pyAnalytics/master/data/clustering.csv'
data = pd.read_csv(url)
data.shape
data.head()
data.describe()
data.columns

#visualise
plt.scatter(data.ApplicantIncome, data.LoanAmount)
plt.xlabel('Income')
plt.ylabel('LoanAmt')
plt.show();

#standardize data : Scaling

#missing values
#https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.dropna.html
data.dtypes
data.isnull().any()
data.isnull().any(axis=1)
data.index[data.isnull().any(axis=1)]
data.iloc[6]  #see the null values
data.isnull().sum().sum()  #75 missing values 
data.isnull().sum(axis=0)  #columns missing
data.isnull().sum(axis=1)
data1 = data.dropna()

data1.isnull().any()
data1.isnull().sum().sum()

data2 =  data1.select_dtypes(exclude=['object'])
data2.head()
from sklearn.preprocessing import StandardScaler
scalar = StandardScaler()
data2_scaled = scalar.fit_transform(data2)

data2_scaled.describe() #it converts to different format
pd.DataFrame(data2_scaled).describe()

#kmeans
from sklearn.cluster import KMeans
kmeans = KMeans(n_clusters=2)  #hyper parameters

kmeans.fit(data2_scaled)
kmeans.inertia_  #sum of sq distances of samples to their centeroid
kmeans.cluster_centers_
kmeans.labels_
kmeans.n_iter_  #iterations to stabilise the clusters
kmeans.predict(data2_scaled)

data2_scaled[1:5]

data.columns
data2.columns
NCOLS = data2.columns 
#['ApplicantIncome','CoapplicantIncome','LoanAmount', 'Loan_Amount_Term', 'Credit_History', 'Property_Area']
NCOLS
clusterNos = kmeans.labels_
clusterNos
type(clusterNos)

data2.groupby([clusterNos]).mean()
pd.options.display.max_columns =None
data2.groupby([clusterNos]).mean()
plt.scatter(data2.ApplicantIncome, data2.LoanAmount, c=clusterNos)
plt.scatter(data2.ApplicantIncome, data2.Credit_History, c=clusterNos) #better distinction
plt.scatter(data2.ApplicantIncome, data2.Loan_Amount_Term, c=clusterNos) #better distinction

#Now use this information ;
#which customers you would like to target.

#hierarchical clustering
import scipy.cluster.hierarchy as shc
dend = shc.dendrogram(shc.linkage(data2_scaled, method='ward'))

plt.figure(figsize = (10,7))
plt.title("Dendrogram")
dend = shc.dendrogram(shc.linkage(data2_scaled, method='ward'))
plt.axhline(y=6, color='r', linestyle='--')
plt.show();

#another method for Hcluster from sklearn
from sklearn.cluster import AgglomerativeClustering
aggCluster = AgglomerativeClustering(n_clusters=2, affinity='euclidean', linkage='ward')
aggCluster.fit_predict(data2_scaled)
aggCluster
aggCluster.labels_

#compare
compare = pd.DataFrame({'kmCluster': kmeans.labels_, 'HCaggl': aggCluster.labels_, 'Diff': kmeans.labels_ - aggCluster.labels_})
compare
compare.Diff.sum()
compare.kmCluster.value_counts()
compare.HCaggl.value_counts()

#Customer Segmentation
#Product Segmentation
