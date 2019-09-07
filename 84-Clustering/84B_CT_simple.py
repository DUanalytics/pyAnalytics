#Topic: Clustering - Simple and Data Camp Site
#-----------------------------
#https://www.datacamp.com/community/tutorials/k-means-clustering-python

X = [1,1,1,2,1,2,1,2]
Y = [4,2,4,1,1,4,1,1]
Z = [1,2,2,2,1,2,2,1]

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import metrics
from scipy.spatial.distance import cdist
df = pd.DataFrame({'X':X, 'Y':Y, 'Z':Z})
df

from sklearn.cluster import KMeans
i=3; 
km3 = KMeans(n_clusters = i, init = 'k-means++', random_state = 42)
km3
dir(km3)
km3.fit_predict(df)
km3.cluster_centers_
km3.labels_   #which row has goes to which cluster no
df
pd.concat([df, pd.Series(km3.labels_)], axis=1)


#not change i = 2
i=2; 
km2 = KMeans(n_clusters = i, init = 'k-means++', random_state = 42)
km2
km2.fit_predict(df)
km2.cluster_centers_
km2.labels_   #which row has goes to which cluster no
df
pd.concat([df, pd.Series(km2.labels_)], axis=1)

#%%% #How to selected i ? - optimal number of clusters
wcss = []
for i in range(1, 5):    kmeans = KMeans(n_clusters = i, init = 'k-means++', random_state = 42)

kmeans.fit(df)
wcss.append(kmeans.inertia_)  
wcss  #this is approx value of i ~ 2


#%%% k means determine k
distortions = []
K = range(1,5)
for k in K:
    kmeanModel = KMeans(n_clusters=k).fit(df)
    kmeanModel.fit(df)
    distortions.append(sum(np.min(cdist(df, kmeanModel.cluster_centers_, 'euclidean'), axis=1)) / df.shape[0])

# Plot the elbow
plt.plot(K, distortions, 'bx-')
plt.xlabel('k')
plt.ylabel('Distortion')
plt.title('The Elbow Method showing the optimal k')
plt.show();
