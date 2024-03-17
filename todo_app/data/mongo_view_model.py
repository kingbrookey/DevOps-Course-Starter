from .mongo_items import ItemService, Item  # Import both ItemService and Item from mongo_items.py

class ViewModel:
    def __init__(self, item_service):
        self._item_service = item_service
        self._items = None  # Cache fetched items

    @property
    def items(self):
        if self._items is None:  # Fetch items only once
            self._items = self._item_service.fetch_todo_items()
        return self._items

    @property
    def done_items(self):
        return [item for item in self.items if item.status == 'Done']

    @property
    def to_do_items(self):
        return [item for item in self.items if item.status == 'To Do']

    @property
    def doing_items(self):
        return [item for item in self.items if item.status == 'Doing']