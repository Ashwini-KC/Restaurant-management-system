from util import create_db_connection, generate_insert_update_query
from random_id import *
class Table:
    def __init__(self,EmpId=None,customerId=None):
        self.EmpID = EmpId
        self.customerId= customerId


    def set_EmpID(self,id):
        self.EmpID = id

    def get_EmpID(self):
        return self.EmpID

    def get_customerId(self):
        return self.customerId

    def set_customerId(self,id):
        self.customerId = id


    def table_detail_list(self):
        return self.tableList 


    def table_details(self):
        '''
        0 SIGNIFIES THE TABLES WHICH ARE NOT BOOKED
        '''
        
        try:
            conn = create_db_connection()
            with conn.cursor() as cursor:
                cursor.execute("select tableID,EmpID from tables where available =0; ")

                for i in cursor:
                    self.tableList.append(i)
                
                conn.commit()
                conn.close()
            return self.tableList
        except Exception as e:
            return e
                    


    def add_table(self):
        try:
            conn = create_db_connection()
            with conn.cursor() as cursor:
                cursor.execute(generate_insert_update_query(self.__dict__, "tables", "insert"))
                conn.commit()
                conn.close()
            self.table_details()
            return self.tableList
        except Exception as e:
            return e
        

    def change_availability_status(self, tableID, available, customerId=None):
        flag = 0
        if available:
            flag = 1


        try:
            conn = create_db_connection()
            with conn.cursor() as cursor:
                cursor.execute(f"update tables set available = {flag}, custID =\"{customerId}\" where tableID = \"{tableID}\";")
                conn.commit()
                conn.close()
            

            self.table_details()
            return self.table_detail_list
        except Exception as e:
            return e



