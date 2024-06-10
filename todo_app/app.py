import os
import logging
import logging.config
import time
from dotenv import load_dotenv
from flask import Flask, render_template, request, redirect, url_for
from todo_app.flask_config import Config
from todo_app.data.view_model import ViewModel
from todo_app.data.items import ItemService
from loggly.handlers import HTTPSHandler
from logging import Formatter

logging.Formatter.converter = time.gmtime
logger = logging.getLogger('myLogger')

logger.info('Test log')


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config())

    # Set up logging
    logging.basicConfig(level=logging.INFO)
    app.logger.setLevel(app.config['LOG_LEVEL'])

    # Add Loggly handler if LOGGLY_TOKEN is provided
    if app.config['LOGGLY_TOKEN'] is not None:
        handler = HTTPSHandler(f'https://logs-01.loggly.com/inputs/{app.config["LOGGLY_TOKEN"]}/tag/todo-app')
        handler.setFormatter(
            Formatter("[%(asctime)s] %(levelname)s in %(module)s: %(message)s")
        )
        app.logger.addHandler(handler)


    # Set up ItemService
    mongodb_connection_string = os.getenv('MONGODB_CONNECTION_STRING')
    database_name = os.getenv('DATABASE_NAME')
    item_service = ItemService(mongodb_connection_string, database_name)

    @app.route('/')
    def index():
        app.logger.info('Fetching items for index page')
        try:
            # Fetch todo items for each status
            todo_items = item_service.fetch_todo_items('To Do')
            doing_items = item_service.fetch_todo_items('Doing')
            done_items = item_service.fetch_todo_items('Done')

            # Create ViewModel instances for each status category
            todo_view_model = ViewModel(todo_items)
            doing_view_model = ViewModel(doing_items)
            done_view_model = ViewModel(done_items)
            
            app.logger.info('Successfully fetched and categorized items for index page')
            return render_template('index.html', 
                                    todo_items=todo_view_model,
                                    doing_items=doing_view_model,
                                    done_items=done_view_model)
        except Exception as e:
            app.logger.error(f'Error fetching items for index page: {e}')
            return render_template('error.html', error=str(e))

    @app.route('/add', methods=['POST'])
    def add_new_card():
        card_name = request.form.get('item')
        app.logger.info(f'Attempting to add new card: {card_name}')
        try:
            card_id = item_service.create_todo_item('To Do', card_name)
            app.logger.info(f'Successfully added new card with ID: {card_id}')
        except Exception as e:
            app.logger.error(f'Error adding new card: {e}')
            return render_template('error.html', error=str(e))
        return redirect('/')

    @app.route('/update', methods=['POST'])
    def update_card_to_done():
        card_id_to_update = request.form.get('item')
        app.logger.info(f'Attempting to update card ID {card_id_to_update} to Done')
        try:
            item_service.update_item_status(card_id_to_update, 'Done')
            item_service.move_item_to_done_list(card_id_to_update)  # Move item to Done list
            app.logger.info(f'Successfully updated card ID {card_id_to_update} to Done')
        except Exception as e:
            app.logger.error(f'Error updating card ID {card_id_to_update}: {e}')
            return render_template('error.html', error=str(e))
        return redirect(url_for('index'))

    return app
