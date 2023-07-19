import requests
import os
from flask import Flask, render_template, request, redirect
from todo_app.flask_config import Config
from todo_app.data.session_items import get_items, get_item, add_item
from todo_app.data.trello_items import fetch_todo_items, find_list_id_by_name, create_todo_card

    
app = Flask(__name__)
app.config.from_object(Config())

# Update the function that handles the GET request for fetching todo items
@app.route('/')
def index():
    # Get Board ID, API key and API token from env file
    list_id = os.getenv('TO_DO_LIST_ID')
    api_key = os.getenv('API_KEY')
    api_token = os.getenv('API_TOKEN')
    # Use the fetch_todo_items function from trello_items module
    todo_items = fetch_todo_items(list_id, api_key, api_token)
    
    return render_template('index.html', items=todo_items)



@app.route('/add', methods=['GET', 'POST'])
def add_new_card():
    # Get Board ID, API key and API token from env file
    list_id = os.getenv('TO_DO_LIST_ID')
    api_key = os.getenv('API_KEY')
    api_token = os.getenv('API_TOKEN')
    card_name = request.form.get('item')
    updated_items = add_item(card_name)
    to_do_list_items = fetch_todo_items(list_id, api_key, api_token)        
  # Call the function to create a new card
    card_id = create_todo_card(list_id, card_name, api_key, api_token)
    
    return redirect('/')
    
if __name__ == '__main__':
   app.run()
