'''
what is the meaning of life?
--> Nothing really... You're lif is a JOKE. 
this is meaningless
--> This is meaningless indeed. But to get this useless degree we need "THIS"
'''
'''
better code segregation required
--> Done
'''
from util import create_db_connection, generate_insert_update_query

class Employee:
    def __init__(self, EmpID, EmpName, EmpType=None): 
        self.EmpID = EmpID
        self.EmpName = EmpName
        self.EmpType = EmpType

    def employee_details(self):

        '''Returns a dictionary of the employee object.
        '''
        return self.__dict__
    
    def add_employee(self):
        '''Adds news employee detial to the employee table.
        '''
        try:
            connection = create_db_connection()
            with connection.cursor() as cursor:
                cursor.execute(f"INSERT INTO employee VALUES ({self.EmpID}, \"{self.EmpName}\", {self.EmpType})")
                connection.commit()
                connection.close()
            return self.employee_details()
        except Exception as e:
            return e 
    def delete_employee(self):
        '''Deletes an employee from the "employee" table.

        Returns: a dictionary of the deleted employee.
        '''
        try:
            connection = create_db_connection()

            with connection.cursor() as cursor:
                cursor.execute(f"DELETE FROM employee WHERE EmpID = {self.EmpID}")
                connection.commit()
                connection.close()
            return self.employee_details()
        except Exception as e:
            return e 

    def update_employee(self, attributes):
        """Updates the database with new values for a particular employee.

        Args:
            attributes (dict): A dictionary whose keys are the column names in the "employee" table and 
                vlaues are the ones to be updated.

        Returns: A dictionary of the updated employee object.
        """
        oldID = self.EmpID
        query = generate_insert_update_query(attributes, "employee", "update", oldID)
        try:
            connection = create_db_connection()
            with connection.cursor() as cursor:
                cursor.execute(query)
                connection.commit()
                connection.close()
            return self.employee_details()
        except Exception as e:
            return e 
        

class Waiter(Employee):
    def __init__(self, EmpID, EmpName):
        super().__init__(EmpID, EmpName)
        

class Chef(Employee):
    def __init__(self, EmpID, EmpName):
        super().__init__(EmpID, EmpName)