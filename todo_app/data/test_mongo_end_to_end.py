import pytest
from todo_app.data.mongo_view_model import ItemService
from todo_app import app
from dotenv import load_dotenv, find_dotenv
from pymongo import MongoClient

@pytest.fixture
def client():
    # Use our test integration config instead of the 'real' version
    file_path = find_dotenv('.env.test')
    load_dotenv(file_path, override=True)

    # Create a temporary MongoDB database for testing
    with MongoClient("mongodb://localhost:27017") as mongo_client:
        # Define the test database name
        test_db_name = 'test_todo_app'

        # Get the test database reference
        test_db = mongo_client[test_db_name]

        # Set the ItemService database name to the test database
        app.ItemService = ItemService(database_name=test_db_name)

        # Use the app to create a test_client that can be used in our tests.
        test_app = app.create_app()

        # Yield the test client
        with test_app.test_client() as client:
            yield client

        # Drop the test database at the end of the test
        test_db.drop_collection('items')  # Drop only the collection
    

def test_end_to_end(client):
    # Add a new item
    response = client.post('/add', data={'item': 'New Test Item'})
    assert response.status_code == 302  # Ensure redirect
    assert response.headers['Location'] == '/'  # Ensure redirect to home page

    # Verify that the new item appears in the "To Do" list
    response = client.get('/')
    assert b'New Test Item' in response.data  # Ensure item is displayed

    # Update the status of the item
    response = client.post('/update', data={'item': 'New Test Item ID'})
    assert response.status_code == 302  # Ensure redirect
    assert response.headers['Location'] == '/'  # Ensure redirect to home page

    # Verify that the item's status has been updated correctly
    response = client.get('/')
    assert b'New Test Item' not in response.data  # Ensure item no longer in "To Do" list
    assert b'New Test Item' in response.data  # Ensure item in "Done" list (or whichever list it was moved to)
