import json
import config
import news_scrapping

portal_json_file = "portal.json"
with open(portal_json_file, 'r') as f:
    datastore = json.load(f)
    
print(datastore['Kompas'])