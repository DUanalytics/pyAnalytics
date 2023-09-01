# -*- coding: utf-8 -*-
#Install Libraries
#-----------------------------
#%
#https://docs.anaconda.com/free/anaconda/reference/packages/pkg-docs/
#https://docs.anaconda.com/free/anaconda/reference/packages/py3.11_win-64/
#packages installed
pip freeze

pip list

conda list

#these library are installed by default in Anaconda, if not this is how to install
#install additional libraries
#!pip install <library1> <library2>

import pip
dir(pip)

!pip install inspect
from inspect import getmembers, isfunction  
import numpy
print(a for a in getmembers(numpy) if isfunction(a[1]))  

print(getmembers(numpy, isfunction))
#for i in pip.get_installed_distributions():  print(i)

#install from text file with version no
!pip install -r requirements.txt
!pip install beautifulsoup4

!pip install decorator frozenlist gensim glueviz hyperlink imagesize pivottablejs pydot pymysql pyspark quandl pydataset


import beautifulsoup4
import bokeh

conda list
from pip._internal.operations.freeze import freeze
for requirement in freeze(local_only=True):
    print(requirement)

state packages
#open Anaconda prompt as Administrator and type these commands
pip install matplotlib
pip install numpy
pip install pandas

import site
site.getsitepackages()
