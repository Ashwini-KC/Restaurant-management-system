import pytest
from src import Customer
@pytest.fixture
def custId():
    id = '2222PP'
    return id
@pytest.fixture  
def custName():
    name = 'JJ BUXTOM'
    return name
@pytest.fixture  
def custType():
    type = 'Eat-In'
    return type

@pytest.fixture
def get_data():
    data = {custId:'223LPX1',custName:'Harry Maguire',custType:'Takeaway'}
    return data
def test_customer_details(get_data):
    cust = Customer('223LPX1','Harry Maguire','Takeaway')
    cust.add_customer(cust)
    assert dict in cust.customer_details()
def test_ordered_items():
    cust = Customer()
    order = cust.add_items(101, "Pasta", 10, "Main-course")
    assert  order in cust.ordered_items()   
def test_add_customer():
    cust = Customer()
    cust1 ={'111AA','JOHN DOE','Eat-In'}
    cust.add_customer('111AA','JOHN DOE','Eat-In')
    assert  cust1 in cust.customer_details()    
def test_delete_customer():
    cust = Customer()
    cust1 ={'111AA','JOHN DOE','Eat-In'}
    cust.delete_customer('111AA','JOHN DOE','Eat-In')
    assert  cust1 not in cust.customer_details()