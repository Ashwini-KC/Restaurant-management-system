from src import Customer

import pytest


def test_add_custoemr_1():
    '''
    test 1 with normal inputs
    should pass 
    '''
    custName = 'JNM'
    custID = '5341'
    custType = 'Takeaway'

    cust_test_1 = Customer(custID,custName,custType)
    cust_test_result = {'custID': '5341', 'custName': 'JNM', 'custType': 'Takeaway'}

    assert cust_test_result == cust_test_1.add_customer()

def test_add_customer_2():
    '''
    test 2 with similar inputs as test 1 to invoke primary key constraint
    *** should always fail
    '''
    custName = 'JNM'
    custID = '534'
    custType = 'Takeaway'

    cust_test_2 = Customer(custID,custName,custType)
    cust_test_result = {'custID': '5334', 'custName': 'JNM', 'custType': 'Takeaway'}

    assert cust_test_result == cust_test_2.add_customer()



def test_add_customer_3():

    '''
    trying to create a customer without customer type
    *** should always fail
    '''
    custName = 'JNM'
    custID = '5335'
    

    cust_test_3 = Customer(custID,custName)
    cust_test_result = {'custID': '5335', 'custName': 'JNM'}

    assert cust_test_result == cust_test_3.add_customer()

def test_delete_customer_1():
    '''
    trying to delete a customer that doesnt exist in the database

    '''
    custName = 'JNM'
    custID = '53466'
    custType = 'Takeaway'





    cust_test_2 = Customer(custID,custName,custType)

    
    cust_test_result = {'custID': '533466', 'custName': 'JNM', 'custType': 'Takeaway'}
    assert cust_test_result == cust_test_2.delete_customer()


    

