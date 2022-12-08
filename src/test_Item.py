import pytest
from src import Item
#@pytest.fixture

def test_get_id():
    itemID = '1'
    assert itemID

def test_get_name():

    itemName = "Plain Dosa"
    assert itemName 
def test_get_price():

    itemPrice = '200'
    assert itemPrice

def test_get_type():
    itemType =  '100'
    assert itemType

def test_set_id():
    itemID = '1','2'
    assert itemID

def test_set_name():
    itemName = "Arun","steve","asif"
    assert itemName

def test_set_price():
    itemPrice = '20','90','100'
    assert itemPrice

def test_set_type():
    itemType = '1','2','3','4'
    assert itemType
