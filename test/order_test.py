from src import Order

def test_add_items1():
    order = Order()
    actual_addItem = order.add_items('100','employee1','customer1','8')
    Expected_addItem = {'orderID':'','itemID':'100','empID':'employee1' ,'custID': 'customer1', 'quantity':'8'}
    actual_addItem == Expected_addItem


def test_add_items2():
    order = Order()
    actual_addItem = order.add_items('101','employee2','customer3','2')
    Expected_addItem = {'orderID':'','itemID':'101','empID':'employee2','custID':'customer2', 'quantity':'2'}
    actual_addItem == Expected_addItem 
    #limitation random id generator unable to test Order ID of the Test add function
    


        