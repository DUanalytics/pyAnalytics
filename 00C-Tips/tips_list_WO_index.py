#Printing items in list

#-----------------------------
#%
#print list items without using index

list1 = [1, 4, 5, 6, 7] 
list1  

#
for i in range(len(list1)): 
    print ('Item No ', i, ' is ', end = " ") 
    print (list1[i]) 
#
[ i for i in list1]
#enumerate
for index, value in enumerate(list1): 
    print('Item No - ',index, ' is ', value)

#zip
for index, value in zip(range(len(list1)), list1): 
    print('Item No - ',index, ' is ', value)
    
#for
for i in range(len(list1)): print(list1[i], end=' ')

#
print(*list1)
#
list2 =['A','Dhiraj', 'C']
list2
print(' '.join(list2)) 
str(list2)[1:-1]  
print(' '.join(map(str, list2)))
print(('\n'.join(map(str, list2))))
