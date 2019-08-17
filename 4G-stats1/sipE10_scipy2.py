# -*- coding: utf-8 -*-
#statistics

#https://scipy-lectures.org/packages/statistics/index.html
import pandas
data = pandas.read_csv('data/brain_size.csv', sep=';', na_values=".")
data
data.shape
#The weight of the second individual is missing in the CSV file. If we don’t specify the missing value (NA = not available) marker, we will not be able to do statistical analysis.

#create from arrays
import numpy as np
t = np.linspace(-6, 6, 20)
sin_t = np.sin(t)
cos_t = np.cos(t)
pandas.DataFrame({'t': t, 'sin': sin_t, 'cos': cos_t}) 

data.shape    # 40 rows and 8 columns
data.columns
print(data['Gender'])  # Columns can be addressed by name 
data[data['Gender'] == 'Female']['VIQ'].mean()

#groupby: splitting a dataframe on values of categorical variables:
groupby_gender = data.groupby('Gender')
for gender, value in groupby_gender['VIQ']:
    print((gender, value.mean()))

#groupby_gender is a powerful object that exposes many operations on the resulting group of dataframes:
groupby_gender.mean()    

#groupby_gender.boxplot is used for the plots above
groupby_gender.boxplot()


#
#What is the mean value for VIQ for the full population?
#How many males/females were included in this study?
#Hint use ‘tab completion’ to find out the methods that can be called, instead of ‘mean’ in the above example.
#What is the average value of MRI counts expressed in log units, for males and females?


from pandas.tools import plotting
plotting.scatter_matrix(data[['Weight', 'Height', 'MRI_Count']])  
plotting.scatter_matrix(data[['PIQ', 'VIQ', 'FSIQ']]) 

#Plot the scatter matrix for males only, and for females only. Do you think that the 2 sub-populations correspond to gender?


#%%Hypothesis testing: comparing two groups
from scipy import stats

#Student’s t-test: the simplest statistical test

#1-sample t-test: testing the value of a population mean

stats.ttest_1samp(data['VIQ'], 0)
#With a p-value of 10^-28 we can claim that the population mean for the IQ (VIQ measure) is not 0.

#2-sample t-test: testing for difference across populations
#We have seen above that the mean VIQ in the male and female populations were different. To test if this is significant, we do a 2-sample t-test with scipy.stats.ttest_ind()

female_viq = data[data['Gender'] == 'Female']['VIQ']
male_viq = data[data['Gender'] == 'Male']['VIQ']
stats.ttest_ind(female_viq, male_viq)   

# Paired tests: repeated measurements on the same individuals
#PIQ, VIQ, and FSIQ give 3 measures of IQ. Let us test if FISQ and PIQ are significantly different. We can use a 2 sample test:
stats.ttest_ind(data['FSIQ'], data['PIQ']) 
#The problem with this approach is that it forgets that there are links between observations: FSIQ and PIQ are measured on the same individuals. Thus the variance due to inter-subject variability is confounding, and can be removed, using a “paired test”, or “repeated measures test”:
stats.ttest_rel(data['FSIQ'], data['PIQ']) 
#This is equivalent to a 1-sample test on the difference:

stats.ttest_1samp(data['FSIQ'] - data['PIQ'], 0)

#T-tests assume Gaussian errors. We can use a Wilcoxon signed-rank test, that relaxes this assumption:
#

stats.wilcoxon(data['FSIQ'], data['PIQ'])   
#Note The corresponding test in the non paired case is the Mann–Whitney U test, scipy.stats.mannwhitneyu().

#Exercise

#Test the difference between weights in males and females.
#Use non parametric statistics to test the difference between VIQ in males and females.
#Conclusion: we find that the data does not support the hypothesis that males and females have different VIQ.