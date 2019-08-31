#Topic ---- Logistic Regression : Admit ~ Rank etc
#https://stats.idre.ucla.edu/r/dae/logit-regression/

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
path="https://stats.idre.ucla.edu/stat/data/binary.csv"
data = pd.read_csv(path)
data.head()
data.columns
data.dtypes
data.shape
data.std(axis=0)
#%%% Summary
data.groupby(['admit','rank'], as_index=False).size()
data.groupby(['admit','rank'], as_index=False).size().plot(kind='bar')

#%%
from sklearn.linear_model import LogisticRegression
# instantiate the model (using the default parameters)
logreg = LogisticRegression()
data.columns
X = data[['gre','gpa','rank']] # Features
X.head()
rank = pd.get_dummies(X['rank'],drop_first=True)
rank.head()
X.head()
X.drop(['rank'],axis=1,inplace=True)
X.head()
X=pd.concat([X, rank],axis=1)
X.head()
y = data.admit # Target variable
X.head()
# fit the model with data
logreg.fit(X,y)

y_pred=logreg.predict(X)
y_pred


#%%%%
import statsmodels.api as sm
logit_model=sm.Logit(y,X)
result2=logit_model.fit()
print(result2.summary2())
print(result2.summary2())


#%%% Confusion Matrix
from sklearn import metrics
cnf_matrix = metrics.confusion_matrix(y, y_pred)
cnf_matrix

#%%

import seaborn as sns
class_names=[0,1] # name  of classes
fig, ax = plt.subplots()
tick_marks = np.arange(len(class_names))
plt.xticks(tick_marks, class_names)
plt.yticks(tick_marks, class_names)
# create heatmap
sns.heatmap(pd.DataFrame(cnf_matrix), annot=True, cmap="YlGnBu" ,fmt='g')
ax.xaxis.set_label_position("top")
plt.tight_layout()
plt.title('Confusion matrix', y=1.1)
plt.ylabel('Actual label')
plt.xlabel('Predicted label')
plt.show();


#%%%



#%%%

