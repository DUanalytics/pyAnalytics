# -*- coding: utf-8 -*-
#Folder System

import sys

#path where modules are searched
sys.path

#curren working directory
import os
os.getcwd()
os.path.realpath('.')

import os
os.chdir('E:/pyWork')
os.getcwd()

#list all files / folders 
import glob   #install it : pip install glob
print(glob.glob('E:/pywork/pyProjects/pyAnalytics/*.py'))
#only of type

os.listdir('E:/pyWork')
os.listdir('.')  #project dir

os.listdir('/')  #root folder of drive
os.listdir('E:/pywork/pyProjects/')
os.listdir('C:/Users/du/desktop/')


#https://learnbatta.com/blog/working-with-os-module-in-python-71/
