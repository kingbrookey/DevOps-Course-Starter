from pymongo import MongoClient
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
    return list(collection.find() or _DEFAULT_ITEMS.copy())

def get_item(id):
    """
    Fetches the saved item with the specified ID from MongoDB.

    Args:
        id: The ID of the item.

    Returns:
        item: The saved item, or None if no items match the specified ID.
    """
    return collection.find_one({'id': int(id)})

def add_item(title, status='Not Started'):
    """
    Adds a new item with the specified title and status to MongoDB.

    Args:
        title: The title of the item.
        status: The status of the item (default is 'Not Started').

    Returns:
        item: The saved item.
    """
    item = { 'id': collection.count_documents({}) + 1, 'title': title, 'status': status }
    collection.insert_one(item)
    return item

def save_item(item):
    """
    Updates an existing item in MongoDB.

    Args:
        item: The item to save.
    """
    collection.replace_one({'id': item['id']}, item)
    return item