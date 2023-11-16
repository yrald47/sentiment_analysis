import json
# import config
import news_scrapping
import sys
import pytz
from datetime import datetime, timedelta

if len(sys.argv) == 3 and sys.argv[1] == '-t':
    print("Start Scraping with Keyword: " + sys.argv[2])

    portal_json_file = "source.json"
    with open(portal_json_file, 'r') as f:
        datastore = json.load(f)

    for portals in datastore['news_portal']:
        portal_name = portals['name']
        header = "\nScraping News From " + portal_name
        print(header + '\n' + '='*len(header))
        
        keyword = sys.argv[2].replace(' ', portals['keyword_concat'])
        timezone = pytz.timezone('Asia/Jakarta')
        today = datetime.now(timezone).date()
        a_week_before = today - timedelta(weeks=1)
        today_str = today.strftime('%d/%m/%Y')
        a_week_before_str = a_week_before.strftime('%d/%m/%Y')
        # link = portals['link'] + keyword
        link = portals['search_link'].replace('keyword_to_replace', keyword).replace('cdate_replace', today_str).replace('fdate_replace', a_week_before_str).replace('tdate_replace', today_str)
        print("Search news from Link: " + link)
        # exit()
        each_result_tag = portals['each_result_tag']
        each_result_class = portals['each_result_class']
        each_result_link_class = portals['each_result_link_class']
        links = news_scrapping.getLinks(link, each_result_tag, each_result_class, each_result_link_class)
        print("Found " + str(len(links)) + " News list from " + portals['name'])
        # exit(0)

        # portal = portals['name']
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
        # title_tag = portals['title_tag']
        # title_tag_class = portals['title_tag_class']
        # news_date_tag = portals['news_date_tag']
        # news_date_tag_class =  portals['news_date_tag_class']

        for link in links:
            print("LINK: " + link)
            scrap = True
            for text in exception_link_containt:
                if link.find(text) >= 0:
                    scrap = False
                    break
            print("SCRAP: " + str(scrap))
            if scrap == True:
                result = news_scrapping.getContent2(link, content_tag, content_class, paragraph_tag, paragraph_class, news_date_tag, news_date_class, datetime_regex, date_format)
                print("RESULTS: " + str(result))
            
            print("===============")
            # exit()
else:
    print('Ketik python main.py -t "keyword yang bersangkutan" ')