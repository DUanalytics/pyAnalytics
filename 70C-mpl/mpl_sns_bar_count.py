# -*- coding: utf-8 -*-
#%Count Plot
#https://vincentarelbundock.github.io/Rdatasets/datasets.html
import seaborn as sns
import matplotlib.pyplot as plt
import statsmodels.api as sm
dataset_mtcars = sm.datasets.get_rdataset(dataname='mtcars', package='datasets')
dataset_mtcars.data.head()
df = dataset_mtcars.data
df
plt.figure(figsize=(12,6))  #size of figure
sns.countplot(x='cyl',data=df, hue='gear')
plt.xticks(rotation=45);

