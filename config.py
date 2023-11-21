from pymongo import MongoClient
import pandas as pd

hostname = '172.16.100.212'
port = 27017  # Default MongoDB port
username = 'ictdata'  # If authentication is required
password = 'P@ssw0rd'  # If authentication is required

# Create a MongoClient instance
client = MongoClient(hostname, port, username=username, password=password)

db = client['sentiment']
# collection = db['news']

# df = pd.DataFrame(collection.find())
# print(df.head())
# print(collection.find())
