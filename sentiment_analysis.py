import urllib.request as urllib2
from bs4 import BeautifulSoup

keyword = "bca"
# html = urllib2.urlopen("http://www.bhinneka.com/?cari="+keyword).read()
# html = urllib2.urlopen("https://search.kompas.com/search/?q=BCA&submit=Submit#gsc.tab=0&gsc.q=BCA&gsc.sort=date").read()
html = urllib2.urlopen("https://umkm.kompas.com/read/2023/10/26/113538883/ace-ys-2023-libatkan-generasi-muda-bangun-industri-kreatif-dan-digital-di-asia").read()

# print(type(html))
# print(html[1:])

soup = BeautifulSoup(html, "lxml")
# print(type(soup))
# print(soup.prettify()[25000:100000])
# with open('readme.lxml', 'w') as f:
    # f.write(soup.prettify())

# news = soup.find_all("div", "gs-title")
# news = soup.find_all("div", "read__content clearfix")
news = soup.find_all("p")

with open('kompas.lxml', 'w') as f:
    f.write(soup.prettify())
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

# print(len(news))