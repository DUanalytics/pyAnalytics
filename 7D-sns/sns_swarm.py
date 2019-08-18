#SNS - Swarm Plot
#-----------------------------
#%

# Pandas for managing datasets
import pandas as pd
# Matplotlib for additional customization
from matplotlib import pyplot as plt
# Seaborn for plotting and styling
import seaborn as sns
#we gave each of our imported libraries an alias. Later, we can invoke Pandas with pd, Matplotlib with plt, and Seaborn with sns.
#https://elitedatascience.com/python-seaborn-tutorial#step-1
#The argument  index_col=0 simply means we'll treat the first column of the dataset as the ID column.
# Read dataset
df = pd.read_csv('data/pokemon.csv', index_col=0)
df = pd.read_csv('https://elitedatascience.com/wp-content/uploads/2017/04/Pokemon.csv')
df
#One of Seaborn's greatest strengths is its diversity of plotting functions. For instance, making a scatter plot is just one line of code using the lmplot() function.
#There are two ways you can do so.
#The first way (recommended) is to pass your DataFrame to the data= argument, while passing column names to the axes arguments, x= and y=.
#The second way is to directly pass in Series of data to the axes arguments.
#Default ScatterplotPython
# Recommended way
from pydataset import data
mtcars = data('mtcars')
mtcars.head()
sns.lmplot(x='wt', y='mpg', data=mtcars)
 
# Alternative way
sns.lmplot(x=mtcas.wt, y=mtcars.mgp)

#Seaborn doesn't have a dedicated scatter plot function, which is why you see a diagonal line. We actually used Seaborn's function for fitting and plotting a regression line.

#Thankfully, each plotting function has several useful options that you can set. Here's how we can tweak the lmplot():
#First, we'll set fit_reg=False to remove the regression line, since we only want a scatter plot.
#Then, we'll set hue='Stage' to color our points by the Pokémon's evolution stage. This hue argument is very useful because it allows you to express a third dimension of information using color.

2
# Display first 5 observations
df.head()

#Scatterplot parametersPython

# Scatterplot arguments
sns.lmplot(x='wt', y='mpg', data=mtcars, fit_reg=False,       hue='gear')  # No regression line  # Color by evolution stage
# Tweak using Matplotlib
plt.ylim(0, None)
plt.xlim(0, None)

#Seaborn is a high-level interface to Matplotlib. From our experience, Seaborn will get you most of the way there, but you'll sometimes need to bring in Matplotlib.

#Setting your axes limits is one of those times, but the process is pretty simple:

#First, invoke your Seaborn plotting function as normal.
#Then, invoke Matplotlib's customization functions. In this case, we'll use its ylim() and xlim() functions.
#%%
#Even though this is a Seaborn tutorial, Pandas actually plays a very important role. You see, Seaborn's plotting functions benefit from a base DataFrame that's reasonably formatted.
#For example, let's say we wanted to make a box plot for our Pokémon's combat stats:

df=mtcars
# Boxplot
sns.boxplot(data=mtcars[['mpg','wt']])
# Pre-format DataFrame
stats_df = mtcars.drop(['gear', 'cyl', 'am','vs','carb'], axis=1)
 
# New boxplot using stats_df
sns.boxplot(data=stats_df)

#Another advantage of Seaborn is that it comes with decent style themes right out of the box. The default theme is called 'darkgrid'.
#Next, we'll change the theme to 'whitegrid' while making a violin plot.
#Violin plots are useful alternatives to box plots.
#They show the distribution (through the thickness of the violin) instead of only the summary statistics.
# Set theme
sns.set_style('whitegrid')
 
# Violin plot
sns.violinplot(x='gear', y='mpg', data=df)

#Seaborn allows us to set custom color palettes. We can simply create an ordered Python list of color hex values.
gear_type_colors = ['#78C850',  '#F08030', '#6890F0']
# gear1 # gear2 # gear3
sns.violinplot(x='gear', y='mpg', data=df,                palette=gear_type_colors)
 # Set color palette

#Violin plots are great for visualizing distributions. However, since we only have 151 Pokémon in our dataset, we may want to simply display each point.
#That's where the swarm plot comes in. This visualization will show each point, while "stacking" those with similar values:
 # Swarm plot with Pokemon color palette
sns.swarmplot(x='gear', y='mpg', data=df,  palette=gear_type_colors)
#That's handy, but can't we combine our swarm plot and the violin plot
#It's pretty straightforward to overlay plots using Seaborn, and it works the same way as with Matplotlib. Here's what we'll do:
#First, we'll make our figure larger using Matplotlib.
#Then, we'll plot the violin plot. However, we'll set inner=None to remove the bars inside the violins.
#Next, we'll plot the swarm plot. This time, we'll make the points black so they pop out more.
#Finally, we'll set a title using Matplotlib.

# Set figure size with matplotlib
plt.figure(figsize=(10,6))
# Create plot# Remove the bars inside the violins
sns.violinplot(x='gear', y='mpg',  data=df, inner=None,  palette=gear_type_colors)
sns.swarmplot(x='gear', y='mpg', data=df,  alpha=0.7, hue='am')
 # Make points black # and slightly transparent
# Set title with matplotlib
plt.title('MPG by gear')

#
sns.swarmplot(x='gear', y='mpg', data=df, alpha=0.7, hue='am')
plt.legend(bbox_to_anchor=(1, 1), loc=2)

# Calculate correlations
corr = df.corr()

# Heatmap
plt.figure(figsize=(10,6))
sns.heatmap(corr)

sns.distplot(df.mpg)

#
# Count Plot (a.k.a. Bar Plot)
sns.countplot(x='gear', data=df, palette=gear_type_colors)
# Rotate x-labels
plt.xticks(rotation=-45)

#FactorPlotFactor PlotPython

# Factor Plot
g = sns.factorplot(x='gear', 
                   y='mpg', 
                   data=df, 
                   hue='cyl',  # Color by stage
                   col='am',  # Separate by stage
                   kind='swarm') # Swarmplot
 
# Rotate x-axis labels
g.set_xticklabels(rotation=-45)
 
# Doesn't work because only rotates last plot
# plt.xticks(rotation=-45)