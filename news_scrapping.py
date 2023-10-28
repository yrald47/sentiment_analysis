import urllib.request as urllib2
from bs4 import BeautifulSoup
from nltk.sentiment import SentimentIntensityAnalyzer
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import config

def getLinks(tag_search, list_news_tag, list_news_tag_class, news_link_class):
    news_search = urllib2.urlopen(tag_search).read()
    soup = BeautifulSoup(news_search, "lxml")
    news_list = soup.find_all(list_news_tag, list_news_tag_class) if list_news_tag_class != "" else soup.find_all(list_news_tag, class_=False)
    for news in news_list:
        link = news.find('a', href=True)['href'] if news_link_class == "" else news.find('a', news_link_class, href=True)['href']
        title = news.find("h2", "title").get_text()
        print("\nlink: " + link)
        print("title: " + title)


def getContent():
    pass

'''
keyword = "bca"
news_search = urllib2.urlopen("https://www.detik.com/tag/"+keyword).read()

soup = BeautifulSoup(news_search, "lxml")

news_list = soup.find_all("article")

for news in news_list:
    link = news.find('a', href=True)['href']
    title = news.find("h2", "title").get_text()
    print("\nlink: " + link)
    print("title: " + title)
    news_html = urllib2.urlopen(link).read()
    news_lxml = BeautifulSoup(news_html, "lxml")
    try:
        content = news_lxml.find("div", "detail__body-text itp_bodycontent")
        paragraphs = content.find_all("p", class_=False)
        context = ""
        for paragraph in paragraphs:
            context += paragraph.get_text() + "\n"
        mydict = {"title": title, "link": link, "content": context}
        x = config.collection.insert_one(mydict)
    except Exception as error:
        print(error)
'''