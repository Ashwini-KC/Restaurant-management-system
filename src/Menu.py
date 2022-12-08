from util import create_db_connection, generate_select_delete, generate_insert_update_query

class Menu:

    def get_all_items(self):
        try:
            connection = create_db_connection()
            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM MENU")
                results = cursor.fetchall()
                connection.commit()
                connection.close()
            return results
        except Exception as e:
            return "Error"
    
    def add_item(self, item):
        """Adds item object to the items list in the menu and inserts a new item to
            to the "menu" table in the database.

        Args:
            item: An object of the class Item.
        
        Returns: The item which was added to the database.
        """
        try:
            connection = create_db_connection()
            with connection.cursor() as cursor:
                cursor.execute(generate_insert_update_query(item.item_details(), "menu", "insert"))
                connection.commit()
                connection.close()
            return self.find_by_id(item.get_id())
        except Exception as e:
            return "Error"
    
    def delete_item(self, id):
        """Deletes an item from the list and the "menu" table
        
        Args:
            id: itemID of the item to be deleted.

        Returns: The deleted element.
        """
        item = self.find_by_id(id)
        try:
            connection = create_db_connection()
            with connection.cursor() as cursor:
                cursor.execute(generate_select_delete(id, "menu", "delete"))
                results = cursor.fetchall()
                connection.commit()
                connection.close()
            return item
        except Exception as e:
            return "Error"
        
        
    def find_by_id(self, id):
        """Returns an item from the database.

        Args: 
            id: id of the item in the "menu" table.

        Returns: the item form the database if found.
        """
        try:
            connection = create_db_connection()
            with connection.cursor() as cursor:
                cursor.execute(generate_select_delete(id, "menu", "select"))
                results = cursor.fetchone()
                connection.close()
                return results
        except Exception:
            pass

    def get_menu(self):
        """Returns a list containing dictionaries of the item object.
        """
        return [item.item_details() for item in self.items]
    
    def update_item(self, id, item_dict):
        """Updates the database with new values for a particular item.

        Args:
            item: An item object which needs to be updated with new values.

            item_dict (dict): A dictionary whose keys are the column names in the "menu" table and 
                vlaues are the ones to be updated.
        """
        query = generate_insert_update_query(item_dict, "menu", "update", id)
        '''
        Please figure out a way to update an item dinamically when a dictionary of updates is provided
        And also implement the same in the Employee class under update method to maintain consistency in the data
        '''
        try:
            connection = create_db_connection()
            with connection.cursor() as cursor:
                cursor.execute(query)
                connection.commit()
                connection.close()
        except Exception:
            pass