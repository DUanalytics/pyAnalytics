#Topic: Clustering - Simulated Data
#-----------------------------
#libraries

from matplotlib import pyplot as plt #another way to import
#from matplotlib.pyplot as plt
#import matplotlib.pyplot
from scipy.cluster.hierarchy import dendrogram, linkage
import numpy as np

%matplotlib inline
np.set_printoptions(precision=5, suppress=True)  #no scientific values

#sample data
mean = [10, 0]
cov = [[3, 1], [1, 4]]
np.random.seed(4711)
a = np.random.multivariate_normal(mean, cov , size=[100,])
a
np.mean(a, axis=0)
b = np.random.multivariate_normal(mean=[0,20], cov=[[3,1],[1,4]] , size=[100,])
b
X = np.concatenate((a,b),)
X[1:5,]

X.shape


#linkage : distance between cluster
Z = linkage(X, 'ward')
Z
Z.shape
Z2 = linkage(X, method='single', metric='euclidean', optimal_ordering=False)
Z2
Z2.shape

#Pairwise distance
from scipy.cluster.hierarchy import cophenet
from scipy.spatial.distance import pdist
pdist(X)
c, coph_dist = cophenet(Z, pdist(X))
len(coph_dist)
c
Z[0]
Z[1]
Z[:20]


#plot
idxs= [ 33, 68, 62]
X[idxs, 0], X[idxs, 1]
plt.figure(figsize=(10,8))
plt.scatter(X[:,0], X[:,1])
plt.scatter(X[idxs, 0], X[idxs, 1], c='r')
plt.show();


#Dendrogram
plt.figure(figsize=(25,10))
plt.title('Hierarchical Clustering Dendorgram')
plt.xlabel('Sample Index')
plt.ylabel('distance')
dendrogram(Z, leaf_rotation=90, leaf_font_size=8)
plt.show()


#height of horz line - distance at which this lable was merged into another label or cluster. If u don't encounter another borz line, it was just merged with the other label you reach, otherwise it was merged with another cluster that was formed earlier

#horiz lines are cluster merges
#vertical lines tell which clusters/ labels were part of the merge forming that new cluster
#heights - of horz line tell you about the distance that needed to be bridged to form the new cluster
#distance > 25 up there is huge jump of distance to the final merge at distance ~ 180.
Z[-4:, 2]

#dendrogram truncations
plt.title('HC Dendrogram (truncated)')
plt.xlabel('Sample Index')
plt.ylabel('Distance')
dendrogram(Z, truncate_mode ='lastp', p=12, show_leaf_counts=False, leaf_font_size=12, show_contracted=True)
plt.show();
