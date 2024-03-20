import os
import pytest
from flask import Flask
from todo_app.data.items import ItemService
from todo_app.app import create_app
from dotenv import load_dotenv, find_dotenv
from unittest.mock import patch

class StubItemService:
    def __init__(self):
        pass

    def fetch_todo_items(self, list_name):
        # Return stubbed data for fetch_todo_items
        if list_name == 'To Do':
            return [{'_id': 456, 'name': 'Test card', 'status': 'To Do'}]
        elif list_name == 'Doing':
            return [{'_id': 789, 'name': 'Test card 2', 'status': 'Doing'}]
        elif list_name == 'Done':
            return [{'_id': 123, 'name': 'Test card 3', 'status': 'Done'}]

    def create_todo_item(self, list_name, item_name):
        # Stub the create_todo_item method
        pass

    def update_item_status(self, item_id, new_status):
        # Stub the update_item_status method
        pass

@pytest.fixture
def client():
    # Use our test integration config instead of the 'real' version
    file_path = find_dotenv('.env.test')
    load_dotenv(file_path, override=True)

    # Create the new app.
    test_app = create_app()

    # Use the app to create a test_client that can be used in our tests.
    with test_app.test_client() as client:
        yield client

def test_index_page(client):
    with patch('todo_app.app.create_app') as mock_app:
        # Create a StubItemService instance for testing
        item_service = StubItemService()

        # Mock the return value of app to return a Flask app instance
        mock_app.return_value = Flask(__name__)

        # Replace the ItemService with a stub for testing
        mock_app.return_value.config['ItemService'] = item_service

        # Make a request to the index page
        response = client.get('/')

        assert response.status_code == 200
        assert b'Test card' in response.data  # Check for bytes content