import pytest
from src import Order, Customer, Employee
'''
'''


def  ordered_items_list():

        item = "17"

        customer = customer.customer2

        quantity = 4

def test_place_order_items(ordered_items_list):
    
    dict = {18,"employee2", "customer3",4}
    
    assert dict == ordered_items_list

    ord=Order()
    order1= ord.add_items(100,"employee1","customer1",8)
    assert order1 == ord.ordered_items_list

def test_add_items():

        ord = Order()

        customer1 = Customer('TestID', 'Test Name', 'VIP')

        employee1 = Employee('TestEmpID', 'Test Employee', 'Chef')

        # ord1 = {"17",employee1,customer2,2}

        order_list = ord.add_items('17', employee1, customer1, 10)

        assert len(order_list) is 1