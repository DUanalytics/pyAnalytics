#Lambda
#-----------------------------
#%

import csv
file = open('yob1910.txt','r')  # in read mode
data = csv.reader(file)
table = [row for row in data]
print(table[:3])

names = ['name','sex','count']
print(names)

# Grouping the data
from itertools import groupby
for key,group in groupby(table, lambda x: x[1]):
    total = 0
    for item in group:
        total += int(item[2])
    print(item[1], total)

# Anonymous Lambda Functions
def f(x):
    return x*2
f_lambda = lambda x: x*2
f_lambda2 = lambda y: y*3
print(f(3)) # 6
print(f(5)) # 10
print(f_lambda(3)) # 6
print(f_lambda2(4)) # 12

#import pandas as pd
#input_list = [1,2,3]
#print(pd.lreshape(input_list, lambda x: x * 2))

def my_test2(row):
    return row['a'] % row['c']