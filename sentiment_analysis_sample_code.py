#Importing the essential libraries
#Beautiful Soup is a Python library for pulling data out of HTML and XML files
#The Natural Language Toolkit
import requests
import nltk
from bs4 import BeautifulSoup
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
# %matplotlib inline
import random
from wordcloud import WordCloud
import os
import spacy
nlp = spacy.load('en_core_web_sm')
from textblob import TextBlob
from pattern.en import sentiment

#we are using request package to make a GET request for the website, which means we're getting data from it.
r=requests.get('https://www.newsy.com/stories/commercial-companies-advance-space-exploration/')

#Setting the correct text encoding of the HTML page
r.encoding = 'utf-8'

#Extracting the HTML from the request object
html = r.text

# Printing the first 500 characters in html
print(html[:500])

# Creating a BeautifulSoup object from the HTML
soup = BeautifulSoup(html, "lxml")
# Getting the text out of the soup
text = soup.get_text()

#total length
len(text)

#having a look at the text
print(text[100:1100])

# clean_text= text.replace("n", " ")
clean_text= text.replace("/", " ")       
clean_text= ''.join([c for c in clean_text if c != "'"])

clean_text

sentence=[]
tokens = nlp(clean_text)
for sent in tokens.sents:
    sentence.append((sent.text.strip()))

sentence
print(sentence[2])

textblob_sentiment=[]
for s in sentence:
    txt= TextBlob(s)
    a= txt.sentiment.polarity
    b= txt.sentiment.subjectivity
    textblob_sentiment.append([s,a,b])

df_textblob = pd.DataFrame(textblob_sentiment, columns =['Sentence', 'Polarity', 'Subjectivity'])
df_textblob.head()
df_textblob.info()

sns.displot(df_textblob["Polarity"], height= 5, aspect=1.8)
plt.xlabel("Sentence Polarity (Textblob)")

sns.displot(df_textblob["Subjectivity"], height= 5, aspect=1.8)
plt.xlabel("Sentence Subjectivity (Textblob)")

pattern_sentiment=[]
for s in sentence:
    res= sentiment(s)
    c= res[0]
    d= res[1]
    pattern_sentiment.append([s,c,d])

pattern_sentiment[1]

df_pattern = pd.DataFrame(textblob_sentiment, columns =['Sentence', 'Polarity', 'Subjectivity'])
df_pattern.head()
df_pattern.info()

sns.displot(df_pattern["Polarity"], height= 5, aspect=1.8)
plt.xlabel("Sentence Polarity (Pattern)")

sns.displot(df_pattern["Subjectivity"], height= 5, aspect=1.8)
plt.xlabel("Sentence Subjectivity (Pattern)")

#Creating the tokenizer
tokenizer = nltk.tokenize.RegexpTokenizer('w+')

#Tokenizing the text
tokens = tokenizer.tokenize(clean_text)

len(tokens)

print(tokens[0:10])

words = []
# Looping through the tokens and make them lower case
for word in tokens:
    words.append(word.lower())

#Now we have to remove stopwords
#Stop words are a set of commonly used words in any language. 
#For example, in English, “the”, “is” and “and”, would easily qualify as stop words. 
#In NLP and text mining applications, stop words are used to eliminate unimportant words, 
#allowing applications to focus on the important words instead.
#English stop words from nltk
stopwords = nltk.corpus.stopwords.words('english')
#Appending to words_new all words that are in words but not in sw
for word in words:
    if word not in stopwords:
        words_new.append(word)

len(words_new)

print(words_new[0:10])

#The frequency distribution of the words
freq_dist = nltk.FreqDist(words_new)

#Frequency Distribution Plot
plt.subplots(figsize=(16,10))
freq_dist.plot(20)

#converting into string
res=' '.join([i for i in words_new if not i.isdigit()])

plt.subplots(figsize=(16,10))
wordcloud = WordCloud(
                          background_color='black',
                          max_words=100,
                          width=1400,
                          height=1200
                         ).generate(res)
plt.imshow(wordcloud)
plt.title('NEWS ARTICLE (100 words)')
plt.axis('off')
plt.show()