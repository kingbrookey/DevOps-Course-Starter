import os
import pytest
import requests
from todo_app.data.view_model import ViewModel
from todo_app import app
from dotenv import load_dotenv, find_dotenv
from urllib.parse import urlparse, parse_qs


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

class StubResponse:
    def __init__(self, fake_response_data):
        self.fake_response_data = fake_response_data

    def json(self):
        return self.fake_response_data

def stub(url, params={}):
    # Check if the URL starts with the expected endpoint
    if url.startswith("https://api.trello.com/1/lists"):
        # Return a response structure matching your application's expectations
        fake_response_data = [{'id': '456', 'name': 'Test card'}]
        return StubResponse(fake_response_data)

    raise Exception(f'Integration test did not expect URL "{url}"')


def test_index_page(monkeypatch, client):
    # Replace requests.get(url) with our own function
    monkeypatch.setattr(requests, 'get', stub)

    # Make a request to our app's index page
    response = client.get('/')

    assert response.status_code == 200
    assert b'Test card' in response.data  # Check for bytes content
    
def test_add_new_card(monkeypatch, client):
    # Replace trello_service.create_todo_card method with a stub
    def stub_create_todo_card(self, list_id, card_name):
        return {'id': '789', 'name': card_name}
    
    monkeypatch.setattr(app.TrelloService, 'create_todo_card', stub_create_todo_card)

    # Make a POST request to add a new card
    response = client.post('/add', data={'item': 'New Test Card'})

    assert response.status_code == 302  # Redirect
    assert response.headers['Location'] == '/'

def test_update_card_to_done(monkeypatch, client):
    # Replace trello_service.update_card_to_done method with a stub
    def stub_update_card_to_done(self, done_list_id, card_id):
        return {'id': card_id, 'name': 'Updated Test Card', 'idList': done_list_id}
    
    monkeypatch.setattr(app.TrelloService, 'update_card_to_done', stub_update_card_to_done)

    # Make a POST request to update a card to 'Done'
    response = client.post('/update', data={'item': '456'})

    assert response.status_code == 302  # Redirect
    # Print the actual value of the Location header
    print("Actual Location:", response.headers['Location'])
    
    assert response.headers['Location'].startswith('/')  # Check if it starts with the correct URL