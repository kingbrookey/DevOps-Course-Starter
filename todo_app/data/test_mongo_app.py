import os
import pytest
from flask import Flask
from todo_app.data.mongo_view_model import ItemService
from todo_app.mongo_app import create_app
from dotenv import load_dotenv, find_dotenv
from unittest.mock import patch

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
    with patch('todo_app.mongo_app.create_app') as mock_create_app:
        # Create a StubItemService instance for testing
        item_service = StubItemService()

        # Mock the return value of create_app to return a Flask app instance
        mock_create_app.return_value = Flask(__name__)

        # Replace the ItemService with a stub for testing
        mock_create_app.return_value.ItemService = item_service

        # Make a request to the index page
        response = client.get('/')

        assert response.status_code == 200
        assert b'Test card' in response.data  # Check for bytes content

def test_add_new_card(client):
    with patch('todo_app.mongo_app.create_app') as mock_create_app:
        # Create a StubItemService instance for testing
        item_service = StubItemService()

        # Mock the return value of create_app to return a Flask app instance
        mock_create_app.return_value = Flask(__name__)

        # Replace the ItemService with a stub for testing
        mock_create_app.return_value.ItemService = item_service

        # Make a POST request to add a new card
        response = client.post('/add', data={'item': 'New Test Card'})

        assert response.status_code == 302  # Redirect
        assert response.headers['Location'] == '/'

def test_update_card_to_done(client):
    with patch('todo_app.mongo_app.create_app') as mock_create_app:
        # Create a StubItemService instance for testing
        item_service = StubItemService()

        # Mock the return value of create_app to return a Flask app instance
        mock_create_app.return_value = Flask(__name__)

        # Replace the ItemService with a stub for testing
        mock_create_app.return_value.ItemService = item_service

        # Make a POST request to update a card to 'Done'
        response = client.post('/update', data={'item': '456'})

        assert response.status_code == 302  # Redirect
        assert response.headers['Location'].startswith('/')  # Check if it starts with the correct URL