import config

collection = config.db['news']
for post in collection.find({'content': {'$ne': ''}}).limit(5):
    print(post['title'])