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
