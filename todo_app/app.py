import requests
import os
from flask import Flask, render_template, request, redirect
from todo_app.flask_config import Config
from todo_app.data.session_items import get_items, get_item, add_item
from todo_app.data.trello_items import fetch_todo_items, find_list_id_by_name, create_todo_card

    
app = Flask(__name__)
app.config.from_object(Config())

'''''
#comment out section using session_items
@app.route('/')
def index():
    items = get_items()
    return render_template('index.html', items=items)


@app.route('/add', methods=['POST'])
def add():
    item = request.form.get('item')
    items = add_item(item)
    return redirect('/')

'''

# Update the function that handles the GET request for fetching todo items
@app.route('/')
def index():
    # Get Board ID, API key and API token from env file
    board_id = os.getenv('BOARD_ID')
    api_key = os.getenv('API_KEY')
    api_token = os.getenv('API_TOKEN')
    

    # Use the fetch_todo_items function from trello_items module
    todo_items = fetch_todo_items(board_id, api_key, api_token)
    
    return render_template('index.html', items=todo_items)



@app.route('/add')
def add_new_card():
    # Get Board ID, API key and API token from env file
    board_id = os.getenv('BOARD_ID')
    api_key = os.getenv('API_KEY')
    api_token = os.getenv('API_TOKEN')
    board_data = fetch_todo_items(board_id, api_key, api_token)
    list_id = find_list_id_by_name("To Do",board_data)
    card_name = "To Do"
        
  # Call the function to create a new card
    card_id = create_todo_card(board_id, list_id, card_name, api_key, api_token)
    
    return render_template('index.html', items=board_data)

if __name__ == '__main__':
   app.run()
