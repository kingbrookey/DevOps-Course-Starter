import pytest
from todo_app.data.trello_items import Item
from todo_app.data.view_model import ViewModel

def test_done_items_property():
    # Arrange: Create instances of Item with various statuses
    items = [
        Item("1", "Task 1", "Done"),
        Item("2", "Task 2", "Doing"),
        Item("3", "Task 3", "Done"),
        Item("4", "Task 4", "To Do"),
        Item("5", "Task 5", "Done"),
        Item("6", "Task 6", "To Do"),
        Item("7", "Task 7", "Doing"),
    ]
    view_model = ViewModel(items)
    
    # Act: Get the items property
    done_items = view_model.done_items
    to_do_items = view_model.to_do_items
    doing_items = view_model.doing_items
        
    # Assert: Check if the result matches the expected list of done item names
    expected_done_item_names = [item.name for item in [items[0], items[2], items[4]]]
    expected_to_do_item_names = [item.name for item in [items[3], items[5]]]
    expected_doing_item_names = [item.name for item in [items[1], items[6]]]
    actual_done_item_names = [item.name for item in done_items]
    actual_to_do_item_names = [item.name for item in to_do_items]
    actual_doing_item_names = [item.name for item in doing_items]
    
    assert actual_done_item_names == expected_done_item_names
    assert actual_to_do_item_names == expected_to_do_item_names
    assert actual_doing_item_names == expected_doing_item_names
