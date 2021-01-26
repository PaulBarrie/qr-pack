from pymongo import MongoClient
from os import environ
import urllib.parse

class DB:
    def __init__(self, client, db):
        self.address = environ['MONGO_ADDRESS']
        self.port = environ["MONGO_PORT"]
        self.db_name = environ["MONGO_DB"]
        self.username = environ["MONGO_USER"]
        self.password = environ["MONGO_PASSWORD"]
        self.client = client
        self.db = db

    def connect(self):
        username = urllib.parse.quote_plus(self.username)
        password = urllib.parse.quote_plus(self.password)
        self.client = MongoClient('mongodb://%s:%s@%s' % (username, password, self.address))
        self.db = self.client[self.db_name]
    
    def collection(self, collection_name):
        return self.db[collection_name]