from pymongo import MongoClient, UpdateOne
import os

# MongoDB connection string and database name
MONGODB_CONNECTION_STRING = os.environ.get('MONGODB_CONNECTION_STRING')
DATABASE_NAME = os.environ.get('DATABASE_NAME')

# Connect to MongoDB
client = MongoClient(MONGODB_CONNECTION_STRING)
db = client[DATABASE_NAME]
collection = db['items']

_DEFAULT_ITEMS = [
    { 'id': 1, 'title': 'List saved to-do items', 'status': 'Not Started' },
    { 'id': 2, 'title': 'Allow new items to be added', 'status': 'Not Started' }
]

def get_items():
    """
    Fetches all saved items from the MongoDB collection.

    Returns:
        list: The list of saved items.
    """
    return list(collection.find({}, {'_id': 0}))

def get_item(id):
    """
    Fetches the saved item with the specified ID from MongoDB.

    Args:
        id: The ID of the item.

    Returns:
        item: The saved item, or None if no items match the specified ID.
    """
    return collection.find_one({'id': int(id)}, {'_id': 0})

def add_item(title, status='Not Started'):
    """
    Adds a new item with the specified title and status to MongoDB.

    Args:
        title: The title of the item.
        status: The status of the item (default is 'Not Started').

    Returns:
        item: The saved item.
    """
    # Find the maximum ID in the collection and increment by 1
    max_id = collection.find_one(sort=[('id', -1)])['id']
    new_id = max_id + 1 if max_id else 1
    
    item = { 'id': new_id, 'title': title, 'status': status }
    collection.insert_one(item)
    return item

def save_item(item):
    """
    Updates an existing item in MongoDB.

    Args:
        item: The item to save.
    """
    # Use item ID as the filter to update
    filter_query = {'id': item['id']}
    update_query = {'$set': {'title': item['title'], 'status': item['status']}}
    collection.update_one(filter_query, update_query)
    return item