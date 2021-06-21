#Topic:Logistic Regression
#-----------------------------
#libraries

#In general, a binary logistic regression describes the relationship between the dependent binary variable and one or more independent variable/s.

#The binary dependent variable has two possible outcomes:
#‘1’ for true/success; or
#‘0’ for false/failure

#case : let’s say that your goal is to build a logistic regression model in Python in order to determine whether candidates would get admitted to a prestigious university.
#there are two possible outcomes: Admitted (represented by the value of ‘1’) vs. Rejected (represented by the value of ‘0’).

#libraries
import pandas as pd # used to create the DataFrame to capture the dataset in Python
#sklearn    # used to build the logistic regression model in Python
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn import metrics
import seaborn as sns # used to create the Confusion Matrix
import matplotlib.pyplot as plt # used to display charts

#data from csv
# url = "https://stats.idre.ucla.edu/stat/data/binary.csv"
# df = pd.read_csv(url)
# df

#data
gmat =  [780,750,690,710,680,730,690,720,740, 690,610,690,710,680, 770,610,580, 650,540, 590,620, 600,550,550, 570,670,660,580,650,660,640,620,660, 660,680,650,670,580,590,690]
gpa =  [4,3.9,3.3,3.7,3.9,3.7, 2.3,3.3,3.3,1.7,2.7, 3.7,3.7,3.3,3.3, 3,2.7,3.7,2.7,2.3, 3.3, 2,2.3,2.7,3,3.3,3.7,2.3, 3.7,3.3,3,2.7, 4,3.3,3.3,2.3,2.7,3.3,1.7, 3.7]
work_experience = [3,4,3,5,4,6,1,4,5,1,3,5, 6,4,3,1,4,6,2,3,2,1,4,1,2,6,4,2,6, 5,1,2,4,6,5,1,2,1,4,5]
admitted = [1,1,0,1, 0,1,0,1,1,0, 0,1,1,0,1,0,0,1, 0,0,1,0,0,0,0,1,1,0, 1,1,0,0,1,1,1, 0,0,0,0,1]

candidates = {'gmat':gmat, 'gpa': gpa, 'work_experience': work_experience ,'admitted': admitted  }
candidates
type(candidates)

df = pd.DataFrame(candidates,columns= ['gmat', 'gpa','work_experience','admitted'])
df.head()
df.dtypes

#set the independent variables (represented as X) and the dependent variable (represented as y):

X = df[['gmat', 'gpa','work_experience']] #array
y = df['admitted']
X, y

#split data : Then, apply train_test_split. For example, you can set the test size to 0.25, and therefore the model testing will be based on 25% of the dataset, while the model training will be based on 75% of the dataset:

X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.25,random_state=0)
X_train, X_test

#apply logistic regression
logistic_regression= LogisticRegression()
logistic_regression.fit(X_train,y_train)

y_pred=logistic_regression.predict(X_test)

#print the Accuracy and plot the Confusion Matrix:
print('Accuracy: ', metrics.accuracy_score(y_test, y_pred))
y_test
y_pred
confusion_matrix = pd.crosstab(y_test, y_pred, rownames=['Actual'], colnames=['Predicted'])
sns.heatmap(confusion_matrix, annot=True, cmap='coolwarm', annot_kws={'size':20}, cbar=False)
plt.show();

# TP = True Positives = 4
# TN = True Negatives = 4
# FP = False Positives = 1
# FN = False Negatives = 1
Accuracy = (4+4)/10  #(TP+TN)/Total .8
Accuracy

#Confusion Matrix with an Accuracy of 0.8 (may vary with sklearn version)

print (X_test) #test dataset
#original dataset (from step 1) had 40 observations. Since we set the test size to 0.25, then the confusion matrix displayed the results for 10 records (=40*0.25). These are the 10 test records:
print (y_pred) #predicted values
#The prediction was also made for those 10 records (where 1 = admitted, while 0 = rejected):
y_test, y_pred
type(y_test), type(y_pred)

    
#%%predict on new data set
#use the existing logistic regression model to predict whether the new candidates will get admitted. The new set of data can then be captured in a second DataFrame called df2:
    
new_candidates = {'gmat': [590,740,680,610,710], 'gpa': [2,3.7,3.3,2.3,3], 'work_experience': [3,4,6,1,5] }
new_candidates
df2 = pd.DataFrame(new_candidates,columns= ['gmat', 'gpa','work_experience'])
df2

y_pred2=logistic_regression.predict(df2)
print (df2)
print (y_pred2)
#The first and fourth candidates are not expected to be admitted, while the other candidates are expected to be admitted.
#df.concat(y_pred2)
pd.concat([df2, pd.Series(y_pred2)], axis=1, sort=False)


#end here..
