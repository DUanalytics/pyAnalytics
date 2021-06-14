#python : Topic : Introduction to Python Programming Environment

#standard libaries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pydataset import data
import seaborn as sns

#!!!! Steps
#Install Anaconda (latest version)
#Install Git and Git Desktop and create Git Profile
#Create a new blank repository - pyAnalytics
#Open Git Desktop, Login, Clone the repository to folder
#E:/analytics/projects . A folder will get created
#Open Sypder (it will take some time); Create a new blank project
#Choose location : E:/analytics/projects/pyAnalytics

#Change few settings in spyder
#Keyboard Shortcut : Execute Line to Control + Enter
#Theme, Size of text etc

#pip install pydataset  #run this line without comment
from pydataset import data
iris = data('iris')
mtcars = data('mtcars')
iris
mtcars
