# -*- coding: utf-8 -*-
#
#-----------------------------
#%

#The zip() function take iterables (can be zero or more), makes iterator that aggregates elements based on the iterables passed, and returns an iterator of tuples.

#The zip() function takes:

#iterables - can be built-in iterables (like: list, string, dict), or user-defined iterables (object that has __iter__ method).
#The zip() function returns an iterator of tuples based on the iterable object.

#If no parameters are passed, zip() returns an empty iterator
#If a single iterable is passed, zip() returns an iterator of 1-tuples. #Meaning, the number of elements in each tuple is 1.
#If multiple iterables are passed, ith tuple contains ith Suppose, two iterables are passed; one iterable containing 3 and other containing 5 elements. Then, the returned iterator has 3 tuples. It's because iterator stops when shortest iterable is exhaused.

#Iteration is a general term for taking each item of something, one after another. Any time you use a loop, explicit or implicit, to go over a group of items, that is iteration. In Python, iterable and iterator have specific meanings. ... So an iterable is an object that you can get an iterator from.

numberList = [1, 2, 3]
strList = ['one', 'two', 'three']

# No iterables are passed
result = zip()
result
type(result)

# Converting itertor to list
resultList = list(result)
print(resultList)

# Two iterables are passed
result = zip(numberList, strList)
result #zip object
print(result)  #nothing

# Converting itertor to set
resultSet = set(result)
print(resultSet)


#Different no of iterables
numbersList = [1, 2, 3]
strList = ['one', 'two']
numbersTuple = ('ONE', 'TWO', 'THREE', 'FOUR')

result = zip(numbersList, numbersTuple)

# Converting to set
resultSet = set(result)
print(resultSet)

result = zip(numbersList, strList, numbersTuple)

# Converting to set
resultSet = set(result)
print(resultSet)


#unzip the list  :  zip(*zippedList)

coordinate = ['x', 'y', 'z']
value = [3, 4, 5, 0, 9]

result = zip(coordinate, value)
resultList = list(result)
print(resultList)

c, v =  zip(*resultList)
print('c =', c)
print('v =', v)
c
v
#elements 0 and 9 in variable value is not in variable v. It's because the zipped iterables have different number of elements.


#https://www.programiz.com/python-programming/methods/built-in/zip
