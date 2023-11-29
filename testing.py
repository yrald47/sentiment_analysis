## tes xpath from lxml
import urllib.request as urllib2
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup

from lxml import html
import requests
# import datetime
from datetime import datetime

import locale

import re
import json
import sys

def testSysArgv():
    print(len(sys.argv))
    print(sys.argv[2])
    if len(sys.argv) != 3 or sys.argv[1] != '-t':
        print("Format perintah salah. Gunakan: python bin.py -t 'ini adalah topik'")
        exit()


    # Mengambil teks topik tanpa tanda petik
    topik = sys.argv[2].replace(' ', '%20')
    print("Topik yang diambil:", topik)

def ScrapingRequest():
    url = 'https://finance.detik.com/moneter/d-6991494/hingga-september-laba-bersih-bca-tembus-rp-36-4-t-tumbuh-25-8'
    try:
        response = requests.get(url, timeout=20)

        # Memeriksa apakah permintaan berhasil
        if response.status_code == 200:
            # Menyaring elemen dengan BeautifulSoup atau cara lainnya
            # (contoh menggunakan BeautifulSoup)
            from bs4 import BeautifulSoup
            
            soup = BeautifulSoup(response.text, 'html.parser')
            target_element = soup.find('div', 'detail__body-text itp_bodycontent').find_all('p', class_=False)
            
            # Melakukan sesuatu dengan target_element
            # print(target_element.get_text if target_element else "Elemen tidak ditemukan")
            print(target_element)
        else:
            print(f"Permintaan gagal dengan status code {response.status_code}")
    except requests.exceptions.RequestException as e:
            print(f"Error: {e}")

# Contoh string JSON yang berisi pola regex
# json_string = '{"regex_pattern": "\\d{1,2}/\\d{1,2}/\\d{4}"}'

# # Mendapatkan pola regex dari JSON
# json_data = json.loads(json_string)
# regex_pattern = json_data["regex_pattern"]
def findDateRegexinSentence():
    kalimat = "Ini adalah tanggal 08/12/2023 dan juga 8/12/2023, serta 8 Februari 2023."
    regex_pattern = "\\d{1,2}/\\d{1,2}/\\d{4}"

    # Menggunakan string regex langsung dalam re.compile()
    regex = re.compile(regex_pattern)

    # Sekarang, Anda dapat menggunakan objek regex untuk mencocokkan teks
    tanggal = regex.findall(kalimat)

    # Menampilkan tanggal yang ditemukan
    for tgl in tanggal:
        print(tgl)

# for lang in locale.windows_locale.values():
#     print(lang)

def convertDate():
    loc = locale.getlocale()
    print(loc)
    locale.setlocale(locale.LC_ALL , 'id_ID')
    loc = locale.getlocale()
    print(loc)

    string_tanggal3 = "20 Okt 2023 09:00"
    tanggal_objek3 = datetime.strptime(string_tanggal3, "%d %b %Y %H:%M")
    tanggal_hasil3 = tanggal_objek3.strftime("%Y-%m-%d")

    print(tanggal_hasil3)

# text = "https://cnnindonesia.co.id/longtext/12424/lkjasdf-lasdkjfsa-lksdkf/"
# print(text.find("/"))

# xs = ["div", "article", "div", "div"]
# for idx, x in enumerate(xs):
#     print(idx, x)

# exit()

## TESTING XPATH AND FIND TAG DETIK FOTO SLIDER

# url = "https://finance.detik.com/foto-bisnis/d-6976432/indonesia-knowledge-forum-2023-bahas-perekonomian-indonesia/1"
# url = "https://video.tempo.co/read/6460/aksi-ganjal-atm-gunakan-tusuk-gigi-terekam-kamera-cctv"
# url = "https://video.tempo.co/read/6460/aksi-ganjal-atm-gunakan-tusuk-gigi-terekam-kamera-cctv"
# url = "https://finance.detik.com/foto-bisnis/d-6976432/indonesia-knowledge-forum-2023-bahas-perekonomian-indonesia"
# url = "https://www.detik.com/search/searchall?query=bca&siteid=2"
# url = "https://umkm.kompas.com/read/2023/10/26/113538883/ace-ys-2023-libatkan-generasi-muda-bangun-industri-kreatif-dan-digital-di-asia"


# req = Request(url=url, headers={'User-Agent': 'Mozilla/5.0'})
# news_search = urllib2.urlopen(req).read()
# parsed2 = BeautifulSoup(news_search, "lxml")
# b = parsed2.find("article", "detail-artikel").find_all("div", "detail-in")
# print(len(b))
# for i in b:
#     print(i.get_text())

