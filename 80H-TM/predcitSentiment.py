# Predict Sentiments
#-----------------------------
#Sentiment Analysis

from tkinter import * 
import nltk.classify.util
from nltk.classify import NaiveBayesClassifier
from nltk.corpus import names

#create windows object
window=Tk()
window.geometry("1024x800") #set the window size using .geometry command
window.title("Sentiment Analysis") #this is the title of the GUI

def saui(words): return dict([(word, True) for word in words])


positive_vocab = ['awesome', 'outstanding', 'fantastic', 'terrific', 'good', 'nice', 'great', ':)']
negative_vocab = ['bad', 'terrible', 'useless', 'hate', ':(']
neutral_vocab = ['movie', 'the', 'sound', 'was', 'is', 'actors', 'did', 'know', 'words', 'not']

pos_feat = [(saui(pos), 'pos') for pos in positive_vocab]
neg_feat = [(saui(neg), 'neg') for neg in negative_vocab]
neu_feat = [(saui(neu), 'neu') for neu in neutral_vocab]

train_set = neg_feat + pos_feat + neu_feat

classifier = NaiveBayesClassifier.train(train_set)

#set the heading of the GUI
heading=Label(window,text="This is how it works",font= ("arial",12,"bold"),fg="#26482B").pack() 

#set the label, like 'enter text'
label1 = Label(window,text="Enter Some Text", font= ("arial",10,"bold"),fg="black")
label1.place(x=10,y=50)

#take some text as input in the textbox and put that input in a variable 
ip = Text(window,width=60,height=30,bg="white")
ip.place(x=10,y=90)
sentence=ip.get('1.0',END)
sentence = sentence.lower()
words = sentence.split(' ')


#set another label that indicates the results
label2 = Label(window,text="Results", font=("arial",10,"bold"),fg="black")
label2.place(x=680,y=50)
#insert another textbox where you want to show the results
button1 = Button( window,text="Analyze",width=10,height=1,bg="#9B9D9C",fg="black",font= ("arial",8,"bold"),command=saui(words))
button1.place(x=200,y=586)

op = Text(window,width=20,height=15,bg="white")
op.place(x=680,y=90)

#Predict
neg = 0
pos = 0

for word in words: classResult = classifier.classify(saui(word))

if classResult == 'neg': neg = neg + 1
if classResult == 'pos': pos = pos + 1


output1 = 'Positive: ' + str(float(pos) / len(words))
output2 = 'Negative: ' + str(float(neg) / len(words))

op.insert(0.0, output1)
op.insert(1.0,output2)


window.mainloop() 
