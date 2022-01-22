#Topic:Clustering - marks and mtcars
#-----------------------------
#libraries

import matplotlib.pyplot as plt
from kneed import KneeLocator
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
from sklearn.preprocessing import StandardScaler
import pandas as pd

data = {'x': [25,34,22,27,33,33,31, 22,35,34,67,54,57,43,50, 57,59,52,65, 47,49,48,35,33,44,45, 38,43,51,46],'y': [79,51,53, 78,59,74,73,57, 69,75,51,32, 40,47,53,36,35,58, 59,50,25,20,14, 12,20,5,29, 27,8,7]  }
data  
df = pd.DataFrame(data, columns=['x','y'])
df.head()
df.mean(), df.max(), df.min()
df.shape
print(df)

#%% kmeans clustering
from sklearn.cluster import KMeans
kmeans = KMeans(n_clusters=3).fit(df)
dir(kmeans)  #functions / output available after running the model
kmeans.n_clusters
kmeans.inertia_
centroids = kmeans.cluster_centers_
print(centroids)
kmeans.labels_
df
plt.scatter(df['x'], df['y'])
#run these 3 lines together
plt.scatter(df['x'], df['y'], c= kmeans.labels_.astype(float), s=50, alpha=.5)
plt.scatter(centroids[:, 0], centroids[:, 1], c='red', s=100, marker='D')
plt.show();

#%% 4 clusters
kmeans = KMeans(n_clusters=4).fit(df)
centroids = kmeans.cluster_centers_
print(centroids)
kmeans.inertia_
#run these lines together
plt.scatter(df['x'], df['y'], c= kmeans.labels_.astype(float), s=50, alpha=0.5)
plt.scatter(centroids[:, 0], centroids[:, 1], c='red', s=100, marker='D')
plt.show()
#https://matplotlib.org/stable/api/markers_api.html#module-matplotlib.markers

#mtcars

from pydataset import data
mtcars = data('mtcars')
mtcarsData = mtcars.copy()
id(mtcarsData)
mtcarsData.head()
mtcarsData.columns
mtcarsData.shape
# 3 clusters from K means
kmeans = KMeans(n_clusters=3).fit(mtcarsData)
kmeans.n_clusters
kmeans.inertia_
centroids = kmeans.cluster_centers_
print(centroids)
kmeans.labels_
mtcarsData.groupby(kmeans.labels_).aggregate({'mpg':[np.mean, 'count'], 'wt':np.mean})
mtcarsData.groupby('gear').aggregate({'mpg':np.mean})
mtcarsData.min(), mtcarsData.max()


#need for scaling : height & weight are in different scales
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
mtcarsScaledData = scaler.fit_transform(mtcarsData)
mtcarsScaledData[:5]  #values between -3 to +3
np.min(mtcarsScaledData[:,1]), np.max(mtcarsScaledData[:,1])
kmeans = KMeans(init = 'random', n_clusters=3, n_init=3, max_iter=10, random_state=42)
kmeans
kmeans.fit(mtcarsScaledData)
kmeans.inertia_
kmeans.cluster_centers_  #average or rep values
kmeans.n_iter_  #in 3 times, clusters stabilised
kmeans.labels_[:]
len(kmeans.labels_[:])  #32 rows
kmeans.cluster_centers_.shape   #2 rows of centeriod with 11 columns
kmeans.cluster_centers_[0:2]
mtcarsData.groupby(kmeans.labels_).mean()
clustersKM = kmeans.labels_
clustersKM
type(clustersKM)
mtcarsData.groupby([clustersKM])['mpg','wt'].mean()
#https://realpython.com/k-means-clustering-python/

#dendrogram
from scipy.cluster.hierarchy import dendrogram , linkage
#Linkage Matrix
Z = linkage(mtcarsScaledData, method = 'ward')
from sklearn.neighbors import DistanceMetric
dist = DistanceMetric.get_metric('euclidean')
dist
dist.pairwise(mtcarsScaledData)
#plotting dendrogram
dendro = dendrogram(Z)
plt.title('Dendrogram')
plt.ylabel('Euclidean distance')
plt.show()

#select line
#https://stackabuse.com/hierarchical-clustering-with-python-and-scikit-learn
# largest vertical distance without any horizontal line passing through it is represented by blue line. So we draw a new horizontal red line that passes through the blue line. Since it crosses the blue line at two points, therefore the number of clusters will be 2.
import scipy.cluster.hierarchy as shc
plt.figure(figsize=(10, 7))
plt.title("MT cars Clusters")
dend = shc.dendrogram(shc.linkage(mtcarsScaledData, method='ward'))
#draw a horizontal line that passes through longest distance without a horizontal line, we get 2 clusters as shown in the following figure:
#Now we know the number of clusters for our dataset, the next step is to group the data points into these 2 clusters. To do so we will again use the AgglomerativeClustering class of the sklearn.cluster library. Take a look at the following script:

#another plot
plt.figure(figsize = (10,7))
plt.title("Dendrogram")
dend = shc.dendrogram(shc.linkage(mtcarsScaledData, method='ward'))
plt.axhline(y=12.5, color='r', linestyle='--')
plt.show();  


from sklearn.cluster import AgglomerativeClustering
cluster = AgglomerativeClustering(n_clusters=3, affinity='euclidean', linkage='ward')
cluster.fit_predict(mtcarsScaledData)
clustersHC = cluster.fit_predict(mtcarsScaledData)
clustersHC, len(clustersHC)
clustersKM, len(clustersKM)   #from k means
np.vstack((clustersKM,clustersHC))
print(np.vstack((clustersKM,clustersHC)).T)  #there could be some variations

#statistical cluster nos
#%%choosing no of clusters
kmeans_kwargs = {'init':'random', 'n_init':10, 'max_iter': 300, 'random_state': 42}
sse=[]
for k in range(1, 11):
    kmeans = KMeans(n_clusters=k, **kmeans_kwargs)
    kmeans.fit(mtcarsScaledData)
    sse.append(kmeans.inertia_)

plt.style.use('fivethirtyeight')
plt.plot(range(1,11), sse)
plt.xticks(range(1,11))
plt.xlabel('No of clusters')
plt.ylabel('SSE')
plt.show();

kl = KneeLocator(x=range(1,11), y=sse, curve='convex', direction='decreasing')
kl.elbow
#best way to cluster the groups

#end here.
