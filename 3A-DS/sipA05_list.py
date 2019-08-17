# -*- coding: utf-8 -*-
#Data Structure - List
L1 = [1,2, 'SIP', 'Dhiraj', True]
#mixed, ordered
L1
print(L1)
#index starts from 0 ; R starts from 1
L1[0]
#change values # mutable
L1[0] = 99
L1 
#ordered
L1[0], L1[1], L1[3], L1[4]
L1[5]  #does not exist
#another way to print
for i in L1:
    print(i)
#see indentation in line above
for i in L1:  print(i) #same as obove
#range
range(5); range(len(L1))
for i in range(5) : print(i, end =' ')
#ends - how wrap the values
for i in range(len(L1)) : print(L1[i])

#other functions
L1[3]
L1[3].upper()
L1[0:2]  #starts at 0, ends at 1 position
sum(L1[0:2])
count(L1)
L1.count('Dhiraj')  #how many times Dhiraj found
len(L1)  #no of elements
L1.append('Kounal')
L1

L1.remove('Dhiraj')
L1

L1.pop()  #remove last index values
L1.pop(0)  #remove 0th position
L1

del L1[0]  #removes index value
L1

L1.clear()  #clear all values
L1

# Copy List
L1 = [1,2, 'SIP', 'Dhiraj', True]
L1
#method 1
L2 = L1
L2
L1.append('Pooja')
L2, L1
#The two variables are referencing to same location

#method2
L1 = [1,2, 'SIP', 'Dhiraj', True]
L3 = L1.copy()
L3
L1.append('Pooja')
L1
L3  #Pooja not here

#method3
L1 = [1,2, 'SIP', 'Dhiraj', True]
L4 = list(L1)
L1
L4
L1.append('Pooja')
L1
L4

#Methods in list
#append, clear, copy, count, extend, index, insert, pop, remove, reverse, sort

#another list
L5 = [i for i in range(11)]
L5
L5.reverse()
L5
L5.sort()
L5
#inplace sorting, permanent changes

#Ex
fruits = ['apple','banana', 'cherry']
#put mango in 2nd position
fruits.insert(1, 'mango')
fruits

#Join two lists

L6 = L1 + L5
L6

#https://learnbatta.com/blog/python-working-with-lists-51/
