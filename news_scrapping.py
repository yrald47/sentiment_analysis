import urllib.request as urllib2
from urllib.request import Request, urlopen
from urllib.error import URLError
from bs4 import BeautifulSoup
from nltk.sentiment import SentimentIntensityAnalyzer
from datetime import datetime as dt
import pytz
import config
import datetime
from lxml import html
import requests
import locale
import re

from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory
from textblob import TextBlob
from transformers import pipeline
# from nltk.corpus import stopwords
# from nltk.tokenize import word_tokenize
# import sys
def sentiment_scoring_long(text):
    from transformers import AutoTokenizer, AutoModelForSequenceClassification
    import torch

    pretrained_name = "intanm/indonesian_financial_sentiment_analysis_10"

    # Load tokenizer and model
    tokenizer = AutoTokenizer.from_pretrained(pretrained_name)
    model = AutoModelForSequenceClassification.from_pretrained(pretrained_name)
    tokens = tokenizer(text, return_tensors="pt", truncation=True, padding=True, max_length=512)
    # Forward pass through the model
    outputs = model(**tokens)

    return outputs

def sentiment_scoring(text):
    # pretrained_name = "w11wo/indonesian-roberta-base-sentiment-classifier"
    pretrained_name = "intanm/indonesian_financial_sentiment_analysis_10"

    nlp = pipeline(
        "sentiment-analysis",
        model=pretrained_name,
        tokenizer=pretrained_name
    )
    print(type(nlp(text)))
    return nlp(text)

def sentiment_score(news):
    # print(type(news))
    stopword_factory = StopWordRemoverFactory()
    stopword_remover = stopword_factory.create_stop_word_remover()
    news = stopword_remover.remove(news)

    stemmer_factory = StemmerFactory()
    stemmer = stemmer_factory.create_stemmer()
    news = stemmer.stem(news)
    sentimen_analyzer = pipeline('sentiment-analysis', model='nlptown/bert-base-multilingual-uncased-sentiment')

    hasil_sentimen = sentimen_analyzer(news)

    print("Teks Berita (Bahasa Indonesia):", news)
    print("Sentimen:", hasil_sentimen[0]['label'], "(Skor:", hasil_sentimen[0]['score'], ")")
    if hasil_sentimen[0]['label'] == "4 start" or hasil_sentimen[0]['label'] == "5 stars":
        sentimen = "positif"
    elif hasil_sentimen[0]['label'] == "3 stars":
        sentimen = "netral"
    else:
        sentimen = "negatif"
    return sentimen

def getLinks(tag_search, list_news_tag, list_news_tag_class, news_link_class):
    try:
        req = Request(url=tag_search, headers={'User-Agent': 'Mozilla/5.0'})
        news_search = urllib2.urlopen(req).read()
        soup = BeautifulSoup(news_search, "lxml")
        news_list = soup.find_all(list_news_tag, list_news_tag_class) if list_news_tag_class != "" else soup.find_all(list_news_tag, class_=False)
        links = []
        for news in news_list:
            link = news.find('a', href=True)['href'] if news_link_class == "" else news.find('a', news_link_class, href=True)['href']
            collection = config.db['news']
            result = collection.count_documents({"link": {"$regex": re.compile(link[:75])}})
            if result == 0:
                links.append(link)
        return links
    except Exception as e:
        return []

def getContent(link, content_tag, content_class, paragraph_tag, paragraph_class, news_date_tag, news_date_class, datetime_regex, date_format):
    try:
        req = Request(url=link, headers={'User-Agent': 'Mozilla/5.0'})
        news_html = urllib2.urlopen(req).read()
        news_lxml = BeautifulSoup(news_html, "lxml")

        paragraphs = []
        for index, classes in enumerate(content_class):
            # index = content_class.index(classes)
            # print("INDEX: " + str(index) )
            # print("<" + content_tag[index] + " class='" + classes + "'><" + paragraph_tag[index] + " class='" + paragraph_class[index] + "'></" + paragraph_tag[index] + "></" + content_tag[index] + ">")
            # print(news_lxml.find(content_tag[index], tag))
            try:
                # content = news_lxml.find(content_tag[index], classes)
                paragraphs = news_lxml.find(content_tag[index], classes).find_all(paragraph_tag[index], class_=False) if paragraph_class[index] == "" else news_lxml.find(content_tag[index], classes).find_all(paragraph_tag[index], paragraph_class[index])
                break
            except Exception:
                continue
            
        # print(paragraphs)
        # title = news_lxml.find("title").get_text()
        title = news_lxml.title.text
        # print(title, type(title))
        
        str_date = ""
        news_date = dt.now(pytz.timezone('Asia/Jakarta'))
        locale.setlocale(locale.LC_ALL , 'id_ID')
        for index, tags in enumerate(news_date_tag):
            # print(str(index) + ": <" + tags + " class='" + news_date_class[index] + "'>")
            try:
                str_date = news_lxml.find(tags, news_date_class[index]).get_text()
                # str_date = str_date.split(date_string_splitter)[1].split('WIB')[0].strip()
                regex = re.compile(datetime_regex)
                str_date = regex.findall(str_date)
                news_date = dt.strptime(str_date[0], date_format)
                news_date = news_date.strftime("%Y-%m-%d")
                break
            except Exception as e:
                print("Date Error: " + str(e))
                continue

        # print("STR DATE: " + str_date[0])
        # print(type(str_date))
        # print(len(str_date))
        # print("NEWS_DATE: " + str(news_date))

        context = ""
        for paragraph in paragraphs:
            # print("PARAGRAPH LEN: " + str(len(paragraph)))
            if paragraph.get_text().find('Baca Juga:') == -1 and paragraph.get_text().find('Baca juga:') == -1 and paragraph.get_text().find('Pilihan Editor:') == -1:
                context += ' '+paragraph.get_text()

        # print("===CONTEXT===")
        # print(context.encode('utf-8'))

        return {'title': title.lower(), 'news_date': news_date, 'content': context.encode('utf-8'), 'error': ''.encode('utf-8')}
    except Exception as e:
        return {'title': '', 'news_date': '', 'content': str(e).encode('utf-8'), 'error': str(e).encode('utf-8')}