from pymongo import MongoClient
from bson import ObjectId
import os

class Item:
    def __init__(self, id, name, status='To Do'):
        self.id = id
        self.name = name
        self.status = status

class ItemService:
    def __init__(self, mongodb_connection_string, database_name):
        self.mongodb_connection_string = mongodb_connection_string
        self.database_name = database_name

    def _connect_to_mongodb(self):
        client = MongoClient(self.mongodb_connection_string)
        return client[self.database_name]

    def get_list_id(self, list_name):
        db = self._connect_to_mongodb()
        collection = db['items']
        list_doc = collection.find_one({'list': list_name})
        if list_doc:
            return list_doc['list_id']
        else:
            return None

    def fetch_todo_items(self, list_name):
        db = self._connect_to_mongodb()
        collection = db['items']
        todo_items = collection.find({'list': list_name})
        return [Item(item['id'], item['name'], item['status']) for item in todo_items]

    def create_todo_item(self, list_name, item_name):
        db = self._connect_to_mongodb()
        collection = db['items']
        item = {
            'id': collection.count_documents({}) + 1,
            'name': item_name,
            'status': 'To Do',
            'list': list_name
        }
        collection.insert_one(item)
        return item['id']

    def update_item_status(self, item_id, new_status):
        db = self._connect_to_mongodb()
        collection = db['items']
        result = collection.update_one({'_id': ObjectId(item_id)}, {'$set': {'status': new_status}})


