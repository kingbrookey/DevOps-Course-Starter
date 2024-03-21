import os
import pytest
import mongomock
from flask import Flask
from bson import ObjectId
from todo_app.data.items import ItemService
from todo_app.app import create_app
from dotenv import load_dotenv, find_dotenv
from unittest.mock import patch



@pytest.fixture
def client():
    # Use our test integration config instead of the 'real' version
    file_path = find_dotenv('.env.test')
    load_dotenv(file_path, override=True)

    with mongomock.patch(servers=(('fakemongo.com', 27017),)):
        test_app = create_app()
        with test_app.test_client() as client:
            yield client

def test_index_page(client):
        # Set up ItemService
        mongodb_connection_string = os.getenv('MONGODB_CONNECTION_STRING')
        database_name = os.getenv('DATABASE_NAME')
        item_service = ItemService(mongodb_connection_string, database_name)
        item_service.create_todo_item('To Do','Test card')

        # Make a request to the index page
        response = client.get('/')

        assert response.status_code == 200
        assert b'Test card' in response.data  # Check for bytes content