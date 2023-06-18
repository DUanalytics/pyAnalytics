#Topic:Partition DF pandas

#-----------------------------
#libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pydataset import data
mtcars = data('mtcars')
mtcars.head()
df = mtcars
#%%  Numpy random
msk = np.random.rand(len(df)) < 0.8
#create random no and filter all values < .8
msk
len(msk)
train = df[msk]
test = df[~msk]
train
test
#%%%  sklearn
from sklearn.model_selection import train_test_split
train, test = train_test_split(df, test_size=0.2)
train
test

#%%  Sample
train=df.sample(frac=0.8,random_state=200)
test=df.drop(train.index)
train
test
#%%
#   gets a random 80% of the entire set
X_train = df.sample(frac=0.8, random_state=1)
X_train
#gets the left out portion of the dataset
X_test = df.loc[ ~ df.index.isin(X_train.index)]
X_test
len(X_train)
len(X_test)

#%% Kfold 
from sklearn.model_selection import KFold

kf = KFold(n_splits=10)
y_hat_all = []
df.columns
X=df.drop(labels=['mpg'], axis=1)
y=df.mpg
for train_index, test_index in kf.split(X, y):
    reg = RandomForestRegressor(n_estimators=50, random_state=0)
    X_train, X_test = X[train_index], X[test_index]
    y_train, y_test = y[train_index], y[test_index]
    clf = reg.fit(X_train, y_train)
    y_hat = clf.predict(X_test)
    y_hat_all.append(y_hat)

#%%Case 3a: Unbalanced datasets for classification purpose. Following the case 1, here is the equivalent solution:
X
y
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y, test_size=0.3)

#%%%
import pandas as pd
from sklearn.model_selection import train_test_split
datafile_name = 'path_to_data_file'
data = pd.read_csv(datafile_name)
data=df
#target_attribute = data['column_name']
target_attribute = data['mpg']
data = data.drop(columns = ['mpg'], axis = 1) 
X_train, X_test, y_train, y_test = train_test_split(data, target_attribute, test_size=0.2)
X_train
X_test
y_train
y_test
df.applymap(lambda x: len(str(x)))
pd.applymap?
pd.applymaplen(X_train,X_test)

#%%%To split into more than two classes such as train, test, and validation, one can do:
probs = np.random.rand(len(df))
training_mask = probs < 0.7
test_mask = (probs>=0.7) & (probs < 0.85)
validation_mask = probs >= 0.85
probs
training_mask
validation_mask
df_training = df[training_mask]
df_test = df[test_mask]
df_validation = df[validatoin_mask]
#This will put 70% of data in training, 15% in test, and 15% in validation.
df_training
df_test
df_validation
