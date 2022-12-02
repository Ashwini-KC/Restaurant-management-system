
def generate_select_delete(id, table, op):
    """Returns an appropriate SQL query.
        Args:
            id: The value of a primary key of a table.

            table: Table name on which the query is to be performed.

            op: The operation performed on the table [select, delete].
            
        Returns:
            A string which is an SQL query to perform a desired operation.
    """
    match table:
        case "customer":
            table = "CUSTOMER"
            ID = "custID"
        case "employee":
            table = "employee"
            ID = "EmpID"
        case "menu":
            table = "menu"
            ID = "itemID"
        case "order":
            table = "order"
            ID = "orderID"
    
    match op:
        case "select":
            query = f"SELECT * FROM {table} WHERE {ID} = {id}"
        case "delete":
            query = f"DELETE FROM {table} WHERE {ID} = {id}"

    return query


def generate_insert_update_query(obj, table, op, old_id=None):
    """Returns an appropriate SQL query.
        Args:
            obj (dict): A dictionary whose keys are the column names in the database table and 
                vlaues are the ones to be inserted or updated.

            table: Table name on which the query is to be performed.

            op: The operation performed on the table [select, delete].

            old_id: The value of the primary key of a database entry to which an update operation
                is performed

        Returns:
            A string which is an SQL query to perform a desired operation.
    """
    attr = []
    match table:
        case "customer":
            table = "CUSTOMER"
            ID = "CustID"
        case "employee":
            table = "employee"
            ID = "EmpID"
        case "menu":
            table = "menu"
            ID = "itemID"
        case "order":
            table = "order"
            ID = "orderID"
    match op:
        case "insert":
            for key, value in obj.items():
                attr.append(f'"{value}"')
            query = f'INSERT INTO {table} VALUES ({", ".join(attr)})'
        case "update":
            for key, value in obj.items():
                attr.append(f'{key} = "{value}"')
            query = f'UPDATE {table} SET {", ".join(attr)} WHERE {ID} = {old_id}'
    return query

def query_executor_funtion(query):
    pass
    '''
    Remove redundant code which uses create_db_connection function to run queries in Employee.py,
    Menu.py
    '''
