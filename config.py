from pymongo import MongoClient

hostname = ''
port = 27017  # Default MongoDB port
username = ''  # If authentication is required
password = ''  # If authentication is required

# Create a MongoClient instance
client = MongoClient(hostname, port, username=username, password=password)

db = client['your_db']
collection = db['your_collection']

'''
{
    id: "",
    title: "",
    link: "",
    content: "",
    negative_score: "",
    neutral_score: "",
    positive_score: "",
    compound_score: ""
}
'''