"""Ignore file. Used to populate the menu table because somehow importing the csv wasn't working as expected.
"""

from util import create_db_connection
with open("data/menu.csv", 'r') as f:
    data = f.readlines()
    rows = []
    for line in data:
        r = ""
        for _ in [row for row in line.strip().split(",")]:
            r += f"\"{_}\", "
        entry = f"INSERT INTO menu values({r.strip()[: -1]})"
        try:
            connection = create_db_connection()
            with connection.cursor() as cursor:
                cursor.execute(entry)
                connection.commit()
                connection.close()
        except Exception:
            pass