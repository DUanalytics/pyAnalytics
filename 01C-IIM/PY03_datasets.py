#Topic: Data Sets in Python
#-----------------------------
#https://github.com/iamaziz/PyDataset
#libraries

import numpy as np
import pandas as pd

import pydataset
data('iris')
data('iris', show_doc=True)#help

#better way 
from pydataset import data
data()
alldatasets = data().copy()
type(alldatasets)


from pydataset import data
data('iris')
data('marketing')
data('titanic')

alldatasets.head()

#check for availability
data('iris')
data('mtcars')
data('ais')

alldatasets.dataset_id[0:100].sort_values()
alldatasets.iloc[0:20, 0:2]

search1 = alldatasets['dataset_id'].str.contains('iris')
alldatasets[search1]
search2 = alldatasets.dataset_id.str.contains('cars')
alldatasets[search2]

#both
alldatasets[ alldatasets['dataset_id'].str.contains("iris") | alldatasets['dataset_id'].str.contains('cars')] 

print(df1) 


mtcars = data('mtcars')
data1 = mtcars.copy()
data1.head()

iris = data('iris')
data2 = iris.copy()
data2.head()

cars = data('cars')
data3 = cars.copy()
data3.head()

#titanic
data('titanic')

alldatasets['dataset_id'].str.contains('ais')

#other datasets
https://scikit-learn.org/stable/datasets/index.html



#-----
from sklearn.datasets import fetch_openml
mice = fetch_openml(name='miceprotein', version=4)
mice.data.shape
mice.target.shape
np.unique(mice.target)

iris = fetch_openml(name="iris")
iris.details['version']  


#%%%%
#pip install dataset
#https://dataset.readthedocs.io/en/latest/
import dataset
db = dataset.connect('sqlite:///:memory:')

table = db['sometable']
table.insert(dict(name='John Doe', age=37))
table.insert(dict(name='Jane Doe', age=34, gender='female'))

john = table.find_one(name='John Doe')
john


#%%% seaborn
import seaborn as sb
df = sb.load_dataset('tips')
df.head()
sb.get_dataset_names()
sbdatasets = sb.get_dataset_names()
sbdatasets[0:10]
sbdata = pd.DataFrame({'dbname':sb.get_dataset_names()})
sbdata
sbdata[ sbdata['dbname'].str.contains("flight") ]
sbdata[0:10]
sbdata.shape