def xpath():
    url = "https://foto.tempo.co/read/21815/diduga-bunuh-diri-seorang-pria-jatuh-dari-lantai-56"
    print("***==========***")
    page = requests.get(url)
    tree = html.fromstring(page.content)
    # content = tree.xpath(
    #     '//div[@id="slider-foto__detail"]/figure/figcaption[@class="mgt-16"]/text()')
    # content = tree.xpath(
    #     '//article[@class="detail-artikel"]/div[@class="detail-in"]/text()')
    # content = tree.xpath('/html/body/div[2]/div/div[2]/article[1]/a/span[2]/span/text()')
    # content = tree.xpath("/html/body/div[1]/div[2]/div[2]/div[4]/div[1]/div[1]/div[1]/div/text()")
    content = tree.xpath("//article[@class='text-card padding-no']/figcaption[@class='caption']/text()")
    print(content)
    # print(len(content))
    for i in content:
        # print(i.split(',')[1].split('WIB')[0].strip())
        print(i)
        # scraping_date = datetime.datetime.strptime("08 Nov 2023", "%Y-%m-%d")
def dateFormat():
    from datetime import datetime

    # String awal
    string_tanggal = "08 Nov 2023 07:00"
    string_tanggal2 = "8 November 2023 15:41"


    # Membuat objek datetime dari string
    tanggal_objek = datetime.strptime(string_tanggal, "%d %b %Y %H:%M")
    tanggal_objek2 = datetime.strptime(string_tanggal2, "%d %B %Y %H:%M")

    # Mengubah objek datetime ke format tanggal yang diinginkan
    tanggal_hasil = tanggal_objek.strftime("%Y-%m-%d")
    tanggal_hasil2 = tanggal_objek2.strftime("%Y-%m-%d")

    print(tanggal_hasil)
    print(tanggal_hasil2)

# WRITE LXML SITE
# url = "https://finance.detik.com/foto-bisnis/d-6976432/indonesia-knowledge-forum-2023-bahas-perekonomian-indonesia"

# req = Request(url=url, headers={'User-Agent': 'Mozilla/5.0'})
# news_search = urllib2.urlopen(req).read()
# parsed2 = BeautifulSoup(news_search, "lxml")
# with open('video_tempo.lxml', 'w', encoding="utf-8") as f:
#     f.write(str(parsed2))

# b = parsed2.find("div", {"id": "slider-foto__detail"}).find_all("figcaption", "mgt-16")
# for i in b:
#     print(i.get_text())

def dateKompasVideo():
    req = Request(url='https://video.kompas.com/watch/872082/kasus-uang-di-rekening-raib-pin-atm-dibobol-pasangan-sendiri', headers={'User-Agent': 'Mozilla/5.0'})
    news_search = urllib2.urlopen(req).read()
    parsed2 = BeautifulSoup(news_search, "lxml")
    b = parsed2.find("div", "videoKG-date").get_text()
    print(b)
    # for i in b:
    #     print(i.get_text())

def regexMatch():
    # Regex pattern
    regex_pattern = r'\d{1,2}[ /](?:[a-zA-Z]+|\d{1,2})[ /]\d{4}, \d{2}:\d{2}'

    # Test strings
    date_string1 = "16/11/2023, 13:46"
    date_string2 = "16 November 2023, 13:46"

    # Test regex pattern
    match1 = re.fullmatch(regex_pattern, date_string1)
    match2 = re.fullmatch(regex_pattern, date_string2)

    # Print results
    print(f"Match for '{date_string1}': {'Yes' if match1 else 'No'}")
    print(f"Match for '{date_string2}': {'Yes' if match2 else 'No'}")

    str_date = "sekarang adalah 16/11/2023, 14:54 dan 5 hari lalu adalah 11 September 2023, 22:43 WIB"
    regex = re.compile('\\d{1,2}[ /](?:[a-zA-Z]+|\\d{1,2})[ /]\\d{4}, \\d{2}:\\d{2}')
    str_date = regex.findall(str_date)

    print(str_date)

def dateTimeReplace():
    from datetime import datetime, date, timedelta
    import pytz

    # Tentukan zona waktu yang diinginkan
    zona_waktu = pytz.timezone('Asia/Jakarta')

    # Dapatkan waktu saat ini dalam zona waktu yang ditentukan
    tanggal_hari_ini_tz = datetime.now(zona_waktu).date().strftime('%d/%m/%Y')
    print("Tanggal hari ini (pytz):", tanggal_hari_ini_tz, str(type(tanggal_hari_ini_tz)))

    tanggal_hari_ini_now = datetime.now().strftime('%d/%m/%Y')
    print("Tanggal hari ini (now):", tanggal_hari_ini_now, str(type(tanggal_hari_ini_now)))

    tanggal_hari_ini_today = date.today().strftime('%d/%m/%Y')
    print("Tanggal hari ini (today):", tanggal_hari_ini_today, str(type(tanggal_hari_ini_today)))

    timezone = pytz.timezone('Asia/Jakarta')
    today = datetime.now(timezone).date()
    a_week_before = today - timedelta(weeks=1)
    today_str = today.strftime('%d/%m/%Y')
    a_week_before_str = a_week_before.strftime('%d/%m/%Y')
    # link = portals['link'] + keyword
    search_link = 'https://www.detik.com/search/searchall?query=keyword_to_replace&sortby=time&sorttime=0&fromdatex=fdate_replace&todatex=tdate_replace&siteid=2'
    link = search_link.replace('keyword_to_replace', 'bank+bca').replace('cdate_replace', today_str).replace('fdate_replace', a_week_before_str).replace('tdate_replace', today_str)
    print("Search news from Link: " + link)

