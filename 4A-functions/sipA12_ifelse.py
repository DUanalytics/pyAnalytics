# -*- coding: utf-8 -*-
#if-else condition
#logical operations


x=1
#short methods
if x == 1 : print("x = 1")
#
y=2
print(x) if x > y else print(y)
x=1
print("This is X", x) if x==1 else print("x not equal to 1")
#3 conditions
x=3; y=3
print("X") if x > y else print("=") if x == y else print("Y")
#longer way
if x > y:
    print("X")
elif x == y:
    print("=")
else :
    print("Y")



#other logical operations
#==, !=, <, > , <=, >= 

#with else 


if x == 1: 
    print(" x=1")
else:
    print("x not equal to 1")
x=2

if x == 1: 
    print(" x=1")
else:
    print("x not equal to 1")

#no bracket, use of indentation with colon operator
#elif

if x == 1: 
    print(" x=1")
elif x == 2:
    print(" x=2")
else :
    print("x not equal to 1 or 2")

x=3
if x == 1: 
    print(" x=1")
elif x == 2:
    print(" x=2")
else :
    print("x not equal to 1 or 2")


#shorthand if

#or and and
x=3; y=4; z=5
if x < y and y < z:
  print("Both conditions are True")

z=2

if x < y or y > z:
  print("Both conditions are True")

if (x < y) or (y > z) :
  print("Either conditions are True")

if ((x < y) or (y > z)) and (x > 10):
    print("Both conditions are True")
else:
    print("Conditions are not True")

if ((x < y) or (y > z)) or (x > 10):
    print("Either conditions are True")
else:
    print("Conditions are not True")

(x < y) or (y > z) and (x > 10)
x<y, x>z, x<10
True or False and True  #left to right

(x > 10) and (x < y) and (y > z)  

if (x < y) or (y > z) and (x > 10):
    print("Either conditions are True")
else:
    print("Conditions are not True")
