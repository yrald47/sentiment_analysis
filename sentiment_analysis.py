import urllib.request as urllib2
from bs4 import BeautifulSoup
from nltk.sentiment import SentimentIntensityAnalyzer
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import config

# import nltk
# nltk.download('punkt')
# nltk.download('vader_lexicon')
# nltk.download('stopwords')

# client = MongoClient()
# Provide the connection details

keyword = "bca"
# html = urllib2.urlopen("https://search.kompas.com/search/?q=BCA&submit=Submit#gsc.tab=0&gsc.q=BCA&gsc.sort=date").read()
# html = urllib2.urlopen("https://umkm.kompas.com/read/2023/10/26/113538883/ace-ys-2023-libatkan-generasi-muda-bangun-industri-kreatif-dan-digital-di-asia").read()
news_search = urllib2.urlopen("https://www.detik.com/tag/"+keyword).read()

# print(type(news_search))

soup = BeautifulSoup(news_search, "lxml")
# print(type(soup))
# with open('detik.lxml', 'w') as f:
#     f.write(soup.prettify())

news_list = soup.find_all("article")
# print(len(news_list))
# print(news_list[0])
for news in news_list:
    # link = BeautifulSoup(news, "lxml")
    # print(link.find('a', href=True))
    # print(type(news))
    # print(news.find('a').get_text())
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
            # stop_words = set(stopwords.words("indonesian"))
            # tokens = word_tokenize(paragraph.get_text())
            # print(paragraph.get_text(), "\n")
            context += paragraph.get_text() + "\n"
            # result = [i for i in tokens if not i in stop_words]
            # print (result)
        # print(context)
        mydict = {"title": hash(title), "link": link, "content": context}
        x = config.collection.insert_one(mydict)
    except Exception as error:
        print(error)

    # break


'''
## tag p untuk berita kompas
news = soup.find_all("p")

# with open('kompas.lxml', 'w') as f:
#     f.write(soup.prettify())
# print(news)
blank = 0
for item in news:
    if item.get_text() == "":
        blank += 1
    
    if blank == 3:
        break
        
    if item.get_text() != "":
        print(item.get_text())
        blank = 0
'''
# print(len(news))