def urllibTimeout():
    from urllib.request import Request, urlopen
    from urllib.error import URLError
    from bs4 import BeautifulSoup

    url = 'https://www.detik.com/bali/bisnis/d-7037205/ini-daftar-10-orang-terkaya-di-indonesia-siapa-paling-tajir'  # Ganti dengan URL yang sesuai
    headers = {'User-Agent': 'Mozilla/5.0'}

    try:
        req = Request(url=url, headers=headers)
        news_html = urlopen(req).read()
        news_lxml = BeautifulSoup(news_html, "lxml")

        # Lakukan sesuatu dengan news_lxml
        print(news_lxml.title.text)
    except URLError as e:
        print(f"Error: {e}")

def resubDash():
    news = "TEMPO.CO, Jakarta - Pakar keamanan siber dari Vaksincom, Alfons Tanujaya memberikan analisis atas kasus nasabah PT Bank Central Asia Tbk (BCA) yang kehilangan uang senilai Rp 68,5 juta dari rekening tabungannya. Nasabah mengaku itu terjadi saat sedang naik gunung sehingga ponselnya di luar jangkauan internet. Sementara itu, BCA menyebut transaksinya sah karena Quick Response Code Indonesian Standard (QRIS) hanya bisa dilakukan dari perangkat yang terinstal mobile banking.Menurut Alfons, seharusnya bank memiliki bukti perangkat yang melakukan transaksi QRIS seperti fingerprint perangkat, IP perangkat, dan posisi perangkat ketika melakukan transaksi. Selain itu, kata dia, ada cara murah untuk verifikasi transaksi QRIS, tidak perlu melakukan forensik digital.Cara Membuat QRIS untuk Merchant, Ikuti Langkah Berikut“Hubungi saja merchant penerima QRIS dan tanyakan transaksi yang bermasalah itu untuk transaksi apa. Kan jadi ketahuan itu transaksi valid, fraud (penipuan), atau karena kesalahan sistem,” ucap Alfons lewat keterangan tertulis pada Jumat, 17 November 2023.Sehingga, dia melanjutkan, jika merchant atau tokonya valid seharusnya masalah ini selesai. Karena merchant akan memberikan bukti transaksi. Namun, yang menjadi masalah jika merchant-nya menghilang, ini akan menjadi lebih sulit lagi. Artinya kemungkinan besar adalah aksi fraud.Alfons menyarankan agar bank harus meminta bantuan pihak berwenang untuk menyelidiki lebih jauh dan menangkap aktor di balik merchant fraud ini dan memperbaiki sistem penerimaan merchant-nya. “Hal ini mungkin bisa menjadi perhatian Bank Indonesia atas sistem dan prosedur penerimaan merchant QRIS untuk semua bank,” tutur dia.Terkini: Kekayaan Gibran Cawapres Termuda Rp 25 Miliar, Jokowi Akui Belum Ada Investor Asing Masuk IKNSebaliknya, Alfons berujar, nasabah juga harus membuktikan ponselnya ada di mana ketika saat transaksi. Satu-satunya cara adalah melakukan forensik atas ponsel tersebut untuk melihat ada di mana ponselnya ketika transaksi terseb ut dilakukan. Hal ini bisa menghilangkan kemungkinan adanya faktor lain.Dugaan kelemahan di sistem BCA\n"
    # print(news.encode('utf-8'))
    # pattern_to_remove = re.compile(r'.* - ')
    result_text = re.sub(r'.* -\s', '', news)
    print(result_text)

def selectLink():
    import config
    
    link = "https://bisnis.tempo.co/read/1798210/nasabah-bca-hilang-duit-rp-685-juta-karena-transaksi-qris-fraud-atau-salah-sistem"
    # print(link[:75])
    collection = config.db['news']
    result = collection.count_documents({"link": {"$regex": re.compile(link[:75])}})
    # ("link": {"$regex": re.compile(link[:75])})
    print(result)
    # for documents in result:
    #     print(documents)

