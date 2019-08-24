#Topic ---- Plotting
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pydataset import data
mtcars = data('mtcars')
#conda upgrade --all -y
df=mtcars
df.head()
df.columns
df.dtypes
df.shape
#%%
plot([x], y, [fmt], *, data=None, **kwargs)
plot([x], y, [fmt], [x2], y2, [fmt2], ..., **kwargs)
#%%%  Data from Data Frame
df.sort_values(by='wt', inplace=True)
plt.plot('wt', 'mpg', data=df)
plt.show();

#%%%  X vs Ys
#series and DF
X = df.wt 
X
Ys = df[['mpg', 'disp', 'hp']]
plt.plot(X, Ys)
plt.show();
type(Ys)  # DF


#Arrays : ID, 2D
df.head()
npA = df[['mpg', 'wt', 'drat']].values
type(npA)
npA.shape
npA[:,0]
npA[:,0].reshape(-1,1)
npA[:,1:]

plt.plot(npA[:,0], npA[:,1])
plt.show();

plt.plot(npA[:,0], npA[:,1],'g-', npA[:,0], npA[:,2], 'r-' )
plt.show();


#%%%
x1 = df.wt.values
y1 = df.mpg.values
x2 = df.wt.values
y2 = df.hp.values
plt.plot(x1, y1, 'g-', x2, y2, 'r-')
plt.show()
#%%%  X & Y
Y = df.mpg
plt.plot(X,Y)
