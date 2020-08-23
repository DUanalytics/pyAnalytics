#python : Topic : Daily 2
#https://www.digitalvidya.com/blog/python-for-data-science/
#standard libaries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pydataset import data
import seaborn as sns

#data Structures
#List - List in python is same as ‘array’ in other languages. Lists are mutable data types. Which means you can edit the content of list by applying methods.
listA = [1,2,3,4,5]                 #Create list using square braces []
listA.extend([6,7])                 #Extend the list
print(listA)
listA.append([8,9])                 #Append elements to the list
print(listA)

listB = [10,11,12]                  #Create another list
listoflist = [listA, listB]         #Join two lists
print(listoflist)                   #Print

#Below is the list of different methods to manipulate ‘lists’ in order to achieve your goal.
# append()	Add single element to the list
# extend()	Add elements of a list to another list
# insert()	Insert element to list
# remove()	Remove element from list
# index()	Returns smallest index
# count()	Gives occurrences of an element in the list
# pop()	Remove element at given index
# reverse()	Reverse a list
# sort()	Sort elements
# clear()	Remove all elements from the list

#%%% Tuples
# indexing is from 0;  Same as list apart from tuples are immutable; # Use () instead of []
 
tuple = (2, 4, 6, 7)
 
#print length of tuple
print(len(tuple))
 
#print element at index 2
print(tuple[2])
 
#just like lists you can merge tuples too
a = (1, 2, 3)
b = (4, 5, 6)
merge = (a, b)
print(merge)

#%%Functions
#Simple Function
def squareOfNumber(x):
     return x*x
def squareOfNumber(x):     return x*x

print(squareOfNumber(3))
 
#Function using another function
def do(f,x):     return f(x)
print (do(squareOfNumber,4))
#f is function squareOfNumber and value is 4
squareOfNumber(4) 

#Inline Function
print (do(lambda x: x*x*x,5))

#%%% Looping
#loop :  #Range in python defines scope of loop another example is range(3,8)
for x in range(15):   print(x)
 
#loop with skip and continue functions
for x in range(10):
  if (x == 4):
    continue
  if (x > 5):
    break
  print(x)


#while loop
x=0
while(x<10):
     print(x),
     x += 1    

#%% Dictionary
#Dictionary needs a little introduction. Dictionaries in python is nothing but a table that stores information with help of a unique key. Whenever you need that data, call it by the key it was assigned. Here key is ‘ship1’, ‘ship2’ and the values are name of captains.

#create the dictionary
captains = {}
 
#add values into it
captains["ship1"] = "Kirk"
captains["ship2"] = "Marcus"
captains["ship3"] = "Phillips"
captains["ship4"] = "Mike"
 
#fetch the data
#two ways to fetch the result from dictionary
print (captains["ship3"])
print (captains.get("ship4"))

#%%% File Read-Write - not working
#File read and write is not that mandatory but it is good to know that might be useful sometimes.

handle = open('kids','w')  #Open file name 'kids' with 'w'-write permissions
 
for i in range(2):                   #For 2 lines enter name
     name = input("Enter Name: ")
     handle.write(name + '\n')
     handle.close()
 
handle = open('kids','r')            #Open the same file in read mode
 
for line in handle:
     print(line)    #print the names that was previously written
     handle.close()


#%% library
#pip install library-name         #General syntax
#pip install numpy                #installing numpy using pip

#%%
import numpy as np               #Import library
from scipy.stats import mode     #From library import specific module
n = int(input())                 #Take input from user
n=5
arr = list(map(int, input()))    #combine input and return list
print(np.mean(arr))
print(np.median(arr))
mod = mode(arr)
print(*mod[0])                   #asterisk (*) removes square brackets #while printing list