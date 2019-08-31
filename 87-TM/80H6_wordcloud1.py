#word Cloud 2

import pandas as pd
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt

url ='https://raw.githubusercontent.com/DUanalytics/datasets/master/csv/wcwords1.csv'
df = pd.read_csv(url)
#df = pd.read_csv(r"data\wcwords1.csv")
df.head()
df.columns
df1=df.sort_values(by='freq', ascending=False)
df1.head(50)
#now make wordcloud with different options
wc2a = WordCloud(min_font_size=2, max_words=100, max_font_size=10)
wc2b = WordCloud(min_font_size=5, max_words=100, max_font_size=20)
wc2c = WordCloud(min_font_size=8, max_words=50, max_font_size=25)
#collect data from df1
wordcloud2a  = wc2a.generate(' '.join(df1['word']))
wordcloud2b  = wc2b.generate(' '.join(df1['word']))
wordcloud2c =  wc2c.generate(' '.join(df1['word']))
#wordcloud2 = WordCloud().generate(' '.join(df['word']))

plt.figure(figsize=(10,6), facecolor=None)
plt.imshow(wordcloud2b)
#change above to wordcloud2a, 2b, 2c
plt.axis('off')
plt.tight_layout(pad=0)
plt.show();

#%%%  End here....
#
#pandas to dictionary
df
dfdict = df.to_dict('series')
dfdict['word']
dfdict['freq']
dfdict
names = df['word']
freqs = df['freq']
words = zip(names, freqs)
words

wc = WordCloud(background_color='white')
wordcloud3 = wc.generate_from_frequencies(words)



# from text document
import nltk
from nltk.corpus import webtext
from nltk.probability import FreqDist
from wordcloud import WordCloud
import matplotlib.pyplot as plt

#nltk.download("webtext")
import os
os.getcwd()
wt_words = webtext.words('E:/pywork/pyprojects/pyanalytics19/data/testing.txt') #sample data
data_analysis = nltk.FreqDist(wt_words)
data_analysis
filter_words = dict([(m,n) for m, n in data_analysis.items() if len(m) > 3])
filter_words
wcloud = WordCloud().generate_from_frequencies(filter_words)

plt.imshow(wcloud, interpolation ='bilinear')
plt.axis('off')
plt.show()