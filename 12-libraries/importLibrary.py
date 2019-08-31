# -*- coding: utf-8 -*-
#Different ways of importing libraries

Z#Python comes with built in functions like
x=[1, 4.5, 9]
print(x)
abs(x)
int(x[1]) #takes only 1 value
len(x)
#they are limited in functionality
#need more functions - this comes from libraries or modules
#Modules define functions, classes, variables that can be referenced

import math 
print(math.pi)

#if gives an error that no module found, they you have install it from anaconda prompt (as admin)
#pip install xxxxxxx : xxxx - module name
#modules have to be imported to be used
#method 1 - import : functions have to be used with prefix of module name
#list imported libraries

import random

for i in range(10):  print(random.randint(1,25), end =' ')

#method 2
#from xxxxx import 
#functions can be referred by name rather than dot notation

from random import randint
for i in range(10) : print(randint(1,25), end=' ')

#no dot used
#use comma to import more functions from modules
#from module import function1, function2


#Method3 : Alias
# import [module] as [another_name]

import random as rn
for i in range(10) : print(rn.randint(1,25), end=' ')


#Installing modules
#multiple modules
import math, re
import sys, pprint
pprint.pprint(sys.modules)  #loaded modules

#anaconda prompt
#pip install [module]


#Loaded Modules List
import sys
sys.modules.keys()

#2
import math,re
print(dir())
del math, random


#removing imported module
#del [module]

#Checking 


before = [str(m) for m in sys.modules]
print(before)



##how to import libraries in python

import math

from math import pi

from math import *

#
import pandas

#alias
import pandas as pd
#import [module] as [anothername]
#existing name already used, use shorter verion of library name

import math as m
print(m.pi)

import matplotlib as plt

plt.show()

#for OS related commands

import os
print(os.name)
os.getcwd()


#import any python files also
#links
https://leemendelowitz.github.io/blog/how-does-python-find-packages.html
