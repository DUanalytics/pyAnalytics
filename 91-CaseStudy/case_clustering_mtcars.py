#Topic: Assignment - Clustering - mtcars
#-----------------------------
#libraries

import matplotlib.pyplot as plt
from kneed import KneeLocator
from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
from sklearn.preprocessing import StandardScaler

from pydataset import data
mtcars = data('mtcars')
data = mtcars.copy()
data

#need for scaling : height & weight are in different scales
scaler = StandardScaler()
scaled_features = scaler.fit_transform(data)
scaled_features[:5]  #values between -3 to +3

kmeans = KMeans( init = 'random', n_clusters=2, n_init=3, max_iter=300, random_state=42)
kmeans
kmeans.fit(scaled_features)
kmeans.inertia_
kmeans.cluster_centers_  #average or rep values
kmeans.n_iter_  #in 6 times, clusters stabilised
kmeans.labels_[:5]
kmeans.cluster_centers_.shape
kmeans.cluster_centers_[0:1]

#group means
data.groupby(kmeans.labels_).agg({'mpg':'mean','hp':'mean','wt':'mean'})

#plot scatter
plt.scatter(x=data.wt, y=data.mpg, c=kmeans.labels_)
