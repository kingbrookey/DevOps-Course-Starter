import os
from flask import Flask, render_template, request, redirect, url_for
from todo_app.flask_config import Config
from todo_app.data.session_items import get_items, get_item, add_item
from todo_app.data.trello_items import TrelloService

app = Flask(__name__)
app.config.from_object(Config())

# Create an instance of the TrelloService class with the API key and API token
api_key = os.getenv('API_KEY')
api_token = os.getenv('API_TOKEN')
trello_service = TrelloService(api_key, api_token)

# Update the function that handles the GET request for fetching todo items
@app.route('/')
def index():
    # Get Board ID and List ID from env file
    list_id = os.getenv('TO_DO_LIST_ID')
    # Use the TrelloService class method to fetch todo items
    todo_items = trello_service.fetch_todo_items(list_id)
    
    return render_template('index.html', items=todo_items)

@app.route('/add', methods=['POST'])
def add_new_card():
    # Get List ID from env file
    list_id = os.getenv('TO_DO_LIST_ID')
    card_name = request.form.get('item')
    updated_items = add_item(card_name)
    # Call the TrelloService class method to create a new card
    card_id = trello_service.create_todo_card(list_id, card_name)
    
    return redirect('/')

@app.route('/update', methods=['POST'])
def update_card_to_done():
    # Get List IDs from env file
    to_do_list_id = os.getenv('TO_DO_LIST_ID')
    done_list_id = os.getenv('DONE_LIST_ID')
    card_id_to_update = request.form.get('item')  # Get the item ID from the form submission
    # Use the TrelloService class method to update the card
    update_new_card = trello_service.update_card_to_done(done_list_id, card_id_to_update)

    # Redirect back to the index page after updating the item
    return redirect(url_for('index')) 

if __name__ == '__main__':
   app.run()