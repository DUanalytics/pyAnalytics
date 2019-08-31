# -*- coding: utf-8 -*-
#Created on Thu Jun 20 12:20:36 2019 : dhiraj@sony


#Datasets for Graphs and other Tasks

#data can be in CSV , ZIP or other format
#https://support.spatialkey.com/spatialkey-sample-csv-data/
#https://www.stats.govt.nz/large-datasets/csv-files-for-download/
#https://catalog.data.gov/dataset?res_format=CSV
#https://perso.telecom-paristech.fr/eagan/class/igr204/datasets

import pandas as pd
#https://stats.idre.ucla.edu/other/dae/
csvlink1 = 'https://data.cityofnewyork.us/api/views/kku6-nxdu/rows.csv'
data = pd.read_csv(csvlink1)
data.head()
data.shape

csvlink2 = 'https://perso.telecom-paristech.fr/eagan/class/igr204/data/cars.csv'
data2 = pd.read_csv(csvlink2, sep=';')  #check for seperator
data2.head()
data2.shape
data2.columns


#pydataset
#pip install pydataset as admin in anaconda
from pydataset import data
titanic = data('titanic')
titanic.head()

#mtcars
from pydataset import data
mtcars = data('mtcars')
mtcars.head()

#sklearn
from sklearn import datasets
iris = datasets.load_iris()
type(iris)
#it is bunch type - key and values used for Machine Learning
iris.data
iris.feature_names

#bring it into DF format
df = pd.DataFrame(iris.data, columns=iris.feature_names)
df.head()

#Seaborn
import seaborn as sns
iris2 = sns.load_dataset('iris')
iris2.head()

#other way to access seaborn datasets
#https://github.com/mwaskom/seaborn-data
import pandas as pd
url = 'https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv'
iris3 = pd.read_csv(url)
iris3.head()
url2 ='https://raw.githubusercontent.com/mwaskom/seaborn-data/master/diamonds.csv'
diamonds = pd.read_csv(url2)
diamonds.head()





#MVPA ? not working
#from mvpa2.tutorial_suite import *

#nibabel - image processing dataa
#import nibabel 

