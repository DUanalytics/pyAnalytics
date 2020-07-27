#Word Cloud
#-----------------------------
#%
# Libraries
#pip install wordcloud
from wordcloud import WordCloud
import matplotlib.pyplot as plt
 
# Create a list of word
text = ("Ayushi Aditi Ayushi Askhsay Alex Ankita Ankita Shweta Shewta")
# Create the wordcloud object
wordcloud = WordCloud(width=480, height=480, margin=0).generate(text)
# Display the generated image:
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.margins(x=0, y=0)
plt.show()


#text=("Python Python Python Matplotlib Matplotlib Seaborn Network Plot Violin Chart Pandas Datascience Wordcloud Spider Radar Parrallel Alpha Color Brewer Density Scatter Barplot Barplot Boxplot Violinplot Treemap Stacked Area Chart Chart Visualization Dataviz Donut Pie Time-Series Wordcloud Wordcloud Sankey Bubble")