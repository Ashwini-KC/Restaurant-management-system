from util import create_db_connection,generate_insert_update_query,generate_select_delete

class Customer:
    def __init__(self,custId,custName,custType): 
        self.custId=custId
        self.custName=custName
        self.custType=custType    

    def get_custId(self):
        return self.custId
    
    def set_custId(self,id):
        self.custId = id

    def get_custName(self):
        return self.custName

    def set_custName(self,name):
        self.custName = name

    def get_custType(self):
        return self.custType

    def set_custType(self,type):
        self.custType = type

    
    def customer_details(self):
        '''
        show customerdetails when custID is passed
        '''
        return self.__dict__

    def ordered_items(self):
        '''
        show all order details when only customerID Is passed
        '''
        itemlist =[]
        try:
            connection = create_db_connection()
            with connection.cursor() as cursor:
                cursor.execute(f"select * from smqa.order where custID = \"{self.custId}\"")
                for i in cursor:
                    itemlist.append(i)

                connection.commit()
                connection.close()
                
            return itemlist
        except Exception as e:
            return KeyError

    
    def add_customer(self):
        
        
        try:
            conn = create_db_connection()
            with conn.cursor() as cursor:
                cursor.execute(f"insert into customer values(\"{self.custId}\",\"{self.custName}\",\"{self.custType}\")")
                conn.commit()
                conn.close()
            return self.customer_details()

        except Exception as e:
            return e
        
        
    
    def delete_customer(self):
        '''
        same as before
        '''
        try:
            conn = create_db_connection()
            with conn.cursor() as cursor:
                cursor.execute(f"delete from customer where custID = \"{self.custId}\"")
                conn.commit()
                conn.close()
            
        except Exception as e:
            return e
      
