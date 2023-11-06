import json
# import config
import news_scrapping
import sys

keyword = ''.join(sys.argv[1:])

portal_json_file = "portal.json"
with open(portal_json_file, 'r') as f:
    datastore = json.load(f)

for portals in datastore['news_portal']:
    link = portals['link'] + keyword
    print("\n" + link)
    each_result_tag = portals['each_result_tag']
    each_result_class = portals['each_result_class']
    each_result_link_class = portals['each_result_link_class']
    links = news_scrapping.getLinks(link, each_result_tag, each_result_class, each_result_link_class)
    print("News list from " + portals['name'] + " (" + str(len(links)) + ")")

    content_tag = portals['content_tag']
    content_class = portals['content_class']
    paragraph_tag = portals['paragraph_tag']
    paragraph_class = portals['paragraph_class']

    print(content_tag)
    print(content_class)
    print(paragraph_tag)
    print(paragraph_class)
    # title_tag = portals['title_tag']
    # title_tag_class = portals['title_tag_class']
    # news_date_tag = portals['news_date_tag']
    # news_date_tag_class =  portals['news_date_tag_class']

    for link in links:
        print(link)
        news_scrapping.getContent2(link, content_tag, content_class, paragraph_tag, paragraph_class)
        print("===============")