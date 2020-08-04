#Topic: Categorical Variables
#-----------------------------
#libraries
from pydataset import data
data('titanic')
data1 = data('titanic')

data1.dtypes
data2 = data1.select_dtypes(include='object').copy()
data2

data2.isnull().sum()
data2.describe()
data2.survived.value_counts()
data2['class'].value_counts()
data2['age'].value_counts()
data2['sex'].value_counts()
data2['survived'].value_counts()

cleanup = ({'class':{'1st class':1, '2nd class':2, '3rd class':3}, 'sex': {'man':'M','women':'F'}})
cleanup
data2.replace(cleanup, inplace=True)
data2
data2.dtypes

#encoding
data2['survived'] = data2['survived'].astype('category')
data2
data2.dtypes
data2.survived.cat.codes
#Y-1, N-0

#dummies
data2
pd.get_dummies(data2, columns =['sex']).head()
pd.get_dummies(data2, columns =['sex'])

#hot encoding
import numpy as np
data2
np.where(data2['age'].str.contains('child'))
data2['ageCode'] = np.where(data2['age'].str.contains('child'), 0, 1)
data2



#Scikit-Learn
from sklearn.preprocessing import LabelEncoder
lb_make = LabelEncoder()
data2['ageCode'] = lb_make.fit_transform(data2['age'])
data2


#%%%
from pydataset import data
data('mtcars')
mtcars
df1 = data('mtcars')

df1.dtypes

labels = df1['gear'].astype('category').cat.categories.tolist()
counts = df1['gear'].value_counts()
labels
counts
sizes = [counts[var_cat] for var_cat in labels]
sizes

df1
replace_map ={'gear':{3:'G3', 4:'G4', 5:'G5'}}
df2 = df1.replace(replace_map, inplace=False).copy()
df2


#types of encoding - nominal(label), ordinal(orderd categories)
#encoding is required at pre-processing step when working with categorical data
#ordinal encoding for cat variables which have natural rank ordering
#one hot encoding for no order
#dummy variable encoding
sex ={'M', 'F', 'M'}
type(sex)
sex
import numpy as np 
import random
random.sample(sex, k=2)
random.sample(range(100),5)
random.sample(sex, k=3)  #k cannot be higher than list items

random.seed(123) 
random.choices(list(sex), k=5)  #it needs list item
sex=['M','F']
random.choices(sex, k=5, weights = (4,1))  #it needs list item
#M has the highest chance of occuring
random.choices(sex, k=5, cum_weights = (3/5,2/5)) 

from numpy.random import choice
choice(sex, 5, p=[.6, .4], replace=True)  #probability values-> sum to 1

import numpy as np
import pandas as pd
#nominal values

from sklearn.preprocessing import LabelEncoder
sex=['M','F']
gender = choice(sex, 10, p=[6/10, 4/10], replace=True)
gender
genderRS = gender.reshape(-1,1)
genderRS

Lencoder = LabelEncoder()
Lencoder.fit(genderRS)  #fit
genderE = Lencoder.fit_transform(genderRS) #fit and return values
genderE  #print
list(Lencoder.classes_) #categories

genderE.shape
genderE = genderE.reshape(-1,1)
len(genderE)
np.concatenate((genderRS, genderE), axis=1)

#%%% ordinal values
gradetypes = ['C','B','A']
#A > B > C
grades = choice(gradetypes, 10, p=[3/10, 4/10, 3/10], replace=True)
grades
grades.shape
gradesRS = grades.reshape(-1,1)
gradesRS
from sklearn.preprocessing import OrdinalEncoder
Oencoder = OrdinalEncoder()
gradesE = Oencoder.fit_transform(gradesRS)
gradesE
gradesE.shape
print(gradesE)
type(gradesE)
np.concatenate((gradesRS, gradesE), axis=1)


#%%% One Hot Encoding
from sklearn.preprocessing import OneHotEncoder
genderRS
Hencoder = OneHotEncoder(sparse=False)
Hencoder.fit(genderRS)
genderHE = Hencoder.transform(genderRS)
genderHE
genderRS
np.concatenate((genderRS, genderHE), axis=1)
#M - 0 ,1; F = 1, 0


#%%% dummy variable encoding - drop first level
from sklearn.preprocessing import OneHotEncoder
genderRS
DHencoder = OneHotEncoder(drop='first', sparse=False)
DHencoder.fit(genderRS)
genderDHE = DHencoder.transform(genderRS)
genderDHE
genderRS
np.concatenate((genderRS,  genderDHE), axis=1)
#one column less.. M has 1, F is 0 (Alphabet)
#when a person is female, gender has no value
np.concatenate((genderRS, genderHE, genderDHE), axis=1)
#M - 0 ,1; F = 1, 0


#%%% summary
#encoding has to be done column wise
#orginal column to be removed, and encoded to be used with data trainX
