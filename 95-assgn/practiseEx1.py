#python : Topic : Practise  Ex

#standard libaries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pydataset import data
import seaborn as sns

df = data('mtcars')
df

#%%quantiles
intervals = np.linspace(0,1,11)
intervals
df.mpg.sort_values()
np.sort(df.mpg)[16]
df.quantile(q=0.5, axis=0)  #columns
df.quantile(q=intervals, axis=0)  #columns
df.boxplot()
df.boxplot(column=['mpg'])
ax = sns.stripplot(x="gear", y="mpg", data=df)

#quantiles
q3, q1 = np.percentile(df['hp'], [75 ,25])
q3, q1
q3 - q1

from scipy import stats
IQR = stats.iqr(df['hp'])
IQR

#define function to calculate interquartile range
def find_iqr(x):  return np.subtract(*np.percentile(x, [75, 25]))

#calculate IQR for 'rating' and 'points' columns
df[['mpg', 'wt', 'hp']].apply(find_iqr)
df.apply(find_iqr)

#outliers
mpgZ = stats.zscore(df['mpg'])
len(mpgZ)
mpgZ
np.abs(mpgZ)
np.abs(mpgZ) > 2  #T and F
np.where(np.abs(mpgZ) > 2)

dfz = np.abs(stats.zscore(df))
dfz
dfz[:,0] #first column
dfz[:,0] == np.abs(mpgZ)

Q1 = df.quantile(0.25)
Q3 = df.quantile(0.75)
IQR = Q3 - Q1
IQR
dfTF = (df < (Q1 - 1.5 * IQR)) |(df > (Q3 + 1.5 * IQR))
dfTF
dfTF.sum(axis=0)
dfTF.sum(axis=1)

threshold = 3
dfz > threshold
print(np.where(dfz > threshold))

#skewness
skewValue = df.skew(axis=0)
skewValue

#kurtosis
kurtValue = df.kurtosis(axis=0)
kurtValue

#for hp: skew = 0.799407, kurt= 0.275212 
df.hp
#mean/median
df.mean(axis=0)  #average : sum of all values / count
df.median(axis=0)   #middle value : data sorted and then values
np.sum(df.mpg)/32 #mpg is 20.09
df.mpg.quantile(q=0.5)
df.mpg.sort_values()[16]

df.min(axis=0)
df.max(axis=0)
df.describe()
col_ranges = df.max() - df.min()
col_ranges



sns.set(style="whitegrid")
tips = sns.load_dataset("tips")

ax = sns.boxplot(x="day", y="total_bill", data=tips, showfliers = False)
ax = sns.swarmplot(x="day", y="total_bill", data=tips, color=".25")
plt.show()

ax = sns.stripplot(x="day", y="total_bill", data=tips)


#import pandas as pd
import numpy as np
import numpy as np
from scipy.stats import kurtosis, skew
from pydataset import data
import matplotlib.pyplot as plt

plt.style.use('ggplot')
mtcars=data('mtcars')
data=mtcars
data
data.columns
skew(data, axis=0)
kurtosis(mtcars.hp)

