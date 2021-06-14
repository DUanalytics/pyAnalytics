# -*- coding: utf-8 -*-
#Created on Sun Jun 16 08:25:24 2019 @author: dhiraj@dell sip
#
#-----------------------------
#%
#Help in Python
#https://www.geeksforgeeks.org/help-function-in-python/
#https://www.programiz.com/python-programming/methods/built-in/help

#functions in library
import math
dir(math)

#? after function
print?
print('dhiraj', 'upadhyaya', sep=':', end =' ^^^')
#Control + I after selecting the function
print #highlight the print word and press control + I
import
#see on lower left windows - Help

#help help([object])
help(print)
help(dict)
help([1, 2, 3])
help('random thing')

help()
#ython's help utility (interactive help system) starts on the console.
#see the console : quit to exit
#https://en.wikibooks.org/wiki/Python_Programming/Self_Help
help()      # Starts an interactive help : quit
help("topics")  # Outputs the list of help topics
help("OPERATORS") # Shows help on the topic of operators
help("len")    # Shows help on len function
help("re")    # Shows help on re module
help("re.sub")  # Shows help on sub function from re module
help(len)     # Shows help on the object passed, the len function
help([].pop)   # Shows help on the pop function of a list
dir([])      # Outputs a list of attributes of a list, which includes functions
import re
help(re)     # Shows help on the help module
help(re.sub)   # Shows help on the sub function of re module
help(1)      # Shows help on int type
help([])     # Shows help on list type
help(def)     # Fails: def is a keyword that does not refer to an object
help("def")    # Shows help on function definitions

import pandas
help(pandas)

#Module Help
#https://pypi.org/
