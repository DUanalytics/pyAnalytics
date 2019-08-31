#Topic:
#-----------------------------
#libraries
import pandas as pd
import numpy as np

df = pd.read_csv('tt/knndata.csv')
df
df1 = pd.read_clipboard()
df1

dyx1= (7 - 2) + (4 - 3) + (9 - 4)
dyx2 =
df.iloc[0:1,:-1]
df.iloc[10:,:-1]
sample = df.iloc[:9,:-1]
sample
from scipy.spatial.distance import pdist, squareform

distances = pdist(sample.values, metric='euclidean')
dist_matrix = squareform(distances)
dist_matrix

from sklearn.metrics.pairwise import euclidean_distances
dist = euclidean_distances(sample, sample)
dist
dist.shape



#
df
DF1= df.iloc[0:10,:-1]
DF1
DF2= df.iloc[-1:,:-1]
DF2
import scipy
ary = scipy.spatial.distance.cdist(DF1.iloc[:,1:], DF2.iloc[:,1:], metric='euclidean')
pd.DataFrame(ary)
DF1.head(1)
DF2
((7-2)**2 + (4-3)**2 + (9-4)**2)**.5
(25+1+25)**.5
