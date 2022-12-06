from random_id import *
import string
from util import create_db_connection,generate_insert_update_query,generate_select_delete
class Order:
    ordered_items_list = []

    def __init__(self):
        pass

    def place_order_items(self):

        '''
        allows the customer to select things from menu and lets them order
        '''
        try:
            conn =create_db_connection()
            with conn.cursor() as cursor:
                for i in self.ordered_items_list:
                    cursor.execute(f"insert into orders values(\"{i['orderID']}\",\"{i['itemID']}\",\"{i['custID']}\",\"{i['empID']}\",{i['quantity']});")
                
                conn.commit()
                conn.close()
            return self.ordered_items_list
        except Exception as e:
            return e
                


    def add_items(self,item,emp,customer,quantity):
        orderID = random_id(length=7)
        item_details={
            'orderID':orderID,
            'itemID':item,
            'custID':customer.custId,
            'empID':emp.EmpID,
            'quantity':quantity
        }

        self.ordered_items_list.append(item_details)

        return self.ordered_items_list