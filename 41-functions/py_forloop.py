# -*- coding: utf-8 -*-
#https://treyhunner.com/2016/04/how-to-loop-with-indexes-in-python/
#for loop

teamA = ['India', 'Australia','Pakistan', 'England']
teamA
teamA[0], teamA[1]

#team names
for i in teamA : print(i)

#characters of the word
for i in teamA[0]: print(i)

for i in teamA:
    if i == 'India' :
        print('India is in Team A', '\t : ' , i)
        break   #exit if India is found otherwise loop over
    else:
        print("India is not in Team A")
    
#x = 'Pakistan'
x = 'Bangladesh'
teamA
for i in teamA:
    if i == x :
        print(x , " is in Team A", '\t : ' , i)
        break   #exit if x is found otherwise loop over
    else:
        print(x , " is not in Team A")

#
range(6)
for x in range(6) : print(x, end = ' ')

range(2,6)
for x in range(2,6) : print(x, end = ' ')

for x in range(2,10,2) : print(x, end = ' ')


#Nested Loops

#Else in the Loop
for x in range(6):
    print(x, end = ' ')
else:
    print("Finished")



