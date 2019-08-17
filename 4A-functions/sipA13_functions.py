# -*- coding: utf-8 -*-
#Functions
#Block of code which only runs when it is called
#can pass data, known parameters into function
#it can return data as result
#defined using keyword def with colon :

def printHello():
    print("Hello ")
    
printHello()

def printHello2(name):
    print("Hello \t" + name)

printHello2()
printHello2('Dhiraj')

def printHello3(name='Student'):
    print("Hello \t" + name)

printHello3()  #without value
printHello3('Dhiraj')

#passing a list 

def printHello4(names):
    for i in names:
        print("Hello \t" + i)

printHello4()
printHello4('Dhiraj')

printHello4(['Dhiraj','Kounal','Pooja'])

namelist  = ['Student1','Student2','Student3']
printHello4(namelist)


#retun values

def totalSale(x=0,y=0):
    return(x + y)
    
totalSale()
totalSale(5,10)
