#Topic: Py Caret
#-----------------------------
#libraries
#https://pycaret.org/
#PyCaret is an open source, low-code machine learning library in Python that allows you to go from preparing your data to deploying your model within minutes in your choice of notebook environment.
pip install pyCaret
pip install SQLA1chemy
import pycaret
import pandas as pd

# Loading data from pycaret
#datasets - https://pycaret.org/get-data/


from pycaret.datasets import get_data
data = get_data('juice') 


#env for modeling
#https://pycaret.org/setup/
#Classification	from pycaret.classification import *
#Regression	from pycaret.regression import *
#Clustering	from pycaret.clustering import *
#Anomaly Detection	from pycaret.anomaly import *
#Natural Language Processing	from pycaret.nlp import *
#Association Rule Mining	from pycaret.arules import *

#classification
from pycaret.datasets import get_data
diabetes = get_data('diabetes')
# Importing module and initializing setup
from pycaret.classification import *
clf1 = setup(data = diabetes, target = 'Class variable')

#regression
from pycaret.datasets import get_data
boston = get_data('boston')
# Importing module and initializing setup
from pycaret.regression import *
reg1 = setup(data = boston, target = 'medv')

## Clustering
from pycaret.datasets import get_data
jewellery = get_data('jewellery')
# Importing module and initializing setup
from pycaret.clustering import * 
clu1 = setup(data = jewellery)