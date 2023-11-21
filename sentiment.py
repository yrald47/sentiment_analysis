import config

collection = config.db['news']
for post in collection.find({'content': {'$ne': ''}}).limit(50):
    if post['keyword'] in post['content'].lower():    
        print(post['title'], post['keyword'])

print(collection.find_one({'title':'direktur bank mandiri blak-blakan alasan borong saham rp 2 m'}))
print(type(collection.find_one({'title':'direktur bank mandiri blak-blakan alasan borong saham rp 2 m'})))