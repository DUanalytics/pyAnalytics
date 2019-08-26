#Topic ----Logistic Regression : Banking
#https://towardsdatascience.com/building-a-logistic-regression-in-python-step-by-step-becd4d56c9c8
#Logistic Regression is a Machine Learning classification algorithm that is used to predict the probability of a categorical dependent variable. In logistic regression, the dependent variable is a binary variable that contains data coded as 1 (yes, success, etc.) or 0 (no, failure, etc.). In other words, the logistic regression model predicts P(Y=1) as a function of X.

import pandas as pd
import numpy as np
from sklearn import preprocessing
import matplotlib.pyplot as plt 
plt.rc("font", size=14)
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
import seaborn as sns
path='https://raw.githubusercontent.com/madmashup/targeted-marketing-predictive-engine/master/banking.csv'
data = pd.read_csv(path)
data.head()
data.columns
data.dtypes
data.shape

#%%%
sns.set(style="white")
sns.set(style="whitegrid", color_codes=True)


#%%%Predict variable (desired target):
#y — has the client subscribed a term deposit? (binary: “1”, means “Yes”, “0” means “No”) ;The education column of the dataset has many categories and we need to reduce the categories for a better modelling. The education column has the following categories:
data.education.unique()
#group “basic.4y”, “basic.9y” and “basic.6y” together and call them “basic”.
data['education']= np.where(data['education'] =='basic.9y', 'Basic', data['education'])
data['education']=np.where(data['education'] =='basic.6y', 'Basic', data['education'])
data['education']=np.where(data['education'] =='basic.4y', 'Basic', data['education'])
data.education.unique()

#%%%Data exploration
data['y'].unique()
data['y'].value_counts()
sns.countplot(x='y', data=data, palette='hls')
plt.show();

#%%
count_no_sub = len(data[data['y']==0])
count_sub = len(data[data['y']==1])
pct_of_no_sub = count_no_sub/(count_no_sub+count_sub)
print("percentage of no subscription is", pct_of_no_sub*100)
pct_of_sub = count_sub/(count_no_sub+count_sub)
print("percentage of subscription", pct_of_sub*100)
#Our classes are imbalanced, and the ratio of no-subscription to subscription instances is 89:11. Before we go ahead to balance the classes, let’s do some more exploration.
data.groupby('y').mean()

#%%%Observations:
#The average age of customers who bought the term deposit is higher than that of the customers who didn’t.
#The pdays (days since the customer was last contacted) is understandably lower for the customers who bought it. The lower the pdays, the better the memory of the last call and hence the better chances of a sale.
#Surprisingly, campaigns (number of contacts or calls made during the current campaign) are lower for customers who bought the term deposit.
#We can calculate categorical means for other categorical variables such as education and marital status to get a more detailed sense of our data.
#%%
data.columns
data.groupby('job').mean()
data.groupby('marital').mean()
#....
#%%%Visualizations
#%matplotlib inline
#plt.figure(figsize=(10,8))
pd.crosstab(data.job, data.y).plot(kind='bar', figsize=(10,8))
plt.title('Purchase Frequency for Job Title')
plt.xlabel('Job')
plt.ylabel('Frequency of Purchase')
#plt.savefig('purchase_fre_job')
plt.show();

#%%%The frequency of purchase of the deposit depends a great deal on the job title. Thus, the job title can be a good predictor of the outcome variable.
table=pd.crosstab(data.marital,data.y)
table.div(table.sum(1).astype(float), axis=0).plot(kind='bar', stacked=True)
plt.title('Stacked Bar Chart of Marital Status vs Purchase')
plt.xlabel('Marital Status')
plt.ylabel('Proportion of Customers')
#plt.savefig('mariral_vs_pur_stack')

#The marital status does not seem a strong predictor for the outcome variable.

#%%%
table=pd.crosstab(data.education,data.y)
table.div(table.sum(1).astype(float), axis=0).plot(kind='bar', stacked=True)
plt.title('Stacked Bar Chart of Education vs Purchase')
plt.xlabel('Education')
plt.ylabel('Proportion of Customers')
#plt.savefig('edu_vs_pur_stack')

#Education seems a good predictor of the outcome variable.

#%%%
pd.crosstab(data.day_of_week,data.y).plot(kind='bar')
plt.title('Purchase Frequency for Day of Week')
plt.xlabel('Day of Week')
plt.ylabel('Frequency of Purchase')
#plt.savefig('pur_dayofweek_bar')
#Day of week may not be a good predictor of the outcome.
#%%%
pd.crosstab(data.month,data.y).plot(kind='bar')
plt.title('Purchase Frequency for Month')
plt.xlabel('Month')
plt.ylabel('Frequency of Purchase')
#plt.savefig('pur_fre_month_bar')
#Month might be a good predictor of the outcome variable.

