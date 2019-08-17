# -*- coding: utf-8 -*-
#Data Structure - Strings

#group of characters/ literals, surrounded by single or double quote

# 'hello' = "hello'

str1 = ' Hello , World '
str1
type(str1)

str1[0:7]

#removes blank spaces
str2 = str1.strip()
len(str2)
str2
str2.lower()
str2.upper()

str2.replace('H', 'Z')
str2  #temporary

liststr3 = str2.split(',')
type(liststr3)


#taking input from prompt
print('Enter your name ? ')
nameval = input()  #look at console, type your name
nameval


#https://learnbatta.com/blog/python-working-with-strings-38/


#%%%
import pandas as pd
import numpy as np
from string import letters, lowercase, uppercase

lt = list(letters)
lc = list(lowercase)
uc = list(uppercase)
import string
string.ascii_lowercase
list(string.ascii_lowercase)
list(map(chr, range(97, 123))) 
help(string)
[chr(i) for i in range(ord('a'),ord('z')+1)]
