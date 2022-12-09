from src import Bill, Customer, Employee, Order



def test_calculate_Bill():
    customer1 = Customer('1234','jitter','takeaway')
    customer1.add_customer()
    emp1 = Employee()
    emp1.add_employee("211","vidyashree","2")

    orderCust1 = Order()
    #ßorderCust1.add_items("97","211",customer1,5)
    #orderCust1.add_items("99","211",customer1,7)
    #orderCust1.place_order_items()
    
    orderCheck = ([{'orderID': 'drKgZCX', 'itemID': '99', 'itemName': 'Arun Strawberry Icecream', 'quantity': 7, 'itemPrice': 91, 'Price': 637}, {'orderID': 'TIysFnM', 'itemID': '97', 'itemName': 'Mai Tai', 'quantity': 5, 'itemPrice': 26, 'Price': 130}], 767)
    bil1 = Bill("1234")
    assert orderCheck == bil1.calculate_Bill()



   
    
   
    





















