#Plot - Heat Map
#-----------------------------
#%
#e call ‘wide format‘ or ‘untidy format‘ a matrix where each row is an individual, and each column represents an observation. In this case, a heatmap consists to make a visual representation of the matrix: each square of the heatmap represents a cell. The color of the cell changes following its value.

# library
import seaborn as sns
import pandas as pd
import numpy as np

# Create a dataset (fake)
df = pd.DataFrame(np.random.random((5,5)), columns= ["a","b","c","d","e"])
df
# Default heatmap: just a visualization of this square matrix
p1 = sns.heatmap(df)
