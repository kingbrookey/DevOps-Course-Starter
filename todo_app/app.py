import os
from flask import Flask, render_template, request, redirect, url_for
from todo_app.flask_config import Config
from todo_app.data.session_items import get_items, get_item, add_item
from todo_app.data.trello_items import Item

app = Flask(__name__)
app.config.from_object(Config())

# Create an instance of the Item class with the API key and API token
api_key = os.getenv('API_KEY')
api_token = os.getenv('API_TOKEN')
item = Item(api_key, api_token)

# Update the function that handles the GET request for fetching todo items
@app.route('/')
def index():
    # Get Board ID and List ID from env file
    list_id = os.getenv('TO_DO_LIST_ID')
    # Use the Item class method to fetch todo items
    todo_items = item.fetch_todo_items(list_id)
    
    return render_template('index.html', items=todo_items)

@app.route('/add', methods=['POST'])
def add_new_card():
    # Get List ID from env file
    list_id = os.getenv('TO_DO_LIST_ID')
    card_name = request.form.get('item')
    updated_items = add_item(card_name)
    to_do_list_items = item.fetch_todo_items(list_id)        
    # Call the Item class method to create a new card
    card_id = item.create_todo_card(list_id, card_name)
    
    return redirect('/')

@app.route('/update', methods=['POST'])
def update_card_to_done():
    # Get List IDs from env file
    to_do_list_id = os.getenv('TO_DO_LIST_ID')
    done_list_id = os.getenv('DONE_LIST_ID')
    card_name_to_update = request.form.get('item')
    # Use the Item class methods to find card ID and update the card
    card_id = item.find_card_id_by_name(to_do_list_id, card_name_to_update)
    update_new_card = item.update_card_to_done(done_list_id, card_id)

    # Redirect back to the index page after completing the item
    return redirect(url_for('index')) 

if __name__ == '__main__':
   app.run()