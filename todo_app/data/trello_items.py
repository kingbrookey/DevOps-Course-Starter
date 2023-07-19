#trello_items.py

import requests

def fetch_todo_items(list_id, api_key, api_token):
    url = f"https://api.trello.com/1/lists/{list_id}/cards?key={api_key}&token={api_token}"
    response = requests.get(url)
    data = response.json()
    
    todo_items = []
    for item in data:
        todo_items.append(item['name'])
        
    return todo_items

def create_todo_card(to_do_list_id, card_name, api_key, api_token):
    url = f"https://api.trello.com/1/cards?key={api_key}&token={api_token}"
    params = {
        'idList': to_do_list_id,
        'name': card_name,
        }
    response = requests.post(url, params=params)
    data = response.json()
    
    return data.get('id')


def find_list_id_by_name(name, data):
    for item in data:
        if item['name'] == name:
            return item['id']
    return None