def sentiment_scoring():
    print("=====TextBlob=====")
    from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
    from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory
    from textblob import TextBlob

    # Contoh teks berita dalam Bahasa Indonesia
    teks_berita_id = "MPT Bank Central Asia Tbk (BBCA) membukukan kinerja positif. Sepanjang semester pertama tahun ini, perusahaan membukukan kenaikan laba bersih 34% secara tahunan (yoy) menjadi Rp 24,2 triliun. Perfoma positif didorong oleh kenaikan volume kredit, perbaikan kualitas pinjaman, serta peningkatan volume transaksi dan pendanaan."

    # Menghilangkan stop words
    stopword_factory = StopWordRemoverFactory()
    stopword_remover = stopword_factory.create_stop_word_remover()
    teks_berita_id = stopword_remover.remove(teks_berita_id)

    # Stemming kata-kata
    stemmer_factory = StemmerFactory()
    stemmer = stemmer_factory.create_stemmer()
    teks_berita_id = stemmer.stem(teks_berita_id)

    # Membuat objek TextBlob
    blob_id = TextBlob(teks_berita_id)

    # Mendapatkan nilai polaritas sentimen
    polaritas_id = blob_id.sentiment.polarity
    print("Polaritas_id: ", polaritas_id)

    # Menentukan sentimen berdasarkan nilai polaritas
    if polaritas_id > 0:
        sentimen_id = "Positif"
    elif polaritas_id < 0:
        sentimen_id = "Negatif"
    else:
        sentimen_id = "Netral"

    # Menampilkan hasil
    print("Teks Berita (Bahasa Indonesia):", teks_berita_id)
    print("Sentimen:", sentimen_id)

    print("=====SPaCy=====")
    import spacy

    teks_berita_id = "MPT Bank Central Asia Tbk (BBCA) membukukan kinerja positif. Sepanjang semester pertama tahun ini, perusahaan membukukan kenaikan laba bersih 34% secara tahunan (yoy) menjadi Rp 24,2 triliun. Perfoma positif didorong oleh kenaikan volume kredit, perbaikan kualitas pinjaman, serta peningkatan volume transaksi dan pendanaan."

    # Load model bahasa Indonesia
    nlp_id = spacy.load("xx_ent_wiki_sm")

    # Proses teks menggunakan model SpaCy
    doc_id = nlp_id(teks_berita_id)

    # Mendapatkan nilai polaritas sentimen (contoh sederhana)
    polaritas_id = sum([token.sentiment for token in doc_id]) / len(doc_id)
    print("Polaritas id: ", polaritas_id)
    # Menentukan sentimen berdasarkan nilai polaritas
    if polaritas_id > 0:
        sentimen_id = "Positif"
    elif polaritas_id < 0:
        sentimen_id = "Negatif"
    else:
        sentimen_id = "Netral"

    # Menampilkan hasil
    print("Teks Berita (Bahasa Indonesia):", teks_berita_id)
    print("Sentimen:", sentimen_id)
    
    print("=====NLTK=====")
    import nltk

    nltk.download("stopwords")
    nltk.download("indonesian")

    from nltk.sentiment import SentimentIntensityAnalyzer
    from nltk.corpus import stopwords
    from nltk.tokenize import word_tokenize

    teks_berita_id = "MPT Bank Central Asia Tbk (BBCA) membukukan kinerja positif. Sepanjang semester pertama tahun ini, perusahaan membukukan kenaikan laba bersih 34% secara tahunan (yoy) menjadi Rp 24,2 triliun. Perfoma positif didorong oleh kenaikan volume kredit, perbaikan kualitas pinjaman, serta peningkatan volume transaksi dan pendanaan."
    
    # Menghapus stop words (kata-kata umum yang tidak memberikan makna signifikan)
    stop_words = set(stopwords.words("indonesian"))
    kata_kunci = [kata.lower() for kata in word_tokenize(teks_berita_id) if kata.isalnum() and kata.lower() not in stop_words]

    # Inisialisasi SentimentIntensityAnalyzer
    sia = SentimentIntensityAnalyzer()

    # Hitung nilai sentimen
    nilai_sentimen = sia.polarity_scores(" ".join(kata_kunci))["compound"]
    print("Nilai sentimen: ", nilai_sentimen)

    # Menentukan sentimen berdasarkan nilai sentimen
    if nilai_sentimen >= 0.05:
        sentimen_nltk = "Positif"
    elif nilai_sentimen <= -0.05:
        sentimen_nltk = "Negatif"
    else:
        sentimen_nltk = "Netral"

    # Menampilkan hasil
    print("Teks Berita (Bahasa Indonesia):", teks_berita_id)
    print("Sentimen:", sentimen_nltk)

    print("=====Transformers BERT=====")
    from transformers import pipeline

    # Contoh teks berita dalam Bahasa Indonesia
    teks_berita_id = "MPT Bank Central Asia Tbk (BBCA) membukukan kinerja positif. Sepanjang semester pertama tahun ini, perusahaan membukukan kenaikan laba bersih 34% secara tahunan (yoy) menjadi Rp 24,2 triliun. Perfoma positif didorong oleh kenaikan volume kredit, perbaikan kualitas pinjaman, serta peningkatan volume transaksi dan pendanaan."

    # Menghilangkan stop words
    stopword_factory = StopWordRemoverFactory()
    stopword_remover = stopword_factory.create_stop_word_remover()
    teks_berita_id = stopword_remover.remove(teks_berita_id)

    # Stemming kata-kata
    stemmer_factory = StemmerFactory()
    stemmer = stemmer_factory.create_stemmer()
    teks_berita_id = stemmer.stem(teks_berita_id)
    
    sentimen_analyzer = pipeline('sentiment-analysis', model='nlptown/bert-base-multilingual-uncased-sentiment')

    # Analisis sentimen
    hasil_sentimen = sentimen_analyzer(teks_berita_id)

    # Menampilkan hasil
    print("Teks Berita (Bahasa Indonesia):", teks_berita_id)
    print("Sentimen:", hasil_sentimen[0]['label'], "(Skor:", hasil_sentimen[0]['score'], ")")
    if hasil_sentimen[0]['label'] == "4 start" or hasil_sentimen[0]['label'] == "5 stars":
        sentimen = "positif"
    elif hasil_sentimen[0]['label'] == "3 stars":
        sentimen = "netral"
    else:
        sentimen = "negatif"

    print(sentimen)

