# test comments in view model.py
class ViewModel:
    def __init__(self, item_service):
        self._item_service = item_service

    @property
    def items(self):
        return self._item_service.fetch_todo_items()

    @property
    def done_items(self):
        return [item for item in self.items if item.status == 'Done']

    @property
    def to_do_items(self):
        return [item for item in self.items if item.status == 'To Do']

    @property
    def doing_items(self):
        return [item for item in self.items if item.status == 'Doing']