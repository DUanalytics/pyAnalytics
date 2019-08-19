#Topic ----Statistics - T-Test 
#link : https://machinelearningmastery.com/how-to-code-the-students-t-test-from-scratch-in-python/
#The Student’s t-Test is a statistical hypothesis test for testing whether two samples are expected to have been drawn from the same population. It is named for the pseudonym “Student” used by William Gosset, who developed the test.
#The test works by checking the means from two samples to see if they are significantly different from each other. It does this by calculating the standard error in the difference between means, which can be interpreted to see how likely the difference is, if the two samples have the same mean (the null hypothesis).
#The t statistic calculated by the test can be interpreted by comparing it to critical values from the t-distribution. The critical value can be calculated using the degrees of freedom and a significance level with the percent point function (PPF).

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#%% One Sample Test
#compare sample data with assumed mean
import scipy.stats as stats
#https://docs.scipy.org/doc/scipy/reference/stats.html
np.random.seed(1234)
sample_marks = np.random.normal(loc=55, scale=12, size=100)
sample_marks
plt.hist(sample_marks)
np.mean(sample_marks)
assumed_mean = 60
#Hypothesis Ho: mean=60, Ha: mean <> 60 :Two tail test
ttest1S1 = stats.ttest_1samp(a=sample_marks, popmean=assumed_mean)
#https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.ttest_1samp.html#scipy.stats.ttest_1samp
ttest1S1
#pvalue < 0.05 : hence REJECT Ho (Null Hypothesis) in favour of Ha
#ie. True mean is not equal to 60
ttest1S2 = stats.ttest_1samp(a=sample_marks, popmean=55)
ttest1S2
#now pvalue > .05 : Hence accept Ho hypothesis

#%%%
from statsmodels.stats.weightstats import ttest_ind
#Let us generate some random data from the Normal Distriubtion. We will sample 50 points from a normal distribution with mean μ=0 and variance σ2=1 and from another with mean μ=2 and variance σ2=1.
marks_before = np.random.normal(loc=50, scale=10, size=100)
#after undergoing training
marks_after = np.random.normal(loc=55, scale=12, size=100)
#make test
marks_before
marks_after
ttest = ttest_ind(marks_before, marks_after)
ttest
#t-statistics, p-values, degrees of freedom
ttest[0]
ttest[1] < 0.5 #if true, Null Hypothesis true that mean of both the samples is same
#under confidence interval 95%
#https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.ttest_ind.html
from scipy.stats import ttest_ind
ttest_sp = ttest_ind(marks_before, marks_after, axis=0, equal_var=True)
ttest_sp
#same as from statsmodel : no degree of freedom

#%%%
#A One Sample T-Test is a statistical test used to evaluate the null hypothesis that the mean m of a 1D sample dataset of independant observations is equal to the true mean μ of the population from which the data is sampled. In other words, our null hypothesis is that :m=μ


#%%% Links
#https://towardsdatascience.com/inferential-statistics-series-t-test-using-numpy-2718f8f9bf2f
#https://www.youtube.com/watch?v=pTmLQvMM-1M

