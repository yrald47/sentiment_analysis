import json
import config
import news_scrapping
import sys

keyword = sys.argv[1]

portal_json_file = "source.json"
with open(portal_json_file, 'r') as f:
    datastore = json.load(f)
    
for portals in datastore['news_portal']:
    link = portals['link'] + keyword
    print("\n" + link)
    list_news_tag = portals['list_news_tag']
    list_news_tag_class = portals['list_news_tag_class']
    news_link_class = portals['news_link_class']
    print("News list from " + portals['name'])
    links = news_scrapping.getLinks(link, list_news_tag, list_news_tag_class, news_link_class)
    print(len(links))
    
    content_class = portals['content-class']
    title_tag = portals['title_tag']
    title_tag_class = portals['title_tag_class']
    news_date_tag = portals['news_date_tag']
    news_date_tag_class =  portals['news_date_tag_class']
    content_tag = portals['content_tag']
    for link in links:
        print(link)
        news_scrapping.getContent(link, content_tag, content_class, title_tag, title_tag_class, news_date_tag, news_date_tag_class)