#Topic: Random Forests
#-----------------------------

# Importing the libraries 
import numpy as np 
import matplotlib.pyplot as plt 
import pandas as pd 

#data
from pydataset import data
mtcars = data('mtcars')
mtcars.head()
df = mtcars.copy()
df
df[['wt','hp']]

#%% Features and Target
X = df[['wt','hp']].values
X
y = df['mpg'].values  #s
y

## Fitting Random Forest Regression to the dataset 
# import the regressor 
from sklearn.ensemble import RandomForestRegressor 
  
 # create regressor object 
regressor = RandomForestRegressor(n_estimators = 100, random_state = 0) 
#nestimators = trees
  
# fit the regressor with x and y data 
regressor.fit(X, y)   
regressor.predict(X)
pd.DataFrame({'actual':df['mpg'], 'predict': regressor.predict(X),'diff':df['mpg'] - regressor.predict(X) })


df[['wt','hp']].head()
newData = np.array([2.7, 120]).reshape(1, 2)
newData
ypred1 = regressor.predict(newData)  # test the output by changing values 
ypred1

#%% Features and Target
#classification

X2 = df[['wt','hp']].values
X2
y2 = df['am'].values  #s
y2

## Fitting Random Forest Regression to the dataset 
# import the regressor 
from sklearn.ensemble import RandomForestClassifier 
  
 # create regressor object 
classifier = RandomForestClassifier(n_estimators = 100, random_state = 0) 
  
# fit the regressor with x and y data 
classifier.fit(X2, y2)   
classifier.predict(X2)
classifier.predict_proba(X2)
classifier.score(X2,y2)
pd.DataFrame({'actual':df['am'], 'predict': classifier.predict(X2),'diff':df['am'] - classifier.predict(X2) })

from sklearn.metrics import confusion_matrix
confusion_matrix(y2, classifier.predict(X2))


df[['wt','hp']].head()
newData = np.array([2.7, 120]).reshape(1, 2)
newData
ypred2 = classifier.predict(newData)  # test the output by changing values 
ypred2



#https://www.geeksforgeeks.org/random-forest-regression-in-python/


