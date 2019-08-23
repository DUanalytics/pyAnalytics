#Topic:DS - enumerate
#-----------------------------
#A lot of times when dealing with iterators, we also get a need to keep a count of iterations. Python eases the programmers’ task by providing a built-in function enumerate() for this task.
#Enumerate() method adds a counter to an iterable and returns it in a form of enumerate object. This enumerate object can then be used directly in for loops or be converted into a list of tuples using list() method.

#enumerate(iterable, start=0)
#Parameters:
#Iterable: any object that supports iteration
#Start: the index value from which the counter is to be started, by default it is 0 

# enumerate function 
l1 = ["eat","sleep","repeat"] 
obj1 = enumerate(l1) 
print("Return type:",type(obj1)) 
print(list(enumerate(l1))) 
#(position, value)

#printing the tuples in object directly 
for element in enumerate(l1):   print(element) 
for dhiraj in enumerate(l1, start=5):   print(dhiraj) 
# changing index and printing separately 
for count,element in enumerate(l1,start=100): print(count,element)
 
s1 = "geek"
obj2 = enumerate(s1) 
print(list(enumerate(s1,2)) )
#word to characters, start numbering from 2
