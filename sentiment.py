import config
import pandas as pd
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory# create stemmer
factory = StemmerFactory()
stemmer = factory.create_stemmer()# stemming process

collection = config.db['news']
for post in collection.find({'content': {'$ne': ''}}).limit(50):
    if post['keyword'] in post['content'].lower():    
        print(post['title'], post['keyword'])

doc = collection.find_one({'title':'direktur bank mandiri blak-blakan alasan borong saham rp 2 m'})
output   = stemmer.stem(doc['content'])
token = output.split()
df = pd.DataFrame(token)
print(df[0].value_counts().to_frame())
#print(df)

