#Topic:Logistics Regression  - Cut off Values
#-----------------------------
#libraries
import pandas as pd
import statsmodels.api as sm
import pylab as pl
import numpy as np
from sklearn.metrics import roc_curve, auc

# read the data in
url = "https://stats.idre.ucla.edu/stat/data/binary.csv"
df = pd.read_csv(url)
#df = pd.read_csv("http://www.ats.ucla.edu/stat/data/binary.csv")

# rename the 'rank' column because there is also a DataFrame method called 'rank'
df.columns = ["admit", "gre", "gpa", "prestige"]
# dummify rank
dummy_ranks = pd.get_dummies(df['prestige'], prefix='prestige')
# create a clean data frame for the regression
cols_to_keep = ['admit', 'gre', 'gpa']
data = df[cols_to_keep].join(dummy_ranks.iloc[:, 'prestige_2':])

# manually add the intercept
data['intercept'] = 1.0

train_cols = data.columns[1:]
# fit the model
result = sm.Logit(data['admit'], data[train_cols]).fit()
result.summary()

# Add prediction to dataframe
data['pred'] = result.predict(data[train_cols])

fpr, tpr, thresholds =roc_curve(data['admit'], data['pred'])
roc_auc = auc(fpr, tpr)
print("Area under the ROC curve : %f" % roc_auc)

####################################
# The optimal cut off would be where tpr is high and fpr is low
# tpr - (1-fpr) is zero or near to zero is the optimal cut off point
####################################
i = np.arange(len(tpr)) # index for df
roc = pd.DataFrame({'fpr' : pd.Series(fpr, index=i),'tpr' : pd.Series(tpr, index = i), '1-fpr' : pd.Series(1-fpr, index = i), 'tf' : pd.Series(tpr - (1-fpr), index = i), 'thresholds' : pd.Series(thresholds, index = i)})
roc.iloc[(roc.tf-0).abs().argsort()[:1]]

# Plot tpr vs 1-fpr
fig, ax = pl.subplots()
pl.plot(roc['tpr'])
pl.plot(roc['1-fpr'], color = 'red')
pl.xlabel('1-False Positive Rate')
pl.ylabel('True Positive Rate')
pl.title('Receiver operating characteristic')
ax.set_xticklabels([])