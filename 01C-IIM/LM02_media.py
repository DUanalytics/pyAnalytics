#Topic: Linear Regression 2 Media Coy Case
#-----------------------------
#libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#read data
#media = pd.DataFrame(pd.read_csv('data/mediacompany.csv'))
url ='https://raw.githubusercontent.com/DUanalytics/pyAnalytics/master/data/mediacompany.csv'
media = pd.DataFrame(pd.read_csv(url))

media.head()

#check duplicates
sum(media.duplicated(subset = 'Date')) == 0
#if duplicates value will not be = 0

#remove last column
media = media.drop('Unnamed: 7', axis=1)
media.head()

#description
media.describe
media.shape
media.info()

#null values check
media.isnull().sum()  #each col

#outlier analysis
media.dtypes
fig, axs = plt.subplots(2,2, figsize = (10,5))
plt1 = sns.boxplot(media['Views_show'], ax = axs[0,0])
plt1 = sns.boxplot(media['Visitors'], ax = axs[0,1])
plt1 = sns.boxplot(media['Views_platform'], ax = axs[1,0])
plt1 = sns.boxplot(media['Ad_impression'], ax = axs[1,1])
plt.tight_layout()
plt.show();

#date format
media['Date'] = pd.to_datetime(media['Date'], dayfirst = False)
media.dtypes
media.head

#weekday from date
media['Day_of_week'] = media['Date'].dt.dayofweek
media.head()

#exploratory Data Analysis

#Views Show
sns.boxplot(media['Views_show'])

#univariate analysis
media.plot.line(x='Date', y='Views_show')

#DOW
sns.barplot(data = media, x='Day_of_week', y='Views_show')
#which week it was highest - Sun, Sat
#weekdays and weekend(1)
di={5:1, 6:1, 0:0, 1:0, 2:0, 3:0, 4:0} #dictionary
media['weekend'] = media['Day_of_week'].map(di)
media.head()

#weekends
sns.barplot(data = media, x='weekend', y='Views_show')
#higher on weekends

#Ad impressions
ax = media.plot(x='Date', y='Views_show', legend=False)
ax2 = ax.twinx()
media.plot(x='Date', y='Ad_impression', ax=ax2, legend=False, color='r')
ax.figure.legend()
plt.show()

sns.scatterplot(data=media, x='Ad_impression', y='Views_show')

#visitors
sns.scatterplot(data=media, x='Visitors', y='Views_show')

#Views platform
sns.scatterplot(data=media, x='Views_platform', y='Views_show')
#some views are some what proportional related to Platform views

#cricket match
sns.barplot(data = media, x='Cricket_match_india', y='Views_show')
#drop in views in some shows due to cricket match

#character A
sns.barplot(data = media, x='Character_A', y='Views_show')
#presence of Character A improves show viewership


#%%% Model Building
from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()
#scale data ex Yes/No, Ad_impression
num_vars = ['Views_show', 'Visitors', 'Views_platform', 'Ad_impression']
media[num_vars] = scaler.fit_transform(media[num_vars])
media.head()

sns.heatmap(media.corr(), annot=True)

#Model1
X= media[['Visitors', 'weekend']]
X
y = media['Views_show']

from sklearn.linear_model import LinearRegression
lm = LinearRegression()
lm.fit(X,y)
lm.score(X,y)
lm.coef_

#different library: Constant term has to be added here
import statsmodels.api as sm
#need to fit constant
X = sm.add_constant(X)
lm_1 = sm.OLS(y, X).fit()
print(lm_1.summary())
#significnt variables - weekends, Visitors. P>|t| : .05 

#2nd model : keep changing the combination of variables 
X= media[{'Visitors', 'weekend', 'Character_A'}]
y=media['Views_show']
import statsmodels.api as sm
X=sm.add_constant(X)
lm_2 = sm.OLS(y, X).fit()
print(lm_2.summary())



#like this keep creating model. Model which has higher AdjR2 is better.
#see more from here
#(https://www.kaggle.com/ashydv/media-company-case-study-linear-regression)
