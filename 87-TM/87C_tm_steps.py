#Text Processing - Steps

import pandas as pd
import matplotlib.pyplot as plt
#%matplotlib inline  
import nltk
from nltk import word_tokenize, sent_tokenize
from nltk.corpus import stopwords


import re
sent_analysis = {"beer": 10, "wine":13,"spirit": 11,"cider":16,"shot":16}

def sentiment_analysis(dic, text):
    result = 0.00
    s = re.sub(r'[^\w\s]','',text)
    return sum([dic[x] for x in s.split() if x in dic])
sent_analysis

sentiment_analysis(sent_analysis,"the beer,% wine &*and cider @were great")
#beer-10, spirit-11m
#%%%
#remove numbers

import re
input_str = 'Box A contains 3 red and 5 white balls, while Box B contains 4 red and 2 blue balls.'
result = re.sub(r'\d+', '', input_str)
print(result) 

#----------


#Remove punctuation : The following code removes this set of symbols [!”#$%&’()*+,-./:;<=>?@[\]^_`{|}~]:
import string
input_str = 'This &is [an] example? {of} string. with.? punctuation!!!!' # Sample string
input_str
result = input_str.translate(string.maketrans("",""), string.punctuation)
print(result) 

#not working

#%%%
#Remove whitespaces
#To remove leading and ending spaces, you can use the strip() function:
#Example -White spaces removal
input_str = ' \t a string example \t '  #with spaces
input_str
input_str = input_str.strip()
input_str                                           

#%%%
#Tokenisation - Tokenization is the process of splitting the given text into smaller pieces called tokens. Words, numbers, punctuation marks, and others can be considered as tokens. In this table (“Tokenization” sheet) several tools for implementing tokenization are described.
#https://medium.com/@datamonsters/text-preprocessing-in-python-steps-tools-and-examples-bf025f872908


#Remove Stopwords: 
#Stop words are the most common words in a language like “the”, “a”, “on”, “is”, “all”. These words do not carry important meaning and are usually removed from texts. It is possible to remove stop words using Natural Language Toolkit (NLTK), a suite of libraries and programs for symbolic and statistical natural language processing.

input_str = "NLTK is a leading platform for building Python programs to work with human language data."
stop_words = set(stopwords.words('english'))
from nltk.tokenize import word_tokenize
tokens = word_tokenize(input_str)
result = [i for i in tokens if not i in stop_words]
print (result)

#A scikit-learn tool also provides a stop words list:
from sklearn.feature_extraction.stop_words import ENGLISH_STOP_WORDS
#It’s also possible to use spaCy, a free open-source library:
from spacy.lang.en.stop_words import STOP_WORDS

#
#Remove sparse terms and particular words
#In some cases, it’s necessary to remove sparse terms or particular words from texts. This task can be done using stop words removal techniques considering that any group of words can be chosen as the stop words.
#Stemming
#Stemming is a process of reducing words to their word stem, base or root form (for example, books — book, looked — look). The main two algorithms are Porter stemming algorithm (removes common morphological and inflexional endings from words [14]) and Lancaster stemming algorithm (a more aggressive stemming algorithm). In the “Stemming” sheet of the table some stemmers are described.

#Stemming using NLTK:
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
stemmer= PorterStemmer()
input_str='There are several types of stemming algorithms.'
input_str=word_tokenize(input_str)
for word in input_str:    print(stemmer.stem(word))


#Lemmatization
#The aim of lemmatization, like stemming, is to reduce inflectional forms to a common base form. As opposed to stemming, lemmatization does not simply chop off inflections. Instead it uses lexical knowledge bases to get the correct base forms of words.
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
lemmatizer=WordNetLemmatizer()
input_str='been had done languages cities mice'
input_str=word_tokenize(input_str)
for word in input_str:    print(lemmatizer.lemmatize(word))


#Part of speech tagging (POS)
#Part-of-speech tagging aims to assign parts of speech to each word of a given text (such as nouns, verbs, adjectives, and others) based on its definition and its context. There are many tools containing POS taggers including NLTK, spaCy, TextBlob, Pattern, Stanford CoreNLP, Memory-Based Shallow Parser (MBSP), Apache OpenNLP, Apache Lucene, General Architecture for Text Engineering (GATE), FreeLing, Illinois Part of Speech Tagger, and DKPro Core.

#Part-of-speech tagging using TextBlob:
input_str='Parts of speech examples: an article, to write, interesting, easily, and, of'
from textblob import TextBlob
result = TextBlob(input_str)
print(result.tags)

#Chunking (shallow parsing)
#Chunking is a natural language process that identifies constituent parts of sentences (nouns, verbs, adjectives, etc.) and links them to higher order units that have discrete grammatical meanings (noun groups or phrases, verb groups, etc.) [23]. Chunking tools: NLTK, TreeTagger chunker, Apache OpenNLP, General Architecture for Text Engineering (GATE), FreeLing.
#Chunking using NLTK:
#The first step is to determine the part of speech for each word:
input_str='A black television and a white stove were bought for the new apartment of John.'
from textblob import TextBlob
result = TextBlob(input_str)
print(result.tags)

#second step is chunking:
reg_exp = "NP: {<DT>?<JJ>*<NN>}"
rp = nltk.RegexpParser(reg_exp)
result = rp.parse(result.tags)
print(result)
#draw the sentence tree structure using code result.draw()
