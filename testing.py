## tes xpath from lxml
import urllib.request as urllib2
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup

# Import required modules
from lxml import html
import requests

xs = ["div", "article", "div", "div"]
for idx, x in enumerate(xs):
    print(idx, x)

exit()

## TESTING XPATH AND FIND TAG DETIK FOTO SLIDER

# url = "https://finance.detik.com/foto-bisnis/d-6976432/indonesia-knowledge-forum-2023-bahas-perekonomian-indonesia/1"
# url = "https://video.tempo.co/read/6460/aksi-ganjal-atm-gunakan-tusuk-gigi-terekam-kamera-cctv"
url = "https://video.tempo.co/read/6460/aksi-ganjal-atm-gunakan-tusuk-gigi-terekam-kamera-cctv"
# url = "https://finance.detik.com/foto-bisnis/d-6976432/indonesia-knowledge-forum-2023-bahas-perekonomian-indonesia"

req = Request(url=url, headers={'User-Agent': 'Mozilla/5.0'})
news_search = urllib2.urlopen(req).read()
parsed2 = BeautifulSoup(news_search, "lxml")
b = parsed2.find("article", "detail-artikel").find_all("div", "detail-in")
print(len(b))
for i in b:
    print(i.get_text())

print("***==========***")
page = requests.get(url)
tree = html.fromstring(page.content)
# content = tree.xpath(
#     '//div[@id="slider-foto__detail"]/figure/figcaption[@class="mgt-16"]/text()')
content = tree.xpath(
    '//article[@class="detail-artikel"]/div[@class="detail-in"]/text()')
print(len(content))
for i in content:
    print(i)

# WRITE LXML SITE
url = "https://finance.detik.com/foto-bisnis/d-6976432/indonesia-knowledge-forum-2023-bahas-perekonomian-indonesia"

req = Request(url=url, headers={'User-Agent': 'Mozilla/5.0'})
news_search = urllib2.urlopen(req).read()
parsed2 = BeautifulSoup(news_search, "lxml")
with open('video_tempo.lxml', 'w', encoding="utf-8") as f:
    f.write(str(parsed2))

# b = parsed2.find("div", {"id": "slider-foto__detail"}).find_all("figcaption", "mgt-16")
# for i in b:
#     print(i.get_text())