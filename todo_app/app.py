import requests
import os
from flask import Flask, render_template, request, redirect
from todo_app.flask_config import Config
from todo_app.data.session_items import get_items, get_item, add_item
from todo_app.data.trello_items import fetch_todo_items
    
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
    
if __name__ == '__main__':
    app.run()
