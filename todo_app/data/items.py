from pymongo import MongoClient

class Item:
    def __init__(self, id, name, status='To Do'):
        self.id = id
        self.name = name
        self.status = status

class ItemService:
    def __init__(self, mongodb_connection_string, database_name):
        self.client = MongoClient(mongodb_connection_string)
        self.db = self.client[database_name]
        self.collection = self.db['items']

    def fetch_todo_items(self, list_name):
        todo_items = self.collection.find({'list': list_name})
        return [Item(item['id'], item['name'], item['status']) for item in todo_items]

    def create_todo_item(self, list_name, item_name):
        item_count = self.collection.count_documents({})
        item = {
            'id': item_count + 1,
            'name': item_name,
            'status': 'To Do',
            'list': list_name
        }
        self.collection.insert_one(item)
        return item['id']

    def update_item_status(self, item_id, new_status):
        result = self.collection.update_one({'id': item_id}, {'$set': {'status': new_status}})
        return result.modified_count > 0

    def move_item_to_done_list(self, item_id):
        result = self.collection.update_one({'id': item_id}, {'$set': {'list': 'Done'}})
        return result.modified_count > 0

    def get_list_id(self, list_name):
        list_doc = self.collection.find_one({'list': list_name}, {'_id': 0, 'list_id': 1})
        return list_doc['list_id'] if list_doc else None