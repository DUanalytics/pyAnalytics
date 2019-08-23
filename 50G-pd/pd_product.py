#
#-----------------------------
#%
#data frame from Product
import pandas as pd
import numpy as np

pd.MultiIndex.from_product([np.linspace(1, 5, 2), np.linspace(0, 8, 3)], names=['a', 'b']).to_frame(index=False)

slist = ['S1','S2','S3']
sub = ['sub1','sub2']

pd.MultiIndex.from_product([slist, sub]).to_frame(index=False)

pd.MultiIndex.from_product([slist, sub]).to_frame(columns=['Student', 'Subject'], index=False)  #not correct

df1= pd.MultiIndex.from_product([slist, sub]).to_frame(index=False)
df1
df1.columns = (['Student', 'Subject'])
df1
