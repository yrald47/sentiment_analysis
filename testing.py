## tes xpath from lxml
import urllib.request as urllib2
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup

# Import required modules
from lxml import html
import requests
# import datetime
from datetime import datetime

import locale

import re
import json

# Contoh string JSON yang berisi pola regex
# json_string = '{"regex_pattern": "\\d{1,2}/\\d{1,2}/\\d{4}"}'

# # Mendapatkan pola regex dari JSON
# json_data = json.loads(json_string)
# regex_pattern = json_data["regex_pattern"]
regex_pattern = "\\d{1,2}/\\d{1,2}/\\d{4}"

# Menggunakan string regex langsung dalam re.compile()
regex = re.compile(regex_pattern)

# Sekarang, Anda dapat menggunakan objek regex untuk mencocokkan teks
kalimat = "Ini adalah tanggal 08/12/2023 dan juga 8/12/2023, serta 8 Februari 2023."
tanggal = regex.findall(kalimat)

# Menampilkan tanggal yang ditemukan
for tgl in tanggal:
    print(tgl)
exit()

# for lang in locale.windows_locale.values():
#     print(lang)

loc = locale.getlocale()
print(loc)
locale.setlocale(locale.LC_ALL , 'id_ID')
loc = locale.getlocale()
print(loc)

string_tanggal3 = "20 Okt 2023 09:00"
tanggal_objek3 = datetime.strptime(string_tanggal3, "%d %b %Y %H:%M")
tanggal_hasil3 = tanggal_objek3.strftime("%Y-%m-%d")

print(tanggal_hasil3)

exit(0)
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
url = "https://foto.tempo.co/read/21815/diduga-bunuh-diri-seorang-pria-jatuh-dari-lantai-56"

# req = Request(url=url, headers={'User-Agent': 'Mozilla/5.0'})
# news_search = urllib2.urlopen(req).read()
# parsed2 = BeautifulSoup(news_search, "lxml")
# b = parsed2.find("article", "detail-artikel").find_all("div", "detail-in")
# print(len(b))
# for i in b:
#     print(i.get_text())

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