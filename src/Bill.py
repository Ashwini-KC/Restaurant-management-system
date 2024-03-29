from random_id import *
import string
from util import create_db_connection
class Bill:
    billID = random_id(length=8,character_set=string.digits)
    billed_item_list = []
    bill_Total = 0


    def __init__(self, CustID):
        self.CustID = CustID
        
        
    def get_custID(self):
        return self.CustID

    def set_custID(self,CustID):
        self.CustID = CustID




    def calculate_Bill(self):
        try:
            conn = create_db_connection()
            with conn.cursor() as cursor:
                cursor.execute(f"select o.orderID, o.itemID, m.itemName, o.quantity, m.itemPrice, o.quantity * m.itemPrice as Price from smqa.orders as o, smqa.menu as m where o.itemID = m.itemID and custID =\"{self.CustID}\";")
                for i in cursor:
                    self.billed_item_list.append(i)
                    self.bill_Total += i['Price']
                conn.commit()
                conn.close()
                
            return self.billed_item_list,self.bill_Total
                

        except Exception as e:
            return e
        
        '''
        calculates bill based on ordered items
        '''
        

    def generate_Bill(self,empID):
        try:
            conn = create_db_connection()
            with conn.cursor() as cursor:
                cursor.execute(f"insert into bill values (\"{self.billID}\",\"{empID}\",\"{self.CustID}\",{self.bill_Total});")
                conn.commit()
                conn.close()
            
            
            return {'billID': self.billID,'EmpID':empID,'CustID':self.CustID,'total':self.bill_Total}

        except Exception as e:
            return e
