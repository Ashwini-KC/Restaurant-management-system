import pytest
from src import Customer, Order
@pytest.fixture
def custId():
    custID = '2222PP'
    return custID
@pytest.fixture  
def custName():
    custname = 'JJ BUXTOM'
    return custname
@pytest.fixture  
def custType():
    custtype = 'Eat-In'
    return custtype

@pytest.fixture
def get_data():
    data = {"custId":'223LPX12',"custName":'Harry Maguire',"custType":'Takeaway'}
    return data
def test_customer_details(get_data):
    cust = Customer('223193','Harry Maguire','Takeaway')
    cust.add_customer()
    assert get_data == cust.customer_details()   
def test_add_customer():
    cust = Customer('223193','Harry Maguire','Takeaway')
    cust1 = {"custId":'223193',"custName":'Harry Maguire',"custType":'Takeaway'}
    
    assert  cust1 == cust.add_customer()
def test_delete_customer():
    cust = Customer('223LPX1','Harry Maguire','Takeaway')
    cust1 = {"custId":'223LPX1',"custName":'Harry Maguire',"custType":'Takeaway'}
    cust.delete_customer()
    assert  cust1 == cust.customer_details()