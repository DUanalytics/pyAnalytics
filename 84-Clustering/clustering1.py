#Clustering
#https://github.com/jupyter/docker-demo-images/blob/master/datasets/cluster/xclara.csv
from copy import deepcopy
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

plt.rcParams['figure.figsize'] = (16,9)
plt.style.use('ggplot')

#import data set
data = pd.read_csv('./data/xclara.csv')
data.head()

#plot the values : should be numeric - create array
f1 = data['V1'].values
f2 = data['V2'].values
X = np.array(list(zip(f1,f2)))
X
plt.scatter(f1,f2, c='black', s=7)

def dist(a, b, ax=1):
    return np.linalg.norm(a - b, axis=ax)

k=3
#coordinates of centeroid : random : integer values: betw the range
C_x = np.random.randint(0, np.max(X) - 20, size=k)
C_x
C_y = np.random.randint(0, np.max(X) - 20, size=k)
C_y
X
C = np.array(list(zip(C_x, C_y)), dtype=np.float32)
C

#plotting with Centeriods
plt.scatter(f1, f2, c='#050505', s=7)
plt.scatter(C_x, C_y, marker = '*', s=200, c='r')


#store values of centeriods when it updates
C_old = np.zeros(C.shape)
C_old
clusters = np.zeros(len(X))
clusters

#distance 





#Implement using Algo
#https://mubaris.com/2017/10/01/kmeans-clustering-in-python/

from sklearn.cluster import KMeans

# Number of clusters
kmeans = KMeans(n_clusters=3)
kmeans
# Fitting the input data
kmeans = kmeans.fit(X)
kmeans.cluster_centers_

# Getting the cluster labels
labels = kmeans.predict(X)
labels

# Centroid values
centroids = kmeans.cluster_centers_
centroids

# Comparing with scikit-learn centroids
print(C) # From Scratch  : Part - 1
print(centroids) # From sci-kit learn



#%%

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs

plt.rcParams['figure.figsize'] = (16, 9)

# Creating a sample dataset with 4 clusters
X, y = make_blobs(n_samples=800, n_features=3, centers=4)
fig = plt.figure()
ax = Axes3D(fig)
ax.scatter(X[:, 0], X[:, 1], X[:, 2])

# Initializing KMeans
kmeans = KMeans(n_clusters=4)
# Fitting with inputs
kmeans = kmeans.fit(X)
# Predicting the clusters
labels = kmeans.predict(X)
# Getting the cluster centers
C = kmeans.cluster_centers_
#run next 4 lines together
fig = plt.figure()
ax = Axes3D(fig)
ax.scatter(X[:, 0], X[:, 1], X[:, 2], c=y)
ax.scatter(C[:, 0], C[:, 1], C[:, 2], marker='*', c='#050505', s=1000)

#In the above image, you can see 4 clusters and their centroids as stars. scikit-learn approach is very simple and concise.
