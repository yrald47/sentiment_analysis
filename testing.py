## tes xpath from lxml
import urllib.request as urllib2
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup

# Import required modules
from lxml import html
import requests

url = "https://finance.detik.com/foto-bisnis/d-6976432/indonesia-knowledge-forum-2023-bahas-perekonomian-indonesia/1"
# url = "https://www.cnnindonesia.com/ekonomi/20231019175158-78-1013529/bca-raup-laba-bersih-rp364-t-kuartal-iii-2023"
req = Request(url=url, headers={'User-Agent': 'Mozilla/5.0'})

news_search = urllib2.urlopen(req).read()
# soup = BeautifulSoup(news_search, "lxml")
 
# parsing with html parser
# parsed = BeautifulSoup(news_search, "html.parser")
 
# tag found
# print("Tag found :", parsed.h1.name)
# the content inside the tag
# print("Content :", parsed.h1.string)
# a = parsed.find("div", "slick-track")

parsed2 = BeautifulSoup(news_search, "lxml")
# print(parsed2)

b = parsed2.find("div", {"id": "slider-foto__detail"}).find_all("figcaption", "mgt-16")
for i in b:
    print(i.get_text())
# exit(0)
'''print("======\n", b)

# the encoded method
print("Encoding method :", parsed.original_encoding)
with open('detik_compare.lxml', 'w', encoding="utf-8") as f:
    f.write("detik HTML here")
    for i in a:
        f.write(i.get_text())
    f.close()

with open('detik_compare.lxml', 'a', encoding="utf-8") as f:
    f.write("============================")
    for i in b:
        f.write(i.get_text())
# print(soup)
# exit()

''' 
# Request the page
page = requests.get("https://finance.detik.com/foto-bisnis/d-6976432/indonesia-knowledge-forum-2023-bahas-perekonomian-indonesia/1")
 
# Parsing the page
tree = html.fromstring(page.content)
# Get element using XPath
# print(tree)
content = tree.xpath(
    '//div[@id="slider-foto__detail"]/figure/figcaption[@class="mgt-16"]/text()')
print("\n" + content[0])
'''


import requests
from lxml.html import fromstring

url = 'https://www.cnnindonesia.com/ekonomi/20231019175158-78-1013529/bca-raup-laba-bersih-rp364-t-kuartal-iii-2023'  # Replace with the desired URL
response = requests.get(url)

soup = fromstring(response.text)

# Select elements using XPath
elements = soup.xpath('//div[@class="detail-text text-cnn_black text-sm grow min-w-0"]/p/text()')  # Replace with your XPath expression

# Iterate over the selected elements
print(len(elements))
print(elements)
'''