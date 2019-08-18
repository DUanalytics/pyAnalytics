#Pandas + NP
#-----------------------------
#%
import pandas as pd
pd.np.random.randint(10,100, 50)

import numpy as np

df = pd.DataFrame(np.random.randn(8, 4),)
df.rename({0:'A',1:'B',2:'C',3:'D'}, axis=1,inplace=True)
df.head()
df['A']
df.loc[:,'A':'B']
df.loc[:,slice('A','C')]
df.loc[:,['A','C']]

df.filter(items=['A','C'])
df
df.filter(like='0', axis=0)
df.filter(like='A', axis=1)


import string
string.ascii_lowercase
list(map(chr, range(97, 123))) 
#or list(map(chr, range(ord('a'), ord('z')+1)))
string.ascii_lowercase[::-1]
[chr(i) for i in range(ord('a'),ord('z')+1)]
import string
list(string.ascii_lowercase[0:10])
