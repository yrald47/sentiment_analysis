# pip install Wordcloud
# pip install Sastrawi
from pylab import *
import pandas as pd
import Sastrawi
from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory, StopWordRemover, ArrayDictionary
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
import matplotlib.pyplot as plt
import seaborn as sns

import re
import nltk
from nltk.corpus import stopwords
from wordcloud import WordCloud, STOPWORDS

data = pd.read_csv('https://drive.google.com/file/d/1tHvfAQbwNilG2CDRWO82y8u2KxeF_I5-/view?usp=drive_link')
print(data.head()) # Menampilkan 5 data teratas
# exit()

## DATA UNDERSTANDING
data.dtypes # Melihat tipe data masing2 column data frame
data.shape # Outuput: (total row, total column)
data.isnull().sum() # Menghitung jumlah data null di masing2 column
data = data.dropna() # Membersihkan data yang kosong
data.duplicated().sum() # Meampilkan jumlah data yang duplikat
data.describe() # Masing2 column data akana ditampikan atribut-atribut untuk menghitung jumlah row (count), unique value, value terbanyak, dan jumlah value terbanyak terebut

## PREPROCESSING DATA
data = data.drop(columns='id_komentar')
data.head()
data['text_cleaning'] = data['text_cleaning'].str.lower()

## Normalisasi
norm = {"dgn": "dengan", "problem": "masalah"} # Kosakata yang tidak ada di KBBI
# Mengubah kata yang tak terdaftar menjadi terdaftar
def normalisasi(str_text):
    for i in norm:
        str_text = str_text.replace(i, norm(i))
        return str_text
    
data['text_cleaning'] = data['text_cleaning'].apply(lambda x: normalisasi(x))

## Stopwords: Menghilangkan kata yang tidak terlalu penting seperti konjungsi
more_stop_word = []
stop_words = StopWordRemoverFactory().get_stop_words()
new_array = ArrayDictionary(stop_words)
stop_words_remover_new = StopWordRemover(new_array)

def stopWords(str_text):
    str_text = stop_words_remover_new.remove(str_text)
    return str_text

data['data_cleaning'] = data['data_cleaning'].apply(lambda x: stopWords(x))
data.head()

## Tokenisasi: Memisahkan kata-kata dalam kalimat/berita
tokenize = data['data_cleaning'].apply(lambda x:x.split())

## Stemming: Mengubah kata berimbuhan menjadi kata dasar
def stemming(text_cleaning):
    factory = StemmerFactory()
    stemmer = factory.create_stemmer()
    do = []
    for w in text_cleaning:
        dt = stemmer.stem(w)
        do.append(dt)
    d_clean = []
    d_clean = ''.join(do)
    print(d_clean)
    return d_clean

tokenize = tokenize.apply(stemming)
tokenize.to_csv('https://drive.google.com/file/d/107_tjPimBF7Qw3CE7KTzPgIZHmiyrcXk/view?usp=drive_link', index=False)
data_clean = pd.read_csv('https://drive.google.com/file/d/107_tjPimBF7Qw3CE7KTzPgIZHmiyrcXk/view?usp=drive_link', encoding='latin1')

at1 = pd.read_csv('https://drive.google.com/file/d/107_tjPimBF7Qw3CE7KTzPgIZHmiyrcXk/view?usp=drive_link')
at2 = pd.read_csv('https://drive.google.com/file/d/1tHvfAQbwNilG2CDRWO82y8u2KxeF_I5-/view?usp=drive_link')
att2 = at2['sentimen']

data_clean = pd.concat((at1, att2), axis = 1)
data_clean.head()

data_clean = data_clean.dropna() # Menhilangkan data yang NaN
data_clean = data_clean[data_clean['sentimen'] != 'netral'] # Menghilangkan data sentimen netral

data_clean = data_clean.replace({"positif": 1, "negatif": 0}) # Mengganti positif dengan 1 dan negatif dengan 0

## Visualisasi Kata
data_positif = data_clean[data_clean['sentimen'] == 1]
data_negatif = data_clean[data_clean['sentimen'] == 0]

alt_text_s0 = ' '.join(word for word in data_negatif['text_cleaning'])
wordcloud = WordCloud(colormap='Reds', width=1000, height=1000, mode='RGBA', background_color='White').generate(alt_text_s0)
plt.figure(figsize=(9, 6))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.title('Visualisasi kata Negatif')
plt.margins(x=0, y=0)
plt.show()

data_clean['sentimen'].value_counts() # Menghitung jumlah setiap value
plt.figure(figsize=(5, 3))
sns.countplot(data=data_clean, x='sentimen', palette={0: 'red', 1: 'lightskyblue'})
plt.title('Visualisasi Sentimen Positif dan Negatif')
plt.xlabel('Sentimen')
plt.ylabel('Jumlah')
plt.show()


# df['Score'].value_counts().sort_index().plot(kind='bar', title='Count of Reviews by Star', figsize=(15, 5))


