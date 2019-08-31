#Topic: TT
#-----------------------------
#
#Ex1.1
#Write a program to get the Python version you are using
import sys
print(sys.version)
#https://tecadmin.net/check-python-version-shell-script/
#or in anacond command prompt
#C:\>python

#Ex1.2
#Write a python programm which accepts the radius of a circle from the user and computes the area

name = input("Enter your name : ") 
radius = float(input("Enter your radius : "))
#if int values has to passed use : int(input())
print(name, ' Area of Circle is ', 3.14 * radius **2)

#using lib
import math
print(math.pi)
print(name, " Area is ", math.pi * pow(radius,2))

#%%%

#Ex2.1
#Write a python program to displya the current date and time
import datetime
currentDT = datetime.datetime.now()
print(str(currentDT))    
print (currentDT.strftime("%Y-%m-%d %H:%M:%S"))
#https://tecadmin.net/get-current-date-time-python/
#Ex2.2 : same as Ex2.1

#%%%
#Ex2.2 
#Accept user's first and last name and print them in reverse order with a space in between 
#https://www.geeksforgeeks.org/reverse-words-given-string-python/

name='Tanvi Tiwari'
print(name)
namesplit = name.split()  # split first
namesplit
namesplit.reverse() # reverse list
namesplit  #should ['Tiwari', 'Tanvi']
# now join them
result = " ".join(namesplit)
print(result)

#another method
myname = input("Enter Your Name")
print(" ".join(myname.split(" ")[::-1]))
#another method
my_string = "I live in Wakhnaghat"
reversed_string = " ".join(my_string.split(" ")[::-1])
reversed_string
#https://stackoverflow.com/questions/34128842/how-to-reverse-the-order-of-the-words-string-using-python

##3.2 : Display first and last colors from the following list
color_list = ['Red', 'Green', 'White', 'Black']
len(color_list)
color_list[0]
color_list[len(color_list)-1]
for color in color_list: print(color, "=", len(color))  #size of word
for i in range(len(color_list)):    print(color_list[i], end=' ,')
#another method
for i in range(len(color_list)):    
    if (i==0)   :
        print(color_list[i])
    elif( i == len(color_list)-1)  :
        print(color_list[i])


#%%%
#Ex4: Write a python program to print the documents (syntax, description etc of python built in function)
abs(-4.4)
help(abs)
abs?
def printSyntax(functionName):  print(help(functionName))
printSyntax(abs)
printSyntax(max)

#%%%
#Ex5 Write a python program to get the difference between a given number and 17.If the no is > 178, return double the absoluted difference
inputNo = int(input("Enter your number "))
if( inputNo - 17 > 178):
    print(2 * abs(inputNo-17))
#using a function: run next 3 lines together to create function
def lab5a(inputValue):
    if( inputValue - 17 > 178):
        print(2 * abs(inputValue-17))
    
lab5a(inputNo)

#Write a program to test whether a number is between 1000 or 2000:
inputNo = int(input("Enter your number "))
if((inputNo > 100) & (inputNo < 2000)):
    print(" Number between 100 and 2000")
else:
    print(" Number NOT between 100 and 2000")
    

    
#Write a program to check whether a specified value is contained in a group of values
#Test Data : 3 -> [1,5,8,3] : True ; -1 -> False
list1 = [1,5,8,3]
n1= 3
n1 in list1
n2 in list1
#using a function
def lab5c(no):
    if no in list1:
        print(no, " is in the list ", list1)
    else:
        print(no, " is NOT in the list ", list1)    
lab5c(n1)
lab5c(n2)


#%%%
#%%%
#Ex6a : Write a program to print all even nos from a given no list in the same order and stop printing if any no that come after 237 in the sequence
numbers = [386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978,328, 615, 953, 345, 399, 162, 758, 219, 918, 237, 412, 566,826, 248, 866, 950, 626, 949, 687, 217, 815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717, 958,743, 527]
#check for even no
3%2==0
4%2==0

for no in numbers:
    if (no%2 == 0)  :
        print(no , end=', ')

for no in numbers:
    if (no%2 == 0)  :
        print(no , end=', ')
    if (no == 237)  :
        break
print(numbers, end=' , ')
numbers.index(237)  #this is position of 237 in the list : 21st
#print this list into a file
#printing list
print(*numbers, sep='\n')
print(*numbers, file='tt/numbers2.txt')
print('\n'.join(map(str, numbers))) 

#saving into a file
import pickle
with open('tt/numbers2.txt', 'wb') as fp:
    pickle.dump(numbers, fp)
#reading it pack
with open ('tt/numbers2', 'rb') as fp:
    itemlist = pickle.load(fp)
itemlist

#Ex: using file as input: change the path of the file.
#data = [line.strip() for line in open("tt/numbers2.txt", 'r')]
#execute the earlier function
for no in itemlist:
    if (no%2 == 0)  :
        print(no , end=', ')
    if (no == 237)  :
        break


