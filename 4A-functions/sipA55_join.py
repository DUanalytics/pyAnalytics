#Topic: Join 
#-----------------------------
#libraries

numList = ['1', '2', '3', '4']
seperator = ', '
print(seperator.join(numList))

numTuple = ('1', '2', '3', '4')
print(seperator.join(numTuple))

s1 = 'abc'
s2 = '123'

""" Each character of s2 is concatenated to the front of s1""" 
print('s1.join(s2):', s1.join(s2))

""" Each character of s1 is concatenated to the front of s2""" 
print('s2.join(s1):', s2.join(s1))

#sets
test =  {'2', '1', '3'}
s = ', '
print(s.join(test))

test = {'Python', 'Java', 'Ruby'}
s = '->->'
print(s.join(test))

#dictionaries
test =  {'mat': 1, 'that': 2}
s = '->'
print(s.join(test))

test =  {1:'mat', 2:'that'}
s = ', '

# this gives error
print(s.join(test))
#   The join() method tries to concatenate the key (not value) of the dictionary to the string. If the key of the string is not a string, it raises TypeError exception. 
#https://www.programiz.com/python-programming/methods/string/join

#%%
list1 = ['1','2','3','4']  
s = "-"
# joins elements of list1 by '-' # and stores in sting s 
s = s.join(list1) 
  
# join use to join a list of # strings to a separator s 
print(s) 

#
"asd%d" % 9
"asd" + str(9)
"abc" + str(9)
'abc{0}'.format(9)
#%%
s = ' this   is  my string '
s.split()
s.split(maxsplit=1)
'a' + 'b' + 'c'
'do' * 2
'Hello' + 2  #error

strings = ['do', 're', 'mi']
','.join(strings)


#%%%
str = ""
str1 = ( "geeks", "for", "geeks" )
str.join(str1)

def convert(s): 
    str1 = "" 
    return(str1.join(s))     
s = ['g', 'e', 'e', 'k', 's', 'f', 'o', 'r', 'g', 'e', 'e', 'k', 's'] 
print(convert(s)) 


#%%
str?
result = ""
for i in range(1, 11):    result += str(i) + " "
print(result)


#%%%
import pandas as pd


my_list = [1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 1, 0]
''.join([str(item) for item in my_list])

string1 = "student"
string1
for i in range(1, 11):    print(string1 + str(i))

slist1 = [string1 + str(i) for i in range(1,11)]
slist1
#----
rollno = pd.Series(range(1,11))
rollno
name = pd.Series(["student" + str(i) for i in range(1,11)])
name