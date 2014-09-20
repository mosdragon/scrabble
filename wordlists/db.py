import pymongo
client = MongoClient("mongodb://scrabblehack:hackornot000@ds039000.mongolab.com:39000/scrabble")
db = client.test_database
collection = db['test-collection']
