import config
import pandas as pd
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory# create stemmer

import string
from urllib.request import urlopen
import warnings

import stanfordnlp
import nltk
from nltk.corpus import stopwords
from nltk.util import ngrams
from collections import Counter

warnings.filterwarnings('ignore')

nlp = stanfordnlp.Pipeline(lang='id', processors='tokenize,pos')

factory = StemmerFactory()
stemmer = factory.create_stemmer()# stemming process

grammar = "NP: {<NOUN|PROPN>+ <ADJ>*}"
parser = nltk.RegexpParser(grammar)

collection = config.db['news']
for post in collection.find({'content': {'$ne': ''}}).limit(50):
    if post['keyword'] in post['content'].lower(): 
        wordlist = []
        doc = nlp(post['content'].lower())   
        for sentence in doc.sentences:
            for word in sentence.words:
                if word.upos in ['NOUN', 'VERB']:
                    wordlist += [word.text]

        print(word.text, word.upos)
        df = pd.DataFrame(wordlist)
        print(df[0].value_counts().to_frame())
'''word_pos_pairs = [(word.text, word.upos) for word in doc.sentences[0].words]
tree = parser.parse(word_pos_pairs)
print(tree)'''
'''        print(post['title'], post['keyword'])
        output   = stemmer.stem(post['content'])
        token = output.split()
        df = pd.DataFrame(token)
        print(df[0].value_counts().to_frame())
'''
'''doc = collection.find_one({'title':'direktur bank mandiri blak-blakan alasan borong saham rp 2 m'})
output   = stemmer.stem(doc['content'])
token = output.split()
df = pd.DataFrame(token)
print(df[0].value_counts().to_frame())'''
#print(df)

