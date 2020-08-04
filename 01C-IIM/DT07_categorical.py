#Topic: DT using Categorical values
#-----------------------------
#libraries

import pandas as pd
from sklearn.tree import DecisionTreeClassifier
data = pd.DataFrame()
data['subject1'] = ['B', 'A', 'C', 'A', 'B']
data['age'] = [25, 27, 30, 28, 16]
data['gender'] = ['M','F','M','F', 'F']
data['exam'] = ['Pass','Fail','Pass', 'Fail', 'Pass']
data
df = data.copy()
df
tree = DecisionTreeClassifier()
data.iloc[:,0:3]
data.iloc[:,:-1]
X=data[['subject1', 'age', 'gender']]
data.iloc[:,-1]
data.iloc[:,3]
y=data['exam']
X,y
tree.fit(X, y )  #error
#cannot convert string to float

data
data['exam'] = data['exam'].astype('category')
data
data.dtypes
X=data[['subject1', 'age', 'gender']]
y=data['exam']
X,y
tree.fit(X, y )  #error

#other columns
from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
le.fit(X['gender'].astype(str))
le.transform(X['gender']).astype(str)
data['gender']

#now do it for other categorical columns
data
le=LabelEncoder()
le.fit(data['subject1'].astype(str))
data['subject1'] = le.transform(data['subject1'].astype(str))

le.fit(data['gender'].astype(str))
data['gender'] = le.transform(data['gender'].astype(str))
data

df
#this could have been manually also
data.dtypes
X=data[['subject1', 'age', 'gender']]
y=data['exam']
X,y
tree.fit(X, y )  #now working
data.iloc[0:1,:-1]
tree.predict(data.iloc[0:1,-1])  #cannot use original data format
#need to have numerical encodings

newdata = pd.DataFrame({'subject':[0,1], 'age':[22,24], 'gender':[1,1]})
newdata
tree.predict(newdata)
data
newdata['predicted'] = tree.predict(newdata)
newdata
