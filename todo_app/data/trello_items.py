import requests

class Item:
    def __init__(self, api_key, api_token):
        self.api_key = api_key
        self.api_token = api_token

    def fetch_todo_items(self, list_id):
        url = f"https://api.trello.com/1/lists/{list_id}/cards?key={self.api_key}&token={self.api_token}"
        response = requests.get(url)
        data = response.json()
    
        todo_items = []
        for item in data:
            todo_items.append(item['name'])
        
        return todo_items

    def create_todo_card(self, to_do_list_id, card_name):
        url = f"https://api.trello.com/1/cards?key={self.api_key}&token={self.api_token}"
        params = {
            'idList': to_do_list_id,
            'name': card_name,
        }
        response = requests.post(url, params=params)
        data = response.json()
    
        return data.get('id')

    def find_list_id_by_name(self, board_id, name):
        url = f"https://api.trello.com/1/boards/{board_id}/lists?key={self.api_key}&token={self.api_token}"
        response = requests.get(url)
        data = response.json()
    
        for item in data:
            if item['name'] == name:
                return item['id']
        return None

    def find_card_id_by_name(self, list_id, card_name):
        url = f"https://api.trello.com/1/lists/{list_id}/cards?key={self.api_key}&token={self.api_token}"
        response = requests.get(url)
        data = response.json()
    
        for item in data:
            if item['name'] == card_name:
                print(card_name)
                return item['id']
        return None

    def update_card_to_done(self, done_list_id, card_id):
        # Trello API endpoint for updating a card's properties, such as moving it to a different list
        url = f"https://api.trello.com/1/cards/{card_id}"

        params = {
            'key': self.api_key,       
            'token': self.api_token,   
            'idList': done_list_id 
        }
    
        try:
            # Perform the API call using PUT method to update the card
            response = requests.put(url, params=params)

            return True
    
        except requests.exceptions.RequestException as e:
            # Handle exceptions that may occur during the API call, such as network errors
            print("Error occurred during API call:", e)
            return False