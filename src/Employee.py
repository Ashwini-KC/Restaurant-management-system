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
from util import create_db_connection, generate_insert_update_query, generate_select_delete

from util import create_db_connection
class Employee:
    # def __init__(self, EmpID, EmpName, empType=None): 
    #     self.EmpID = EmpID
    #     self.EmpName = EmpName
    #     self.empType = empType
    def employee_details(self, empID):
>>>>>>> features

        '''
        Returns a dictionary of the employee object.
        '''
        query = generate_select_delete(empID, "employee", "select")

        try:
            connection = create_db_connection()
            with connection.cursor() as cursor:
                cursor.execute(query)
                results = cursor.fetchone()
                connection.commit()
                connection.close()
            return results
        except Exception as e:
            return e 
    
    def add_employee(self, empID, empName, empType):
        '''Adds news employee detial to the employee table.
        '''
        employee = {
            'empID': empID,
            'empName': empName,
            'empType':empType 
        }
        query = f"INSERT INTO employee VALUES ({employee['empID']}, \"{employee['empName']}\", {employee['empType']})"

        try:
            connection = create_db_connection()
            with connection.cursor() as cursor:
                cursor.execute(query)
                connection.commit()
                connection.close()
            return employee
        except Exception as e:
            return e 
    def delete_employee(self, empID):
        '''Deletes an employee from the "employee" table.

        Returns: a dictionary of the deleted employee.
        '''
        try:
            connection = create_db_connection()

            with connection.cursor() as cursor:
                cursor.execute(f"DELETE FROM employee WHERE empID = {empID}")
                connection.commit()
                connection.close()
            return True
        except Exception as e:
            return e 

    def update_employee(self, empID, attributes):
        """Updates the database with new values for a particular employee.

        Args:
            attributes (dict): A dictionary whose keys are the column names in the "employee" table and 
                vlaues are the ones to be updated.

        Returns: A dictionary of the updated employee object.
        """
        oldID = empID
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

    def get_all_employees(self):
        try:
            connection = create_db_connection()
            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM EMPLOYEE")
                results = cursor.fetchall()
                connection.commit()
                connection.close()
            return results
        except Exception as e:
            return e 

class Waiter(Employee):
    def __init__(self, empID, empName):
        super().__init__(empID, empName)
        

class Chef(Employee):
    def __init__(self, empID, empName):
        super().__init__(empID, empName)