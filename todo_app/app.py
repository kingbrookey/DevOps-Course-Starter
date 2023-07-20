import requests
import os
from flask import Flask, render_template, request, redirect, url_for
from todo_app.flask_config import Config
from todo_app.data.session_items import get_items, get_item, add_item
from todo_app.data.trello_items import fetch_todo_items, find_list_id_by_name, create_todo_card, find_card_id_by_name, update_card_to_done

    
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
    # Get List ID, API key and API token from env file
    list_id = os.getenv('TO_DO_LIST_ID')
    api_key = os.getenv('API_KEY')
    api_token = os.getenv('API_TOKEN')
    card_name = request.form.get('item')
    updated_items = add_item(card_name)
    to_do_list_items = fetch_todo_items(list_id, api_key, api_token)        
  # Call the function to create a new card
    card_id = create_todo_card(list_id, card_name, api_key, api_token)
    
    return redirect('/')


@app.route('/update', methods=['GET', 'POST'])
def updates_card_to_done():
    # Get Board ID, API key and API token from env file
    to_do_list_id = os.getenv('TO_DO_LIST_ID') 
    done_list_id = os.getenv('DONE_LIST_ID')
    #card_id = os.getenv('CARD_ID')
    #board_id = os.getenv('BOARD_ID')
    api_key = os.getenv('API_KEY')
    api_token = os.getenv('API_TOKEN')
    #name = "Done"
    card_name_to_update = request.form.get('card_name')
    #done_list_id = find_list_id_by_name(board_id, name, api_key, api_token)
    card_id = find_card_id_by_name(to_do_list_id, card_name_to_update, api_key, api_token)
    print (card_id)
            
  # Call function to change list ID of card from To Do to Done
    update_new_card = update_card_to_done(done_list_id, card_id, api_key, api_token)
    
    #return redirect('/')
    to_do_list_items = fetch_todo_items(to_do_list_id, api_key, api_token)
    print (to_do_list_items)
    #return render_template('index.html', items=to_do_list_items)
    #return redirect('/')
  
    # Redirect back to the index page after completing the item
    return redirect(url_for('index')) 

  
if __name__ == '__main__':
   app.run()
