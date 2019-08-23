#Topic:Data Set from 
#-----------------------------
#libraries
#https://scikit-learn.org/stable/datasets/index.html
#https://kite.com/python/docs/sklearn.datasets
The sklearn.datasets package embeds some small toy datasets as introduced in the Getting Started section.

This package also features helpers to fetch larger datasets commonly used by the machine learning community to benchmark algorithms on data that comes from the ‘real world’.

To evaluate the impact of the scale of the dataset (n_samples and n_features) while controlling the statistical properties of the data (typically the correlation and informativeness of the features), it is also possible to generate synthetic data.

scikit-learn comes with a few small standard datasets that do not require to download any file from some external website.

They can be loaded using the following functions:

load_boston([return_X_y])	Load and return the boston house-prices dataset (regression).
load_iris([return_X_y])	Load and return the iris dataset (classification).
load_diabetes([return_X_y])	Load and return the diabetes dataset (regression).
load_digits([n_class, return_X_y])	Load and return the digits dataset (classification).
load_linnerud([return_X_y])	Load and return the linnerud dataset (multivariate regression).
load_wine([return_X_y])	Load and return the wine dataset (classification).
load_breast_cancer([return_X_y])	Load and return the breast cancer wisconsin dataset (classification).


#%%
scikit-learn provides tools to load larger datasets, downloading them if necessary.

They can be loaded using the following functions:

fetch_olivetti_faces([data_home, shuffle, …])	Load the Olivetti faces data-set from AT&T (classification).
fetch_20newsgroups([data_home, subset, …])	Load the filenames and data from the 20 newsgroups dataset (classification).
fetch_20newsgroups_vectorized([subset, …])	Load the 20 newsgroups dataset and vectorize it into token counts (classification).
fetch_lfw_people([data_home, funneled, …])	Load the Labeled Faces in the Wild (LFW) people dataset (classification).
fetch_lfw_pairs([subset, data_home, …])	Load the Labeled Faces in the Wild (LFW) pairs dataset (classification).
fetch_covtype([data_home, …])	Load the covertype dataset (classification).
fetch_rcv1([data_home, subset, …])	Load the RCV1 multilabel dataset (classification).
fetch_kddcup99([subset, data_home, shuffle, …])	Load the kddcup99 dataset (classification).
fetch_california_housing([data_home, …])	Load the California housing dataset (regression).