from src import Bill, Customer,Employee, Order
from util import create_db_connection

bil1 = Bill("1234")
print(bil1.calculate_Bill())
print(bil1.generate_Bill(21))

try:
    conn = create_db_connection()
    with conn.cursor() as cursor:
        cursor.execute("select count(*) from bill")
        row = cursor.fetchone()
        print(type(row))

        
except Exception as e:
    print(e)