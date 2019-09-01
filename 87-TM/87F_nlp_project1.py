#NLP Projects

#-----------------------------
#%
#Run these lines of code in the command prompt of the computer or in the python editor
pip install beautifulsoup4
pip install -U nltk
pip install -U numpy
pip install -U setuptools
pip install -U sumy

#Kindly run the bunch of codes under a specific comment one by one

#Importing library nltk
import nltk
nltk.download('punkt')
#Downloading stopwords which include all the english alphabets
nltk.download("stopwords")

#Importing BeautifulSoup, urlib.request and re libraries
import bs4 as bs
import urllib.request
import re

#Importing the article from a url
data = urllib.request.urlopen('https://www.espncricinfo.com/series/19366/report/1190801/west-indies-a-vs-india-a-3rd-unofficial-odi-india-a-in-west-indies-2019')
article = data.read()

#Making the article beautiful(Easy to read)
parsed_article = bs.BeautifulSoup(article,'lxml')

#Inspecting elements from different websites, 'p' tags are mostly used, thus used find_all function that returns all the paragraphs in the article in the form of a list
paragraphs = parsed_article.find_all('p')

text = ""

for p in paragraphs:  
    text += p.text


#Removing unnecessary punctuations
text = re.sub(r'\[[0-9]*\]', ' ', text)
text = re.sub(r'\s+', ' ', text)

#Removing special characters and digits
formatted_text = re.sub('[^a-zA-Z]', ' ', text )  
formatted_text = re.sub(r'\s+', ' ', formatted_text)

#Converting text to sentences using tokenization technique
sentence_list = nltk.sent_tokenize(text)

#Finding out the frequency of each word
stopwords = nltk.corpus.stopwords.words('english')

frequencies = {}
for word in nltk.word_tokenize(formatted_text):
    if word not in stopwords:
        if word not in frequencies.keys():
            frequencies[word] = 1
        else:
            frequencies[word] += 1

#Now find out the weighted frequency so that long sentences do not end up with higher scores though they have lesser frequent words
maximum_frequncy = max(frequencies.values())

for word in frequencies.keys():
    frequencies[word] = (frequencies[word]/maximum_frequncy)

#Finding out the sentence scores
sentence_scores = {}
for sent in sentence_list:
    for word in nltk.word_tokenize(sent.lower()):
        if word in frequencies.keys():
            if len(sent.split(' ')) < 30:
                if sent not in sentence_scores.keys():
                    sentence_scores[sent] = frequencies[word]
                else:
                    sentence_scores[sent] += frequencies[word]

#Importing heapq library to find the summary of the article which gives the desired summary

import heapq
summary = heapq.nlargest(3, sentence_scores, key=sentence_scores.get)

final_summary = ' '.join(summary)
print(final_summary)