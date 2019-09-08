#Topic: Clustering - Simple and Data Camp Site
#-----------------------------
#https://www.datacamp.com/community/tutorials/k-means-clustering-python
#https://scikit-learn.org/stable/modules/clustering.html
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
#https://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html
i=3; 
km3 = KMeans(n_clusters = i, init = 'k-means++', random_state = 42)
km3
#KMeans(n_clusters=8, init=’k-means++’, n_init=10, max_iter=300, tol=0.0001, precompute_distances=’auto’, verbose=0, random_state=None, copy_x=True, n_jobs=None, algorithm=’auto’)
dir(km3)
km3.fit_predict(df)
km3.cluster_centers_
km3.inertia_
km3.labels_   #which row has goes to which cluster no
km3.get_params
km3.n_clusters

df
pd.concat([df, pd.Series(km3.labels_)], axis=1)


#not change i = 2
i=2; 
km2 = KMeans(n_clusters = i, init = 'k-means++', random_state = 42)
km2
km2.fit_predict(df)
km2.cluster_centers_
km2.labels_   #which row has goes to which cluster no
km2.inertia_
km3.inertia_ # less
df
pd.concat([df, pd.Series(km2.labels_)], axis=1)

#%%% #How to selected i ? - optimal number of clusters
wcss = []
#run these together
for i in range(1, 5):    
    kmeans = KMeans(n_clusters = i, init = 'k-means++', random_state = 42)
    kmeans.fit(df)
    wcss.append(kmeans.inertia_)  

wcss  #this is approx value of i ~ 2
plt.plot(wcss)
#%%%
km1 = KMeans(n_clusters = 1, init = 'k-means++', random_state = 42)
km1.fit(df)
km1.inertia_

km2 = KMeans(n_clusters = 2, init = 'k-means++', random_state = 42)
km2.fit(df)
km2.inertia_

km3 = KMeans(n_clusters = 3, init = 'k-means++', random_state = 42)
km3.fit(df)
km3.inertia_

km4 = KMeans(n_clusters = 4, init = 'k-means++', random_state = 42)
km4.fit(df)
km4.inertia_
km1.inertia_, km2.inertia_, km3.inertia_, km4.inertia_
#https://www.datanovia.com/en/lessons/determining-the-optimal-number-of-clusters-3-must-know-methods/


#%%% k means determine k
distortions = []
K = range(1,5)
for k in K:
    kmeanModel = KMeans(n_clusters=k).fit(df)
    kmeanModel.fit(df)
    distortions.append(sum(np.min(cdist(df, kmeanModel.cluster_centers_, 'euclidean'), axis=1)) / df.shape[0])

distortions
# Plot the elbow
plt.plot(K, distortions, 'bx-')
plt.xlabel('k')
plt.ylabel('Distortion')
plt.title('The Elbow Method showing the optimal k')
plt.show();
#%%%%
#Plot clusters %%%%
km3b = KMeans(n_clusters = 3, init = 'k-means++', random_state = 42)
X2 = np.random.randint(50,100, size=100)
Y2 = np.random.randint(60,90, size=100)

df2 = pd.DataFrame({'X':X2, 'Y':Y2})
km3b.fit(df2)
km3b.inertia_
centers = np.array(km3b.cluster_centers_)
centers
plt.scatter(x=df2.X, y=df2.Y)
plt.scatter(centers[:,0], centers[:,1], marker="x", color='r')
plt.show();


#end here...