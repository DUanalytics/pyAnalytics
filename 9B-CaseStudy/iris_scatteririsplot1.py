#Plots - Iris - Categories
#%

import pandas as pd
df = pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data', header=None)
df.tail()
df.shape
import matplotlib.pyplot as plt
import numpy as np
y = df.iloc[0:100, 4].values
y[1:15]
y = np.where(y == 'Iris-setosa', -1, 1)
y[1:15]
X = df.iloc[0:100, [0, 2]].values
X[1:15]

plt.scatter(X[:50, 0], X[:50, 1], color='red', marker='o', label ='setosa')
plt.scatter(X[50:100, 0], X[50:100, 1], color='blue', marker='x', label='versicolor')
plt.xlabel('petal length')
plt.ylabel('sepal length')
plt.legend(loc='upper left')
plt.show();