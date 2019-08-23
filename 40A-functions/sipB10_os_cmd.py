# -*- coding: utf-8 -*-
#File System


import os
os.listdir(os.curdir)
os.getcwd()  #current working dir
os.chdir("..")
os.getcwd()  #current working dir
os.listdir(os.curdir)
os.chdir("data")
os.getcwd()  #current working dir
os.listdir(os.curdir)

import os
os.listdir("E:/pyWork")

import glob

glob.glob("E:/pyWork/pyProjects")
csvfiles = []
for file in glob.glob("*.csv"):
    csvfiles.append(file)

mylist = [f for f in glob.glob("*.csv")]
mylist

#%%

import os
files_path = [os.path.abspath(x) for x in os.listdir()]
files_path

#%%
thisdir = os.getcwd()
#r-root, d-directories, f-files
for r, d ,f in os.walk(thisdir):
    for file in f:
        if ".csv" in file:
            print(os.path.join(r, file))
            
#%%
import os
arr = os.listdir(".")
arr

arr2 = os.listdir("E:\\pyWork")
arr2

arr3 = next(os.walk("."))[2]
arr3

#%%
import glob
glob.glob("*")
glob.glob("data/*.xlsx")

