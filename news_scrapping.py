import urllib.request as urllib2
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
from nltk.sentiment import SentimentIntensityAnalyzer
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from datetime import datetime
import pytz
import config
import sys

def getLinks(tag_search, list_news_tag, list_news_tag_class, news_link_class):
    req = Request(url=tag_search, headers={'User-Agent': 'Mozilla/5.0'})
    news_search = urllib2.urlopen(req).read()
    soup = BeautifulSoup(news_search, "lxml")
    news_list = soup.find_all(list_news_tag, list_news_tag_class) if list_news_tag_class != "" else soup.find_all(list_news_tag, class_=False)
    links = []
    for news in news_list:
        link = news.find('a', href=True)['href'] if news_link_class == "" else news.find('a', news_link_class, href=True)['href']
        links.append(link)
    return links


def getContent(link, news_tag, news_tag_class, title_tag, title_tag_class, news_date_tag, news_date_tag_class):
    req = Request(url=link, headers={'User-Agent': 'Mozilla/5.0'})
    news_html = urllib2.urlopen(req).read()
    news_lxml = BeautifulSoup(news_html, "lxml")
    # print(news_lxml)
    for item in news_tag_class:
        index = news_tag_class.index(item)
        try:
            content = news_lxml.find(news_tag[index], item)
            paragraphs = content.find_all("p", class_=False)
            break
        except Exception:
            continue
    
    print(paragraphs)
    # print(paragraphs)
    # title = news_lxml.find(title_tag, title_tag_class).get_text()
    title = news_lxml.find("title").get_text()
    print(title, type(title))
    # news_date = news_lxml.find(news_date_tag, news_date_tag_class).get_text()
    # title = "titlelellelel"
    # news_date = "2023"
    context = ""
    for paragraph in paragraphs:
        context += paragraph.get_text() + "\n"
    
    jakarta = pytz.timezone('Asia/Jakarta')
    scraping_date = datetime.now(jakarta)
    mydict = {"scraping_date": scraping_date, "title": hash(title.lower()), "link": link, "content": context}
    x = config.collection.insert_one(mydict)