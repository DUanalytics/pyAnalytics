# -*- coding: utf-8 -*-
#list comprehension - used for creating new lists from other iterables
#they return lists; 
#quick way of creating lists

list5 = [1,3,5,23]  #manually created
type(list5)

#how do we print the values 
list5  #all
list5[0:2]

#how to generate in quick manner
#Even Numbers
even1 = [ 2*i for i in range(1,11)]
even1

#check how many from above are even
for i in even1: print(i, "\t", round(i/3,1), "\t", i%3 == 0 , end = "\n")

#even no but divisible by 2 and 3
even2 = [ 2*i for i in range(1,11) if i%3 ==0]
even2


#uses - quick creation of list like items
gender = random.choices(['M','F'], weights=(.7,.3), k=100)
gender.size()
gender.count('M')
from collections import Counter
Counter(gender)


#
rollno = pd.Series(range(1,11))
rollno
name = pd.Series(["student" + str(i) for i in range(1,11)])