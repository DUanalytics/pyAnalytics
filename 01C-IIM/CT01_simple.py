#Topic: Clustering
#-----------------------------

#libraries
import matplotlib.pyplot as plt
#pip install kneed
from kneed import KneeLocator
from sklearn.datasets import make_blobs  #simulate data
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

#parameters for creating simulated data
#n_samples - total samples to generate
#centers - no of centers or clusters
#cluster_std - standard deviation

#simulated / synthentic data
features, true_labels = make_blobs( n_samples=200, centers=3, cluster_std=2.75, random_state=42)
features[:5]
features.shape
true_labels[:5]

#need for scaling : height & weight are in different scales
scaler = StandardScaler()
scaled_features = scaler.fit_transform(features)
scaled_features[:5]  #values between -3 to +3

kmeans = KMeans( init = 'random', n_clusters=3, n_init=10, max_iter=300, random_state=42)
kmeans
kmeans.fit(scaled_features)
kmeans.inertia_
kmeans.cluster_centers_  #average or rep values
kmeans.n_iter_  #in 6 times, clusters stabilised
kmeans.labels_[:5]


#%%choosing no of clusters
kmeans_kwargs = {'init':'random', 'n_init':10, 'max_iter': 300, 'random_state': 42,}
sse=[]
for k in range(1, 11):
    kmeans = KMeans(n_clusters=k, **kmeans_kwargs)
    kmeans.fit(scaled_features)
    sse.append(kmeans.inertia_)

plt.style.use('fivethirtyeight')
plt.plot(range(1,11), sse)
plt.xticks(range(1,11))
plt.xlabel('No of clusters')
plt.ylabel('SSE')
plt.show();

kl = KneeLocator(x=range(1,11), y=sse, curve='convex', direction='decreasing')
kl.elbow


##https://realpython.com/k-means-clustering-python/
