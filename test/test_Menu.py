import pytest
from src import Menu, Item
@pytest.fixture
def item():
   item = "Naan"
   return item
@pytest.fixture  
def id():
   id = 99
   return id


def test_add_item(item):
        menu = Menu()
        menu.add_item(item)
        assert item == 'Naan'


@pytest.fixture
def item_dict():
    dict = {"itemID": 69, "itemName": "Garlic Naan",'itemPrice' :100, 'itemType' : 1}
    return dict

def test_delete_item(id):
        
        menu = Menu()
        item = Item()
        menu.delete_item(id)
        assert  id  not in item.item_details(item, item.item_dict)
   
def test_find_by_id(id):
        menu = Menu()
        menu.find_by_id(id)
        assert id in menu.get_menu()


def test_get_menu(item_dict):
        menu = Menu()
        result = menu.get_menu()
        assert result == item_dict

def test_update_item( item,item_dict):
        menu = Menu()
        result = menu.update_item(item,item_dict)
        expectedresult = {item,item_dict}

        assert result == expectedresult

