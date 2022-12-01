import pymysql.cursors
from properties import DB_NAME, DB_HOST, DB_USERNAME, DB_PASSWORD

# Connect to the database
connection = pymysql.connect(host=DB_HOST,
                             user=DB_USERNAME,
                             password=DB_PASSWORD,
                             database=DB_NAME,
                             cursorclass=pymysql.cursors.DictCursor)

with connection.cursor() as cursor:
        # Read a single record
        cursor.execute("SHOW TABLES")
        tables = cursor.fetchall()
        # print(tables)
        cursor.close()


with connection.cursor() as cursor:
    for table  in tables:
        table_name = table["Tables_in_smqa"]
        cursor.execute(f"DESCRIBE smqa.{table_name}")
        results = cursor.fetchall()
        print()
        print(table_name)
        for result in results:
            print(result)

with connection.cursor() as cursor:
    pass
connection.close()

# LOAD DATA LOCAL INFILE '/Users/ashwinikc/Desktop/SMQA/data/employee.csv' INTO TABLE employee FIELDS TERMINATED BY ',' LINES TERMINATED BY '\n' IGNORE 1 ROWS (EmpID,EmpName,EmpType);

"""
LOAD DATA INFILE "/Users/ashwinikc/Desktop/SMQA/data/menu.csv"
INTO TABLE menu
COLUMNS TERMINATED BY ','
OPTIONALLY ENCLOSED BY '"'
ESCAPED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 LINES;
"""