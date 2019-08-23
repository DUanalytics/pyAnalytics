#Cross - Section - Index
#-----------------------------
#%
##https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.xs.html

d = {'num_legs': [4, 4, 2, 2],   'num_wings': [0, 0, 2, 2], 'class': ['mammal', 'mammal', 'mammal', 'bird'], 'animal': ['cat', 'dog', 'bat', 'penguin'], 'locomotion': ['walks', 'walks', 'flies', 'walks']}
d
df = pd.DataFrame(data=d)
df = df.set_index(['class', 'animal', 'locomotion'])
df

df.xs('mammal', axis=0)
