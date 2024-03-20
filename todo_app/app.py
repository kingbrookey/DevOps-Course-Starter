import os
from flask import Flask, render_template, request, redirect, url_for
from todo_app.flask_config import Config
from todo_app.data.view_model import ViewModel
from todo_app.data.items import ItemService

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config())

    # Set up ItemService
    mongodb_connection_string = os.getenv('MONGODB_CONNECTION_STRING')
    database_name = os.getenv('DATABASE_NAME')
    item_service = ItemService(mongodb_connection_string, database_name)

    @app.route('/')
    def index():
        # Fetch todo items for each status
        todo_items = item_service.fetch_todo_items('To Do')
        doing_items = item_service.fetch_todo_items('Doing')
        done_items = item_service.fetch_todo_items('Done')

        # Create ViewModel instances for each status category
        todo_view_model = ViewModel(todo_items)
        doing_view_model = ViewModel(doing_items)
        done_view_model = ViewModel(done_items)

        return render_template('index.html', 
                                todo_items=todo_view_model,
                                doing_items=doing_view_model,
                                done_items=done_view_model)
        
    @app.route('/add', methods=['POST'])
    def add_new_card():
        card_name = request.form.get('item')
        item_service.create_todo_item('To Do', card_name)
        return redirect('/')
        
    @app.route('/update', methods=['POST'])
    def update_card_to_done():
        card_id_to_update = request.form.get('item')
        item_service.update_item_status(card_id_to_update, 'Done')
        item_service.move_item_to_done_list(card_id_to_update)  # Move item to Done list
        # Redirect back to the index page after updating the item
        return redirect(url_for('index'))

    return app