#%%%
#Ex 7: Write a Python program that accepts a single integer value entered by the user. If the value entered is less than one, the program prints nothing. If the user enters a positive integer, n, the program prints an n×n box drawn with * characters. If the users enters 1, for example, the program prints * If the user enters a 2, it prints ** ** An entry of three

def lab7a(userinput):
    print("your input is ", userinput)
    if (userinput <=1 )  :
        print("No <= 1")
    else:
        for i in range(0, userinput):
            for j in range(0, userinput):
                print('*', end =' ')
            print(' ', end = ' ')
#use the function now
lab7a(1)
lab7a(2)
lab7a(3)
lab7a(4)
userVal = int(input("Enter a integer value between 1 and 10 : "))
print("your input is ", userVal)
lab7a(userVal)


#%%%
#Ex 8a : Write a Python program to sum of two given integers.However, if the sum is between 15 to 20 it will return 20. 
#https://www.geeksforgeeks.org/taking-multiple-inputs-from-user-in-python/

x, y = [int(x) for x in input("Enter 2 value with space in betw: ").split()] 
print(x, " ", y)
#sumNos = n1 + n2
def lab8a(n1, n2):
    sumNos = n1 + n2
    print('Sum of the two nos is ', sumNos)
    if (sumNos > 15 & sumNos < 20)  :
        print('Sum is ', 20 , " because their sum is between 15 & 20")
    else:
        print("Sum ", sumNos,  " not between 15 and 20")

lab8a(x,y)


#Ex 8b : Write a Python program to compute the future value of a specified principal amount, rate of interest, and a number of years.
#Test Data : amt = 10000, int = 3.5, years = 7 Expected Output : 12722.79
#FV = (PV * Rate * Interest) / 100 + PV
amt = 10000; int=3.5; years=7
print('Amount : ', amt, ' Interest : ', int, " Years : ", years)
#simple Interest
FV1 = (amt * int * years)/ 100 + amt
print("Future Value using Simple Interest ", FV1)
#compount Interest
FV2 = amt * pow((1 + int/100),years)
print("Future Value using Compound Interest ", round(FV2,2))


#%%
#Ex 9 : Write a Python program to create an array of 5 integers and display the array items. Access individual element through indexes. Write a Python program to convert an array to an ordinary list with the same items.

from array import *
array1 = array('i',[4,8,10,3,6])
print(array1)
for element in array1:  print(element, end=' , ')
list(array1)
print("Array to List ", list(array1))

#another method using numpy
import numpy as np
array2 = np.array([40,80,100,30,60], dtype='int32')
print(array2)
for element in array2:  print(element, end =' : ')
print("NP array to list ", list(array2))


#Ex10 : Write a Python program to display all the member name of an enum class ordered by their values. Expected Output: Country Name ordered by Country Code: Afghanistan Algeria Angola Albania Andorra Antarctica
countries = {'Afghanistan': 93, 'Albania': 355, 'Algeria': 213, 'Andorra': 376, 'Angola': 244, 'Antarctica': 672}
countries
for i in countries:     print(i, countries[i])
countries.keys()
countries.values()
list(countries.values())
#another way if codes are not known
countries2 = ['Aghanistan', 'Algeria', 'Angola', 'Albania', 'Andora', 'Antartica']
ecountries2 = enumerate(countries2)
print(list(ecountries2))
print(list(enumerate(countries2, start=2)))  #start code from 2
#https://www.geeksforgeeks.org/enumerate-in-python/
# printing the tuples in object directly 
for element in enumerate(countries2): print(element) 
# changing index and printing separately 
for count,element in enumerate(countries2,100): print(count,element) 
#https://www.w3resource.com/python-exercises/data-structures-and-algorithms/python-data-structure-exercise-4.php

#%%%
#Ex 11 : Write a Python program to get all values from an enum class.
#Expected output: [93, 355, 213, 376, 244, 672].
from enum import IntEnum
class Color(IntEnum):
   RED = 1
   BLUE = 2
[e.value for e in Color]
#
from enum import Enum
class Letter(Enum):
   A = 1
   B = 2
   C = 3
print({i.name: i.value for i in Letter})
# prints {'A': 1, 'B': 2, 'C': 3}

from enum import IntEnum
class Country(IntEnum):
    Afghanistan = 93
    Albania = 355
    Algeria = 213
    Andorra = 376
    Angola = 244
    Antarctica = 672
print({i.name: i.value for i in Country})
print({i.value for i in Country})

#https://stackoverflow.com/questions/29503339/how-to-get-all-values-from-python-enum-class


#%%
#Ex12 : Write a Python program to get an array buffer information
#Expected Output: Array buffer start address in memory and number of elements. (25855056, 2)
from array import array
a = array("I", (12,25))
print("Array buffer start address in memory and number of elements." , a.buffer_info())
#https://www.w3resource.com/python-exercises/data-structures-and-algorithms/python-data-structure-exercise-14.php
