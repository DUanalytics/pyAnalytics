# -*- coding: utf-8 -*-
#word Cloud 2

import pandas as pd
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt


df = pd.read_csv(r"data\wcwords1.csv")
df.columns
df1=df.sort_values(by='freq', ascending=False)
df1.head(50)
#now make wordcloud
wc = WordCloud(min_font_size=5, max_words=100, max_font_size=20)
wc2a = WordCloud(min_font_size=5, max_words=100, max_font_size=20)
wc2b = WordCloud(min_font_size=8, max_words=50, max_font_size=25)

wordcloud2a  = wc2a.generate(' '.join(df1['word']))
wordcloud2b =  wc2b.generate(' '.join(df1['word']))
#wordcloud2 = WordCloud().generate(' '.join(df['word']))


plt.figure(figsize=(15,20), facecolor=None)
plt.imshow(wordcloud2b)
plt.axis('off')
plt.tight_layout(pad=0)
plt.show()

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