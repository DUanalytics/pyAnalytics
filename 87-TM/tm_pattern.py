#python : Topic :Text Parsing
#https://analyticsindiamag.com/hands-on-guide-to-pattern-a-python-tool-for-effective-text-processing-and-data-mining/
#https://stackabuse.com/python-for-nlp-introduction-to-the-pattern-library/
#standard libaries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pydataset import data
import seaborn as sns

#pip install pattern
from pattern.en import parse
from pattern.en import pprint
parse('Hello Everyone and Welcome to Analytics India Magazine')
#parse function differentiate the words in the sentence as a noun, verb, subject, or subject. We can also use the ‘pprint’ function defined in the pattern library to display the parsed sentence in a clear manner. 
pprint(parse('Hello Everyone and Welcome to Analytics India Magazine', relations  = True,tokenize= True, lemmata= True))

#%% ngrams
# "n" combination of words in a sentence.
from pattern.en import ngrams
print(ngrams("Hello Everyone and Welcome to Analytics India Magazine", n=3))
print(ngrams("He goes to hospital", n=2))

#sentiment 
#Sentiment refers to an opinion or feeling towards a certain thing. sentiment object is used to find the polarity (positivity or negativity) of a text along with its subjectivity.

from pattern.en import sentiment
print(sentiment("He is a good boy but sometimes he behaves miserably"))

print(sentiment("he is has done extremely well"))
print(sentiment("This is an excellent movie to watch. I really love it"))
#The sentence "This is an excellent movie to watch. I really love it" has a sentiment of 0.75, which shows that it is highly positive. Similarly, the subjectivity of 0.8 refers to the fact that the sentence is a personal opinion of the user.

#%%%Modality
#Checking if a Statement is a Fact; The modality function returns a value between -1 to 1. For facts, the modality function returns a value greater than 0.5

from pattern.en import parse, Sentence
from pattern.en import modality

text = "Paris is the capital of France"
sent = parse(text, lemmata=True)
sent = Sentence(sent)
print(modality(sent))
#Since the text string "Paris is the capital of France" is a fact, in the output, you will see a value of 1.

text = "I think we can complete this task"
sent = parse(text, lemmata=True)
sent = Sentence(sent)
print(modality(sent))
#0.25 : Since the string in the above example is not very certain, the modality of the above string will be 0.25.

text = parse('He is a good boy but sometimes he behaves miserably')
text
text= Sentence(text)
print(modality(text))

#%%% Pluralism
from pattern.en import pluralize, singularize
print(pluralize('leaf'))
print(singularize('theives'))

#%%%Converting Adjective to Comparative and Superlative Degrees
from pattern.en import comparative, superlative
print(comparative('good'))
print(superlative('good'))

#%%% Suggest
#Suggest function is used for spelling corrections but it is more than that. It not only checks the spelling it also gives you suggestions of what might be the correct word with their probabilities. This function also distinguishes pattern from other libraries. 
#Spelling Corrections  : The suggest method can be used to find if a word is spelled correctly or not. The suggest method returns 1 if a word is 100% correctly spelled. Otherwise the suggest method returns the possible corrections for the word along with their probability of correctness.

from pattern.en import suggest
print(suggest("Heroi"))

print(suggest("Whitle"))
#In the script above we have a word Whitle which is incorrectly spelled. In the output, you will see possible suggestions for this word.
#According to the suggest method, there is a 0.64 probability that the word is "While", similarly there is a probability of 0.29 that the word is "White", and so on.

print(suggest("Fracture"))
#From the output, you can see that there is a 100% chance that the word is spelled correctly.
#%%% Quantify
#Quantify function is used to provide a word count estimation of the words given.
#quantify function is used to get a word count estimation of the items in the list, which provides a phrase for referring to the group. If a list has 3-8 similar items, the quantify function will quantify it to "several". Two items are quantified to a "couple".

from pattern.en import quantify
print(quantify(['apple', 'apple', 'apple', 'banana', 'banana', 'banana', 'mango', 'mango']))
#In the list, we have three apples, three bananas, and two mangoes. The output of the quantify function for this list looks like this:
  
#demonstrates the other word count estimations.
from pattern.en import quantify
print(quantify({'strawberry': 200, 'peach': 15}))
print(quantify('orange', amount=1200))


from pattern.en import quantify

a = quantify(['Pencil', 'Pencil', 'Eraser', 'Sharpener', 'Sharpener', 'Sharpener', 'Scale', 'Compass'])
a
print(a)

#%%% Working with Numbers
#The Pattern library contains functions that can be used to convert numbers in the form of text strings into their numeric counterparts and vice versa. To convert from text to numeric representation the number function is used. Similarly to convert back from numbers to their corresponding text representation the numerals function is used. Look at the following script:

from pattern.en import number, numerals
print(number("one hundred and twenty two"))
print(numerals(256.390, round=2))

#%%%Data Mining
from pattern.web import Google
google = Google()
for results in google.search('Analytics India Magazine'):
    print(results.url)
    print(results.text)

for results in google.search('Gamification'):
    print(results.url)

#twitter
from pattern.web import Twitter

twitter = Twitter()

for results in twitter.search('Analytics India Magazine'):
    print(results.url)
    print(results.text)

for results in twitter.search('Gamification'):
    print(results.url)

#flickr
from pattern.web import Flickr
flickr = Flickr(license=None)
for result in flickr.search('Analytics India Magazine'):
    print(result.url)
    print(result.text)

#%%%Accessing Web Pages
#The URL object is used to retrieve contents from the webpages. It has several methods that can be used to open a webpage, download the contents from a webpage and read a webpage.
#You can directly use the download method to download the HTML contents of any webpage. The following script downloads the HTML source code for the Wikipedia article on artificial intelligence.

from pattern.web import download
page_html = download('https://en.wikipedia.org/wiki/Artificial_intelligence', unicode=True)

#You can also download files from webpages, for example, images using the URL method:

from pattern.web import URL, extension
page_url = URL('https://upload.wikimedia.org/wikipedia/commons/f/f1/RougeOr_football.jpg')
file = open('football' + extension(page_url.page), 'wb')
file.write(page_url.download())
file.close()

#%%%Finding URLs within Text
#You can use the findurl method to extract URLs from text strings. Here is an example:
from pattern.web import find_urls
print(find_urls('To search anything, go to www.google.com', unique=True))

#%%Parsing PDF Documments
#The Pattern library contains PDF object that can be used to parse a PDF document. PDF (Portable Document Format) is a cross platform file which contains images, texts, and fonts in a stand-alone document.

from pattern.web import URL, PDF
pdf_doc = URL('http://demo.clab.cs.cmu.edu/NLP/syllabus_f18.pdf').download()
pdf_doc
print(PDF(pdf_doc.decode('utf-8')))


#%% Clearning Cache
from pattern.web import cache
cache.clear()