#%%%
data.age.hist()
plt.title('Histogram of Age')
plt.xlabel('Age')
plt.ylabel('Frequency')
#plt.savefig('hist_age')
#Most of the customers of the bank in this dataset are in the age range of 30–40.


#%%%
pd.crosstab(data.poutcome,data.y).plot(kind='bar')
plt.title('Purchase Frequency for Poutcome')
plt.xlabel('Poutcome')
plt.ylabel('Frequency of Purchase')
#plt.savefig('pur_fre_pout_bar')
#Poutcome seems to be a good predictor of the outcome variable.


#%%%Create dummy variables:That is variables with only two values, zero and one.

cat_vars=['job','marital','education','default','housing','loan','contact','month','day_of_week','poutcome']
for var in cat_vars:
    cat_list='var'+'_'+var
    cat_list = pd.get_dummies(data[var], prefix=var)
    data1=data.join(cat_list)
    data=data1
cat_vars
cat_list
cat_vars=['job','marital','education','default','housing','loan','contact','month','day_of_week','poutcome']
data_vars=data.columns.values.tolist()
to_keep=[i for i in data_vars if i not in cat_vars]

#final data columns will be:
data_final=data[to_keep]
data_final.columns.values



#%%%SMOTE:Over-sampling using SMOTE
#http://imbalanced-learn.org/en/stable/over_sampling.html#smote-variants

X = data_final.loc[:, data_final.columns != 'y']
y = data_final.loc[:, data_final.columns == 'y']
#%%%
import statsmodels.api as sm
logit_model=sm.Logit(y,X)
result=logit_model.fit()
print(result.summary2())

#%%%The p-values for most of the variables are smaller than 0.05, except four variables, therefore, we will remove them.
cols=['euribor3m', 'job_blue-collar', 'job_housemaid', 'marital_unknown', 'education_illiterate', 'month_apr', 'month_aug', 'month_dec', 'month_jul', 'month_jun', 'month_mar', 'month_may', 'month_nov', 'month_oct', "poutcome_failure", "poutcome_success"] 
X=X[cols]
y=y['y']
logit_model=sm.Logit(y,X)
result=logit_model.fit()
print(result.summary2())


#%%%
from sklearn.linear_model import LogisticRegression
from sklearn import metrics
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)
logreg = LogisticRegression()
logreg.fit(X_train, y_train)

y_pred = logreg.predict(X_test)
print('Accuracy of logistic regression classifier on test set: {:.2f}'.format(logreg.score(X_test, y_test)))

from sklearn.metrics import confusion_matrix
confusion_matrix = confusion_matrix(y_test, y_pred)
print(confusion_matrix)

from sklearn.metrics import classification_report
print(classification_report(y_test, y_pred))

#%%%from sklearn.metrics import roc_auc_score
from sklearn.metrics import roc_curve
from sklearn import metrics
metrics.roc_curve(y_test,  y_pred_proba)
logit_roc_auc = metrics.roc_curve(y_test, logreg.predict(X_test))
logit_roc_auc
fpr, tpr, thresholds = metrics.roc_curve(y_test, logreg.predict_proba(X_test)[:,1])
fpr
tpr
thresholds

plt.figure()
plt.plot(fpr, tpr, label='Logistic Regression (area = %0.2f)' + str(logit_roc_auc))
#plt.plot(fpr, tpr, label='Logistic Regression (area = %0.2f)' % logit_roc_auc))
plt.plot([0, 1], [0, 1],'r--')
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.05])
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('Receiver operating characteristic')
plt.legend(loc="lower right")
#plt.savefig('Log_ROC')
plt.show();
#%%%The receiver operating characteristic (ROC) curve is another common tool used with binary classifiers. The dotted line represents the ROC curve of a purely random classifier; a good classifier stays as far away from that line as possible (toward the top-left corner).

#https://github.com/susanli2016/Machine-Learning-with-Python/blob/master/Logistic%20Regression%20balanced.ipynb

#%%%

from imblearn.over_sampling import SMOTE
os = SMOTE(random_state=0)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)
columns = X_train.columns
os_data_X,os_data_y=os.fit_sample(X_train, y_train)
os_data_X = pd.DataFrame(data=os_data_X,columns=columns )
os_data_y= pd.DataFrame(data=os_data_y,columns=['y'])
# we can Check the numbers of our data
print("length of oversampled data is ",len(os_data_X))
print("Number of no subscription in oversampled data",len(os_data_y[os_data_y['y']==0]))
print("Number of subscription",len(os_data_y[os_data_y['y']==1]))
print("Proportion of no subscription data in oversampled data is ",len(os_data_y[os_data_y['y']==0])/len(os_data_X))
    print("Proportion of subscription data in oversampled data is ",len(os_data_y[os_data_y['y']==1])/len(os_data_X))
    
    
    