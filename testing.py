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

selectLink()