#python : Topic : KNN  Aug 2020
#https://towardsdatascience.com/k-nearest-neighbor-python-2fccc47d2a55
#https://www.youtube.com/watch?v=UqYde-LULfs
#https://www.youtube.com/watch?v=wTF6vzS9fy4
#https://www.youtube.com/watch?v=6kZ-OPLNcgE&t=1s
#standard libaries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#from pydataset import data
import seaborn as sns
#additional libraries
from sklearn.datasets import load_breast_cancer
from sklearn.metrics import confusion_matrix, accuracy_score
#https://scikit-learn.org/stable/modules/generated/sklearn.metrics.accuracy_score.html
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
sns.set()
#The dataset classifies tumors into two categories (malignant and benign) and contains something like 30 features. In the real world, you’d look at the correlations and select a subset of features that plays the greatest role in determining whether a tumor is malignant or not. However, for the sake of simplicity, we’ll pick a couple at random. We must encode categorical data for it to be interpreted by the model (i.e. malignant = 0 and benign = 1).
breast_cancer = load_breast_cancer()
breast_cancer
X = pd.DataFrame(breast_cancer.data, columns=breast_cancer.feature_names)
X.head()
X = X[['mean area', 'mean compactness']]  #selected columns
y = pd.Categorical.from_codes(breast_cancer.target, breast_cancer.target_names)
y
y = pd.get_dummies(y, drop_first=True)
y  #one column 1- benign True(1), cancer present
#point of building a model, is to classify new data with undefined labels. Therefore, we need to put aside data to verify whether our model does a good job at classifying the data. By default, train_test_split sets aside 25% of the samples in the original dataset for testing.
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=1)
X_train.shape, X_test.shape 
#he sklearn library has provided a layer of abstraction on top of Python. Therefore, in order to make use of the KNN algorithm, it’s sufficient to create an instance of KNeighborsClassifier. By default, the KNeighborsClassifier looks for the 5 nearest neighbors. We must explicitly tell the classifier to use Euclidean distance for determining the proximity between neighboring points.
knn = KNeighborsClassifier(n_neighbors=5, metric='euclidean')
knn.fit(X_train, y_train)

#Using our newly trained model, we predict whether a tumor is benign or not given its mean compactness and area.
y_pred = knn.predict(X_test)
y_pred
#We visually compare the predictions made by our model with the samples inside the testing set.
sns.scatterplot( x='mean area',    y='mean compactness',  hue='benign',     data=X_test.join(y_test, how='outer'))
#
plt.scatter( X_test['mean area'],     X_test['mean compactness'], c=y_pred,     cmap='coolwarm',  alpha=0.7)
#Another way of evaluating our model is to compute the confusion matrix. The numbers on the diagonal of the confusion matrix correspond to correct predictions whereas the others imply false positives and false negatives.
confusion_matrix(y_test, y_pred)
#Given our confusion matrix, our model has an accuracy of 121/143 = 84.6%.
accuracy_score(y_test, y_pred)
#The K Nearest Neighbors algorithm doesn’t require any additional training when new data becomes available. Rather it determines the K closest points according to some distance metric (the samples must reside in memory). Then, it looks at the target label for each of the neighbors and places the new found data point into the same category as the majority. Given that KNN computes distance, it’s imperative that we scale our data. In addition, since KNN disregards the underlying features, it’s our responsibility to filter out any features that are deemed irrelevant.