#SNS - Box Plot
#-----------------------------
#%
# library & dataset
import seaborn as sns
df = sns.load_dataset('iris')
 
# Usual boxplot
ax = sns.boxplot(x='species', y='sepal_length', data=df)
 
# Add jitter with the swarmplot function.
ax = sns.swarmplot(x='species', y='sepal_length', data=df, color="grey")
