from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    def __init__(self):
        USER = 'aacuser'
        PASS = 'SNHU1234'
        HOST = 'localhost'  
        PORT = 32642
        DB = 'AAC'
        COL = 'animals'
        
        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (USER,PASS,HOST,PORT))
        self.database = self.client[DB]
        self.collection = self.database[COL]

    def create(self, data):
        if data:
            result = self.collection.insert_one(data)
            return True if result.inserted_id else False
        else:
            raise ValueError("Data to insert cannot be empty")

    def read(self, query):
        return list(self.collection.find(query))

    def update(self, query, new_data):
        result = self.collection.update_many(query, {'$set': new_data})
        return result.modified_count

    def delete(self, query):
        result = self.collection.delete_many(query)
        return result.deleted_count
