#python : Topic : Divisive Hierarchical Clustering & Plotting on iris
#1 to many (single)
#https://www.askpython.com/python/examples/hierarchical-clustering
#Divisive hierarchical clustering is opposite to what agglomerative HC is. Here we start with a single cluster consisting of all the data points. With each iteration, we separate points which are distant from others based on distance metrics until every cluster has exactly 1 data point.
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

#sklearn.cluster module provides us with AgglomerativeClustering class to perform clustering on the dataset.
#As an input argument, it requires a number of clusters (n_clusters), affinity which corresponds to the type of distance metric to use while creating clusters, linkage linkage{“ward”, “complete”, “average”, “single”}, default=”ward”.
#The linkage criterion determines which distance to use between the given sets of observations.


from sklearn.datasets import load_iris
from sklearn.cluster import AgglomerativeClustering
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

math=[20,25,35,40]
science=[25,22,40,35]
indexNo = ['S1','S2','S3','S4']
df = pd.DataFrame({'math':math, 'science':science}, index=indexNo)
df
df.plot(kind='scatter', x='math', y='science')
plt.scatter(df['math'], df['science'], s = 20, c = 'k')

agg_clustering = AgglomerativeClustering(n_clusters = 3, affinity = 'euclidean', linkage = 'ward')
#predicting the labels
labels = agg_clustering.fit_predict(df)
labels

from scipy.cluster.hierarchy import dendrogram , linkage
#Linkage Matrix
Z = linkage(df, method = 'ward')
 
#plotting dendrogram
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

from sklearn.neighbors import DistanceMetric
dist = DistanceMetric.get_metric('euclidean')
dist
df.to_numpy()
dist.pairwise(df.to_numpy())


#iris dataset
from sklearn.datasets import load_iris
from sklearn.cluster import AgglomerativeClustering
import numpy as np
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import dendrogram , linkage
 
#Getting the data ready
from pydataset import data
iris = data('iris')
df2 = iris.copy() 
df3 = df2.sample(5)
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
 
#plotting dendrogram
dendro = dendrogram(Z)
plt.title('Dendrogram')
plt.ylabel('Euclidean distance')
plt.show()
df3
