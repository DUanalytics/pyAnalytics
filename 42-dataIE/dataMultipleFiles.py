#python : Topic :Load from multiple files.......

#standard libaries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pydataset import data
import seaborn as sns

import os
os.listdir()
os.listdir('E:/data/analytics')

import glob
print(glob.glob('.'))
#print file names
for file_name in glob.iglob('E:/data/analytics/*.txt', recursive=True): print(file_name)

from glob import glob
filenames = glob('E:/data/analytics/mv*.txt')
filenames
dataframes1 = [pd.read_csv(f) for f in filenames]
dataframes1

#2nd method
filenames2 = filenames 
dataframes2 = []
for f in filenames2:    dataframes2.append(pd.read_csv(f))
dataframes2


#https://stackoverflow.com/questions/208120/how-to-read-and-write-multiple-files
#https://honingds.com/blog/read-multiple-data-files-into-pandas