def nltkOnly():
    from nltk.sentiment import SentimentIntensityAnalyzer
    sia = SentimentIntensityAnalyzer()
    print(sia.polarity_scores("aku pintar"))
    
def textblobBard():
    import textblob
    # Import teks yang akan dianalisis
    teks = "Film ini sangat bagus, ceritanya menarik dan aktingnya juga keren."
    # Buat objek TextBlob
    blob = textblob.TextBlob(teks)
    # Dapatkan nilai polarity
    polarity = blob.sentiment.polarity
    # Dapatkan nilai subjectivity
    subjectivity = blob.sentiment.subjectivity
    # Cetak hasil
    print("Polarity:", polarity)
    print("Subjectivity:", subjectivity)

def texblobBard2():
    import textblob

    # Import teks yang akan dianalisis
    teks = "Film ini sangat bagus, ceritanya menarik dan aktingnya juga keren"

    # Analisis sentimen teks
    sentiment = textblob.TextBlob(teks).sentiment

    # Cetak hasil analisis
    print("Polarity:", sentiment.polarity)
    print("Subjectivity:", sentiment.subjectivity)

    # Interpretasi hasil analisis
    if sentiment.polarity > 0:
        print("Sentimen: Positif")
    elif sentiment.polarity < 0:
        print("Sentimen: Negatif")
    else:
        print("Sentimen: Netral")
def islLexicon():
    import json
    import requests

    def get_indonesia_sentiment_lexicon():
        url = "https://raw.githubusercontent.com/fajri91/InSet/master/data/lexicon-indoslang.json"
        response = requests.get(url)
        
        try:
            response.raise_for_status()
            lexicon_data = json.loads(response.text)
            return lexicon_data
        except requests.exceptions.HTTPError as errh:
            print ("HTTP Error:",errh)
        except requests.exceptions.ConnectionError as errc:
            print ("Error Connecting:",errc)
        except requests.exceptions.Timeout as errt:
            print ("Timeout Error:",errt)
        except requests.exceptions.RequestException as err:
            print ("Something went wrong:",err)

    def analyze_sentiment(text, sentiment_lexicon):
        words = text.lower().split()
        sentiment_score = 0

        for word in words:
            if word in sentiment_lexicon:
                sentiment_score += sentiment_lexicon[word]

        # Nilai positif jika sentiment_score > 0, negatif jika < 0, dan netral jika 0
        if sentiment_score > 0:
            return "Positif"
        elif sentiment_score < 0:
            return "Negatif"
        else:
            return "Netral"

    # Contoh teks untuk dianalisis
    teks = "Buku itu bagus sekali, wangi, ceritanya juga bagus"

    # Ambil kamus sentimen bahasa Indonesia dari ISL
    isl_lexicon = get_indonesia_sentiment_lexicon()

    # Analisis sentimen
    if isl_lexicon:
        hasil_sentimen = analyze_sentiment(teks, isl_lexicon)
        # Tampilkan hasil
        print(f"Sentimen dari teks '{teks}': {hasil_sentimen}")
    else:
        print("Gagal mendapatkan kamus sentimen.")

