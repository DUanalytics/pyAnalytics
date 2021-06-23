#Starting Case on Clustering
#standard libaries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pydataset import data
import seaborn as sns

#eg
#data related to marks scored by 4 students in Math and Science and we need to create clusters of students to draw insights
#see how distant each data point is from each other. we construct a Distance matrix. Distance between each point can be found using various metrics i.e. Euclidean Distance, Manhattan Distance, etc.
#We now formed a Cluster between S1 and S2 because they were closer to each other. Now a question arises, what does our data look like now?
#We took the average of the marks obtained by S1 and S2 and the values we get will represent the marks for this cluster. Instead of averages, we can consider maximum or minimum values for data points in the cluster.
#Again find the closest points and create another cluster.
#If we repeat the steps above and keep on clustering until we are left with just one cluster containing all the clusters, we get a result which looks something like this:
#The figure we get is what we call a Dendrogram. A dendrogram is a tree-like diagram that illustrates the arrangement of the clusters produced by the corresponding analyses. The samples on the x-axis are arranged automatically representing points with close proximity that will stay closer to each other.

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

math=[20,50,25,35,40]
science=[25,45,22,40,35]
indexNo = ['S1','S2','S3','S4','S5']
df = pd.DataFrame({'math':math, 'science':science}, index=indexNo)
df
df.plot(kind='scatter', x='math', y='science')
plt.scatter(df['math'], df['science'], s = 20, c = 'k')

from scipy.cluster.hierarchy import dendrogram , linkage
#Linkage Matrix
Z = linkage(df, method = 'ward')
 
#plotting dendrogram
df
dendro = dendrogram(Z)
plt.title('Dendrogram')
plt.ylabel('Euclidean distance')
plt.show()
df

from scipy.spatial import distance
import numpy as np
distance.euclidean([1, 0, 0], [0, 1, 0])
distance.euclidean([20,25],[25,22])  #closest : S1 with S2
np.sqrt(((20-25)**2 + (25-22)**2)) #sqrt(sum(x-y)^2)

distance.euclidean([20,25],[35,40]) 
distance.euclidean([20,25],[40,35])
distance.euclidean([35,40],[40,35])

#distance of all points in DF
from sklearn.neighbors import DistanceMetric
dist = DistanceMetric.get_metric('euclidean')
dist
df.to_numpy()
dist.pairwise(df.to_numpy())


#Kmeans clustering
df
from sklearn.cluster import KMeans
kmeans = KMeans(n_clusters=2).fit(df)
centroids = kmeans.cluster_centers_
print(centroids)
df
plt.scatter(df['math'], df['science'], c= kmeans.labels_.astype(float), s=50, alpha=0.5)
plt.scatter(centroids[:, 0], centroids[:, 1], c='red', s=50, marker='D')
plt.show()
kmeans.fit(df)
kmeans = KMeans(n_clusters=3).fit(df)
kmeans.inertia_
kmeans.cluster_centers_  #average or rep values
kmeans.n_iter_  #in n times, clusters stabilised
kmeans.labels_
df

#iris dataset
import numpy as np
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import dendrogram , linkage
 
#Getting the data ready
from pydataset import data
iris = data('mtcars')
df2 = iris.copy() 
df2.shape
df3 = df2.sample(5)
df3
df3.shape
df3.iloc[:,0:3].values
#Selecting certain features based on which clustering is done 
df4 = df3.iloc[:,0:3].values
df4

#Linkage Matrix
Z = linkage(df4, method = 'ward')

dist = DistanceMetric.get_metric('euclidean')
dist
dist.pairwise(df4)
 
kmeans = KMeans(n_clusters=2).fit(df4)
kmeans.inertia_
kmeans.cluster_centers_  #average or rep values
kmeans.n_iter_  #in n times, clusters stabilised
cn=kmeans.labels_
df4
df3.groupby(kmeans.labels_).mean()

#plotting dendrogram
dendro = dendrogram(Z)
plt.title('Dendrogram')
plt.ylabel('Euclidean distance')
plt.show()
df3

# cluster the mtcars data set into 2 groups, 3 groups
#find the average mileage, wt of these groups

from sklearn.cluster import AgglomerativeClustering
#agg_clustering = AgglomerativeClustering(n_clusters = 3, affinity = 'euclidean', linkage = 'ward')
#predicting the labels
labels = agg_clustering.fit_predict(df)
labels