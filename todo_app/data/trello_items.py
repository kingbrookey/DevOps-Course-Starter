# trello_items.py

import requests

def fetch_todo_items(board_id, api_key, api_token):
    url = f"https://api.trello.com/1/boards/{board_id}/lists?cards=open&key={api_key}&token={api_token}"
    response = requests.get(url)
    data = response.json()
    
    #todo_items = []
    trello_to_do = []
    for item in data:
        trello_to_do.append({'id': item['id'], 'name': item['name']})
        print(trello_to_do)
        #cards = item["cards"]
        #todo_items.extend(cards)
    
    return trello_to_do


def create_todo_card(board_id, list_id, card_name, api_key, api_token):
    url = f"https://api.trello.com/1/cards?key={api_key}&token={api_token}"
    params = {
        'idList': list_id,
        'name': card_name,
        'idBoard': board_id
    }
    response = requests.post(url, params=params)
    data = response.json()
    
    return data.get('id')  # Return the ID of the created card

def find_list_id_by_name(name, data):
    for item in data:
        if item['name'] == name:
            return item['id']
    return None

