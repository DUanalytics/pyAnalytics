# -*- coding: utf-8 -*-
#https://docs.scipy.org/doc/scipy/reference/stats.html
#https://docs.scipy.org/doc/scipy/reference/tutorial/stats.html
#import scipy
#scipy.stats package is imported as
from scipy import stats

# individual objects are imported as
from scipy.stats import norm

norm.cdf(0)
norm.cdf([-1., 0, 1])
import numpy as np
norm.cdf(np.array([-1., 0, 1]))
norm.mean(), norm.std(), norm.var()
norm.stats(moments="mv")
norm.ppf(0.5)
norm.rvs(size=3) #random nos

#drawing random numbers relies on generators from numpy.random package. In the example above, the specific stream of random numbers is not reproducible across runs. To achieve reproducibility, you can explicitly seed a global variable
np.random.seed(1234)
#Relying on a global state is not recommended though. A better way is to use the random_state parameter which accepts an instance of numpy.random.RandomState class, or an integer which is then used to seed an internal RandomState object:
norm.rvs(size=5, random_state=1234)
norm.rvs(5)  #one no only

#Shifting and Scaling¶
#All continuous distributions take loc and scale as keyword parameters to adjust the location and scale of the distribution, e.g. for the standard normal distribution the location is the mean and the scale is the standard deviation.
norm.stats(loc=3, scale=4, moments="mv")

#uniform distribution
from scipy.stats import uniform
uniform.cdf([0, 1, 2, 3, 4, 5], loc=1, scale=4)

#5, gets passed to set the loc parameter.
np.mean(norm.rvs(5, size=500))
#norm.rvs(5) generates a single normally distributed random variate with mean loc=5, because of the default size=1.

#Shape Parameters¶
#some distributions require additional shape parameters. For instance, the gamma distribution, with density
from scipy.stats import gamma
gamma.numargs
1
gamma.shapes
#set the value of the shape variable to 1 to obtain the exponential distribution
gamma(1, scale=2.).stats(moments="mv")
gamma(a=1, scale=2.).stats(moments="mv")

#Freezing a Distribution
#Passing the loc and scale keywords time and again can become quite bothersome. The concept of freezing a RV is used to solve such problems.
rv = gamma(1, scale=2.)
rv.mean(), rv.std()

#Broadcasting
#basic methods pdf and so on satisfy the usual numpy broadcasting rules. For example, we can calculate the critical values for the upper tail of the t distribution for different probabilities and degrees of freedom.
stats.t.isf([0.1, 0.05, 0.01], [[10], [11]])


#Specific Points for Discrete Distributions
#Discrete distribution have mostly the same basic methods as the continuous distributions. However pdf is replaced the probability mass function pmf, no estimation methods, such as fit, are available, and scale is not a valid keyword parameter. The location parameter, keyword loc can still be used to shift the distribution.
#ppf(q) = min{x : cdf(x) >= q, x integer}
from scipy.stats import hypergeom
[M, n, N] = [20, 7, 12]
x = np.arange(4)*2
x
#array([0, 2, 4, 6])
prb = hypergeom.cdf(x, M, n, N)
prb
hypergeom.ppf(prb, M, n, N)
