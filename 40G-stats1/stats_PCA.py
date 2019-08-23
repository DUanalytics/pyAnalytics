#Topic: Statistics - PCA
#-----------------------------
#libraries
from sklearn.decomposition import PCA
from sklearn.datasets import load_iris
iris = load_iris()
X = iris.data
pca = PCA(n_components=2)
pca
X_new = pca.fit_transform(X)
print(X.shape)
print(X_new.shape)


#https://kite.com/python/docs/sklearn.datasets.lfw.Bunch
