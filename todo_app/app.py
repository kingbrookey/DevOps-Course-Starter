from flask import Flask
from flask import render_template, request, redirect
from todo_app.flask_config import Config
from todo_app.data.session_items import get_items
from todo_app.data.session_items import get_item
from todo_app.data.session_items import add_item

app = Flask(__name__)
app.config.from_object(Config())


@app.route('/')
def index():
    items = get_items()
    return render_template('index.html', items=items)


@app.route('/add', methods=['POST'])
def add():
    item = request.form.get('item')
    items = add_item(item)
    return redirect('/')

if __name__ == '__main__':
    app.run()
