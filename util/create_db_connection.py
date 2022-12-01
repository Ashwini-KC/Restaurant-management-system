import pymysql.cursors
from properties import DB_NAME, DB_HOST, DB_USERNAME, DB_PASSWORD

# Connect to the database

def create_db_connection():

    connection = pymysql.connect(host=DB_HOST,
                                user=DB_USERNAME,
                                password=DB_PASSWORD,
                                database=DB_NAME,
                                cursorclass=pymysql.cursors.DictCursor)
    return connection