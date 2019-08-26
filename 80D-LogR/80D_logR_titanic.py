#Topic: Logistic Regression - Python - Titanic
#-----------------------------
#https://www.kaggle.com/mnassrib/titanic-logistic-regression-with-python
#libraries

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
#%matplotlib inline
url_train = 'https://raw.githubusercontent.com/DUanalytics/datasets/master/csv/titanic_train.csv'
url_test  ='https://raw.githubusercontent.com/DUanalytics/datasets/master/csv/titanic_test.csv'

train = pd.read_csv(url_train)
train.head()
train.count()
train.info()
train.describe()
#%%%
PassengerID-type should be integers
Survived-survived or not
Pclass-class of Travel of every passenger
Name- the name of the passenger
Sex -gender
Age-age of passengers
SibSp -No. of siblings/spouse aboard
Parch-No. of parent/child aboard
Ticket-Ticket number
Fare -what Prices they paid
Cabin -cabin number
Embarked-the port in which a passenger has embarked.
#%% Missing Data
sns.heatmap(train.isnull(),yticklabels=False,cbar=False,cmap='viridis')
#Roughly 20 percent of the Age data is missing. The proportion of Age missing is likely small enough for reasonable replacement with some form of imputation. Looking at the Cabin column, it looks like we are just missing too much of that data to do something useful with at a basic level. 

#%%Visualisation
#count-plot of people survided 
sns.set_style('whitegrid')
sns.countplot(x='Survived', hue='Sex', data=train, palette='RdBu_r')
#after looking at this graph we can tell that the people who did not survive were much more likely to be male and people who did survive were almost like twice as likely to be female
#no. of people who survived according to their Passenger Class
sns.set_style('whitegrid')
sns.countplot(x='Survived', hue='Pclass', data=train)
#after looking at this we can tell that people who did not survive were more likely to be belonging to third class i.e the lowest class, the cheapest to get on to and people who did survive were more towards belonging to higher classes.
#distribution plot of age of the people
sns.distplot(train['Age'].dropna(), kde=False, bins=30, color='Green')
#The average age group of people to survive is somewhere between 20 to 30and as older you get lesser chances of you to have on board.
##countplot of the people having siblings or spouce
sns.countplot(x='SibSp',data=train)
#looking at this plot we can directly tell that most people on board did not have either children, siblings or spouse on board and the second most popular option is 1which is more likely to be spouse. We have a lot of single people on board, they don’t have spouse or children.
#distribution plot of the ticket fare
train['Fare'].hist(color='green',bins=40,figsize=(8,4))
#It looks like most of the purchase prices are between 0 and50, which actually makes sense tickets are more distributed towards cheaper fare prices because most passengers are in cheaper third class.

#%%%Data Cleaning
#We want to fill in missing age data instead of just dropping the missing age data rows. One way to do this is by filling in the mean age of all the passengers. However, we can be smarter about this and check the average age by passenger class.
#boxplot with age on y-axis and Passenger class on x-axis.
plt.figure(figsize=(12, 7))
sns.boxplot(x='Pclass',y='Age',data=train,palette='winter');

#We can see the wealthier passengers in the higher classes tend to be older, which makes sense. We’ll use these average age values to impute based on Pclass for Age.
#function 
def impute_age(cols):
    Age = cols[0]
    Pclass = cols[1]
    if pd.isnull(Age):
        if Pclass == 1:  return 37
        elif Pclass == 2:  return 29
        else: return 24
    else:   return Age

#Now apply that function!
train['Age'] = train[['Age','Pclass']].apply(impute_age,axis=1)
#Now let’s check that heatmap again!
sns.heatmap(train.isnull(),yticklabels=False,cbar=False,cmap='viridis')
#Now let us go ahead and drop the Cabin column and the row in Embarked that is NaN.
train.drop('Cabin', axis=1,inplace=True)
sns.heatmap(train.isnull(),yticklabels=False,cbar=False,cmap='viridis')
train.dropna(inplace=True)
sns.heatmap(train.isnull(),yticklabels=False,cbar=False,cmap='viridis')
#No missing now
train.head()


#%%Converting Categorical Features
#We’ll need to convert categorical features to dummy variables using pandas! Otherwise, our machine learning algorithm won’t be able to directly take in those features as inputs.
sex = pd.get_dummies(train['Sex'],drop_first=True)
embark = pd.get_dummies(train['Embarked'],drop_first=True)
#drop the sex,embarked,name and tickets columns
train.drop(['Sex','Embarked','Name','Ticket'],axis=1,inplace=True)
#concatenate new sex and embark column to our train dataframe
train = pd.concat([train,sex,embark],axis=1)
#check the head of dataframe
train.head()
#%%%Now our data is ready for our model!

#%%%Building a Logistic Regression model
#Let’s start by splitting our data into a training set and test set(there is another test.csv file that you can play around with in case you want to use all this data for training).
#%%%
#Train Test Split
#X will contain all the features and y will contain the target variable
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split ( train.drop('Survived',axis=1), train['Survived'], test_size=0.30,      random_state=101)

#Here y is the actual data which we are going to predict, everything else is going to be the features(x).
#Set the test size to 30 percent and you don’t actually have to set your random state but this is put so if you want your result to match mines exactly.
#We will use train_test_split from the cross_validation module to split our data. 70%of the data will be training data and %30 will be testing data.
#%%%Training and Predicting
#Let’s use Logistic Regression to train the model

from sklearn.linear_model import LogisticRegression
#create an instance and fit the model 
logmodel = LogisticRegression()
logmodel.fit(X_train, y_train)
#We start by importing the LogisticRegression package from the Linear model family.Then create an instance of the logistic regression model and call it log model and then fit the model on the training dataset.
#Let’s see how accurate is our model for predictions
#predictions: Now we call some predictions based on the X_test dataset.
predictions = logmodel.predict(X_test)
#%%% Model Evaluation
#We can check precision, recall, f1-score using classification report and also see how accurate is our model for predictions:
from sklearn.metrics import classification_report
print(classification_report(y_test,predictions))
#81% accuracy which is not bad at all.

#%%Let us now see the confusion matrix:
#To evaluate our model for some specific values, it can be directly done from our confusion matrix.
from sklearn.metrics import confusion_matrix
print(confusion_matrix(y_test, predictions))

#%%%
#From our confusion matrix we conclude that:
True positive: 148(We predicted a positive result and it was positive)
True negative: 68(We predicted a negative result and it was negative)
False positive: 15(We predicted a positive result and it was negative)
False negative: 36(We predicted a negative result and it was positive)
Accuracy = (TP+TN)/total
Accuracy = (148+68)/267 ~ 81%
Error Rate = (FP+FN)/total
Error rate = (36+15)/267 ~19%

#%%%
The homogeneity of variance does not need to be always TRUE for the Logistic Regression model.
Logistic Regression uses maximum likelihood estimation (MLE) rather than ordinary least squares (OLS) to estimate the parameters, therefore its predictions depend upon large-sample approximations.
Logistic Regression does not assume a linear relationship between the dependent and the independent variables, but it will assume a linear relationship between the logic of the explanatory variables and the response.