def chatGPTSentiment():
    # Install pustaka yang dibutuhkan
    # pip install numpy pandas scikit-learn nltk

    import pandas as pd
    from sklearn.model_selection import train_test_split
    from sklearn.feature_extraction.text import TfidfVectorizer
    from sklearn.naive_bayes import MultinomialNB
    from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
    from nltk.corpus import stopwords
    from nltk.tokenize import word_tokenize
    from nltk.stem import PorterStemmer

    # Pra-pemrosesan teks
    def preprocess_text(text):
        stop_words = set(stopwords.words('indonesian'))
        ps = PorterStemmer()
        
        # Tokenisasi
        words = word_tokenize(text)
        
        # Hapus stop words dan lakukan stemming
        words = [ps.stem(word) for word in words if word.isalnum() and word not in stop_words]
        
        return ' '.join(words)

    # Baca dataset
    # Pastikan dataset berisi dua kolom: 'text' dan 'label'
    # 'text' berisi teks berita, 'label' berisi sentimen (pos, neg, net)
    df = pd.read_csv('dataset_berita_sentimen.csv')

    # Pra-pemrosesan teks pada kolom 'text'
    df['text'] = df['text'].apply(preprocess_text)

    # Bagi dataset menjadi set pelatihan dan pengujian
    X_train, X_test, y_train, y_test = train_test_split(df['text'], df['label'], test_size=0.2, random_state=42)

    # Ekstraksi fitur menggunakan TF-IDF
    tfidf_vectorizer = TfidfVectorizer()
    X_train_tfidf = tfidf_vectorizer.fit_transform(X_train)
    X_test_tfidf = tfidf_vectorizer.transform(X_test)

    # Buat model klasifikasi Naive Bayes
    model = MultinomialNB()
    model.fit(X_train_tfidf, y_train)

    # Prediksi pada set pengujian
    y_pred = model.predict(X_test_tfidf)

    # Evaluasi model
    print('Accuracy:', accuracy_score(y_test, y_pred))
    print('\nClassification Report:\n', classification_report(y_test, y_pred))
    print('\nConfusion Matrix:\n', confusion_matrix(y_test, y_pred))

def sentimentBagas():
    import string
    from urllib.request import urlopen
    import warnings
    import stanfordnlp
    # stanfordnlp.download('id')
    import nltk
    from nltk.corpus import stopwords
    from nltk.util import ngrams
    from collections import Counter
    from IPython.display import display
    
    warnings.filterwarnings('ignore')
    nlp = stanfordnlp.Pipeline(lang='id', processors='tokenize,pos')

    s = "Pemberi kerja adalah orang perseorangan, pengusaha, badan hukum, atau badan-badan lainnya yang  mempekerjakan tenaga kerja dengan membayar upah atau imbalan dalam bentuk lain. Pengusaha adalah orang perseorangan, persekutuan atau badan hukum yang menjalankan suatu perusahaan milik sendiri."

    doc = nlp(s.lower())
    # print(doc.sentences)

    for word in doc.sentences[1].words:
        print(word.text, word.upos)
    
    words = [word.text for word in doc.sentences[1].words]
    bigrams = [
        bigram for bigram in list(ngrams(words, 2))
        if bigram[0] not in string.punctuation and bigram[1] not in string.punctuation
    ]
    print(bigrams)
    grammar = "NP: {<NOUN|PROPN>+ <ADJ>*}"
    parser = nltk.RegexpParser(grammar)
    word_pos_pairs = [(word.text, word.upos) for word in doc.sentences[0].words]
    tree = parser.parse(word_pos_pairs)
    print(tree)

    keywords = []
    for subtree in tree.subtrees():
        if subtree.label() == 'NP' and len(subtree.leaves()) >= 1:
            words = [item[0] for item in subtree.leaves()]
            keywords.append(' '.join(words))
                
    print(keywords)


    text = """
                                    UNDANG-UNDANG REPUBLIK INDONESIA
                                            NOMOR 13 TAHUN 2003
                                                TENTANG
                                            KETENAGAKERJAAN

                                    DENGAN RAHMAT TUHAN YANG MAHA ESA

                                        PRESIDEN REPUBLIK INDONESIA,

            Menimbang:
            a.   bahwa pembangunan nasional dilaksanakan dalam rangka pembangunan manusia
                Indonesia seutuhnya dan pembangunan masyarakat Indonesia seluruhnya untuk
                mewujudkan masyarakat yang sejahtera, adil, makmur, yang merata, baik materiil maupun
                spiritual berdasarkan Pancasila dan Undang-Undang Dasar Negara Republik Indonesia
                Tahun 1945;
            b.   bahwa dalam pelaksanaan pembangunan nasional, tenaga kerja mempunyai peranan dan
                kedudukan yang sangat penting sebagai pelaku dan tujuan pembangunan;
            c.   bahwa sesuai dengan peranan dan kedudukan tenaga kerja, diperlukan pembangunan
                ketenagakerjaan untuk meningkatkan kualitas tenaga kerja dan 
            """
    print(len(text.split()))
    doc = nlp(text.lower())    
    # create word and POS tag pair
    pairs = []
    for sentence in doc.sentences:
        tagged = []
        for word in sentence.words:
            tagged.append((word.text, word.upos))
        pairs.append(tagged)
        
    keywords = []
    for sentence in pairs:
        parse_tree = parser.parse(sentence)
        for subtree in parse_tree.subtrees():
            if subtree.label() == 'NP' and len(subtree.leaves()) >= 2:  # only consider bigram
                words = [item[0] for item in subtree.leaves()]
                keywords.append(' '.join(words))
    print(keywords[:20])
    print(len(keywords))
    freq = Counter(keywords)
    print("Freq: ", freq)
    print("Most Common: ", freq.most_common(50))
    

