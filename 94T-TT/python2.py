#Topic: TT: Ex
#-----------------------------
#libraries

#Ex-13 : Write a Python program to push three items into a heap andreturn the smallest item from the heap. Also Pop and return the smallest item from the heap
#https://www.w3resource.com/python-exercises/data-structures-and-algorithms/python-data-structure-exercise-21.php
#https://www.geeksforgeeks.org/heap-queue-or-heapq-in-python/

import heapq
myheap = []
heapq.heappush(myheap, ('V', 3))
myheap
heapq.heappush(myheap, ('V', 2))
myheap
heapq.heappush(myheap, ('V', 1))
myheap

print("Items in the heap:")
for a in myheap: 	print(a)

#Using heap push item on the heap and return the smallest item
myheap
#when we pop, smallest item is popped out
print("The smallest item in the heap ")
heapq.heappop(myheap)
print("Items in the heap ")
myheap  #1 removed
print("Next smallest item in the heap ")
heapq.heappop(myheap)
myheap  #2 removed
heapq.heappop(myheap)
myheap  #3 removed

#add 5
heapq.heappush(myheap, ('V', 4))
heapq.heappush(myheap, ('V', 5))
myheap
#pop and push together
heapq.heappushpop(myheap, ('V', 6))
for a in myheap: 	print(a)

#Another ex in heap: # initializing list 
#https://www.geeksforgeeks.org/heap-queue-or-heapq-in-python/
list1 = [5, 7, 9, 1, 3]   
# using heapify to convert list into heap 
heapq.heapify(list1) 
# printing created heap 
print ("The created heap is : ",end="") 
print (list(list1)) 
# using heappush() to push elements into heap 
# pushes 4 
heapq.heappush(list1,4) 
list1  
# printing modified heap 
print ("The modified heap after push is : ",end="") 
print (list(list1)) 
  
# using heappop() to pop smallest element 
print ("The popped and smallest element is : ",end="") 
print (heapq.heappop(list1)) 


#%%%
#Ex: 15/16 : Write a function named print_big_enough that accepts two parameters, a list of numbers and a number. The function should print, in order, all the elements in the list that are at least as large as the second parameter.
#list of numbers = xlist, number = y
xlist = [3,5,2,6,2,22,52,8]
y = 10
#Output = [3,5,2,6,2,8]
for i in range(len(xlist)):
    if (xlist[i] < y):
        print(xlist[i], end=' ,')

def lab15a(xlist, y):
    print("list : ", xlist, " Number ", y)
    for i in range(len(xlist)):
        if (xlist[i] < y):
            print(xlist[i], sep =' ', end =' ')
#
print("Enter numbers with spaces which go into a list")
inputList = list(map(int, input().split()))
inputList
# enter elements separated by spaces and x will be your list
# you can change the type of your elements like int for 
# integer,str for string,etc. 
no1 = int(input("Enter the number you want to compare with ? "))
print(no1)
lab15a(xlist = inputList, y=no1)

#%%%
#Ex17
#Write a function called draw_rectangle that takes a Canvasand a Rectangle as arguments and draws a representation of  the Rectangle on the Canvas. 
#2. Add an attribute named color to your Rectangle objects and modify draw_rectangle so that it uses the color attribute as the fill color. 
#3. Write a function called draw_point that takes a Canvas and a Point a arguments and draws a representation of the Point on the Canvas.
#4. Define a new class called Circle with appropriate attributes and instantiate a few Circle objects. Write a function called draw_circle that draws circles on the canvas.



#5. Write a program that draws the national flag of the India. Hint: you can draw a polygon like this: points = [[-150,-100], [150, 100], [150, -100]] canvas.polygon(points, fill='saffron,white,green')
#Ex18e



#Ex19


#Ex21


#Ex23

#Ex25

#Ex27

#Ex29




