#Topic:Clustering 
#-----------------------------
#libraries
#https://www.analyticsvidhya.com/blog/2019/08/comprehensive-guide-k-means-clustering/
url="https://raw.githubusercontent.com/DUanalytics/datasets/master/csv/clustering.csv"
#import libraries
import pandas as pd
import numpy as np
import random as rd
import matplotlib.pyplot as plt

data = pd.read_csv(url)
data.head()

X = data[["LoanAmount","ApplicantIncome"]]
X.head()
#Visualise data points
plt.scatter(X["ApplicantIncome"],X["LoanAmount"],c='black')
plt.xlabel('AnnualIncome')
plt.ylabel('Loan Amount (In Thousands)')
plt.show();


#%%% select k
#Steps 1 and 2 of K-Means were about choosing the number of clusters (k) and selecting random centroids for each cluster. We will pick 3 clusters and then select random observations from the data as the centroids:

# Step 1 and 2 - Choose the number of clusters (k) and select random centroid for each cluster

#number of clusters
K=3

# Select random observation as centroids
Centroids = (X.sample(n=K))
Centroids
plt.scatter(X["ApplicantIncome"],X["LoanAmount"],c='black')
plt.scatter(Centroids["ApplicantIncome"],Centroids["LoanAmount"],c='red', s=100)
plt.xlabel('AnnualIncome')
plt.ylabel('Loan Amount (In Thousands)')
plt.show();

#Here, the red dots represent the 3 centroids for each cluster. Note that we have chosen these points randomly and hence every time you run this code, you might get different centroids.
#Next, we will define some conditions to implement the K-Means Clustering algorithm. 


#K-Means++ to Choose Initial Cluster Centroids for K-Means Clustering
#In some cases, if the initialization of clusters is not appropriate, K-Means can result in arbitrarily bad clusters. This is where K-Means++ helps. It specifies a procedure to initialize the cluster centers before moving forward with the standard k-means clustering algorithm.

#Using the K-Means++ algorithm, we optimize the step where we randomly pick the cluster centroid. We are more likely to find a solution that is competitive to the optimal K-Means solution while using the K-Means++ initialization.

#The steps to initialize the centroids using K-Means++ are:
#The first cluster is chosen uniformly at random from the data points that we want to cluster. This is similar to what we do in K-Means, but instead of randomly picking all the centroids, we just pick one centroid here
#Next, we compute the distance (D(x)) of each data point (x) from the cluster center that has already been chosen
#Then, choose the new cluster center from the data points with the probability of x being proportional to (D(x))2
#We then repeat steps 2 and 3 until k clusters have been chosen


#%%%
# standardizing the data
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
data.head()
data.describe()
data2 = data._get_numeric_data()

data_scaled = scaler.fit_transform(data2)
data_scaled.shape
# statistics of scaled data
pd.DataFrame(data_scaled).describe()
type(data_scaled)
    # defining the kmeans function with initialization as k-means++
kmeans = KMeans(n_clusters=2, init='k-means++')

# fitting the k means algorithm on scaled data
kmeans.fit(data_scaled)
data_scaled = data_scaled[~np.isnan(data_scaled).any(axis=1)]
#data_scaled = data_scaled [ , ~ np.isnan(data_scaled)]
np.equal(data_scaled, None)  #check for Missing
data_scaled
kmeans.fit(data_scaled)

#Let’s evaluate how well the formed clusters are. To do that, we will calculate the inertia of the clusters:

# inertia on the fitted data
kmeans.inertia_

#We got an inertia value of almost 1395. Now, let’s see how we can use the elbow curve to determine the optimum number of clusters in Python

# fitting multiple k-means algorithms and storing the values in an empty list
SSE = []
for cluster in range(1,10):
    kmeans = KMeans(n_jobs = -1, n_clusters = cluster, init='k-means++')
    kmeans.fit(data_scaled)
    SSE.append(kmeans.inertia_)

# converting the results into a dataframe and plotting them
len(SSE)
frame = pd.DataFrame({'Cluster':range(1,10), 'SSE':SSE})
plt.figure(figsize=(12,6))
plt.plot(frame['Cluster'], frame['SSE'], marker='o')
plt.xlabel('Number of clusters')
plt.ylabel('Inertia')

# k means using 5 clusters and k-means++ initialization
kmeans = KMeans(n_jobs = -1, n_clusters = 5, init='k-means++')
kmeans.fit(data_scaled)
pred = kmeans.predict(data_scaled)


frame = pd.DataFrame(data_scaled)
frame['cluster'] = pred
frame['cluster'].value_counts()

#So, there are 144 data points belonging to cluster 1 (index 0),
# This is how we can implement K-Means Clustering in Python.
#we discussed one of the most famous clustering algorithms – K-Means. We implemented it from scratch and looked at its step-by-step implementation. We looked at the challenges which we might face while working with K-Means and also saw how K-Means++ can be helpful when initializing the cluster centroids.
#Finally, we implemented k-means and looked at the elbow curve which helps to find the optimum number of clusters in the K-Means algorithm.