def huggingFacePipelineTransformer():
    from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
    from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory
    from transformers import pipeline
    from transformers import AutoTokenizer, AutoModelForSequenceClassification
    # print(type(news))
    # Replace 'indobenchmark/indonlu-lite-base' with the actual path to the model if needed
    model_name = 'indobenchmark/indonlu-lite-base'
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForSequenceClassification.from_pretrained(model_name)

    # Example text
    text = "aku sayang kamu"

    # Tokenize and predict sentiment
    inputs = tokenizer(text, return_tensors="pt")
    outputs = model(**inputs)
    logits = outputs.logits
    predicted_class = logits.argmax().item()

    # Print the predicted class
    print(predicted_class)

def sentimentTextBlob(text):
    # text = "Aku sayang kamu"
    from textblob import TextBlob
    try:
        analysis = TextBlob(text)
        if analysis.sentiment.polarity > 0:
            return 'Positif'
        elif analysis.sentiment.polarity == 0:
            return 'Netral'
        else:
            return 'Negatif'
    except Exception as e:
        print(f"An error occurred: {e}")
        return 'Error'

# Testing
# text = "Saya sangat senang hati dengan kemajuan teknologi terbaru."
# result = sentimentTextBlob(text)
# print(f"Sentiment: {result}")
import nltk
from nltk.sentiment.util import *
from nltk.sentiment import SentimentIntensityAnalyzer
import pandas as pd
def nltkVader():

    # Inisialisasi SentimentIntensityAnalyzer
    nltk.download('vader_lexicon') 
    sia = SentimentIntensityAnalyzer()

    # Contoh paragraf
    text = "Aku sayang kamu"

    # Menghitung sentimen pada setiap kata dalam paragraf
    words = text.split()
    print(words)
    scores = [sia.polarity_scores(word) for word in words]
    print(scores)

    # Menghitung rata-rata sentimen
    score_df = pd.DataFrame(scores)
    print(score_df.head())
    avg_score = score_df['compound'].mean()

    # Menentukan sentimen pada paragraf
    print(avg_score)
    if avg_score > 0.05:
        sentiment = "Positif"
    elif avg_score < -0.05:
        sentiment = "Negatif"
    else:
        sentiment = "Netral"

    print("Paragraf: ", text)
    print("Sentiment: ", sentiment)

def torchTensi():
    from transformers import pipeline

    # Load sentiment analysis pipeline for Indonesian
    sentiment_pipeline = pipeline('sentiment-analysis', model="indobenchmark/indonlu-lite-base")

    # Example text for analysis
    text = "Saya senang sekali dengan produk ini. Kualitasnya sangat baik!"

    # Perform sentiment analysis
    result = sentiment_pipeline(text)

    # Display the result
    print(result)

def transformerBERT():
    from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
    from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory
    from transformers import pipeline
    # from transformers import AutoTokenizer, AutoModelForSequenceClassification
    print("=====Transformers BERT=====")

    # Contoh teks berita dalam Bahasa Indonesia
    teks_berita_id = "Saya senang sekali dengan produk ini. Kualitasnya sangat baik!"

    # Menghilangkan stop words
    stopword_factory = StopWordRemoverFactory()
    stopword_remover = stopword_factory.create_stop_word_remover()
    teks_berita_id = stopword_remover.remove(teks_berita_id)

    # Stemming kata-kata
    stemmer_factory = StemmerFactory()
    stemmer = stemmer_factory.create_stemmer()
    teks_berita_id = stemmer.stem(teks_berita_id)
    
    sentimen_analyzer = pipeline('sentiment-analysis', model='nlptown/bert-base-multilingual-uncased-sentiment')

    # Analisis sentimen
    hasil_sentimen = sentimen_analyzer(teks_berita_id)

    # Menampilkan hasil
    print("Teks Berita (Bahasa Indonesia):", teks_berita_id)
    print("Sentimen:", hasil_sentimen[0]['label'], "(Skor:", hasil_sentimen[0]['score'], ")")
    if hasil_sentimen[0]['label'] == "4 start" or hasil_sentimen[0]['label'] == "5 stars":
        sentimen = "positif"
    elif hasil_sentimen[0]['label'] == "3 stars":
        sentimen = "netral"
    else:
        sentimen = "negatif"

    print(sentimen)

def sklearnSentiment():
    import torch
    from transformers import BertTokenizer, BertForSequenceClassification

    # Inisialisasi model dan tokenizer
    model = BertForSequenceClassification.from_pretrained("indonesian-emotion")
    tokenizer = BertTokenizer.from_pretrained("indonesian-emotion")

    # Teks yang akan dianalisis
    text = "Contoh paragraf bahasa Indonesia yang akan dianalisis untuk mengidentifikasi emosi yang dihasilkan oleh teks tersebut."

    # Tokenize teks
    encoded_input = tokenizer(text, return_tensors='pt')

    # Prediksi emosi
    output = model(**encoded_input)

    # Ekstrak nilai probabilities dari hasil prediksi
    probs = torch.nn.functional.softmax(output.logits, dim=-1)

    # Tampilkan hasil analisis
    for idx, label in enumerate(model.config.id2label):
        print(f"{label}: {probs.numpy()[0][idx]:.2f}")

