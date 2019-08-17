#Heat Map 2
#-----------------------------
#%
# library
import seaborn as sns
import pandas as pd
import numpy as np
 
# Create a dataset (fake)
df = pd.DataFrame(np.random.random((10,10)), columns=["a","b","c","d","e","f","g","h","i","j"])
#1/ Annotate each cell with value
#annot=True will add a label into each cell, providing the exact value behind the color.
sns.heatmap(df, linewidths=2, linecolor='yellow')
sns.plt.show()


#view sourceprint?
sns.heatmap(df, annot=True, annot_kws={"size": 7})
#sns.plt.show()

#
#3/ Remove X or Y labels
#yticklabels and xticklabels control the presence / abscence of labels for the Y and X axis respectively.

#view sourceprint?
sns.heatmap(df, yticklabels=False)
#sns.plt.show()

#/ Remove color bar

sns.heatmap(df, cbar=False)
#sns.plt.show()

#
sns.heatmap(df, xticklabels=4)
#sns.plt.show()

