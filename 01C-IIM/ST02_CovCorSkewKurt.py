#Topic: Correlation, Covariance,
#-----------------------------
#libraries

#The difference between variance, covariance, and correlation is:

#Variance is a measure of variability from the mean
#Covariance is a measure of relationship between the variability of 2 variables - covariance is scale dependent because it is not standardized
#Correlation is a of relationship between the variability of of 2 variables - correlation is standardized making it not scale dependent

import pandas as pd
import numpy as np

# Setting a seed so the example is reproducible
np.random.seed(4272018)
df = pd.DataFrame(np.random.randint(low= 0, high= 20, size= (5, 2)),  columns= ['Commercials Watched', 'Product Purchases'])
df
df.agg(["mean", "std"])
df.cov()
df.corr()


#skewness & Kurtosis
#%matplotlib inline
import numpy as np
import pandas as pd
from scipy.stats import kurtosis
from scipy.stats import skew

import matplotlib.pyplot as plt

plt.style.use('ggplot')

data = np.random.normal(0, 1, 10000000)
data
len(data)
np.var(data)

plt.hist(data, bins=60)

print("mean : ", np.mean(data))
print("var  : ", np.var(data)) #sq of sd
print("skew : ", skew(data))
print("kurt : ", kurtosis(data))
#https://www.spcforexcel.com/knowledge/basic-statistics/are-skewness-and-kurtosis-useful-statistics
#https://www.researchgate.net/post/What_is_the_acceptable_range_of_skewness_and_kurtosis_for_normal_distribution_of_data distribution
#If the skewness is between -0.5 and 0.5, the data are fairly symmetrical
#If the skewness is between -1 and – 0.5 or between 0.5 and 1, the data are moderately skewed
#If the skewness is less than -1 or greater than 1, the data are highly skewed




import numpy as np
from scipy.stats import kurtosis, skew

x_random = np.random.normal(0, 2, 10000)

x = np.linspace( -5, 5, 10000 )
y = 1./(np.sqrt(2.*np.pi)) * np.exp( -.5*(x)**2  )  # normal distribution

np.skewness(y)
skew(y)

import matplotlib.pyplot as plt

f, (ax1, ax2) = plt.subplots(1, 2)
ax1.hist(x_random, bins='auto')
ax1.set_title('probability density (random)')
ax2.hist(y, bins='auto')
ax2.set_title('(your dataset)')
plt.tight_layout()


#find skewness and kurtosis of mtcars columns
mtcars
skew(mtcars.mpg)
plt.hist(mtcars.mpg, bins=5)
kurtosis(mtcars.mpg)
#find columns normal distributed, skewed and kurtosis