def roberta():
    start_time = time.time()
    from transformers import pipeline

    pretrained_name = "w11wo/indonesian-roberta-base-sentiment-classifier"

    nlp = pipeline(
        "sentiment-analysis",
        model=pretrained_name,
        tokenizer=pretrained_name
    )

    text = "PT Bank Mandiri (Persero) Tbk. menjadi salah satu lembaga perbankan yang menjalankan program kredit usaha rakyat (KUR). Bank Mandiri berhasil menyalurkan KUR kepada lebih dari 195 ribu debitur dengan nilai Rp 20,52 triliun hingga akhir Agustus 2023. KUR Mandiri menyasar debitur pemilik usaha mikro, kecil, dan menengah (UMKM), UMKM dari anggota keluarga dari karyawan yang berpenghasilan tetap, Pekerja Migran Indonesia (PMI) atau Tenaga Kerja Indonesia (TKI), hingga calon peserta magang di luar negeri. Cara Transfer Mandiri ke DANA Lewat Livin' by Mandiri, ATM, dan Internet BankingLantas, bagaimana skema pembiayaan KUR Mandiri 2023 dan persyaratannya? Berikut persyaratannya seperti dikutip dari situs Bank Mandiri:Syarat KUR Mandiri 2023KUR Mandiri dibedakan menjadi lima jenis, yaitu KUR Super Mikro, KUR Mikro, KUR Kecil, KUR TKI, dan KUR Khusus. Penyaluran KUR diprioritaskan pada sektor produksi, seperti pertanian, kehutanan, dan perburuan, kelautan dan perikanan, industri pengolahan, konstruksi, pertambangan garam rakyat, pariwisata, serta jasa produksi. Terkini: Setelah Beroperasi Sejak 1968 Citibank Tutup Layanan Consumer Banking, Buruh Mogok Nasional 2 Hari Tuntut Kenaikan UMP 15 PersenBerikut persyaratan KUR Mandiri berdasarkan jenisnya periode sampai dengan 31 Desember 2023: 1. KUR Super Mikro- Calon debitur berusia minimal 21 tahun atau sudah menikah.- Limit kredit sampai dengan Rp 10 juta.- Jangka waktu pelunasan Kredit Modal Kerja (KMK) maksimal 3 tahun dan Kredit Investasi (KI) maksimal 5 tahun.- Suku bunga 3 persen efektif per tahun.- Agunan pokok berupa usaha atau objek yang dibiayai.- Syarat KUR Mandiri 2023 Super Mikro tidak diberlakukan agunan tambahan.- Calon debitur dimungkinkan bagi usaha kurang dari 6 bulan, tetapi harus memenuhi salah satu syarat, antara lain mengikuti pendampingan, pelatihan kewirausahaan atau pelatihan lainnya, tergabung dalam kelompok usaha, maupun mempunyai anggota keluarga yang sudah memiliki usaha produktif dan layak.- Tidak dibatasi dengan total akumulasi plafon per debitur"

    print(f"Text: {text}")
    print(f"Sentiment: {nlp(text)}")
    end_time = time.time()
    print(f"total waktu: {end_time - start_time}")

def mdughol():
    start_time = time.time()
    print(f"[{time.time()}] Initialize")
    from transformers import pipeline
    from transformers import AutoTokenizer, AutoModelForSequenceClassification

    pretrained= "mdhugol/indonesia-bert-sentiment-classification"

    model = AutoModelForSequenceClassification.from_pretrained(pretrained)
    tokenizer = AutoTokenizer.from_pretrained(pretrained)

    sentiment_analysis = pipeline("sentiment-analysis", model=model, tokenizer=tokenizer)

    label_index = {'LABEL_0': 'positive', 'LABEL_1': 'neutral', 'LABEL_2': 'negative'}

    print(f"[{time.time()}] Declare")
    pos_text = "Sangat bahagia hari ini"
    neg_text = "Dasar anak sialan!! Kurang ajar!!"

    print(f"[{time.time()}] Output 1")
    result = sentiment_analysis(pos_text)
    status = label_index[result[0]['label']]
    score = result[0]['score']
    print(f'Text: {pos_text} | Label : {status} ({score * 100:.3f}%)')

    print(f"[{time.time()}] Output 2")
    result = sentiment_analysis(neg_text)
    status = label_index[result[0]['label']]
    score = result[0]['score']
    print(f'Text: {neg_text} | Label : {status} ({score * 100:.3f}%)')
    end_time = time.time()
    print(f"total waktu: {end_time - start_time}")

roberta()

#* TextBlob tanda baca dihilangkan, imbuhan dihilangkan, text di-lower
#* Spacy Tidak, melakukan tetap melakukan, di TextBlob jadi laku, di spacy koma dan titik tetap ada, di textblob hilang