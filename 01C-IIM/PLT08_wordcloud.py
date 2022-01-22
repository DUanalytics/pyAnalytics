#Word Cloud
from wordcloud import WordCloud  #check if avl
#conda install -c conda-forge wordcloud  #or
#!pip install wordcloud
from wordcloud import WordCloud

# Read the whole text.
s = 'adithya adithya adithya adithya dhiraj upadhyaya dhiraj dhiraj noida delhi'
text = s

# Generate a word cloud image
wordcloud = WordCloud().generate(text)
wordcloud
# Display the generated image:
# the matplotlib way:
import matplotlib.pyplot as plt


# take relative word frequencies into account, lower max_font_size
wordcloud = WordCloud(background_color="white", max_words=len(s), max_font_size=40, relative_scaling=.5).generate(text)
plt.figure()
plt.imshow(wordcloud)
plt.show();
#plt.axis("off")

## Libraries
from wordcloud import WordCloud
import matplotlib.pyplot as plt
 
# Create a list of word
text=("Python Python Python Matplotlib Matplotlib Seaborn Network Plot Violin Chart Pandas Datascience Wordcloud Spider Radar Parrallel Alpha Color Brewer Density Scatter Barplot Barplot Boxplot Violinplot Treemap Stacked Area Chart Chart Visualization Dataviz Donut Pie Time-Series Wordcloud Wordcloud Sankey Bubble")

# Create the wordcloud object
wordcloud = WordCloud(width=800, height=600, margin=0).generate(text)
 
# Display the generated image:
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.margins(x=0, y=0)
plt.show();

#https://python-graph-gallery.com/260-basic-wordcloud/
#https://python-graph-gallery.com/261-custom-python-wordcloud/
#https://python-graph-gallery.com/262-worcloud-with-specific-shape/

## Load the image (http://python-graph-gallery.com/wp-content/uploads/wave.jpg)
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
# Create a list of word (https://en.wikipedia.org/wiki/Data_visualization)

text=("Data visualization or data visualisation is viewed by many disciplines as a modern equivalent of visual communication. It involves the creation and study of the visual representation of data, meaning information that has been abstracted in some schematic form, including attributes or variables for the units of information A primary goal of data visualization is to communicate information clearly and efficiently via statistical graphics, plots and information graphics. Numerical data may be encoded using dots, lines, or bars, to visually communicate a quantitative message.[2] Effective visualization helps users analyze and reason about data and evidence. It makes complex data more accessible, understandable and usable. Users may have particular analytical tasks, such as making comparisons or understanding causality, and the design principle of the graphic (i.e., showing comparisons or showing causality) follows the task. Tables are generally used where users will look up a specific measurement, while charts of various types are used to show patterns or relationships in the data for one or more variables")
#wave_mask = np.array(Image.open("wave.jpg"))
#copy this wave.jpg in root folder of project 
# Make the figure
#wordcloud = WordCloud(mask=wave_mask).generate(text)  #not found
wordcloud = WordCloud().generate(text)
plt.figure()
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.margins(x=0, y=0)
plt.show();
