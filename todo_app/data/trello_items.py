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


def find_list_id_by_name(board_id, name, api_key, api_token):
    url = f"https://api.trello.com/1/boards/{board_id}/lists?key={api_key}&token={api_token}"
    response = requests.get(url)
    data = response.json()
    
    for item in data:
        if item['name'] == name:
            return item['id']
    return None

def find_card_id_by_name(list_id, card_name, api_key, api_token):
    url = f"https://api.trello.com/1/lists/{list_id}/cards?key={api_key}&token={api_token}"
    response = requests.get(url)
    data = response.json()
    
    for item in data:
        if item['name'] == card_name:
            print (card_name)
            return item['id']
    return None
'''''''''''
def update_card_to_done(done_list_id, card_id, api_key, api_token):
    url = f"https://api.trello.com/1/cards/{card_id}?key={api_key}&token={api_token}"
    params = {
        'idList': done_list_id,
    }
    response = requests.post(url, params=params)
    #data = response.json()
    
    return
    #return data.get('id')
'''''''''''

def update_card_to_done(done_list_id, card_id, api_key, api_token):
    # Trello API endpoint for updating a card's properties, such as moving it to a different list
    url = furl = f"https://api.trello.com/1/cards/{card_id}?key={api_key}&token={api_token}"

    params = {
        'key': api_key,       
        'token': api_token,   
        'idList': done_list_id 
    }
    
    try:
        # Perform the API call using POST method to update the card
        response = requests.post(url, params=params)
        #response.raise_for_status()  # Raise an exception if the API call was not successful
        
        # If the API call was successful, you can handle the response if needed
        # For example, you can return the updated card ID or any other relevant information
        # data = response.json()
        # return data.get('id')
        
        # If you don't need any specific response, you can simply return True to indicate success
        return True
    
    except requests.exceptions.RequestException as e:
        # Handle exceptions that may occur during the API call, such as network errors
        print("Error occurred during API call:", e)
        return False