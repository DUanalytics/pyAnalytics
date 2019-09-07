#Random Forests - iris
#https://github.com/alexhwoods/Machine-Learning/tree/master/Random%20Forest
# RandomForests
# First let's import the dataset, using Pandas.
import pandas as pd

train = pd.read_csv("./data/train-iris.csv")    # make sure you're in the right directory if using iPython!
test = pd.read_csv("./data/test-iris.csv") 

train.head()             # ignore the first column, it's how I split the data.
train.describe(include='all')
train.columns
train.petal_length.describe()   #class not working because of keyword
train.describe(include=[np.object])
train.describe(include=['category'])  #nothing so far
train.describe(exclude=[np.number])
train['class'].value_counts()
test['class'].value_counts()

from sklearn.ensemble import RandomForestClassifier


#%%# however, are data has to be in a numpy array in order for the random forest algorithm to except it!
cols = ['petal_length', 'petal_width', 'sepal_length', 'sepal_width']
colsRes = ['class']
trainArr = train.as_matrix(cols)    # training array
trainArr
trainRes = train.as_matrix(colsRes) # training results
trainRes
## Training!

rf = RandomForestClassifier(n_estimators=100)    # 100 decision trees is a good enough number
rf.fit(trainArr, trainRes)          # finally, we fit the data to the algorithm!!! :)

# note - you might get an warning saying you entered a 2 column vector..ignore it.

#%%
## Testing!

# put the test results in the same format!
testArr = test.as_matrix(cols)
results = rf.predict(testArr)

# add it back to the dataframe, so I can compare side-by-side
test['predictions'] = results
test.head()



#end here...
