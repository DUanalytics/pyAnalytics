# -*- coding: utf-8 -*-
#Loop - while
#execute set of statements as long as the condition is true

i = 1
while (i < 10):
    print(i, end =' ')
    i += 1  #import to increment

#break the loop in between

i = 1
while (i < 10):
    print(i, end = '\t')
    if i == 5 : #end here
        print('Exiting Loop at this point')
        break
    i += 1

#use of continue - continue with loop
i = 1
while (i < 10):
    print(i, end = '\t')
    i += 1
    if i == 5 : #continue with loop
        continue

