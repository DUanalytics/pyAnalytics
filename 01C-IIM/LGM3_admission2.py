#Topic: Logistic Regression - GRE
#-----------------------------
#libraries

import pandas as pd
import statsmodels.api as sm
import pylab as pl
import numpy as np

# read the data in
url = "https://stats.idre.ucla.edu/stat/data/binary.csv"
df = pd.read_csv(url)
df.head()
df.dtypes
df.columns

#    admit  gre   gpa  rank
# 0      0  380  3.61     3
# 1      1  660  3.67     3
# 2      1  800  4.00     1
# 3      1  640  3.19     4
# 4      0  520  2.93     4

# rename the 'rank' column because there is also a DataFrame method called 'rank'
df.columns = ["admit", "gre", "gpa", "prestige"]
df.columns
# array([admit, gre, gpa, prestige], dtype=object)
#one of the columns is called "rank." This presents a problem since rank is also the name of a method belonging to pandas DataFrame (rank calculates the ordered rank (1 through n) of a DataFrame/Series). To make things easier, rename the rank column to "prestige".

df.describe()
df.std()
#frequency table cutting presitge and whether or not someone was admitted
pd.crosstab(df['admit'], df['prestige'], rownames=['admit'])

# plot all of the columns
df.hist() ; pl.show()

#Histograms are often one of the most helpful tools you can use during the exploratory phase of any data analysis project. They're normally pretty easy to plot, quick to interpret, and they give you a nice visual representation of your problem.
#dummy variables : pandas gives you a great deal of control over how categorical variables are represented. We're going dummify the "prestige" column using get_dummies.
#get_dummies creates a new DataFrame with binary indicator variables for each category/option in the column specified. In this case, prestige has four levels: 1, 2, 3 and 4 (1 being most prestigious). When we call get_dummies, we get a dataframe with four columns, each of which describes one of those levels.

# dummify rank
dummy_ranks = pd.get_dummies(df['prestige'], prefix='prestige')
dummy_ranks.head()

# create a clean data frame for the regression
cols_to_keep = ['admit', 'gre', 'gpa']
data = df[cols_to_keep].join(dummy_ranks.loc[:, 'prestige_2':])
data.head()

# manually add the intercept
data['intercept'] = 1.0
data
#we merge the new dummy columns into the original dataset and get rid of the prestige column which we no longer need.
#Specify the column containing the variable you're trying to predict followed by the columns that the model should use to make the prediction.
#In our case we'll be predicting the admit column using gre, gpa, and the prestige dummy variables prestige_2, prestige_3 and prestige_4. We're going to treat prestige_1 as our baseline and exclude it from our fit. This is done to prevent multicollinearity, or the dummy variable trap caused by including a dummy variable for every single category.

train_cols = data.columns[1:]

# Index([gre, gpa, prestige_2, prestige_3, prestige_4], dtype=object)

logit = sm.Logit(data['admit'], data[train_cols])

# fit the model
result = logit.fit()



#Interpreting the results
result.summary()
result.conf_int()


#odds ratio
np.exp(result.params)

# odds ratios and 95% CI
params = result.params
conf = result.conf_int()
conf['OR'] = params
conf.columns = ['2.5%', '97.5%', 'OR']
np.exp(conf)


#predict : We're going to use np.linspace to create a range of values for "gre" and "gpa". This creates a range of linearly spaced values from a specified min and maximum value--in our case just the min/max observed values.

# instead of generating all possible values of GRE and GPA, we're going
# to use an evenly spaced range of 10 values from the min to the max 
gres = np.linspace(data['gre'].min(), data['gre'].max(), 10)
print gres



#ref : http://blog.yhat.com/posts/logistic-regression-and-python.html