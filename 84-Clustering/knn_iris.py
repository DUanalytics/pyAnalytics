#Topic: KNN using iris
#-----------------------------
#https://stackabuse.com/k-nearest-neighbors-algorithm-in-python-and-scikit-learn/
#libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#df = pd.read_csv('data/mtcars.csv')
#pip install pydataset
from pydataset import data
iris = data('iris')
df = iris
df.head()
#split our dataset into its attributes and labels. X variable contains the first four columns of the dataset (i.e. attributes) while y contains the labels
df.columns
X = df.iloc[:, :-1].values
y = df.iloc[:, 4].values
X[0:2]
y[0:2]
df.head(2)

#Split Dataset : Train and Test (20%)
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20)
#splits the dataset into 80% train data and 20% test data. This means that out of total 150 records, the training set will contain 120 records and the test set contains 30 of those records.
X_train.shape
y_test.shape

#Feature Scaling
#Before making any actual predictions, it is always a good practice to scale the features so that all of them can be uniformly evaluated

from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
scaler.fit(X_train)

X_train = scaler.transform(X_train)
X_test = scaler.transform(X_test)
X_train[0:2]
X_test[0:2]

#Training and Predictions
#train the KNN algorithm and make predictions: using Scikit-Learn.

from sklearn.neighbors import KNeighborsClassifier
classifier = KNeighborsClassifier(n_neighbors=5)
#read/see video about KNN
classifier.fit(X_train, y_train)
#mport the KNeighborsClassifier class from the sklearn.neighbors library. In the second line, this class is initialized with one parameter, i.e. n_neigbours. This is basically the value for the K. There is no ideal value for K and it is selected after testing and evaluation, however to start out, 5 seems to be the most commonly used value for KNN algorithm.

#final step is to make predictions on our test data. To do so, execute the following script:
y_pred = classifier.predict(X_test)
y_pred

#Evaluating the Algorithm
#For evaluating an algorithm, confusion matrix, precision, recall and f1 score are the most commonly used metrics. The confusion_matrix and classification_report methods of the sklearn.metrics can be used to calculate these metrics. Take a look at the following script:

from sklearn.metrics import classification_report, confusion_matrix
print(confusion_matrix(y_test, y_pred))
print(classification_report(y_test, y_pred))

#The results show that our KNN algorithm was able to classify all the 30 records in the test set with almost 100% accuracy, which is excellent. Although the algorithm performed very well with this dataset, don't expect the same results with all applications. As noted earlier, KNN doesn't always perform as well with high-dimensionality or categorical features.


#k value : Comparing Error Rate with the K Value
#In the training and prediction section we said that there is no way to know beforehand which value of K that yields the best results in the first go. We randomly chose 5 as the K value and it just happen to result in 100% accuracy.
#One way to help you find the best value of K is to plot the graph of K value and the corresponding error rate for the dataset.
#In this section, we will plot the mean error for the predicted values of test set for all the K values between 1 and 40.
#To do so, let's first calculate the mean of error for all the predicted values where K ranges from 1 and 40. Execute the following script:

#manual way
error =[]
#change value of n_neigbours manually
knn = KNeighborsClassifier(n_neighbors=1)
knn.fit(X_train, y_train)
pred_i = knn.predict(X_test)
np.mean(pred_i != y_test)
error.append(np.mean(pred_i != y_test))
error

#Let use loop now
error = []
#check values ???
# Calculating error for K values between 1 and 40
for i in range(1, 40):
    knn = KNeighborsClassifier(n_neighbors=i)
    knn.fit(X_train, y_train)
    pred_i = knn.predict(X_test)
    error.append(np.mean(pred_i != y_test))
#The above script executes a loop from 1 to 40. In each iteration the mean error for predicted values of test set is calculated and the result is appended to the error list. The next step is to plot the error values against K values. Execute the following script to create the plot:
error
plt.figure(figsize=(12, 6))
plt.plot(range(1, 40), error, color='red', linestyle='dashed', marker='o', markerfacecolor='blue', markersize=10)
plt.title('Error Rate K Value')
plt.xlabel('K Value')
plt.ylabel('Mean Error')

#From the output we can see that the mean error is zero when the value of the K is between 5 and 18. I would advise you to play around with the value of K to see how it impacts the accuracy of the predictions.

