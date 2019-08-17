# -*- coding: utf-8 -*-
#Data sets in Python Libraries
#https://gitential.com/datasets

#%%
import statsmodels.api as sm
prestige = sm.datasets.get_rdataset("Duncan", "car", cache=True).data
print(prestige.head())
load_boston([return_X_y])#	Load and return the boston house-prices dataset (regression).
load_iris([return_X_y])#	Load and return the iris dataset (classification).
load_diabetes([return_X_y])	#Load and return the diabetes dataset (regression).
load_digits([n_class, return_X_y])	#Load and return the digits dataset (classification).
load_linnerud([return_X_y]) #	Load and return the linnerud dataset (multivariate regression).
#
import statsmodels.api as sm
anes96 = sm.datasets.anes96
print(anes96.DESCRLONG)
anes96.data
print(anes96.NOTE)
dataset_anes96 = anes96.load_pandas()
df_anes96 = dataset_anes96.data
df_anes96.head()

#If you know the submodule in which the dataset is stored (e.g., anes96), you can get the DataFrame with the data in just one line:

sm.datasets.anes96.load_pandas().data
#https://kolesnikov.ga/Datasets_in_Python/
#%%

import statsmodels.api as sm
dataset_iris = sm.datasets.get_rdataset(dataname='iris', package='datasets')
dataset_iris.data
df_iris = dataset_iris.data
df_iris.head()
#https://vincentarelbundock.github.io/Rdatasets/datasets.html
dataset_mtcars = sm.datasets.get_rdataset(dataname='mtcars', package='datasets')
dataset_mtcars.data.head()

#%%%

# Load libraries
from sklearn import datasets
import matplotlib.pyplot as plt 

#datasets
datasets.california_housing().data.shape()
data
# Load digits dataset
iris = datasets.load_iris()

# Create feature matrix
X = iris.data
X.columns
# Create target vector
y = iris.target

# View the first observation's feature values
X[0]
y[0]

#%%%
from sklearn.datasets import load_iris

# Load Iris data (https://en.wikipedia.org/wiki/Iris_flower_data_set)
iris = load_iris()
# Load iris into a dataframe and set the field names
df = pd.DataFrame(iris['data'], columns=iris['feature_names'])
df.head()
# Feature names are in .target & .target_names
iris.target_names[:5]
iris.target
# Change target to target_names & merge with main dataframe
df['species'] = pd.Categorical.from_codes(iris.target, iris.target_names)
df['species'].head()
#https://python-data-science.readthedocs.io/en/latest/datasets.html

#%%%

#not working
from rpy2.robjects import r, pandas2ri
def data(name): 
    return pandas2ri.ri2py(r[name])

#%%
#pip install pydataset
from pydataset import data
titanic = data('titanic')
titanic.head()    

#%%%
from sklearn import datasets
load_boston()  #        Load and return the boston house-prices dataset (regression).
load_iris()     #       Load and return the iris dataset (classification).
load_diabetes()  #      Load and return the diabetes dataset (regression).
load_digits([n_class])# Load and return the digits dataset (classification).
load_linnerud()  #      Load and return the linnerud dataset (multivariate regression).

from sklearn.datasets import load_iris
iris = load_iris()

#%%
import seaborn as sns

iris = sns.load_dataset('iris')
iris.head()

import seaborn as sns
sns.get_dataset_names()
df_planets = sns.load_dataset('planets')
df_planets.head()


#%%
iris = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv')
iris.head()

import pandas as pd
#data = pd.read_csv("http://www.ats.ucla.edu/stat/data/binary.csv")
#data.head()
#%%
import statsmodels.api as sm

iris = sm.datasets.get_rdataset('iris').data
iris.head()


#%%
from pydataset import data
iris = data('iris')
iris.head()


#%%
#pip install quilt
#quilt install uciml/iris
import quilt.data.uciml.iris as ir

iris = ir.tables.iris()
iris.head()


#%%  NOt working
import statsmodels.api as sm
duncan_prestige = sm.datasets.get_rdataset("car")
duncan_prestige.__doc__


#%% Not working
from mvpa2.tutorial_suite import *



#%%
import seaborn.apionly as sns
iris = sns.load_dataset('iris')
iris.head()
#
import statsmodels.api as sm
duncan_prestige = sm.datasets.get_rdataset("Duncan", "carData")
duncan_prestige.data

#%%
https://machinelearningmastery.com/generate-test-datasets-python-scikit-learn/
https://www.dataquest.io/blog/pandas-big-data/
https://data36.com/pandas-tutorial-1-basics-reading-data-files-dataframes-data-selection/
#https://www.statsmodels.org/dev/datasets/index.html
https://github.com/plotly/datasets
https://datascienceplus.com/introduction-to-data-analysis-in-python-with-ipl-dataset/
