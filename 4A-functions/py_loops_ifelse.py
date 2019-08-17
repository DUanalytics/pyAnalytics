#Loops / if Else
#-----------------------------
#%
marks=43
if marks > 60:
    print("First Division")
elif marks > 40:
    print(" Pass")
elif (marks < 40):
    print(" Fail")
else:
    print("Incorrect Marks")

#multi line comment
primes = [2,3,5,7]
for prime in primes:    print(prime)

for x in range(5):    print(x)
for x in range(7,10):    print("\t", x)
for x in range(7,100,5):    print(x,sep="\t")


count=0
while count < 5:
    print(count)
    count += 1

count =1
while (True):
    print(count)
    count += 1
    if (count > 5):
        break

from time import time as t

def xrange(x):

    return iter(range(x))

def count():
    st = t()
    [x for x in xrange(10000000) if x%4 == 0]
    et = t()
    print (et-st)
count()

for x in range(10):
    if x%2 == 0:
        continue
    print(x)

count=0
while(count<5):
    print(count)
    count += 1
else:
    print(" While Loop Complete")

for i in range(10):
    if(i%5==0):
        break
    print(i)
else:
    print(" Not printed because of loop configuration; It does not reach here")