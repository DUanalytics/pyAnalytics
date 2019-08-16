#Topic ----K Means Clustering
#https://www.analyticsindiamag.com/beginners-guide-to-k-means-clustering/
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pydataset import data
iris = data('iris')
data=iris
data.head()
data.columns
data.dtypes
data.shape
#%%%K-Means Algorithm
#Selecting an appropriate value for K which is the number of clusters or centroids
#Selecting random centroids for each cluster
#Assigning each data point to its closest centroid
#Adjusting the centroid for the newly formed cluster in step 4
#Repeating step 4 and 5 till all the data points are perfectly organised within a cluster space


#%%%
#Dropping the 'Species' column
iris_clustering = iris.drop(columns = ['Species'])
iris_clustering
#Selecting 2 random features from the dataset for clustering
#Here we choose Sepal Length @ column 0 and Petal Length @ column 2
X = iris_clustering.iloc[:, [0,2]].values
X
#We only chose 2 features as we are going to plot in 2D space. The algorithm will work  for any number of features.
#%%%Using Elbow Graph To Find Optimum Number Of Clusters
# Using the elbow method to find the optimal number of clusters
from sklearn.cluster import KMeans
wcss = []
for i in range(1, 11):
    kmeans = KMeans(n_clusters = i, init = 'k-means++', random_state = 42)
kmeans.fit(X)
#appending the WCSS to the list (kmeans.inertia_ returns the WCSS value for an initialized cluster)
wcss.append(kmeans.inertia_)  
wcss
#Plotting The Elbow graph
plt.plot(range(1, 11), wcss)
plt.title('The Elbow Point Graph')
plt.xlabel('Number of clusters')
plt.ylabel('WCSS')
plt.show()


#%%nitialising K-Means With Optimum Number Of Clusters
#Fitting K-Means to the dataset
kmeans = KMeans(n_clusters = 3, init = 'k-means++', random_state = 0)
#Returns a label for each data point based on the number of clusters
y = kmeans.fit_predict(X)
print(y)
X,y

#%%Visualising The Clusters
#Scatter plotting for (x,y) with label 1 as Cluster 1 in color c = red and points in size s = 50 
plt.scatter(X[y == 0, 0], X[y == 0, 1], s = 50, c = 'red', label = 'Cluster 1')
#Scatter plotting for (x,y) with label 2 as Cluster 2 in color c = blue and points in size s = 50 
plt.scatter(X[y == 1, 0], X[y == 1, 1], s = 50, c = 'blue', label = 'Cluster 2')
#Scatter plotting for (x,y) with label 3 as Cluster 3 in color c = green and points in size s = 50 
plt.scatter(X[y == 2, 0], X[y == 2, 1], s = 50, c = 'green', label = 'Cluster 3')

#Scatter plotting the centroids with label = 'Centroids' in color c = cyan and points in size s = 100 
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], s = 100, c = 'cyan', label = 'Centroids')
plt.title('Iris Flower Clusters')
plt.xlabel('Sepal Length in cm')
plt.ylabel('Petal Length in cm')
plt.legend()
plt.show()