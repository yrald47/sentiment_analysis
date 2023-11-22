import json
import config
import news_scrapping
import sys
import pytz
from datetime import datetime, timedelta
import datetime as dt
import time
import re
import threading
# import pprint

def scrape_portal(portals):
    portal_name = portals['name']
    header = "\nScraping News From " + portal_name
    print('='*len(header) + '\n' + header + '\n' + '='*len(header))
    
    keyword = sys.argv[2].replace(' ', portals['keyword_concat'])
    timezone = pytz.timezone('Asia/Jakarta')
    today = datetime.now(timezone).date()
    a_week_before = today - timedelta(weeks=1)
    today_str = today.strftime('%d/%m/%Y')
    a_week_before_str = a_week_before.strftime('%d/%m/%Y')
    link = portals['search_link'].replace('keyword_to_replace', keyword).replace('cdate_replace', today_str).replace('fdate_replace', a_week_before_str).replace('tdate_replace', today_str)
    print("Search news from Link: " + link)
    # exit()
    each_result_tag = portals['each_result_tag']
    each_result_class = portals['each_result_class']
    each_result_link_class = portals['each_result_link_class']
    links = news_scrapping.getLinks(link, each_result_tag, each_result_class, each_result_link_class)
    print("Found " + str(len(links)) + " News list from " + portals['name'])
    # exit(0)

    content_tag = portals['content_tag']
    content_class = portals['content_class']
    paragraph_tag = portals['paragraph_tag']
    paragraph_class = portals['paragraph_class']
    news_date_tag = portals['news_date_tag']
    news_date_class = portals['news_date_class']
    exception_link_containt = portals['exception_link_containt']
    datetime_regex = portals['datetime_regex']
    date_format = portals['date_format']

    print("Content Tag: " + str(content_tag))
    print("Content Class" + str(content_class))
    print("Paragraph Tag: " + str(paragraph_tag))
    print("Paragraph Class: " + str(paragraph_class))
    print("Exception: " + str(exception_link_containt))
    print("Datetime Regex: " + str(datetime_regex))
    print("Format: " + str(date_format))

    for link in links:
        jakarta = pytz.timezone('Asia/Jakarta')
        dt_now = datetime.now(jakarta)
        scraping_date = dt.datetime.strptime(dt_now.strftime("%Y-%m-%d"), "%Y-%m-%d")
        print("LINK: " + link)
        scrap = True
        for text in exception_link_containt:
            if link.find(text) >= 0:
                scrap = False
                break
        print("SCRAP: " + str(scrap))
        if scrap == True:
            result = news_scrapping.getContent2(link, content_tag, content_class, paragraph_tag, paragraph_class, news_date_tag, news_date_class, datetime_regex, date_format)
            print("Scraping at: " + str(scraping_date))
            print("RESULTS: " + str(result))
            # with open('news_content.txt', 'a', encoding="utf-8") as f:
            #     f.write(str(result['content'].decode('utf-8')) + "\n\n")
            collection = config.db['news']
            scrapped_news = {"keyword": sys.argv[2], "source": portal_name, "scraping_date": scraping_date, "link": link, "title": result['title'], "news_date": result['news_date'], "content": re.sub(r'.* -\s', '', result['content'].decode('utf-8')), "error": result['error'].decode('utf-8')}
            x = collection.insert_one(scrapped_news)
        print("===============")
        # exit()

if __name__ == "__main__":
    start_time = time.time()
    if len(sys.argv) == 3 and sys.argv[1] == '-t':
        print("Start Scraping with Keyword: " + sys.argv[2])

        threads = []
        portal_json_file = "source.json"
        with open(portal_json_file, 'r') as f:
            datastore = json.load(f)

        # with open('news_content.txt', 'w', encoding="utf-8") as f:
        #     f.write("")
        for portals in datastore['news_portal']:
            thread = threading.Thread(target=scrape_portal, args=(portals,))
            threads.append(thread)
            thread.start()

        for thread in threads:
            thread.join()
    else:
        print('Ketik python main.py -t "keyword yang bersangkutan"')

    end_time = time.time()
    print(f"total waktu: {end_time - start_time}")