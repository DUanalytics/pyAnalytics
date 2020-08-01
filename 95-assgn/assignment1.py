#Topic: Assignments
#-----------------------------

#%% Linear Regression -1 Marketing Data - Sales - YT, FB, print
#libraries
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
from sklearn import linear_model #1st method
import statsmodels.api as sm  #2nd method
import matplotlib.pyplot as plt
import seaborn as sns

url ='https://raw.githubusercontent.com/DUanalytics/datasets/master/R/marketing.csv'
marketing = pd.read_csv(url)
marketing.head()

#describe data

#visualise few plots to check correlation

#split data into train and test

#build the model

#predict on test values

#find metrics - R2, Adjt R2, RMSE, MAPE etc

#predict on new value
newdata = pd.DataFrame({'youtube':[50,60,70], 'facebook':[20, 30, 40], 'newspaper':[70,75,80]})
newdata
#your ans should be close to [ 9.51, 11.85, 14.18] 

#conclude by few lines



#%% Logistic Regression
