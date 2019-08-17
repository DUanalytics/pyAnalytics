# -*- coding: utf-8 -*-
#data structures
#are structures which can hold some data together. used to store collection of related data
#types - list, tuple, dictionary, set

#%%
#list
#ordered collection of items; sequence of items in a list
shoplist =['apple','carrot','mango', 'banana']
shoplist
len(shoplist)

#run next 2 lines together
for item in shoplist:
    print(item, end =' ')

#add item to list
shoplist.append('rice')
shoplist

#sort
shoplist.sort()  #inplace sort
shoplist

#index/select
shoplist[0]
shoplist[0:4]

#delete item
del shoplist[0]


#%% Tuple
#Used to hold multiple object; similar to lists; less functionality than list
#immutable - cannot modify- fast ; ( )

zoo = ('python','lion','elephant','bird')
zoo
len(zoo)
languages = 'c', 'java', 'php'  #better to put (), this also works
languages

#filter 
zoo[1]
zoo[1:4]

#Dictionary - like an addressbook. use of associate keys with values
#key-value pairs { 'key1':value1, 'key2':value2} ; { } bracket, :colon

student = {'A101': 'Dhiraj', 'A102': 'Ramesh', 'A103':'Tanvi', 'A104': 'Kanika'}
student
student['A103']
print('Name of rollno A103 is ', student['A103'])
del student['A104']
student
len(student)

for rollno, name in student.items():
    print('name of {} is {} '.format(rollno, name) )

#adding a value
student['A104'] = 'Hitesh'
student

#%% 
#Sequences - lists, tuples, strings are eg of sequence
#dictionaries are not sequence type

#Strings
name = 'Kounal Gupta'
name
name[0]
name[0:6]
name[:]
name[3:]

#sequences
shoplist[1:4]
zoo[1:3]


#%% Set
#Sets are unordered collections of objects; ( [ , ])
teamA = set(['india', 'england', 'australia','sri lanka','ireland'])
teamA
teamB = set(['pakistan', 'south africa','bangladesh','ireland'])
teamB

'india' in teamA
'india' in teamB

teamA.add('china')
teamA  #puts in order
teamA.add('india')
teamA  #no duplicates
teamA.remove('australia')
teamA


#More on Strings
name ='Dhiraj Upadhyaya'
name.startswith('Dh')
'U' in name
name.find('ya')  #position

#%%
#tuples

x = 3,5,2
x
type(x)

x1 = (3,7,3)
type(x1)

x2 = (3, 'a', 45.6, 'Dhiraj')
x2

x3= (3, 56, [55, 78])
type(x3)

x5= (('x','y'),('a','b'))
type(x3)

x5[0]
x5[1]
x5[0][1]

len(x5)


#%%
#Zip data structure

name =['dhiraj', 'kanika','tanvi','upen']
rollno = [1,2,3,4]
mapped = zip(name, rollno)

mapped = set(mapped)
mapped


#unzipping
namez, rollnoz = zip(*mapped)
namez
rollnoz

#printing
for rollno, name in zip(rollno, name):
    print('Student is ", (rollno, name))
    
list(range(3))
list(zip(range(3), 'abc'))
list(zip('abc','abc'))

#
name =['dhiraj', 'kanika','tanvi','upen']
rollno = [1,2,3,4]

for name, rollno in zip(name, rollno):
    print(name, "....", rollno)
#
list1 = [10,20,30,40]
list2 = [ 11,21,31]
result = zip(list1, list2)

for element1, element2 in result:
    print(element1, element2)

zipped= zip(list1, list2)
result_list = list(zipped)
result_list
list(result_list).items()

from collections import Counter
cnt= Counter()
for word in words: cnt[words] +=1

cnt.items()


#https://docs.python.org/3/tutorial/datastructures.html

