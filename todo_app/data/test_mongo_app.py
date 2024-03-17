import os
import pytest
from flask import session
from todo_app.data.mongo_view_model import ItemService, ViewModel
from todo_app.mongo_app import app
from dotenv import load_dotenv, find_dotenv
from pymongo import MongoClient

@pytest.fixture
def client():
    # Use our test integration config instead of the 'real' version
    file_path = find_dotenv('.env.test')
    load_dotenv(file_path, override=True)

    # Create the new app.
    test_app = app.create_app()

    # Use the app to create a test_client that can be used in our tests.
    with test_app.test_client() as client:
        yield client


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



    def update_item_status(self, item_id, new_status):
        # Stub the update_item_status method
        pass

def test_index_page(client):
    # Replace the ItemService with a stub for testing
    app.ItemService = StubItemService()

    # Make a request to the index page
    response = client.get('/')

    assert response.status_code == 200
    assert b'Test card' in response.data  # Check for bytes content

def test_add_new_card(client):
    # Replace the ItemService with a stub for testing
    app.ItemService = StubItemService()

    # Make a POST request to add a new card
    response = client.post('/add', data={'item': 'New Test Card'})

    assert response.status_code == 302  # Redirect
    assert response.headers['Location'] == '/'

def test_update_card_to_done(client):
    # Replace the ItemService with a stub for testing
    app.ItemService = StubItemService()

    # Make a POST request to update a card to 'Done'
    response = client.post('/update', data={'item': '456'})

    assert response.status_code == 302  # Redirect
    assert response.headers['Location'].startswith('/')  # Check if it starts with the correct URL
