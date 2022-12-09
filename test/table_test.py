from src import Table
from random_id import *
from util import create_db_connection


def fetch_table_details():
    table_list = []
    try:
        conn = create_db_connection()

        with conn.cursor() as cursor:
            cursor.execute("select tableID,EmpID from tables where available = 0;")
            for i in cursor:
                table_list.append(i)

    except Exception as e:
        return e

    return table_list



def test_table_details_1():
    '''
    standard function that doesnt require any input output
    function wont fail in absence of any table
    '''
    table1 = Table('abcd','emp5')
    assert fetch_table_details() == table1.table_details()

def test_change_availability_status_1():

    '''
    should fail because the provided employee ID and customer ID are not in the database
    violates the foreign key
    '''
    table1 = Table('abcd','emp5')
    assert fetch_table_details() == table1.change_availability_status('abcd','emp5')


def test_change_availability_status_2():
    '''
    test fails due to buggy code
    logic stays solid
    '''
    table1 = Table('abcd','emp5')
    table1.change_availability_status('011TA9LXG','1234')
    assert fetch_table_details() == table1.table_details()