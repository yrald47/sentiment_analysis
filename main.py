import json
import config
import news_scrapping
import sys

keyword = sys.argv[1]

portal_json_file = "portal.json"
with open(portal_json_file, 'r') as f:
    datastore = json.load(f)
    
# print(datastore['news_portal'][0]['link'] + keyword)
for portals in datastore['news_portal']:
    link = portals['link'] + keyword
    list_news_tag = portals['list_news_tag']
    list_news_tag_class = portals['list_news_tag_class']
    news_link_class = portals['news_link_class']
    print("List news from " + portals['name'])
    news_scrapping.getLinks(link, list_news_tag, list_news_tag_class, news_link_class)