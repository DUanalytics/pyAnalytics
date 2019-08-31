#
#-----------------------------
#%
#https://programminghistorian.org/en/lessons/sentiment-analysis

import nltk
nltk.download('vader_lexicon')
nltk.download('punkt')
# first, we import the relevant modules from the NLTK library
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# next, we initialize VADER so we can use it within our Python script
sid = SentimentIntensityAnalyzer()

# the variable 'message_text' now contains the text we will analyze.
message_text = '''Like you, I am getting very frustrated with this process. I am genuinely trying to be as reasonable as possible. I am not trying to "hold up" the deal at the last minute. I'm afraid that I am being asked to take a fairly large leap of faith after this company (I don't mean the two of you -- I mean Enron) has screwed me and the people who work for me.'''
message_text
# Calling the polarity_scores method on sid and passing in the message_text outputs a dictionary with negative, neutral, positive, and compound scores for the input text
scores = sid.polarity_scores(message_text)
                                                                                                                                                                                                                                                                                      print(message_text)
                                                                                                                                                                                                                                                                                      
                                                                                                                                                                                                                                                                                      # Here we loop through the keys contained in scores (pos, neu, neg, and compound scores) and print the key-value pairs on the screen
for key in sorted(scores):
        print('{0}: {1}, '.format(key, scores[key]), end='')