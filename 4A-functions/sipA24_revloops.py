# -*- coding: utf-8 -*-
#loops

#for loop

for i in range(1,5):
    print(i, end=' ')

#while

while True:
    s = input("Enter something, end to exit :  ")
    if s == 'end':
        break;
    if (len(s) < 3):
        print('small text')
        continue

        