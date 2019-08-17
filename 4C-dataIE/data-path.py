# -*- coding: utf-8 -*-
#%
#data import

import pandas as pd
import numpy as np

import os
os.getcwd()
os.listdir()
os.listdir(os.getcwd())

#when using fwd slash use single
df1 = pd.read_csv('data/iris.csv')
df1.head()
df1
#change for your folder
df1a = pd.read_csv('E:/pywork/pyProjects/duanalytics/pyAnalytics/data/iris.csv')
df1a.head()

#when reverse slash use two back slash
df2 = pd.read_csv('data\\iris.csv')
df2.head()


#import from explorer
import subprocess

subprocess.call("explorer E:\\pywork\\data", shell=True)

import easygui
file = easygui.fileopenbox()
file
#not working
#df3 = pd.read_csv(file = easygui.fileopenbox())
#https://www.shanelynn.ie/python-pandas-read_csv-load-data-from-csv-files/
