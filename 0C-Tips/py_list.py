#
#-----------------------------
#%

import pandas as pd
df = pd.DataFrame({'ID':['1','2','3'], 'col_1':[0,2,3],'col_2': [1,4,5]})
df
mylist = ['a','b','c','d','e','f']
def get_sublist(sta, end):    return mylist[sta:end+1]

print(df)

df['col_3'] = df['col_1'] + df['col_2']
print(df)
print(mylist)

def f(x):
    return x[0] + x[1]


print(df.apply(f, axis=0))

print(df.apply(lambda x: x[0] + x[1], axis=0))

def sublist(row):
    return mylist[row['col_1']:row['col_2']]
df['J3'] = df.apply(sublist,axis=1)
print(df)
df['col_4'] = list(map(get_sublist,df['col_1'],df['col_2']))
print(df)
