from pymongo import MongoClient, errors 
from decouple import config

class DataDB:

    SAMPLE_COLL = "forex_sample"
    CALANDER_COLL = "forex_calander"
    INSTRUMENT_COLL = "forex_instruments"

    def __init__(self):
        self.client = MongoClient(config("MONGO_CONN_STR"))
        self.db = self.client.Forex

    def test_connect(self):
        print(self.db.list_collection_names())

    def add_one(self, collection, object):
        try:
            _ = self.db[collection].insert_one(object)
        except errors.InvalidOperation as error:
            print(f"add_one error: {error} ")

    def add_many(self, collection, list_object):
        try:
            _ = self.db[collection].insert_many(list_object)
        except errors.InvalidOperation as error:
            print(f"add_one error: {error} ")

    def query_distinct(self, collection, key):
        try:
            return self.db[collection].distinct(key)

        except errors.InvalidOperation as error:
            print(f"query_single error:  {error} ")
    

    def query_single(self, collection, **kwargs):
        try:
            result = self.db[collection].find_one(kwargs, {'_id':0})
            return result
        except errors.InvalidOperation as error:
            print(f"query_single error:  {error} ")


    def query_all(self, collection, **kwargs):
        try:
            data = []
            result = self.db[collection].find(kwargs, {'_id':0})
            for item in result:
                data.append(item)
            return data
        except errors.InvalidOperation as error:
            print(f"query_all: {error} ")

    def delete_many(self, collection, **kwargs):
        try:
            _ = self.db[collection].delete_many(kwargs)
        except errors.InvalidOperation as error:
            print(f"delete_many erorr: {error}")
