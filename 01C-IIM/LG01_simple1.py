#Topic:Logistic Regression
#-----------------------------
#libraries
#S1 : libraries
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix
import seaborn as sns
#%%S2 sklearn
#create data

#S1 : Data
x = np.arange(10).reshape(-1, 1)
x
x.shape  #IV can be more than 1 variable also
y = np.array([0, 0, 0, 0, 1, 1, 1, 1, 1, 1])
y
#S3: model
model = LogisticRegression(solver='liblinear', random_state=0)
model.fit(x, y)
model = LogisticRegression(solver='liblinear', random_state=0).fit(x, y)
x
model.classes_
model.intercept_
model.coef_  #odd ratio

#S4 : Evaluate Model
y
model.predict_proba(x)  #prob of 0 & 1 class
#each corresponds to single observation. ie prob of class being 0 & 1 for value 1 is .629 & .37 resp
x, y
model.predict(x)  #actual predictions : which is on higher side. since prob for value 1 was .629, hence class is 0

y
model.score(x,y)  # accuracy using confusion matrix
# 9 out 10 times prediction was correct like original data

confusion_matrix(y, model.predict(x))
#TN FP
#FN TP 
#we want more TN(Acutal-0, Predict-0) & TP
#FN (Actual-1, Predict-0)
y
cm = confusion_matrix(y, model.predict(x))
cm
sns.heatmap(cm, annot=True)
(3+6)/10
#report
classification_report(y, model.predict(x))


#%% scikit-learn

#S1 : libraries
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix
#S2 : data
x = np.arange(10).reshape(-1, 1)
y = np.array([0, 0, 0, 0, 1, 1, 1, 1, 1, 1])
x
y
#S3: Model - Train
model = LogisticRegression(solver='liblinear')
model.fit(x, y)
#S4: Evaluate
p_pred = model.predict_proba(x)
p_pred
y_pred = model.predict(x)
score_ = model.score(x, y)
conf_m = confusion_matrix(y, y_pred)
report = classification_report(y, y_pred)
x
y
model.intercept_
model.coef_
p_pred  #prob values
y_pred  #class
score_
conf_m
report

#Stats Model


#Logistic Regression - fundamental classification technique
#Other Classification Technique - knn, naivebayes, decisin trees, randomforest


#further reading
#https://realpython.com/logistic-regression-python/
