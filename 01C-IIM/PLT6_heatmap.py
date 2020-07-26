#Topic: Heat Map and Correlation Matrix
#-----------------------------
#libraries

import pandas as pd

data = {'A': [45,37,42,35,39], 'B': [38,31,26,28,33], 'C': [10,15,17,21,12]  }

df = pd.DataFrame(data,columns=['A','B','C'])
df

df.corr()  #cor betw A&B, A&C, B&C

import seaborn as sn
import matplotlib.pyplot as plt
sn.heatmap(df.corr(), annot=True)
plt.show()



#http://alanpryorjr.com/visualizations/seaborn/heatmap/heatmap/