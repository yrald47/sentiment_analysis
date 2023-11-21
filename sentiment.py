import config

collection = config.db['news']
for post in collection.find({'content': {'$ne': ''}}).limit(50):
    if post['keyword'] in post['content'].lower():    
        print(post['title'], post['keyword'])
