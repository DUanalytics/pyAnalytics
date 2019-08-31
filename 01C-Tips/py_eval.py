#
#-----------------------------
#%
#pandas.eval() 
import pandas as pd
nrows, ncols = 100000, 100
nrows, ncols
rng = np.random.RandomState(42)
rng
df1, df2, df3, df4 = (pd.DataFrame(rng.rand(nrows, ncols)) for i in range(4))
df1.head()
df2
df3
df4
%timeit df1 + df2 + df3 + df4
%timeit pd.eval('df1+df2+df3+df4')

np.allclose(df1+df2+df3+df4, pd.eval('df1+df2+df3+df4'))

#Arithmetic Operators

#Comparison

#Bitwise

#Object Attributes


#Columnwise Operations