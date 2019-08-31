#
#-----------------------------
#%https://data-science-blog.com/en/blog/2018/11/04/sentiment-analysis-using-python/
#There are a few NLP libraries existing in Python such as Spacy, NLTK, gensim, TextBlob, etc. For this particular article, we will be using NLTK for pre-processing and TextBlob to calculate sentiment polarity and subjectivity.
#install libraries if not done
import pandas as pd
import matplotlib.pyplot as plt
#%matplotlib inline  
import nltk
from nltk import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from nltk.stem import LancasterStemmer, WordNetLemmatizer, PorterStemmer
from wordcloud import WordCloud, STOPWORDS
from textblob import TextBlob

dataurl = 'https://www.kaggle.com/datafiniti/consumer-reviews-of-amazon-products#1429_1.csv'
#download and load - this is large data.. better to download and read
amz_reviews = pd.read_csv('../../pydata/1429_1.csv')
amz_reviews.shape
amz_reviews.columns

#select few columns
columns = ['id','name','keys','manufacturer','reviews.dateAdded', 'reviews.date','reviews.didPurchase', 'reviews.userCity', 'reviews.userProvince', 'reviews.dateSeen', 'reviews.doRecommend', 'asins','reviews.id', 'reviews.numHelpful', 'reviews.sourceURLs', 'reviews.title']
df = pd.DataFrame(amz_reviews.drop(columns,axis=1,inplace=False))
df.columns
df.head(3)
df['reviews.rating'].value_counts().plot(kind='bar')

#Data pre-processing for textual variables
#Lowercasing
## Change the reviews type to string
df['reviews.text'] = df['reviews.text'].astype(str)

## Before lowercasing 
df['reviews.text'][2]
df.columns
## Lowercase all reviews
df['reviews.text'] = df['reviews.text'].apply(lambda x: " ".join( x.lower() for x in x.split()))

df['reviews.text'][2] ## to see the difference
#'inexpensive tablet for him to use and learn on, step up from the nabi. he was thrilled with it, learn how to skype on it already...'

#Special Characters
## remove punctuation- not ^\w\s
df['reviews.text'] = df['reviews.text'].str.replace('[^\w\s]','')
df['reviews.text'][2]
df.head(5)
df.columns
df['reviews.text'].head(3)
#Stopwords
stop = stopwords.words('english')
df['reviews.text'] = df['reviews.text'].apply(lambda x: " ".join(x for x in x.split() if x not in stop))
df['reviews.text'][2]

#Stemming
st = PorterStemmer()
#from nltk.stem
df['reviews.text'] = df['reviews.text'].apply(lambda x: " ".join([st.stem(word) for word in x.split()]))
df['reviews.text'][2]

#%%%
#Sentiment Score

# Define a function which can be applied to calculate the score for the whole dataset

def senti(x):    return TextBlob(x).sentiment  
df['senti_score'] = df['reviews.text'].apply(senti)
df.senti_score.head()

#there are two scores: the first score is sentiment polarity which tells if the sentiment is positive or negative and the second score is subjectivity score to tell how subjective is the text.
