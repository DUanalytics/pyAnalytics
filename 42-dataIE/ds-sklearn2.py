#Topic: Data Sets - sklearn
#-----------------------------
#libraries
#https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_breast_cancer.html#sklearn.datasets.load_breast_cancer
from sklearn.datasets import load_breast_cancer
data = load_breast_cancer()
data.data
#Let’s say you are interested in the samples 10, 50, and 85, and want to know their class name.
data.target[[10, 50, 85]]
#array([0, 1, 0])
list(data.target_names)
#['malignant', 'benign']
