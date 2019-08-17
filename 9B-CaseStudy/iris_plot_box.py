#Plots using iris data sets
#-----------------------------
#%
#https://python-graph-gallery.com/36-add-jitter-over-boxplot-seaborn/
# library & dataset
import seaborn as sns
df = sns.load_dataset('iris')

 
# Usual boxplot
ax = sns.boxplot(x='species', y='sepal_length', data=df)
ax = sns.swarmplot(x='species', y='sepal_length', data=df, color="grey")
# Add jitter with the swarmplot function.