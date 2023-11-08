# pip install Wordcloud
# pip install Sastrawi

import pandas as pd
import Sastrawi
from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory, StopWordRemover, ArrayDictionary
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory

data = pd.read_csv('https://drive.google.com/file/d/1tHvfAQbwNilG2CDRWO82y8u2KxeF_I5-/view?usp=drive_link')
print(data.head()) # Menampilkan 5 data teratas
exit()

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
norm = {"dgn": "dengan", "problem": "masalah"} # Kosakata yang tidak ada diKBBI
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