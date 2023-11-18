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
# from nltk.corpus import stopwords
# from nltk.tokenize import word_tokenize
# import sys

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

def getContent2(link, content_tag, content_class, paragraph_tag, paragraph_class, news_date_tag, news_date_class, datetime_regex, date_format):
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
                context += paragraph.get_text()

        # print("===CONTEXT===")
        # print(context.encode('utf-8'))

        return {'title': title.lower(), 'news_date': news_date, 'content': context.encode('utf-8'), 'error': ''.encode('utf-8')}
    except Exception as e:
        return {'title': '', 'news_date': '', 'content': str(e).encode('utf-8'), 'error': str(e).encode('utf-8')}

    # collection = config.db['news']
    # scrapped_news = {"scraping_date": scraping_date, "title": hash(title.lower()), "link": link, "content": context}
    # x = collection.insert_one(scrapped_news)